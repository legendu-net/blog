# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

Ben Du's personal blogging system: a Python CLI that indexes/manages MyST Markdown & Jupyter Notebook posts and builds a static site with **Jupyter Book 2**, deployed to GitHub Pages (https://www.legendu.net). See https://deepwiki.com/legendu-net/blog for additional context.

## Commands

```bash
uv sync                      # install deps (Python >=3.14, managed by uv)
uv run pytest                # run all tests
uv run pytest tests/test_utils.py::test_name   # run a single test
uv run ruff format && uv run ruff check && uv run ty check && uv run deptry .   # lint/typecheck/dep-check (matches CI intent)
./blog.py -h                 # list CLI sub-commands
./blog.py <subcmd> -h        # help for a sub-command
```

Most work happens through `./blog.py`. Common subcommands (most have short aliases): `s`/search, `l`/list, `last`, `add`, `edit`, `vim`, `move`, `build`/`b`, `reload-posts`, `tags`, `trash`.

## Architecture

Two Python modules at the repo root do everything:

- **`blog.py`** — the CLI layer only. Each subcommand is registered by a `_subparse_*` function and dispatched via argparse `set_defaults(func=...)`. The entry point (`if __name__ == "__main__"`) constructs a single `Blogger()` and calls `args.func(blogger, args)`. To add a command: write a handler `def foo(blogger, args)`, write `_subparse_foo(subparsers)`, and register it in `parse_args`.
- **`blogger.py`** — all core logic:
  - `Post` — one post file. Parses YAML frontmatter + content, writes/reformats, converts between `.md` and `.ipynb`, validates required disclaimers, produces a `Record`.
  - `Blogger` — owns the SQLite connection and all index operations.
  - Module-level helpers — spells I/O, editor detection, title/label formatting, record parsing.

### Post storage convention

Posts live at `docs/{articles,drafts,outdated}/YYYY/MM/<slug>/index.{md,ipynb}` (see the glob in `_parse_records`/`get_post_paths`). The three top-level `doc_dir`s are `articles` (stable), `drafts` (immature; requires the drafts disclaimer), `outdated` (legacy; requires the outdated disclaimer). `DISCLAIMER_DRAFTS`/`DISCLAIMER_OUTDATED` are enforced by `Post._check_disclaimer`.

### The two-table index (key to the CLI UX)

The SQLite db `.blogger.sqlite3` (gitignored) has two tables:

- **`posts`** — an FTS5 virtual table (porter tokenizer) holding every post, columns = `POSTS_COLS`. Rebuilt from disk by `reload_posts`.
- **`srps`** — "search result posts", a plain table that `_srps()` overwrites on every `search`/`last`/`tags` with the current result set (`path, title, label`).

This is why the CLI is **index-based**: `search`/`list` print rows numbered by their `srps` rowid, and subsequent commands (`edit`, `vim`, `move`, `match-title`, …) take positional `indexes` that are resolved back to file paths via `Blogger.path("srps", ...)`. A `search` invalidates the previous `srps` numbering.

`Record` is a `namedtuple` whose fields are exactly `POSTS_COLS` — keep the two in sync when adding a column.

### `build` pipeline

`./blog.py build` runs: `reload_posts` → `commit` → `gen_toc()` (regenerates `docs/toc.yml` from the dated directory tree) → `gen_tags_md()` (writes `docs/tags.md`) → `jupyter-book build --html` in `docs/`. Site config is `docs/myst.yml` (extends the generated `docs/toc.yml`).

### Spells

`spells/spells_title.yml` and `spells/spells_tag.yml` are YAML correction maps applied to scraped/derived titles and tags (`read_spells_*`, `match_title`, `update_tags`). Add entries via `add-spells-title` / `add-spells-tag` subcommands rather than hand-editing logic.

## CI / deployment

- `.github/workflows/deploy.yml` — on push to `main`, runs `./blog.py build` and deploys `docs/_build/html` to GitHub Pages.
- `.github/workflows/create_pr_dev_to_main.yml` — on push to `dev`, auto-opens a PR into `main`.

## Conventions

- `ruff` excludes `docs/` and `*.ipynb`; `ty` excludes notebooks; `deptry` excludes `docs/`. Don't fight these — they're intentional (notebooks are content, not source).
- Content is MyST Markdown or Jupyter Notebooks with YAML frontmatter (title, author, tags, labels).
