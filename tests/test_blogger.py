import shlex
import sqlite3
import sys
from argparse import Namespace
from types import SimpleNamespace

import pytest

import blog
import blogger
from blogger import SITE, Blogger, Post


def _write_post(base, doc_dir, label, title, body):
    path = base / "docs" / doc_dir / "2021" / "04" / label / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    front = (
        "---\n"
        f"title: {title}\n"
        "created: 2021-04-01 00:00:00\n"
        "date: 2021-04-01 00:00:00\n"
        "authors:\n  - bendu\n"
        f"label: {label}\n"
        "license: CC-BY-4.0\n"
        "tags:\n  - programming\n"
        "---\n\n"
    )
    path.write_text(front + body, encoding="utf-8")
    return path


@pytest.fixture
def base_dir(tmp_path, monkeypatch):
    base = tmp_path.resolve()
    monkeypatch.setattr(blogger, "BASE_DIR", base)
    monkeypatch.chdir(base)
    # Posts write themselves at interpreter exit if they have pending changes;
    # that misfires once pytest restores the working directory, so disable it.
    monkeypatch.setattr(blogger.Post, "shutdown_hook", lambda self: None)
    return base


@pytest.fixture
def env(base_dir):
    base = base_dir
    # Post A is referenced by Post B both relatively and via an absolute URL.
    url_a = f"{SITE}/articles/2021/04/post-a"
    _write_post(base, "articles", "post-a", "Post A Renamed", "Body of A.\n")
    body_b = (
        f'See [Post A](post-a) and [abs]({url_a}).\n\n<a href="{url_a}">Post A</a>\n'
    )
    _write_post(base, "articles", "post-b", "Post B", body_b)
    bg = Blogger(db=str(base / ".blogger.sqlite3"))
    bg.reload_posts()
    bg.commit()
    return bg, base


def _refs(bg, rel_path):
    rows = list(bg._conn.execute("SELECT refs FROM posts WHERE path = ?", [rel_path]))
    return rows[0][0]


def test_refs_column_populated(env):
    bg, _ = env
    refs_b = _refs(bg, "docs/articles/2021/04/post-b/index.md")
    assert "|post-a|" in refs_b
    assert f"|{SITE}/articles/2021/04/post-a|" in refs_b


def test_match_title_updates_references(env):
    bg, base = env
    path_b = base / "docs/articles/2021/04/post-b/index.md"
    bg.match_title("docs/articles/2021/04/post-a/index.md")
    bg.commit()
    # The post directory is renamed to the new label.
    assert (base / "docs/articles/2021/04/post-a-renamed/index.md").exists()
    # Both the relative and absolute references in B are rewritten.
    text_b = path_b.read_text(encoding="utf-8")
    assert "[Post A](post-a-renamed)" in text_b
    assert f"{SITE}/articles/2021/04/post-a-renamed" in text_b
    assert "post-a)" not in text_b
    assert f"{SITE}/articles/2021/04/post-a)" not in text_b
    # B's refs row in the database is refreshed.
    refs_b = _refs(bg, "docs/articles/2021/04/post-b/index.md")
    assert "|post-a-renamed|" in refs_b
    assert "|post-a|" not in refs_b


def test_move_updates_absolute_url_only(env):
    bg, base = env
    path_b = base / "docs/articles/2021/04/post-b/index.md"
    bg.move("docs/articles/2021/04/post-a/index.md", "drafts")
    bg.commit()
    text_b = path_b.read_text(encoding="utf-8")
    # The absolute URL's doc_dir segment is updated ...
    assert f"{SITE}/drafts/2021/04/post-a" in text_b
    assert f"{SITE}/articles/2021/04/post-a" not in text_b
    # ... while the relative reference (label) is left untouched.
    assert "[Post A](post-a)" in text_b


# --- Post.update_xref -------------------------------------------------------


def _urls(old_label, new_label, doc_dir="articles"):
    base = f"{SITE}/{doc_dir}/2021/04"
    return f"{base}/{old_label}", f"{base}/{new_label}"


def _rewrite(base, raw, old_label, new_label, old_url, new_url):
    path = base / "docs/articles/2021/04/tmp/index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(raw, encoding="utf-8")
    n = Post(path).update_xref(old_label, new_label, old_url, new_url)
    return path.read_text(encoding="utf-8"), n


def test_update_xref_inline_relative(base_dir):
    old_url, new_url = _urls("old-label", "new-label")
    text, n = _rewrite(
        base_dir, "see ](old-label) ok", "old-label", "new-label", old_url, new_url
    )
    assert text == "see ](new-label) ok"
    assert n == 1


def test_update_xref_preserves_anchor(base_dir):
    old_url, new_url = _urls("old-label", "new-label")
    text, n = _rewrite(
        base_dir, "](old-label#setup)", "old-label", "new-label", old_url, new_url
    )
    assert text == "](new-label#setup)"
    assert n == 1


def test_update_xref_reference_definition(base_dir):
    old_url, new_url = _urls("old-label", "new-label")
    text, n = _rewrite(
        base_dir, "[Foo]: old-label\n", "old-label", "new-label", old_url, new_url
    )
    assert text == "[Foo]: new-label\n"
    assert n == 1


def test_update_xref_reference_definition_in_notebook_json(base_dir):
    # In a raw .ipynb the line is wrapped in quotes; the refdef must still match.
    old_url, new_url = _urls("old-label", "new-label")
    raw = '      "[Foo]: old-label\\n",\n'
    text, n = _rewrite(base_dir, raw, "old-label", "new-label", old_url, new_url)
    assert text == '      "[Foo]: new-label\\n",\n'
    assert n == 1


def test_update_xref_absolute_url_forms(base_dir):
    old_url, new_url = _urls("old-label", "new-label")
    raw = f"[t]({old_url}) <a href='{old_url}'>x</a> [r]: {old_url}\n"
    text, n = _rewrite(base_dir, raw, "old-label", "new-label", old_url, new_url)
    assert old_url not in text
    assert text.count(new_url) == 3
    assert n == 3


def test_update_xref_url_prefix_collision(base_dir):
    old_url, new_url = _urls("spark-sql", "renamed")
    raw = f"[t]({old_url}-tips)"
    text, n = _rewrite(base_dir, raw, "spark-sql", "renamed", old_url, new_url)
    assert text == raw
    assert n == 0


def test_update_xref_relative_prefix_collision(base_dir):
    old_url, new_url = _urls("old-label", "new-label")
    text, n = _rewrite(
        base_dir, "](old-label-extended)", "old-label", "new-label", old_url, new_url
    )
    assert text == "](old-label-extended)"
    assert n == 0


def test_update_xref_ignores_prose(base_dir):
    old_url, new_url = _urls("old-label", "new-label")
    text, n = _rewrite(
        base_dir, "old-label is a topic", "old-label", "new-label", old_url, new_url
    )
    assert text == "old-label is a topic"
    assert n == 0


def test_update_xref_move_rewrites_url_only(base_dir):
    # A move keeps the label but changes the doc_dir segment of the URL.
    old_url = f"{SITE}/drafts/2021/04/post-x"
    new_url = f"{SITE}/articles/2021/04/post-x"
    raw = f"[rel](post-x) and [abs]({old_url})"
    text, n = _rewrite(base_dir, raw, "post-x", "post-x", old_url, new_url)
    assert text == f"[rel](post-x) and [abs]({new_url})"
    assert n == 1


# --- Post._extract_xrefs ----------------------------------------------------


def _extract(base, body):
    post = Post(base / "docs/articles/2021/04/x/index.md")
    post.lines = [body]
    return post._extract_xrefs()


def test_extract_xrefs_relative_link(base_dir):
    assert _extract(base_dir, "see [Foo](build-docker-images) here") == [
        "build-docker-images"
    ]


def test_extract_xrefs_drops_anchor(base_dir):
    assert _extract(base_dir, "[Foo](some-post#setup)") == ["some-post"]


def test_extract_xrefs_reference_definition(base_dir):
    assert _extract(base_dir, "[Foo]: some-post\n") == ["some-post"]


def test_extract_xrefs_absolute_url(base_dir):
    url = f"{SITE}/articles/2021/04/date-functions-in-spark"
    assert _extract(base_dir, f"see [t]({url}) and <a href='{url}'>x</a>") == [url]


def test_extract_xrefs_ignores_non_post_targets(base_dir):
    body = f"[a](#anchor) [b](image.png) [c](../other) [d]({SITE}/articles/2021/04/foo)"
    assert _extract(base_dir, body) == [f"{SITE}/articles/2021/04/foo"]


def test_extract_xrefs_dedupes(base_dir):
    assert _extract(base_dir, "[a](post-x) and [b](post-x)") == ["post-x"]


def test_extract_xrefs_ignores_non_post_absolute_urls(base_dir):
    # Only canonical SITE/{doc_dir}/{YYYY}/{MM}/{label} URLs are post refs.
    body = f"[a]({SITE}/tags/#fun) [b]({SITE}/misc/blog/llm-in-rust)"
    assert _extract(base_dir, body) == []


def test_extract_xrefs_absolute_url_stops_at_label(base_dir):
    body = f"[a]({SITE}/articles/2021/04/post-a/extra)"
    assert _extract(base_dir, body) == [f"{SITE}/articles/2021/04/post-a"]


POST_A = "docs/articles/2021/04/post-a/index.md"


def test_busy_timeout_configured(base_dir):
    bg = Blogger(db=str(base_dir / ".blogger.sqlite3"))
    assert bg._conn.execute("PRAGMA busy_timeout").fetchone()[0] == 30000


def test_edit_commits_before_launching_editor(env, monkeypatch):
    # An editing session is unbounded, so no write transaction may be open
    # while the editor runs.
    bg, _ = env
    seen = {}
    # Replace the subprocess module as seen by blogger only, so that patching
    # does not leak into anything else shelling out during the test.
    fake_sp = SimpleNamespace(
        run=lambda *_, **__: seen.update(txn=bg._conn.in_transaction)
    )
    monkeypatch.setattr(blogger, "sp", fake_sp)
    bg.insert_records(Blogger.SRPS, Blogger.SRPS_COLS, [(POST_A, "Post A", "post-a")])
    assert bg._conn.in_transaction
    bg.edit([POST_A], editor="true")
    assert seen["txn"] is False


def test_second_process_can_write_while_editor_runs(env):
    # A stand-in editor that writes to the same database from another process,
    # i.e. what a second blog.py instance does while the first sits in NeoVim.
    bg, base = env
    db = str(base / ".blogger.sqlite3")
    script = (
        "import sqlite3;"
        f"conn = sqlite3.connect({db!r}, timeout=2);"
        f'conn.execute("INSERT INTO {Blogger.SRPS} ({Blogger.SRPS_COLS})'
        " VALUES ('other', 'Other', 'other')\");"
        "conn.commit()"
    )
    bg.insert_records(Blogger.SRPS, Blogger.SRPS_COLS, [(POST_A, "Post A", "post-a")])
    # Blogger.edit runs the editor with check=True, so a locked-out child fails here.
    bg.edit([POST_A], editor=shlex.join([sys.executable, "-c", script]))
    bg.commit()
    sql = "SELECT count(*) FROM srps WHERE path = 'other'"
    assert bg._conn.execute(sql).fetchone()[0] == 1


def test_convert_updates_srps_path(env):
    bg, _ = env
    bg.last(5)  # populate srps, as a search/last would before a convert
    bg.convert(POST_A)
    bg.commit()
    sql = f"SELECT count(*) FROM {Blogger.SRPS} WHERE path = ?"
    assert bg._conn.execute(sql, [POST_A.replace(".md", ".ipynb")]).fetchone()[0] == 1
    assert bg._conn.execute(sql, [POST_A]).fetchone()[0] == 0


def test_reload_posts_parses_before_deleting(env, monkeypatch):
    bg, _ = env
    sql = f"SELECT count(*) FROM {Blogger.POSTS}"
    num_posts = bg._conn.execute(sql).fetchone()[0]

    def _boom():
        raise RuntimeError("parse failed")

    monkeypatch.setattr(blogger, "_parse_records", _boom)
    with pytest.raises(RuntimeError):
        bg.reload_posts()
    assert bg._conn.execute(sql).fetchone()[0] == num_posts


def test_last_commits(env):
    bg, base = env
    sql = f"SELECT count(*) FROM {Blogger.SRPS}"
    blog.last(bg, Namespace(n=5))
    num_srps = bg._conn.execute(sql).fetchone()[0]
    assert num_srps
    # Only committed rows are visible to a separate connection.
    conn = sqlite3.connect(str(base / ".blogger.sqlite3"))
    try:
        assert conn.execute(sql).fetchone()[0] == num_srps
    finally:
        conn.close()


# --- update_title/update_tags --all-posts -----------------------------------


def test_update_title_all_posts_updates_db(base_dir):
    # get_post_paths() returns absolute paths, but Post._set_path normalizes
    # them relative to BASE_DIR, matching what's stored in the posts table; if
    # that normalization broke, the UPDATE below would silently match 0 rows.
    base = base_dir
    _write_post(base, "articles", "hello-world", "hello world", "Body.\n")
    rel_path = "docs/articles/2021/04/hello-world/index.md"
    bg = Blogger(db=str(base / ".blogger.sqlite3"))
    bg.reload_posts()
    bg.commit()
    blog.update_title(bg, Namespace(indexes=(), files=(), all=False, all_posts=True))
    sql = f"SELECT title FROM {Blogger.POSTS} WHERE path = ?"
    assert bg._conn.execute(sql, [rel_path]).fetchone()[0] == "Hello World"


def test_update_tags_all_posts_updates_db(base_dir):
    base = base_dir
    _write_post(base, "articles", "hello-world", "hello world", "Body.\n")
    rel_path = "docs/articles/2021/04/hello-world/index.md"
    bg = Blogger(db=str(base / ".blogger.sqlite3"))
    bg.reload_posts()
    bg.commit()
    blog.update_tags(
        bg,
        Namespace(
            indexes=(),
            files=(),
            all=False,
            all_posts=True,
            tags=("programming", "python"),
        ),
    )
    sql = f"SELECT tags FROM {Blogger.POSTS} WHERE path = ?"
    assert bg._conn.execute(sql, [rel_path]).fetchone()[0] == "|python|"


def test_flush_writes_immediately(tmp_path, monkeypatch):
    # Unlike base_dir, this does NOT neuter Post.shutdown_hook, so it exercises
    # blog._flush()'s actual disk-write path rather than the deferred,
    # write-at-interpreter-exit default.
    base = tmp_path.resolve()
    monkeypatch.setattr(blogger, "BASE_DIR", base)
    monkeypatch.chdir(base)
    path = _write_post(base, "articles", "flush-me", "flush me", "Body.\n")
    post = Post(path).parse()
    post.update_meta_field({"title": "Flushed"})
    assert post._should_write
    blog._flush(post)
    assert not post._should_write
    assert "title: Flushed" in path.read_text(encoding="utf-8")
