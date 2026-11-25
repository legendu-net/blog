import pytest

from blog import _expand_indexes, parse_args


def test_expand_indexes_single():
    assert _expand_indexes(["3"]) == [3]
    assert _expand_indexes(["3", "5", "8"]) == [3, 5, 8]


def test_expand_indexes_range():
    assert _expand_indexes(["3-7"]) == [3, 4, 5, 6, 7]
    assert _expand_indexes(["0-0"]) == [0]


def test_expand_indexes_reversed_range():
    assert _expand_indexes(["7-3"]) == [3, 4, 5, 6, 7]


def test_expand_indexes_mixed():
    assert _expand_indexes(["1", "3-5", "9"]) == [1, 3, 4, 5, 9]


def test_expand_indexes_dedup_preserves_order():
    assert _expand_indexes(["3", "3"]) == [3]
    assert _expand_indexes(["1-3", "2", "2-4"]) == [1, 2, 3, 4]


def test_expand_indexes_empty():
    assert _expand_indexes([]) == []


@pytest.mark.parametrize("value", ["a", "3-", "-3", "1-2-3", "3.5"])
def test_expand_indexes_invalid_raises(value):
    with pytest.raises(ValueError):
        _expand_indexes([value])


def test_parse_args_expands_indexes():
    args = parse_args(["edit", "1", "3-5", "3"])
    assert args.indexes == [1, 3, 4, 5]


def test_parse_args_invalid_index_exits():
    with pytest.raises(SystemExit):
        parse_args(["edit", "a"])


@pytest.mark.parametrize("cmd", ["utitle", "utag"])
@pytest.mark.parametrize("flag", ["-A", "--all-posts"])
def test_parse_args_all_posts(cmd, flag):
    args = parse_args([cmd, flag])
    assert args.all_posts
    assert not args.all


@pytest.mark.parametrize("flag", ["-a", "--all-srps"])
def test_parse_args_all_srps_renamed(flag):
    assert parse_args(["utitle", flag]).all
    assert parse_args(["trash", flag]).all


def test_parse_args_all_still_unambiguous_prefix_elsewhere():
    # "trash" only has --all-srps, so --all remains an unambiguous prefix.
    assert parse_args(["trash", "--all"]).all


def test_parse_args_all_ambiguous_on_utitle():
    # utitle now has both --all-srps and --all-posts, so the bare --all
    # prefix is ambiguous and must fail loudly rather than guess.
    with pytest.raises(SystemExit):
        parse_args(["utitle", "--all"])


def test_parse_args_all_posts_not_available_elsewhere():
    with pytest.raises(SystemExit):
        parse_args(["trash", "-A"])


@pytest.mark.parametrize(
    "cmd",
    ["format", "fmt", "f", "format_notebook", "fnb", "format_markdown", "fmd"],
)
def test_parse_args_format_commands_no_args(cmd):
    args = parse_args([cmd])
    assert not args.indexes
    assert not args.files
    assert not args.all
    assert not args.all_posts


@pytest.mark.parametrize(
    "cmd",
    ["format", "fmt", "f", "format_notebook", "fnb", "format_markdown", "fmd"],
)
def test_parse_args_format_commands_targets(cmd):
    assert parse_args([cmd, "0", "1-3"]).indexes == [0, 1, 2, 3]
    assert parse_args([cmd, "--files", "a.md", "b.ipynb"]).files == [
        "a.md",
        "b.ipynb",
    ]
    assert parse_args([cmd, "-a"]).all
    assert parse_args([cmd, "--all-srps"]).all
    assert parse_args([cmd, "-A"]).all_posts
    assert parse_args([cmd, "--all-posts"]).all_posts


def test_resolve_format_paths_filters_and_defaults(monkeypatch, tmp_path):
    from typing import cast

    import blog
    from blogger import Blogger

    all_posts = [tmp_path / "a.md", tmp_path / "b.ipynb", tmp_path / "c.txt"]
    monkeypatch.setattr(blog, "get_post_paths", lambda: all_posts)

    class FakeBlogger:
        def path(self, table, where, params=()):
            return [str(tmp_path / "srp.md"), str(tmp_path / "srp.ipynb")]

    bg = cast(Blogger, FakeBlogger())
    # Default (no target) -> get_post_paths()
    assert blog._resolve_format_paths(bg, parse_args(["fmt"])) == [
        tmp_path / "a.md",
        tmp_path / "b.ipynb",
    ]
    assert blog._resolve_format_paths(bg, parse_args(["fnb"]), suffix=".ipynb") == [
        tmp_path / "b.ipynb"
    ]
    assert blog._resolve_format_paths(bg, parse_args(["fmd"]), suffix=".md") == [
        tmp_path / "a.md"
    ]
    # Indexes -> blogger.path
    assert blog._resolve_format_paths(bg, parse_args(["fmt", "0"])) == [
        tmp_path / "srp.md",
        tmp_path / "srp.ipynb",
    ]
    # --files
    assert blog._resolve_format_paths(
        bg, parse_args(["fnb", "--files", "x.md", "y.ipynb"]), suffix=".ipynb"
    ) == [blog.Path("y.ipynb")]
