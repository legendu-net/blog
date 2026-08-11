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
