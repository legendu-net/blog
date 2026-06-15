from blogger import _concat, qmarks


def test_qmarks_int():
    assert qmarks(1) == "?"
    assert qmarks(2) == "?, ?"
    assert qmarks(3) == "?, ?, ?"


def test_qmarks_list():
    assert qmarks(["path", "atime"]) == "?, ?"
    assert qmarks(["a", "b", "c"]) == "?, ?, ?"


def test_qmarks_str():
    assert qmarks("path, atime") == "?, ?"
    assert qmarks("a, b, c") == "?, ?, ?"


def test_qmarks_single_field_str():
    assert qmarks("path") == "?"


def test_concat():
    assert _concat([], "|") == ""
    assert _concat(["a"], "|") == "|a|"
    assert _concat(["a", "b"], "|") == "|a|b|"
