#!.venv/bin/python3
from argparse import ArgumentParser, Namespace
import getpass
import itertools as it
import os
from pathlib import Path
import subprocess as sp
from dulwich import porcelain
from dulwich.repo import Repo
from loguru import logger
from blogger import (
    BASE_DIR,
    ARTICLES,
    DRAFTS,
    OUTDATED,
    Blogger,
    add_spells_title as _add_spells_title,
    add_spells_tag as _add_spells_tag,
    get_vim,
    get_code,
    qmarks,
    format_title,
)

USER = getpass.getuser()
DASHES = "\n" + "-" * 100 + "\n"


INDEXES_HELP = (
    "Positve row IDs in the search results. "
    "Each value is a single ID (e.g. 3) or an inclusive range (e.g. 3-7)."
)


def _expand_indexes(values) -> list[int]:
    """Expand index/range strings into a deduplicated list of row IDs.

    Each value is either a single non-negative integer (e.g. ``"3"``) or an
    inclusive range ``"start-end"`` (e.g. ``"3-7"``). Reversed ranges such as
    ``"7-3"`` are normalized. The result preserves first-seen order with
    duplicates removed.

    :param values: An iterable of index/range strings.
    :return: A list of deduplicated row IDs.
    :raises ValueError: If a value is not a valid index or range.
    """
    indexes: list[int] = []
    for idx in values:
        try:
            if "-" in idx:
                start, end = idx.split("-")
                low, high = sorted((int(start), int(end)))
                indexes.extend(range(low, high + 1))
            else:
                indexes.append(int(idx))
        except ValueError as exc:
            raise ValueError(f"invalid index or range: '{idx}'") from exc
    return list(dict.fromkeys(indexes))


def option_indexes(subparser):
    """Add the positional option "indexes".

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "indexes",
        nargs="*",
        type=str,
        default=(),
        help=INDEXES_HELP,
    )


def option_files(subparser):
    """Add the option --files.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "--files", nargs="+", dest="files", default=(), help="Paths to files."
    )


def option_where(subparser):
    """Add the option --where.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-w",
        "--where",
        dest="where",
        default="",
        help="A user-specified filtering condition.",
    )


def option_dir(subparser):
    """Add the option --doc-dir.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-d",
        "--doc-dir",
        dest="doc_dir",
        default="",
        help="The doc directory to searching/querying operations.",
    )


def option_num(subparser):
    """Add the option -n.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-n", dest="n", type=int, default=5, help="Number of matched records to show."
    )


def option_full_path(subparser):
    """Add the option --full-path.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-F",
        "--full-path",
        dest="full_path",
        action="store_true",
        help="whether to show full (instead of short/relative) path.",
    )


def option_editor(subparser):
    """Add the option --editor.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-v",
        "--vim",
        dest="editor",
        action="store_const",
        const=get_vim(),
        default="auto",
        help="Edit the post using NeoVim/Vim.",
    )
    subparser.add_argument(
        "--code",
        "--vscode",
        dest="editor",
        action="store_const",
        const=get_code(),
        help="Edit the post using Code Server/VSCode.",
    )


def option_all(subparser):
    """Add the option --all.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-a",
        "--all",
        dest="all",
        action="store_true",
        help="Select all files in the search results.",
    )


def gen_toc(path: str | Path = BASE_DIR / "docs/toc.yml") -> None:
    mapping = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec",
    }

    def _gen_toc_month(dir_: str, year: str, month: str):
        path = Path(f"docs/{dir_}/{year}/{month}")
        if any(True for _ in path.glob("*/index.md")):
            if any(True for _ in path.glob("*/index.ipynb")):
                return f"""
            - title: "{mapping[month]}"
              children:
                - pattern: {dir_}/{year}/{month}/*/*.md
                - pattern: {dir_}/{year}/{month}/*/*.ipynb"""
            else:
                return f"""
            - title: "{mapping[month]}"
              children:
                - pattern: {dir_}/{year}/{month}/*/*.md"""
        else:
            if any(True for _ in path.glob("*/index.ipynb")):
                return f"""
            - title: "{mapping[month]}"
              children:
                - pattern: {dir_}/{year}/{month}/*/*.ipynb"""
            else:
                return ""
        path.glob()

    def _gen_toc_year(dir_: str, year: str):
        path = Path(f"docs/{dir_}/{year}")
        months = sorted((p.name for p in path.glob("??/")), reverse=True)
        return f"""
        - title: "{year}"
          children:""" + "".join(_gen_toc_month(dir_, year, month) for month in months)

    def _gen_toc_dir(dir_: str):
        path = Path(f"docs/{dir_}")
        years = sorted((p.name for p in path.glob("????/")), reverse=True)
        return (
            f"""
    - title: "{dir_.capitalize()}"
      children:""".strip("\n")
            + "".join(_gen_toc_year(dir_, year) for year in years)
        )

    text = "\n".join(
        [
            "version: 1",
            "project:",
            "  toc:",
            "    - file: index.md",
            _gen_toc_dir("articles"),
            _gen_toc_dir("drafts"),
            _gen_toc_dir("outdated"),
            "    - file: tags.md",
        ]
    )
    if isinstance(path, str):
        path = Path(path)
    path.write_text(text)


def move(blogger, args):
    _resolve_files(args)
    if args.files:
        blogger.move(args.files, args.target)
    blogger.commit()


def _resolve_files(args: Namespace) -> None:
    if "all" in args and args.all:
        args.files = blogger.path(Blogger.SRPS, where="")
        return
    if "indexes" in args and args.indexes:
        args.files = blogger.path(
            Blogger.SRPS,
            where=f"rowid IN ({qmarks(args.indexes)})",
            params=args.indexes,
        )


def trash(blogger, args):
    _resolve_files(args)
    if args.files:
        for index, file in enumerate(args.files):
            print(f"\n{index}: {file}")
        answer = input(
            "\nAre you sure to delete the specified files in the srps table (y/N): "
        )
        if answer.lower() in ("y", "yes"):
            blogger.trash(args.files)
    else:
        print("No file to delete is specified!\n")
    blogger.commit()


def _subparse_trash(subparsers):
    desc = "Move posts to the trash directory."
    subparser_trash = subparsers.add_parser(
        "trash", aliases=["rm"], help=desc, description=desc
    )
    option_indexes(subparser_trash)
    option_all(subparser_trash)
    option_files(subparser_trash)
    subparser_trash.set_defaults(func=trash)


def find_mismatch(blogger, args):
    blogger.find_mismatch()
    blogger.show(args.n)
    blogger.commit()


def _subparse_find_mismatch(subparsers):
    desc = "Find posts where their label and title are mismatched."
    subparser_find_mismatch = subparsers.add_parser(
        "findmismatch",
        aliases=["fmm"],
        help=desc,
        description=desc,
    )
    option_num(subparser_find_mismatch)
    option_full_path(subparser_find_mismatch)
    subparser_find_mismatch.set_defaults(func=find_mismatch)


def match_title(blogger, args):
    _resolve_files(args)
    if not args.files:
        print("No specifed files to update labels to match titles!\n")
        return
    for file in args.files:
        blogger.match_title(file)
    blogger.commit()


def vim(blogger, args):
    args.editor = get_vim()
    edit(blogger, args)


def edit(blogger, args):
    _resolve_files(args)
    if args.files:
        blogger.edit(args.files, args.editor)
    else:
        print("No post is specified for editing!\n")
    blogger.commit()


def add_spells_title(_, args):
    if len(args.words) % 2:
        raise ValueError("Words for spell corrections must be in pairs.")
    _add_spells_title(it.batched(args.words, 2))


def add_spells_tag(_, args):
    if len(args.words) % 2:
        raise ValueError("Words for spell corrections must be in pairs.")
    _add_spells_tag(it.batched(args.words, 2))


def add_refs(blogger, args):
    _resolve_files(args)
    if args.files:
        blogger.add_refs(args.files, args.urls)
    else:
        print("No post is specified for adding references!\n")
    blogger.commit()


def search(blogger, args):
    filter_ = []
    if args.filter:
        filter_.append(" ".join(args.filter))
    if args.doc_dir:
        dirs = ", ".join(f"'{d}'" for d in args.doc_dir)
        filter_.append(f"doc_dir IN ({dirs})")
    if args.tags:
        tags = " ".join(args.tags)
        filter_.append(f"tags MATCH '{tags}'")
    if args.title:
        args.title = " ".join(args.title)
        filter_.append(f"title MATCH '{args.title}'")
    blogger.search(" ".join(args.phrase), " AND ".join(filter_))
    blogger.show(args.n)
    blogger.commit()


def last(blogger, args):
    blogger.last(args.n)
    blogger.show(args.n)


def add(blogger, args):
    title = format_title(" ".join(args.title))
    file = blogger.add_post(title, args.doc_dir, notebook=args.notebook)
    blogger.edit(file, args.editor)
    blogger.insert_records(
        table=Blogger.SRPS,
        fields=Blogger.SRPS_COLS,
        values=[(file, title, Path(file).parts[4])],
    )
    blogger.show(n=1, order_by="rowid DESC")
    blogger.commit()


def update_tags(blogger, args):
    if len(args.tags) % 2:
        raise ValueError("Tags for update must be in pairs.")
    _resolve_files(args)
    if args.files:
        kvs = dict(it.batched(args.tags, 2))
        for file in args.files:
            blogger.update_tags(file, kvs)
    else:
        print("No file is specified for updating tags!\n")
    blogger.commit()


def update_title(blogger, args):
    _resolve_files(args)
    if args.files:
        for file in args.files:
            blogger.update_title(file)
    else:
        print("No file is specified for updating title!\n")
    blogger.commit()


def tags(blogger, args):
    tags = blogger.tags(where=args.where)
    for tag in tags:
        print(tag)


def _auth_kwargs(repo: Repo) -> dict:
    """Dynamically determine authentication kwargs for git push."""
    push_kwargs = {}
    config = repo.get_config()
    remote_url = config.get((b"remote", b"origin"), b"url")
    if remote_url.startswith(b"http"):
        github_token = os.environ.get("GITHUB_TOKEN")
        if github_token:
            push_kwargs["username"] = "PersonalAccessToken"
            push_kwargs["password"] = github_token
    return push_kwargs


def auto_git_push(blogger, args):
    """Push changes in this repository."""
    blogger.sync_dates()
    blogger.commit()
    repo = Repo(str(BASE_DIR))
    porcelain.add(repo)
    porcelain.commit(repo, message=b"add/update posts")
    porcelain.push(repo, "origin", "main", **_auth_kwargs(repo))


def clean_db(blogger, _):
    blogger.clean_db()


def exec_notebook(blogger, args):
    _resolve_files(args)
    if args.files:
        cmd = [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--inplace",
            "--execute",
        ] + args.files
        sp.run(cmd, check=True)


def format_notebook(_, args):
    # TODO: is this necessary?
    # Can you use ruff to format notebooks? And if so, you can do this directly, right?
    # _resolve_files(args)
    cmd = f"black {BASE_DIR}"
    sp.run(cmd, shell=True, check=True)


def _subparse_format_notebook(subparsers):
    desc = "Format notebooks."
    subparser_format_notebook = subparsers.add_parser(
        "format_notebook",
        aliases=["format", "fmt", "f"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_format_notebook)
    option_files(subparser_format_notebook)
    option_all(subparser_format_notebook)
    subparser_format_notebook.set_defaults(func=format_notebook)


def _subparse_trust_notebooks(subparsers):
    desc = "Trust notebooks."
    subparsers.add_parser(
        "trust_notebooks",
        aliases=["trust"],
        help=desc,
        description=desc,
    )


def _subparse_exec_notebook(subparsers):
    desc = "Execute a notebook."
    subparser_exec_notebook = subparsers.add_parser(
        "exec_notebook",
        aliases=["exec"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_exec_notebook)
    option_files(subparser_exec_notebook)
    subparser_exec_notebook.set_defaults(func=exec_notebook)


def _subparse_clean_db(subparsers):
    desc = "Remove the underlying SQLite3 database."
    subparser_clean_db = subparsers.add_parser(
        "clean_db",
        help=desc,
        description=desc,
    )
    subparser_clean_db.set_defaults(func=clean_db)


def _subparse_update_tags(subparsers):
    desc = "update tags of posts."
    subparser_utag = subparsers.add_parser(
        "update_tags",
        aliases=["utag"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_utag)
    option_files(subparser_utag)
    option_all(subparser_utag)
    subparser_utag.add_argument(
        "-t",
        "--tags",
        dest="tags",
        nargs="*",
        default=(),
        help="Tag pairs in the format o1 n1 o2 n2...",
    )
    subparser_utag.set_defaults(func=update_tags)


def _subparse_update_title(subparsers):
    desc = "update titles of posts."
    subparser_utitle = subparsers.add_parser(
        "update_title",
        aliases=["utitle"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_utitle)
    option_files(subparser_utitle)
    option_all(subparser_utitle)
    subparser_utitle.set_defaults(func=update_title)


def _subparse_tags(subparsers):
    desc = "List all tags and their frequencies."
    subparser_tags = subparsers.add_parser(
        "tags",
        aliases=["t"],
        help=desc,
        description=desc,
    )
    option_where(subparser_tags)
    option_dir(subparser_tags)
    subparser_tags.set_defaults(func=tags)


def reload_posts(blogger, _):
    blogger.reload_posts()
    blogger.commit()


def _subparse_reload_posts(subparsers):
    desc = "Reload information of posts."
    subparser_reload = subparsers.add_parser(
        "reload_posts",
        aliases=["reload", "r"],
        help=desc,
        description=desc,
    )
    subparser_reload.set_defaults(func=reload_posts)


def _subparse_last(subparsers):
    desc = "List recently changed posts."
    subparser_last = subparsers.add_parser(
        "last",
        aliases=[],
        help=desc,
        description=desc,
    )
    option_num(subparser_last)
    option_full_path(subparser_last)
    subparser_last.set_defaults(func=last)


def _subparse_list(subparsers):
    desc = "List last search results."
    subparser_list = subparsers.add_parser(
        "show",
        aliases=["list", "l"],
        help=desc,
        description=desc,
    )
    option_num(subparser_list)
    option_full_path(subparser_list)
    subparser_list.set_defaults(func=lambda blogger, args: blogger.show(args.n))


def _subparse_search(subparsers):
    desc = (
        "Search for posts. "
        "Tokens separated by spaces ( ) or plus signs (+) in the search phrase "
        "are matched in order with tokens in the text. "
        "ORDERLESS match of tokens can be achieved by separating them with the AND keyword. "
        "You can also limit match into specific columns. "
        "For more information, please refer to https://sqlite.org/fts5.html"
    )
    subparser_search = subparsers.add_parser(
        "search",
        aliases=["s"],
        help=desc,
        description=desc,
    )
    subparser_search.add_argument(
        "phrase",
        nargs="*",
        default=(),
        help="The phrase to match in posts. "
        "The phrase is optional. "
        "For example if you want to filter by category only without constraints on full-text search, "
        "you can use ./blog.py s the -c some_category.",
    )
    subparser_search.add_argument(
        "-i",
        "--title",
        nargs="+",
        dest="title",
        default=(),
        help="Search for posts with the sepcified title.",
    )
    subparser_search.add_argument(
        "-t",
        "--tags",
        nargs="+",
        dest="tags",
        default=(),
        help="Search for posts with the sepcified tags.",
    )
    subparser_search.add_argument(
        "-d",
        "--doc-dir",
        dest="doc_dir",
        nargs="+",
        default=(),
        help="Search for posts in the specified sub blog directory.",
    )
    subparser_search.add_argument(
        "-f",
        "--filter",
        dest="filter",
        nargs="+",
        default=(),
        help="Futher filtering conditions in addition to the full-text match.",
    )
    option_num(subparser_search)
    option_full_path(subparser_search)
    subparser_search.set_defaults(func=search)


def _subparse_add(subparsers):
    desc = "Add a new post."
    subparser_add = subparsers.add_parser(
        "add", aliases=["a"], help=desc, description=desc
    )
    option_editor(subparser_add)
    subparser_add.add_argument(
        "-a",
        "--articles",
        dest="doc_dir",
        action="store_const",
        const=ARTICLES,
        default=DRAFTS,
        help="Create a post in the en sub blog directory.",
    )
    group = subparser_add.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-m",
        "--markdown",
        dest="notebook",
        action="store_false",
        help="Create a MarkDown (default Notebook) post.",
    )
    group.add_argument(
        "-n",
        "--notebook",
        "--ipynb",
        dest="notebook",
        action="store_true",
        help="Create a MarkDown (default Notebook) post.",
    )
    subparser_add.add_argument(
        "title", nargs="+", help="Title of the post to be created."
    )
    subparser_add.set_defaults(func=add)


def _subparse_vim(subparsers):
    desc = "Edit a post using Vim."
    subparser_vim = subparsers.add_parser(
        "vim",
        aliases=["v"],
        help=desc,
        description=desc,
    )
    subparser_vim.add_argument("indexes", nargs="*", type=str, help=INDEXES_HELP)
    subparser_vim.add_argument(
        "-f",
        "--files",
        nargs="+",
        default=[],
        dest="files",
        help="Path of the post to be edited.",
    )
    subparser_vim.set_defaults(func=vim)


def _subparse_edit(subparsers):
    desc = "Edit posts."
    subparser_edit = subparsers.add_parser(
        "edit",
        aliases=["e"],
        help=desc,
        description=desc,
    )
    subparser_edit.add_argument("indexes", nargs="*", type=str, help=INDEXES_HELP)
    option_editor(subparser_edit)
    subparser_edit.add_argument(
        "-f",
        "--files",
        nargs="+",
        default=[],
        dest="files",
        help="Path of the post to be edited.",
    )
    subparser_edit.set_defaults(func=edit)


def _subparse_add_spells_title(subparsers):
    desc = "Add spell corrections."
    subparser_add_spells_title = subparsers.add_parser(
        "add_spells_title",
        aliases=["ast"],
        help=desc,
        description=desc,
    )
    subparser_add_spells_title.add_argument(
        "words", nargs="+", help="Word pairs in the format w1 c1 w2 c2..."
    )
    subparser_add_spells_title.set_defaults(func=add_spells_title)


def _subparse_add_spells_tag(subparsers):
    desc = "Add tag spell corrections."
    subparser_add_spells_tag = subparsers.add_parser(
        "add_spells_tag",
        aliases=["astag"],
        help=desc,
        description=desc,
    )
    subparser_add_spells_tag.add_argument(
        "words", nargs="+", help="Word pairs in the format w1 c1 w2 c2..."
    )
    subparser_add_spells_tag.set_defaults(func=add_spells_tag)


def _subparse_add_refs(subparsers):
    desc = "Add URL references into posts."
    subparser_add_refs = subparsers.add_parser(
        "add_refs",
        aliases=["ar"],
        help=desc,
        description=desc,
    )
    subparser_add_refs.add_argument("indexes", nargs="*", type=str, help=INDEXES_HELP)
    subparser_add_refs.add_argument(
        "-f",
        "--files",
        nargs="+",
        default=[],
        dest="files",
        help="Path of the post to be edited.",
    )
    subparser_add_refs.add_argument(
        "-u",
        "--urls",
        nargs="+",
        required=True,
        dest="urls",
        help="URLs to be added as references.",
    )
    subparser_add_refs.set_defaults(func=add_refs)


def _subparse_move(subparsers):
    desc = "Move a post."
    subparser_move = subparsers.add_parser(
        "move",
        aliases=["m"],
        help=desc,
        description=desc,
    )
    subparser_move.add_argument("indexes", type=str, nargs="*", help=INDEXES_HELP)
    subparser_move.add_argument(
        "-f", "--files", nargs="*", dest="files", help="Path of the post to be moved."
    )
    subparser_move.add_argument(
        "-t", "--target", dest="target", default=DRAFTS, help="Path of destination file"
    )
    subparser_move.add_argument(
        "-a",
        "--articles",
        dest="target",
        action="store_const",
        const=ARTICLES,
        help="Move to the articles sub blog directory.",
    )
    subparser_move.add_argument(
        "-d",
        "--drafts",
        dest="target",
        action="store_const",
        const=DRAFTS,
        help="Move to the drafts sub blog directory.",
    )
    subparser_move.add_argument(
        "-o",
        "--out",
        "--outdated",
        dest="target",
        action="store_const",
        const=OUTDATED,
        help="Move to the outdated sub blog directory.",
    )
    subparser_move.set_defaults(func=move)


def _subparse_match_title(subparsers):
    desc = "match post name and title"
    subparser_match_post = subparsers.add_parser(
        "matchtitle",
        aliases=["mt"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_match_post)
    option_all(subparser_match_post)
    subparser_match_post.set_defaults(func=match_title)


def _subparse_auto(subparsers):
    desc = "Auto push the Git repository."
    subparser_auto = subparsers.add_parser(
        "auto_git_push",
        aliases=["auto", "agp", "ap"],
        help=desc,
        description=desc,
    )
    subparser_auto.set_defaults(func=auto_git_push)


def _subparse_git_status(subparsers):
    desc = "The git status command."
    subparser_status = subparsers.add_parser(
        "status",
        aliases=["st", "sts"],
        help=desc,
        description=desc,
    )
    subparser_status.set_defaults(func=_git_status)


def _subparse_git_diff(subparsers):
    desc = "The git diff command."
    subparser_git = subparsers.add_parser(
        "diff",
        aliases=["df", "dif"],
        help=desc,
        description=desc,
    )
    subparser_git.add_argument(
        "file", nargs="*", default=(), help="Path of the post to run git diff on."
    )
    subparser_git.set_defaults(func=_git_diff)


def _git_status(_, __):
    sp.run("git status", shell=True, check=True)


def _git_diff(_, args):
    sp.run(f"git diff {' '.join(args.file)}", shell=True, check=True)


def _git_pull(blogger, args):
    logger.info("Pulling origin/main ...")
    sp.run("git pull origin main && git status", shell=True, check=True)
    reload_posts(blogger, args)


def _subparse_git_pull(subparsers):
    desc = "The git pull command."
    subparser_status = subparsers.add_parser(
        "pull",
        aliases=["pu"],
        help=desc,
        description=desc,
    )
    subparser_status.set_defaults(func=_git_pull)


def empty_posts(blogger, args):
    blogger.empty_posts()
    blogger.show(args.n)
    blogger.commit()


def _subparse_empty_posts(subparsers):
    desc = "Find empty post."
    subparser_status = subparsers.add_parser(
        "empty",
        aliases=["em"],
        help=desc,
        description=desc,
    )
    option_num(subparser_status)
    option_full_path(subparser_status)
    subparser_status.set_defaults(func=empty_posts)


def convert(blogger, args):
    _resolve_files(args)
    if args.files:
        for file in args.files:
            blogger.convert(file)


def _subparse_convert(subparsers):
    desc = "Convert markdown/notebook to notebooks/markdown."
    subparser_convert = subparsers.add_parser(
        "convert",
        aliases=["conv"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_convert)
    option_files(subparser_convert)
    subparser_convert.set_defaults(func=convert)


def srp(blogger, args):
    if args.keep is not None:
        blogger.keep_srps(_expand_indexes(args.keep))
    elif args.remove is not None:
        blogger.remove_srps(_expand_indexes(args.remove))
    blogger.show(args.n)
    blogger.commit()


def _subparse_srp(subparsers):
    desc = "Keep or remove posts from the search results (srps table)."
    subparser_srp = subparsers.add_parser(
        "srp",
        help=desc,
        description=desc,
    )
    group = subparser_srp.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-k",
        "--keep",
        dest="keep",
        nargs="+",
        default=None,
        metavar="INDEX",
        help=INDEXES_HELP,
    )
    group.add_argument(
        "-r",
        "--remove",
        dest="remove",
        nargs="+",
        default=None,
        metavar="INDEX",
        help=INDEXES_HELP,
    )
    option_num(subparser_srp)
    subparser_srp.set_defaults(func=srp)


def build(blogger, _):
    """Build the blog."""
    blogger.reload_posts()
    blogger.commit()
    gen_toc()
    blogger.gen_tags_md()
    cmd = f"""cd {BASE_DIR}/docs && \
        NODE_OPTIONS=--max-old-space-size=8192 uv run jupyter-book build --html"""
    sp.run(cmd, shell=True, check=True)


def _subparse_build(subparsers):
    desc = "Build the blog."
    subparser_build = subparsers.add_parser(
        "build",
        aliases=["b"],
        help=desc,
        description=desc,
    )
    subparser_build.set_defaults(func=build)


def parse_args(args=None, namespace=None) -> Namespace:
    """Parse command-line arguments.

    :param args: The arguments to parse.
        If None, the arguments from command-line are parsed.
    :param namespace: An inital Namespace object.
    :return: A namespace object containing parsed options.
    """
    parser = ArgumentParser(description="Write blog in command line.")
    subparsers = parser.add_subparsers(dest="sub_cmd", help="Sub commands.")
    _subparse_build(subparsers)
    _subparse_update_tags(subparsers)
    _subparse_update_title(subparsers)
    _subparse_tags(subparsers)
    _subparse_reload_posts(subparsers)
    _subparse_list(subparsers)
    _subparse_last(subparsers)
    _subparse_search(subparsers)
    _subparse_srp(subparsers)
    _subparse_add(subparsers)
    _subparse_edit(subparsers)
    _subparse_add_refs(subparsers)
    _subparse_add_spells_title(subparsers)
    _subparse_add_spells_tag(subparsers)
    _subparse_vim(subparsers)
    _subparse_move(subparsers)
    _subparse_auto(subparsers)
    _subparse_clean_db(subparsers)
    _subparse_git_status(subparsers)
    _subparse_git_diff(subparsers)
    _subparse_git_pull(subparsers)
    _subparse_empty_posts(subparsers)
    _subparse_trash(subparsers)
    _subparse_find_mismatch(subparsers)
    _subparse_match_title(subparsers)
    _subparse_exec_notebook(subparsers)
    _subparse_format_notebook(subparsers)
    _subparse_trust_notebooks(subparsers)
    _subparse_convert(subparsers)
    parsed_args = parser.parse_args(args=args, namespace=namespace)
    if hasattr(parsed_args, "indexes") and parsed_args.indexes:
        try:
            parsed_args.indexes = _expand_indexes(parsed_args.indexes)
        except ValueError as exc:
            parser.error(f"argument indexes: {exc}")
    return parsed_args


if __name__ == "__main__":
    blogger = Blogger()
    args = parse_args()
    args.func(blogger, args)
