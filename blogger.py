#!/usr/bin/env python3
# encoding: utf-8
"""Main logic of the blogging system."""

from collections import namedtuple
import datetime
from functools import cache
import itertools as it
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import sqlite3
import subprocess as sp
from typing import Any, Iterable, Self, Sequence, TypeAlias
import atexit
from dulwich import porcelain
from bs4 import BeautifulSoup
import nbformat
from loguru import logger
import requests
from tqdm import tqdm
import yaml

AnyPath: TypeAlias = str | Path
Number: TypeAlias = int | float
BASE_DIR = Path(__file__).resolve().parent
SPELLS_TITLE = BASE_DIR / "spells/spells_title.yaml"
SPELLS_TAG = BASE_DIR / "spells/spells_tag.yaml"
ARTICLES = "articles"
DRAFTS = "drafts"
OUTDATED = "outdated"
DISCLAIMER_DRAFTS = "**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**\n"
DISCLAIMER_OUTDATED = "**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**\n"
MARKDOWN = ".md"
IPYNB = ".ipynb"
# TODO: move into Record directly and access via .fields
POSTS_COLS = [
    "path",
    "doc_dir",
    "created",
    "date",
    "title",
    "label",
    "tags",
    "content",
    "empty",
    "match",
    "refs",
]
SEPARATOR = "|"
# SITE = "https://legendu-net.github.io/blog"
SITE = "https://www.legendu.net"
Record = namedtuple("Record", POSTS_COLS)


@cache
def _read_spells(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8") as fin:
        return yaml.load(fin, Loader=yaml.FullLoader)


def read_spells_title() -> dict[str, str]:
    return _read_spells(SPELLS_TITLE)


def read_spells_tag() -> dict[str, str] | dict[str, str | list[str]]:
    kvs = _read_spells(SPELLS_TITLE).copy()
    kvs.update(_read_spells(SPELLS_TAG))
    return kvs


def _clear_spells_caches() -> None:
    """Drop every cache derived from the spells files.

    Spells are added and applied within a single run (``./blog.py ast ... -A``),
    so the derived title overrides have to be dropped together with the files.
    """
    _read_spells.cache_clear()
    _title_overrides.cache_clear()
    _title_phrases.cache_clear()


def add_spells_title(pairs: Iterable[tuple[str, str]]) -> None:
    spells = list(read_spells_title().items())
    spells.extend(pairs)
    spells.sort(key=lambda x: x[0])
    merged = dict(spells)
    # Validate before writing: a spell that conflicts with an existing one makes
    # every later format_title() raise, so it must not reach the file.
    _build_title_overrides(merged)
    _build_title_phrases(merged)
    with SPELLS_TITLE.open("w", encoding="utf-8") as fout:
        yaml.dump(merged, fout)
    _clear_spells_caches()


def add_spells_tag(pairs: Iterable[tuple[str, str]]) -> None:
    spells = list(_read_spells(SPELLS_TAG).items())
    spells.extend(pairs)
    spells.sort(key=lambda x: x[0])
    with SPELLS_TAG.open("w", encoding="utf-8") as fout:
        yaml.dump(dict(spells), fout)
    _clear_spells_caches()


def extract_url_title(url: str) -> str:
    """Extract the title of a web page."""
    url = url.strip("/")
    if re.search(r"^https://github.com/\w+/\w+$", url):
        return "/".join(url.split("/")[-2:]) + " @ GitHub"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    if not soup.title:
        return ""
    return soup.title.string if soup.title.string else ""


def get_vim() -> str | None:
    return shutil.which("nvim") or shutil.which("vim")


def get_code() -> str | None:
    return shutil.which("code-server") or shutil.which("code")


def get_euporie() -> str:
    if shutil.which("euporie"):
        return (
            "euporie notebook "
            "--no-warn-venv "
            "--show-status-bar "
            "--syntax-highlighting "
            "--color-depth 24 "
            "--edit-mode vi "
            "--cursor-blink "
            "--autocomplete "
            "--autosuggest smart "
            "--line-numbers"
        )
    return ""


def get_preferred_editor(suffixes: Sequence[str]) -> str:
    """Get an editor for editing the specified file types."""
    nft = len(suffixes)
    if nft <= 0:
        raise ValueError("No file types specified for editing.")
    if nft >= 2:
        editor = get_code()
        if not editor:
            raise FileNotFoundError(
                "The preferred editor code-server/code (for editing markdown and notebook at the same time) was not found."
            )
        return editor
    if suffixes[0] == IPYNB:
        editor = get_euporie() or get_code()
        if not editor:
            raise FileNotFoundError(
                "The preferred editor euporie/code-server/code (for editing notebook) was not found."
            )
        return editor
    editor = get_vim() or get_code()
    if not editor:
        raise FileNotFoundError(
            "The preferred editor nvim/vim/code-server/code (for editing markdown) was not found."
        )
    return editor


def qmarks(n: int | Sequence) -> str:
    """Generate n question marks delimited by comma."""
    if isinstance(n, int):
        return ", ".join(["?"] * n)
    if isinstance(n, str):
        return qmarks(n.count(",") + 1)
    return qmarks(len(n))


def _parse_record(path: AnyPath):
    return Post(path).parse().record()


def get_post_paths() -> list[Path]:
    paths = []
    for doc_dir in (ARTICLES, DRAFTS, OUTDATED):
        for ext in (MARKDOWN, IPYNB):
            paths.extend(BASE_DIR.glob(f"docs/{doc_dir}/20??/??/*/index{ext}"))
    return paths


def _parse_records() -> list[Record]:
    logger.info("Parsing posts into records ...")
    # TODO: 1. do you need multiprocessing?
    # TODO: 2. if not, no need to use a list
    # with multiprocessing.Pool(processes=1) as pool:
    # return pool.map(_parse_record, paths)
    return [_parse_record(path) for path in get_post_paths()]


_TITLE_LEADING_PUNCT = frozenset(["(", '"', "'", "“", "‘"])
_TITLE_TRAILING_PUNCT = frozenset(
    [")", '"', "'", "”", "’", ":", ",", ";", ".", "!", "?"]
)
# Function words kept lowercase inside a title (never first or last).
_TITLE_SMALL_WORDS = frozenset(
    [
        "a",
        "an",
        "and",
        "as",
        "at",
        "but",
        "by",
        "for",
        "in",
        "of",
        "on",
        "or",
        "the",
        "to",
        "via",
        "vs",
    ]
)
# House style on top of the standard set above: these read better lowercase in
# this blog's titles. This frozenset is the single knob for that choice; empty
# it and the words follow ordinary title case instead.
_TITLE_HOUSE_WORDS = frozenset(
    [
        "about",
        "after",
        "among",
        "before",
        "behind",
        "between",
        "during",
        "except",
        "from",
        "inside",
        "into",
        "over",
        "than",
        "through",
        "with",
        "without",
    ]
)
# Function words are cased by position, which a spell cannot express, so spells
# never own them. Listed out rather than derived from the two sets above so that
# emptying the house style cannot hand these words back to a spell.
_TITLE_FUNCTION_WORDS = frozenset(
    [
        "a",
        "about",
        "after",
        "among",
        "an",
        "and",
        "as",
        "at",
        "before",
        "behind",
        "between",
        "but",
        "by",
        "during",
        "except",
        "for",
        "from",
        "in",
        "inside",
        "into",
        "of",
        "on",
        "or",
        "over",
        "than",
        "the",
        "through",
        "to",
        "via",
        "vs",
        "with",
        "without",
    ]
)


def _split_punct(token: str) -> tuple[str, str, str]:
    """Split a token into its leading punctuation, core word and trailing punctuation.

    Spells are looked up on the core, so a word glued to punctuation (e.g.
    ``AnalysisException:``, ``(UDF)``, ``"rsnapshot"``) is still corrected.

    :param token: A whitespace-delimited token of a title.
    :return: A ``(lead, core, trail)`` tuple that re-joins to ``token``.
    """
    lead = trail = ""
    while token and token[0] in _TITLE_LEADING_PUNCT:
        lead += token[0]
        token = token[1:]
    while token and token[-1] in _TITLE_TRAILING_PUNCT:
        trail = token[-1] + trail
        token = token[:-1]
    return lead, token, trail


def _build_title_overrides(spells: dict[str, str]) -> dict[str, str]:
    """Fold title spells into a lookup keyed by the lowercased word.

    Keys are folded to lowercase because titles are no longer passed through
    ``str.title()`` first, so a spell must match the word however it was typed.
    Skipped are multi-word keys, which no longer have a matching pass, and
    ``_TITLE_FUNCTION_WORDS``, whose casing is positional.

    :param spells: Title spells as read from ``SPELLS_TITLE``.
    :return: A mapping from lowercased word to its replacement.
    :raise ValueError: If two spells disagree about the same lowercased word.
    """
    overrides: dict[str, str] = {}
    origins: dict[str, str] = {}
    for origin, replace in spells.items():
        key = origin.lower()
        if " " in origin or key in _TITLE_FUNCTION_WORDS:
            continue
        if overrides.get(key, replace) != replace:
            raise ValueError(
                f"Conflicting title spells: {origins[key]!r} -> {overrides[key]!r} "
                f"and {origin!r} -> {replace!r}."
            )
        overrides[key] = replace
        origins[key] = origin
    return overrides


@cache
def _title_overrides() -> dict[str, str]:
    """Build the title override lookup from the spells file.

    :return: A mapping from lowercased word to its replacement.
    """
    return _build_title_overrides(read_spells_title())


def _build_title_phrases(spells: dict[str, str]) -> dict[tuple[str, ...], list[str]]:
    """Fold multi-word title spells into a lookup keyed by lowercased words.

    A phrase spells a run of words that only reads correctly together, e.g.
    ``Over Partition: OVER PARTITION``, where neither word can be cased on its
    own without hitting ordinary prose.

    :param spells: Title spells as read from ``SPELLS_TITLE``.
    :return: A mapping from a tuple of lowercased words to its replacements.
    :raise ValueError: If a phrase does not replace word for word, which would
        change the spacing and therefore the post's label and URL.
    """
    phrases: dict[tuple[str, ...], list[str]] = {}
    for origin, replace in spells.items():
        if " " not in origin:
            continue
        key = tuple(origin.lower().split())
        words = replace.split()
        if len(words) != len(key):
            raise ValueError(
                f"Title spell {origin!r} -> {replace!r} must replace word for "
                f"word: {len(key)} words became {len(words)}."
            )
        phrases[key] = words
    return phrases


@cache
def _title_phrases() -> dict[tuple[str, ...], list[str]]:
    """Build the multi-word title lookup from the spells file.

    :return: A mapping from a tuple of lowercased words to its replacements.
    """
    return _build_title_phrases(read_spells_title())


def _apply_title_phrases(
    tokens: list[str], parts: list[tuple[str, str, str]]
) -> set[int]:
    """Apply multi-word spells to ``tokens`` in place, longest phrase first.

    :param tokens: The title's tokens, updated in place.
    :param parts: The ``_split_punct`` result for each original token.
    :return: The indexes of the tokens a phrase has already cased.
    """
    phrases = _title_phrases()
    handled: set[int] = set()
    if not phrases:
        return handled
    longest = max(len(key) for key in phrases)
    i = 0
    while i < len(tokens):
        for size in range(min(longest, len(tokens) - i), 1, -1):
            key = tuple(parts[j][1].lower() for j in range(i, i + size))
            if key in phrases:
                for offset, word in enumerate(phrases[key]):
                    lead, _, trail = parts[i + offset]
                    tokens[i + offset] = lead + word + trail
                    handled.add(i + offset)
                i += size
                break
        else:
            i += 1
    return handled


def format_title(title: str) -> str:
    """Format a title in title case, preserving names that carry their own casing.

    A word that already contains a capital past its first letter (``Neovim``,
    ``macOS``, ``GRUB``) is left alone, so correct casing survives instead of
    being flattened and then repaired by a spell.

    :param title: The title to format.
    :return: The formatted title.
    """
    overrides = _title_overrides()
    tokens = title.split(" ")
    parts = [_split_punct(token) for token in tokens]
    filled = [i for i, token in enumerate(tokens) if token]
    first, last = (filled[0], filled[-1]) if filled else (None, None)
    phrased = _apply_title_phrases(tokens, parts)
    for i in range(len(tokens)):
        if i in phrased:
            continue
        lead, core, trail = parts[i]
        if not core:
            continue
        key = core.lower()
        if key in overrides:
            core = overrides[key]
        elif any(char.isupper() for char in core[1:]):
            pass  # Self-cased name, e.g. Neovim, macOS, GRUB, GPT-2.
        elif key in _TITLE_SMALL_WORDS or key in _TITLE_HOUSE_WORDS:
            core = key if i not in (first, last) else key.capitalize()
        else:
            # Only the first letter, so hyphenated compounds stay as written
            # ("Cross-platform") and contractions are safe ("Don't").
            core = core[:1].upper() + core[1:]
        tokens[i] = lead + core + trail
    return " ".join(tokens)


def _label(title: str) -> str:
    """Generate a label from the title of the Post.

    :param title: The title to create the slug from.
    :return: A label created from the title.
    """
    title = title.lower()
    hyphen = "-"
    strs = [
        " ",
        "/",
        ",",
        "(",
        ")",
        "[",
        "]",
        ":",
        "=",
        "?",
        "!",
        "#",
        "`",
        '"',
        "'",
        "“",
        "”",
        hyphen * 4,
        hyphen * 3,
        hyphen * 2,
    ]
    for s in strs:
        title = title.replace(s, hyphen)
    return title.strip(hyphen)


def _concat(items: list[str], sep: str) -> str:
    """Concatenate items into a ``sep``-delimited string wrapped with ``sep``.

    The leading/trailing ``sep`` lets membership be tested with
    ``LIKE '%<sep><item><sep>%'``. An empty list yields an empty string.
    """
    if not items:
        return ""
    return sep + sep.join(items) + sep


def _parse_metadata(yaml_str: str) -> dict[str, Any]:
    metadata = yaml.load(yaml_str, Loader=yaml.FullLoader)
    if metadata is None:
        metadata = {}
    for key in ("created", "date"):
        val = metadata.get(key)
        if isinstance(val, str):
            val = datetime.datetime.fromisoformat(val)
        if isinstance(val, datetime.date) and not isinstance(val, datetime.datetime):
            val = datetime.datetime.combine(val, datetime.time.min)
        if isinstance(val, datetime.datetime) and val.tzinfo is None:
            val = val.astimezone()
        metadata[key] = val
    return metadata


class Post:
    """A class abstracting a post."""

    def __init__(self, path: AnyPath):
        self.path: Path = Path()
        self._doc_dir = ""
        self.is_markdown = True
        self.metadata = {}
        self.lines = []
        self.notebook = {}
        self._should_write = False
        self._set_path(path)
        atexit.register(self.shutdown_hook)

    def shutdown_hook(self):
        if self._should_write:
            self._write()
            self._should_write = False

    def change_doc_dir(self, doc_dir: str):
        if doc_dir not in (ARTICLES, DRAFTS, OUTDATED):
            raise ValueError(
                f"doc_dir must be one of {ARTICLES}, {DRAFTS} or {OUTDATED}!"
            )
        if doc_dir == self._doc_dir:
            return
        parts = list(self.path.parts)
        parts[1] = doc_dir
        path_new = BASE_DIR.joinpath(*parts)
        dir_new = path_new.parent
        dir_new.mkdir(parents=True, exist_ok=True)
        self.path.parent.move(dir_new)
        self._set_path(path_new)
        self.parse()

    def parse(self) -> Self:
        if self.is_markdown:
            with self.path.open(encoding="utf-8") as fin:
                lines = fin.readlines()
            self.notebook = {}
        else:
            self.notebook = self._read_notebook()
            lines = self.notebook["cells"][0]["source"].copy()
            for cell in self.notebook["cells"][1:]:
                lines.append("\n<!-- Cell -->\n")
                lines.extend(cell["source"])
        idx = lines.index("---\n", 1)
        try:
            self.metadata = _parse_metadata("".join(lines[:idx]))
        except Exception as err:
            print(
                "Failed to parse the YAML metadata of the following post!\n",
                self.path,
                sep="",
            )
            for line in lines:
                print(line)
            print()
            raise err
        idx += 1
        while idx < len(lines):
            if lines[idx].strip():
                break
            idx += 1
        self.lines = lines[idx:]
        self._check_disclaimer()
        return self

    def _is_disclaimer_valid(self) -> tuple[bool, bool]:
        """Check whether the disclaimer is valid, and whether there's a disclaimer."""
        if self.lines[0] == DISCLAIMER_DRAFTS:
            return self._doc_dir == DRAFTS, True
        if self.lines[0] == DISCLAIMER_OUTDATED:
            return self._doc_dir == OUTDATED, True
        return self._doc_dir == ARTICLES, False

    def _check_disclaimer(self):
        if not self.lines:
            return
        valid, has_disclaimer = self._is_disclaimer_valid()
        if has_disclaimer:
            self.lines = self.lines[1:]
        if not valid:
            self._should_write = True

    def _set_path(self, path: AnyPath):
        if isinstance(path, str):
            path = Path(path)
        path = path.resolve()
        if path.suffix not in (MARKDOWN, IPYNB):
            raise ValueError(f"{self.path} is not a {MARKDOWN} or {IPYNB} file.")
        self.path = path.relative_to(BASE_DIR)
        self._doc_dir = self.path.parts[1]
        self.is_markdown = path.suffix == MARKDOWN

    def label_to_use(self) -> str:
        if not self.metadata:
            return ""
        if next(iter(self.metadata.keys()), "") == "label":
            return self.metadata["label"]
        return _label(self.metadata["title"])

    def is_match(self) -> bool:
        """Check whether the file name and the title of the post does not match.

        :param title: The title of the post.
        :return: 1 if mismatch and 0 otherwise.
        """
        return (
            self.label_to_use() == self.metadata["label"]
            and self.metadata["label"] == self.path.parts[4]
        )

    def mdformat(self):
        sp.run(f"uv run mdformat {self.path}", shell=True)

    def _write(self):
        if self.is_markdown:
            with self.path.open("w", encoding="utf-8") as fout:
                fout.writelines(self._metadata_lines())
                if self._doc_dir == DRAFTS:
                    fout.write(DISCLAIMER_DRAFTS)
                elif self._doc_dir == OUTDATED:
                    fout.write(DISCLAIMER_OUTDATED)
                fout.writelines(self.lines)
            self.mdformat()
        else:
            cell0 = self.notebook["cells"][0]
            cell0["source"] = self._metadata_lines()
            if self._doc_dir == DRAFTS:
                cell0["source"].append(DISCLAIMER_DRAFTS)
            elif self._doc_dir == OUTDATED:
                cell0["source"].append(DISCLAIMER_OUTDATED)
            self.path.write_text(json.dumps(self.notebook, indent=1), encoding="utf-8")

    def _metadata_lines(self) -> list[str]:
        """Convert the metadata dict into metadata lines."""
        metadata = self.metadata.copy()
        for key, value in metadata.items():
            if isinstance(value, (datetime.datetime, datetime.date)):
                metadata[key] = value.isoformat()
        lines = ["---\n"]
        for line in (
            yaml.dump(metadata, allow_unicode=True, sort_keys=False).strip().split("\n")
        ):
            # prefer indention for list
            if line.startswith("- "):
                line = "  " + line
            lines.append(line + "\n")
        lines.append("---\n")
        lines.append("\n")
        return lines

    def _read_notebook(self) -> dict:
        notebook = json.loads(self.path.read_text(encoding="utf-8"))
        if notebook["cells"][0]["cell_type"] != "markdown":
            raise SyntaxError(
                f"The first cell of the notebook {self.path} is not a markdown cell!"
            )
        return notebook

    def _is_post_empty(self) -> bool:
        """Check whether the post is essentially empty."""
        return all(line.strip() == "" for line in self.lines)

    def concat_tags(self) -> str:
        return _concat(self.metadata["tags"], SEPARATOR)

    def _extract_xrefs(self) -> list[str]:
        """Extract outbound cross-references from this post's body.

        Returns the de-duplicated referenced post labels (relative slug links
        and reference definitions) and absolute ``SITE`` URLs. Section anchors
        are dropped; URLs are kept whole.

        :return: A list of unique referenced labels and URLs.
        """
        text = "".join(self.lines)
        rel_ref = r"\]\(([a-z0-9][a-z0-9-]*)(?:#[\w-]+)?\)"
        ref_def = r"(?m)^\s*\[[^\]]+\]:\s*([a-z0-9][a-z0-9-]*)(?:#[\w-]+)?\s*$"
        # Canonical post URLs only: SITE/{doc_dir}/{YYYY}/{MM}/{label}. This
        # excludes non-post links (tags, media, ...) and stops at the label for
        # deeper paths.
        abs_ref = re.escape(SITE) + r"/[a-z]+/\d{4}/\d{2}/[A-Za-z0-9_-]+"
        refs = re.findall(rel_ref, text)
        refs.extend(re.findall(ref_def, text))
        refs.extend(re.findall(abs_ref, text))
        return list(dict.fromkeys(refs))

    def record(self) -> Record:
        tags = self.concat_tags()
        content = self.metadata["title"] + "\n" + tags + "\n" + "".join(self.lines)
        return Record(
            str(self.path),
            self._doc_dir,
            self.metadata["created"],
            self.metadata["date"],
            self.metadata["title"],
            self.label_to_use(),
            tags,
            content,
            int(self._is_post_empty()),
            int(self.is_match()),
            _concat(self._extract_xrefs(), SEPARATOR),
        )

    def update_xref(
        self, old_label: str, new_label: str, old_url: str, new_url: str
    ) -> int:
        """Update cross-references to a renamed/moved post in this post's file.

        The raw file is read and written directly (so both Markdown and
        notebook files are handled without reformatting), and it is only
        written back when something actually changed.

        :param old_label: The previous label (relative-reference slug).
        :param new_label: The new label.
        :param old_url: The previous absolute ``SITE`` URL.
        :param new_url: The new absolute ``SITE`` URL.
        :return: The number of references rewritten.
        """
        text = self.path.read_text(encoding="utf-8")
        # Absolute URL references. The negative lookahead avoids matching a URL
        # whose label is a prefix of a longer one (e.g. ".../spark-sql-tips").
        url_pat = re.compile(re.escape(old_url) + r"(?![A-Za-z0-9-])")
        text, num = url_pat.subn(new_url, text)
        if old_label != new_label:
            # Relative slug references, only in genuine link-target positions;
            # any section anchor is preserved. The reference-definition pattern
            # is not anchored to the physical line start so it also matches
            # inside notebook JSON (where the line is wrapped in quotes), and
            # the trailing lookahead guards against a label that is a prefix of
            # a longer one.
            ol = re.escape(old_label)
            inline = re.compile(r"\]\(" + ol + r"(?P<a>#[A-Za-z0-9_-]+)?\)")
            refdef = re.compile(
                r"(?P<pre>\[[^\]\n]*\]:[ \t]*)"
                + ol
                + r"(?P<a>#[A-Za-z0-9_-]+)?(?![A-Za-z0-9/_-])"
            )
            text, n1 = inline.subn(
                lambda m: f"]({new_label}{m.group('a') or ''})", text
            )
            text, n2 = refdef.subn(
                lambda m: f"{m['pre']}{new_label}{m.group('a') or ''}", text
            )
            num += n1 + n2
        if num:
            self.path.write_text(text, encoding="utf-8")
        return num

    def update_meta_field(self, metadata: dict[str, Any]) -> None:
        """Update metadata."""
        self.metadata.update(metadata)
        self._should_write = True

    def update_title(self) -> bool:
        title = format_title(self.metadata["title"])
        if title == self.metadata["title"]:
            return False
        self.update_meta_field(metadata={"title": title})
        return True

    def update_tags(self, kvs: dict[str, str] | dict[str, str | list[str]]) -> bool:
        if not kvs:
            kvs = read_spells_tag()
        tags = []
        for t in self.metadata["tags"]:
            tag = kvs.get(t, t)
            if not tag:
                continue
            if isinstance(tag, list):
                tags.extend(tag)
            else:
                tags.append(tag)
        tags = list(dict.fromkeys(tags))
        if tags == self.metadata["tags"]:
            return False
        self.update_meta_field(metadata={"tags": tags})
        return True

    def match_title(self) -> None:
        """Make the post's slug and path name match its title."""
        label_to_use = self.label_to_use()
        self.update_meta_field(
            {
                "label": label_to_use,
            }
        )
        dir_ = self.path.parent
        dir_new = dir_.with_name(label_to_use)
        dir_.move(dir_new)
        self._set_path(dir_new / self.path.name)

    def _add_markdown_cell(
        self, index: int | None = None, source: list[str] | None = None
    ):
        """Add an empty markdown cell."""
        cell = nbformat.versions[nbformat.current_nbformat].new_markdown_cell()  # ty: ignore[unresolved-attribute]
        if source:
            cell["source"] = source
        if index is None:
            self.notebook["cells"].append(cell)
        else:
            self.notebook["cells"].insert(index, cell)

    def _new_notebook(self):
        """Create a new notebook with an empty metadata (markdown) cell."""
        self.notebook = nbformat.versions[nbformat.current_nbformat].new_notebook()
        self._add_markdown_cell()

    def create(self, metadata_or_title: dict[str, Any] | str):
        if isinstance(metadata_or_title, str):
            metadata_or_title = {
                "title": format_title(metadata_or_title),
                "created": datetime.datetime.now().astimezone(),
                "date": datetime.datetime.now().astimezone(),
                "authors": ["bendu"],
                "label": _label(metadata_or_title),
                "license": "CC-BY-4.0",
                "tags": ["programming"],
            }
        self.metadata = metadata_or_title
        self.lines = []
        self._new_notebook()
        self._write()

    def convert(self) -> str:
        """Convert a markdown post to a notebook blog, vice versa."""
        if self.is_markdown:
            self._new_notebook()
            self._add_markdown_cell(source=self.lines)
            path_new = self.path.with_suffix(".ipynb")
        else:
            path_new = self.path.with_suffix(".md")
        self.path.rename(path_new)
        self._set_path(path_new)
        self._write()
        return str(path_new)

    def add_refs(self, urls: str | list[str]) -> None:
        """Add URL references into this post."""
        if isinstance(urls, str):
            urls = [urls]
        lines = [f"- [{extract_url_title(url)}]({url})\n" for url in urls]
        ref = "## References"
        if self.is_markdown:
            for idx, line in enumerate(reversed(self.lines)):
                if line.strip() == ref:
                    idx = len(self.lines) - idx
                    self.lines[idx:idx] = lines
                    break
            else:
                self.lines.append(ref + "\n")
                self.lines.extend(lines)
        else:
            for cell in reversed(self.notebook["cells"]):
                if cell["source"][0].strip() == ref:
                    cell["source"][1:1] = lines
                    break
            else:
                self._add_markdown_cell(source=[ref + "\n"] + lines)
        self._should_write = True


class Blogger:
    """A class for managing blog."""

    POSTS = "posts"
    SRPS = "srps"
    SRPS_COLS = "path, title, label"

    def __init__(self, db: str = ""):
        """Create an instance of Blogger.

        :param dir_: the root directory of the blog.
        :param db: the path to the SQLite3 database file.
        """
        self._db = db if db else str(BASE_DIR / ".blogger.sqlite3")
        # A generous busy timeout lets concurrent blog.py instances queue on the
        # write lock instead of failing with "database is locked".
        self._conn = sqlite3.connect(self._db, timeout=30)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._create_vtable_posts()
        self._create_table_srps()

    def _create_vtable_posts(self):
        sql = f"""
            CREATE VIRTUAL TABLE IF NOT EXISTS {self.POSTS} USING fts5 (
                {", ".join(POSTS_COLS)},
                tokenize = porter
            )
            """
        self._conn.execute(sql)

    def _create_table_srps(self):
        sql = f"CREATE TABLE IF NOT EXISTS {self.SRPS} ({self.SRPS_COLS})"
        self._conn.execute(sql)

    def clean_db(self):
        """Remove the SQLite3 database."""
        os.remove(self._db)

    def commit(self):
        """Commit changes made to the SQLite3 database."""
        self._conn.commit()

    def reload_posts(self):
        """Reload posts into the SQLite3 database."""
        # Parse before deleting so that the write lock is not held while
        # thousands of posts are read from disk.
        records = _parse_records()
        self.delete_records(self.POSTS, "")
        logger.info("Inserting records into SQLite3 ...")
        for batch in tqdm(it.batched(records, 1000)):
            self.load_records(batch)

    def load_records(self, records: Iterable[Record]):
        # TODO: can be unified with load_post, use just 1 function
        sql = f"""
            INSERT INTO {self.POSTS} (
                {", ".join(POSTS_COLS)}
            ) VALUES (
                {qmarks(POSTS_COLS)}
            )
            """
        self._conn.executemany(sql, records)

    def load_post(self, post: Post):
        sql = f"""
            INSERT INTO {self.POSTS} (
                {", ".join(POSTS_COLS)}
            ) VALUES (
                {qmarks(POSTS_COLS)}
            )
            """
        self._conn.execute(sql, post.record())

    def trash(self, paths: str | list[str]):
        """Move the specified posts to the trash directory.

        :param paths: Paths of posts to be removed.
        """
        if isinstance(paths, str):
            paths = [paths]
        dir_ = BASE_DIR / "trash"
        if not dir_.is_dir():
            dir_.mkdir(0o700, True, True)
        for path in paths:
            shutil.move(Path(path).parent, dir_)
        self.delete_records(table=self.SRPS, paths=paths)
        self.delete_records(table=self.POSTS, paths=paths)

    def delete_records(self, table: str, paths: str | list[str]) -> None:
        """Delete records from a table.

        :param paths: Paths correspond to records to delete.
            If a trivia value ("" or []) is specified,
            then all records are deleted from the table.
        """
        sql = f"DELETE FROM {table} "
        if not paths:
            self._conn.execute(sql)
            return
        if isinstance(paths, AnyPath):
            paths = [paths]
        sql += f"WHERE path IN ({qmarks(paths)})"
        self._conn.execute(sql, paths)

    def keep_srps(self, indexes: list[int]) -> None:
        """Keep only the srps rows with the given rowids, removing all others."""
        sql = f"DELETE FROM {self.SRPS} WHERE rowid NOT IN ({qmarks(indexes)})"
        self._conn.execute(sql, indexes)

    def remove_srps(self, indexes: list[int]) -> None:
        """Remove srps rows with the given rowids."""
        sql = f"DELETE FROM {self.SRPS} WHERE rowid IN ({qmarks(indexes)})"
        self._conn.execute(sql, indexes)

    def move(self, paths: str | Sequence[str], doc_dir: str) -> None:
        """Move specified posts into a destination directory.

        :param paths: A (sequence of) path(s).
        :param dst: The destination path or directory to move posts to.
        """
        if isinstance(paths, str):
            paths = [paths]
        for path in paths:
            post = Post(path)
            po = Path(path).parts
            old_doc_dir, yyyy, mm, label = po[1], po[2], po[3], po[4]
            post.change_doc_dir(doc_dir)
            self.update_records(
                table=self.SRPS,
                paths=path,
                kvs={"path": str(post.path)},
            )
            self.update_records(
                table=self.POSTS,
                paths=path,
                kvs={"path": str(post.path), "doc_dir": doc_dir},
            )
            # A move changes only the doc_dir, so the label (and thus relative
            # references) is unchanged; only absolute URLs need rewriting.
            old_url = f"{SITE}/{old_doc_dir}/{yyyy}/{mm}/{label}"
            new_url = f"{SITE}/{doc_dir}/{yyyy}/{mm}/{label}"
            if old_url != new_url:
                self.update_xref(label, label, old_url, new_url)

    def match_title(self, post: str | Post) -> None:
        if isinstance(post, str):
            post = Post(post).parse()
        if post.is_match():
            print(
                "The lable and title of the following post already matches.\n    ",
                post.path,
                "\n",
                sep="",
            )
            return
        path_old = str(post.path)
        post.match_title()
        kvs: dict[str, str | datetime.datetime | int] = {
            "path": str(post.path),
        }
        self.update_records(table=self.SRPS, paths=path_old, kvs=kvs)
        kvs["date"] = post.metadata["date"]
        kvs["match"] = 1
        self.update_records(table=self.POSTS, paths=path_old, kvs=kvs)
        # The label changed, breaking both relative slug references and the
        # last segment of absolute URLs in other posts; update them.
        po = Path(path_old).parts
        doc_dir, yyyy, mm, old_label = po[1], po[2], po[3], po[4]
        new_label = post.path.parts[4]
        base = f"{SITE}/{doc_dir}/{yyyy}/{mm}"
        self.update_xref(
            old_label,
            new_label,
            f"{base}/{old_label}",
            f"{base}/{new_label}",
        )

    def update_xref(
        self,
        old_label: str,
        new_label: str,
        old_url: str,
        new_url: str,
    ) -> list[str]:
        """Rewrite cross-references to a renamed/moved post in all other posts.

        Posts referencing the changed label/URL are found via the ``refs``
        column rather than by scanning every file on disk. Only the matching
        files are rewritten, and their database records are refreshed.

        :param old_label: The previous label (relative-reference slug).
        :param new_label: The new label.
        :param old_url: The previous absolute ``SITE`` URL.
        :param new_url: The new absolute ``SITE`` URL.
        :return: The list of changed post paths.
        """
        search = []
        if old_label != new_label:
            search.append(old_label)
        if old_url != new_url:
            search.append(old_url)
        if not search:
            return []
        where = " OR ".join("refs LIKE ?" for _ in search)
        params = [f"%{SEPARATOR}{ref}{SEPARATOR}%" for ref in search]
        changed = []
        for rel_path in self.path(self.POSTS, where=where, params=params):
            post = Post(rel_path)
            if not post.update_xref(old_label, new_label, old_url, new_url):
                continue
            rec = post.parse().record()
            self.update_records(
                table=self.POSTS,
                paths=rel_path,
                kvs={"content": rec.content, "refs": rec.refs},
            )
            changed.append(rel_path)
        return changed

    def update_tags(
        self, post: str | Post, kvs: dict[str, str] | dict[str, str | list[str]]
    ) -> None:
        if isinstance(post, str):
            path = post
            post = Post(path).parse()
        else:
            path = str(post.path)
        if post.update_tags(kvs):
            self.update_records(
                table=self.POSTS,
                paths=path,
                kvs={"tags": post.concat_tags()},
            )

    def update_title(self, post: str | Post) -> None:
        if isinstance(post, str):
            path = post
            post = Post(path).parse()
        else:
            path = str(post.path)
        if post.update_title():
            title_kvs = {"title": post.metadata["title"]}
            self.update_records(table=self.SRPS, paths=path, kvs=title_kvs)
            self.update_records(table=self.POSTS, paths=path, kvs=title_kvs)

    def insert_records(
        self, table: str, fields: str | list[str], values: Sequence[tuple[Any, ...]]
    ):
        if not isinstance(fields, str):
            fields = ", ".join(fields)
        sql = f"""
            INSERT INTO {table} (
                {fields}
            ) VALUES (
                {qmarks(fields)}
            )
            """
        self._conn.executemany(sql, values)

    def add_refs(self, paths: str | list[str], urls: str | list[str]) -> None:
        if isinstance(paths, str):
            paths = [paths]
        if isinstance(urls, str):
            urls = [urls]
        for path in paths:
            Post(path).parse().add_refs(urls)
        self.update_records(
            table=self.POSTS,
            paths=paths,
            kvs={"date": datetime.datetime.now().astimezone()},
        )

    def edit(self, paths: str | list[str], editor: str) -> None:
        """Edit the specified posts using the specified editor.

        Pending changes are committed first so that the SQLite write lock is not
        held for the whole (possibly very long) interactive editing session,
        which would block other blog.py instances.
        """
        self.commit()
        if isinstance(paths, str):
            paths = [paths]
        if not editor:
            raise ValueError("An editor must be specified.")
        if editor == "auto":
            suffixes = list(set(Path(path).suffix for path in paths))
            editor = get_preferred_editor(suffixes)
        sp.run(shlex.split(editor) + list(paths), check=True)

    def update_records(self, table: str, paths: str | Sequence[str], kvs: dict) -> None:
        """Update records corresponding to the specified paths.
        :param kvs: A dictionary of the form dict[field, value].
        :param paths: Paths of records to be updated.
        """
        if isinstance(paths, str):
            paths = [paths]
        sql = f"""
            UPDATE {table}
            SET {", ".join(f"{k} = ?" for k in kvs)}
            WHERE path in ({qmarks(paths)})
            """
        self._conn.execute(sql, list(it.chain(kvs.values(), paths)))

    def sync_dates(self):
        """Sync the date field of changed posts to their mtime."""
        status = porcelain.status(str(BASE_DIR))
        paths = set()
        for staged_paths in status.staged.values():
            paths.update(staged_paths)
        paths.update(status.unstaged)
        paths.update(status.untracked)
        for path_entry in paths:
            if isinstance(path_entry, bytes):
                path_str = path_entry.decode("utf-8")
            else:
                path_str = path_entry
            path = Path(path_str)
            if not (path.suffix in (MARKDOWN, IPYNB) and path.parts[0] == "docs"):
                continue
            if not path.exists():
                continue
            mtime = (
                datetime.datetime.fromtimestamp(path.stat().st_mtime)
                .astimezone()
                .replace(microsecond=0)
            )
            post = Post(path).parse()
            if post.metadata["date"] >= mtime:
                continue
            post.metadata["date"] = mtime
            post._should_write = True
            post.shutdown_hook()
            self.update_records(self.POSTS, path_str, {"date": mtime})

    def add_post(self, title: str, doc_dir: str, notebook: bool = True) -> str:
        """Add a new post with the given title."""
        label = _label(title)
        paths = self.path(
            self.POSTS,
            where="path LIKE ?",
            params=[f"%/{label}/index.%"],
        )
        if paths:
            print(f"\nA post with the specified title already exists.\n{paths[0]}\n")
            return paths[0]
        yyyymm = datetime.date.today().strftime("%Y/%m")
        dir_ = Path("docs") / doc_dir / yyyymm / label
        dir_.mkdir(parents=True, exist_ok=False)
        path = dir_ / ("index" + (IPYNB if notebook else MARKDOWN))
        post = Post(path)
        post.create(title)
        self.load_post(post)
        print("\nThe following post is added.\n", path, "\n", sep="")
        return str(path)

    def convert(self, path: str) -> None:
        path_new = Post(path).parse().convert()
        # The suffix changed, so srps has to be updated too; otherwise a
        # follow-up edit/vim on the same index opens the old, gone path.
        kvs = {"path": path_new}
        self.update_records(table=self.SRPS, paths=path, kvs=kvs)
        self.update_records(table=self.POSTS, paths=path, kvs=kvs)

    def empty_posts(self) -> None:
        """Load all empty posts into the table srps."""
        self.reload_posts()
        self._srps(where="empty = 1")

    def find_mismatch(self):
        self._srps(where="match = 0")

    def _srps(
        self, where: str, order_by: str = "", limit: int = 0, append: bool = False
    ) -> None:
        if not append:
            self.delete_records(self.SRPS, "")
        conditions = []
        if where:
            conditions.append(where)
        if append:
            conditions.append(f"path NOT IN (SELECT path FROM {self.SRPS})")
        where_clause = "WHERE " + " AND ".join(conditions) if conditions else ""
        sql = f"""
            INSERT INTO {self.SRPS}
            SELECT {self.SRPS_COLS}
            FROM {self.POSTS}
            {where_clause}
            {"ORDER BY " + order_by if order_by else ""}
            {f"LIMIT {limit}" if limit else ""}
            """
        self._conn.execute(sql)

    def search(self, phrase: str, filter_: str = "", append: bool = False):
        """Search for posts containing the phrase.

        :param phrase: The phrase to search for in posts.
        :param filter_: Extra filtering conditions.
        :param append: If True, append results to existing srps instead of replacing them.
        """
        conditions = []
        if phrase:
            conditions.append(f"posts MATCH '{phrase}'")
        if filter_:
            conditions.append(filter_)
        self._srps(where=" AND ".join(conditions), order_by="rank", append=append)

    def last(self, n: int):
        """Get last (according to modification time) n posts.
        :param n: The number of posts to get.
        """
        self._srps(where="", order_by="date DESC", limit=n)

    def path(
        self, table: str, where: str, params: Sequence[str | int] = ()
    ) -> list[str]:
        """Get paths correspondings to indexes in the srps table."""
        sql = f"""
            SELECT path FROM {table}
            {"WHERE " + where if where else ""}
            """
        return [row[0] for row in self._conn.execute(sql, params)]

    def gen_tags_md(self) -> None:

        def _num_links(k: str) -> int:
            return sum(len(tags[t]) for t in ids[k])

        sql = f"""
            SELECT label, date, tags FROM {self.POSTS}
            WHERE doc_dir != 'outdated'
            ORDER BY date DESC
        """
        tags: dict[str, list[tuple[str, str]]] = {}
        for label, date, tag_str in self._conn.execute(sql):
            link = f"[](#{label})"
            date_str = str(date)[:10]
            for tag in tag_str.strip(SEPARATOR).split(SEPARATOR):
                if not tag:
                    continue
                tags.setdefault(tag, [])
                tags[tag].append((link, date_str))

        ids: dict[str, list[str]] = {}
        for tag in tags:
            k = "tag-" + _label(tag)
            ids.setdefault(k, [])
            ids[k].append(tag)
        keys = [(k, n) for k in ids if (n := _num_links(k)) > 1]
        keys.sort(key=lambda pair: pair[1], reverse=True)
        with Path(BASE_DIR / "docs/tags.md").open("w", encoding="utf-8") as fout:
            fout.write("---\ntitle: Tags\nsite:\n  hide_outline: true\n---\n\n")
            for k, n in keys:
                entries: list[tuple[str, str]] = []
                for t in ids[k]:
                    entries.extend(tags[t])
                entries = list(dict.fromkeys(entries))
                entries.sort(key=lambda x: x[1], reverse=True)
                fout.write(f"## {' | '.join(ids[k])}\n")
                fout.write("```{dropdown} " + f"Click to expand/collapse {n} links\n")
                fout.write(":::{list-table}\n")
                fout.write(":header-rows: 1\n")
                fout.write(":widths: 70 30\n\n")
                fout.write("* - Title\n")
                fout.write("  - Date\n")
                for link, date_str in entries:
                    fout.write(f"* - {link}\n")
                    fout.write(f"  - {date_str}\n")
                fout.write(":::\n")
                fout.write("```\n\n")

    def gen_recent_posts(self, n: int = 20) -> None:
        sql = f"""
            SELECT label, date FROM {self.POSTS}
            WHERE doc_dir IN (?, ?)
            ORDER BY date DESC
            LIMIT ?
        """
        rows = self._conn.execute(sql, (ARTICLES, DRAFTS, n)).fetchall()
        path = BASE_DIR / "docs/recent_posts.md"
        with path.open("w", encoding="utf-8") as fout:
            fout.write(":::{list-table}\n")
            fout.write(":header-rows: 1\n")
            fout.write(":widths: 70 30\n\n")
            fout.write("* - Title\n")
            fout.write("  - Updated Date\n")
            for label, date in rows:
                date_str = str(date)[:10]
                fout.write(f"* - [](#{label})\n")
                fout.write(f"  - {date_str}\n")
            fout.write(":::\n")

    def tags(self, where: str = "", order_by: str = "") -> dict[str, list[str]]:
        """Get all tags and their frequencies in all posts.

        :param where: A filtering condition.
        """
        kvs = {}
        sql = f"""
            SELECT title, label, tags FROM {self.POSTS}
            {"WHERE " + where if where else ""}
            {"ORDER BY " + order_by if order_by else ""}
            """
        for title, label, tags in self._conn.execute(sql):
            link = f"[{title}]({label})"
            for tag in tags.strip(SEPARATOR).split(SEPARATOR):
                kvs.setdefault(tag, [])
                kvs[tag].append(link)
        return kvs

    def num_srps(self) -> int:
        row = self._conn.execute(f"SELECT count(*) FROM {self.SRPS}").fetchone()
        return row[0]

    def show(self, n: int, order_by: str = "") -> None:
        print("\nNumber of posts in srps:", self.num_srps())
        for row in self._conn.execute(
            f"""
            SELECT rowid, {self.SRPS_COLS}
            FROM {self.SRPS}
            {"ORDER BY " + order_by if order_by else ""}
            {f"LIMIT {n}" if n else ""}
            """
        ):
            rowid, path, title, label = row
            parts = list(Path(path).parts[0:5])
            parts[0] = SITE
            parts[-1] = parts[-1][:50]
            url = "/".join(parts)
            print(f"\n{rowid}: {title}  |  [](#{label})  |  {path}")
            print(f"    {url}  |  archives/blog/{path}")
        print("")
