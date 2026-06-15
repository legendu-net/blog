import pytest

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
