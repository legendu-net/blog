Status: published
Author: Ben Chuanlong Du
Date: 2013-10-30 12:29:42
Slug: regex-equivalence
Title: Regular Expression Equivalent
Category: Computer Science
Tags: tips, regex, equivalent, regular expression, regexp, Python, R, CRAN, Perl, SAS, grep, egrep
Modified: 2021-10-31 11:04:04

1. The order of precedence of operators in POSIX extended regular expression is as follows.

    1. Collation-related bracket symbols `[==]`, `[::]`, `[..]`
    2. Escaped characters `\`
    3. Character set (bracket expression) `[]`
    4. Grouping `()`
    5. Single-character-ERE duplication `*`, `+`, `?`, `{m,n}`
    6. Concatenation
    7. Anchoring `^`, `$`
    8. Alternation `|`

2. Some regular expression patterns are defined using a single leading backslash, 
    e.g., `\s`, `\b`, etc.
    However, 
    since special characters (e.g., `\`) need to be escaped in strings in most programming languages,
    you will need the string `"\\s"` to represent the regular expression pattern `\s`,
    and similar for other regular expression patterns with a leading backslash. 
    Python is specialy as it provides raw strings (without escaping) to make it easier to write regular expression patterns. 
    It even goes one step further to auto correct non-properly escape strings. 
    For more discussions on Python regular expressions, 
    pleaser fer to
    [Regular Expression in Python](http://www.legendu.net/en/blog/regular-expression-python)
    .
    
3. It becomes tricky if you use a programming language to call another programming language to 
    perform regular expression operations.
    Taking `\s` for example,
    since `\` needs to be escaped in both programming languages, 
    you will end up using `\\\\s` to represent `\s`. 
    If you use Python to call other languages to perform regular expression patterns, 
    things can be simplifed by using raw strings in Python.
    For example, 
    instead of `"\\\\s"`,
    you can use `r"\\s"` in Python.

1. In some programming languages,
    you have to compile a plain/text pattern into a regular expression pattern object
    before using it.
    The Python module `re` automatically compiles a plain/text pattern 
    (using `re.compile`)
    and caches it,
    so there is not much benefit to compile regular expressions by yourself in Python.

2. `\W` does not include `^` and `$`.

3. Regular expression modifiers makes regular expression more flexible and powerful. 
    It is also a more universal way 
    than remembering different options in different programming languages or tools. 
    It is suggested that you use regular expression modifiers when possible.

4. Word boundry (`\b`) is a super set of white spaces (`\s`).

5. `[[:alnum:]]` contains all letters and numbers 
    while `\w` contains not only letters and numbers but also some special character such as `_`. 
    So in short `\w` is a super set of `[[:alnum:]]`.


<div style="overflow-x:auto;">
<table style="width:100%">
    <tr>
        <th> </th>
        <th> Vim search </th>
        <th> Python </th>
        <th> JavaScript </th>
        <th> Teradata SQL </th>
        <th> Oracle SQL </th>
        <th> grep </th>
        <th> sed </th>
    </tr>
    <tr>
        <td> Modifiers </td>
        <td> 
        </td>
        <td> 
            Partial<sup>[1]</sup>
        </td>
        <td> 
            Partial<sup>[1]</sup>
        </td>
        <td> Full </td>
        <td> 
            No<sup>[2]</sup> 
        </td>
        <td> Full[3] </td>
        <td> </td>
    </tr>
    <tr>
        <td> Greedy <br> or not</td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            Both<sup>[4]</sup>
        </td>
        <td> </td>
    </tr>
    <tr>
        <td> Popular <br> functions </td>
        <td> 
        </td>
        <td> 
            re.search, re.sub
        </td>
        <td> 
        </td>
        <td> 
            regexp_instr
        </td>
        <td> 
        </td>
        <td> </td>
        <td> </td>
    </tr>
    <tr>
        <td> White <br> spaces </td>
        <td> 
            <code>\s</code>
        </td>
        <td> 
            <code>"\\s" or r"\s" </code> 
            <sup> [5] </sup>
        </td>
        <td> 
        </td>
        <td> 
            [[:blank:]]
            [[:space:]]
        </td>
        <td> 
        </td>
        <td> 
            <code>\s</code> or <code>[[:space:]]</code>
        </td>
        <td> 
            <code>[[:space:]]</code> (recommended) or <code>\s</code>
        </td>
    </tr>
    <tr>
        <td> Non-white <br> space </td>
        <td> 
            <code> \S </code>
        </td>
        <td> 
            <code> "\\S" or r"\S" </code>
        </td>
        <td> 
        </td>
        <td> 
            [[:blank:]]
            [[:space:]]
        </td>
        <td> 
        </td>
        <td> 
            <code>\S</code>
        </td>
        <td> 
            <code>[^[:space:]]</code> or <code>\S</code>
        </td>
    </tr>
    <tr>
        <td> 
            Lower-case <br> letters
        </td>
        <td> 
            <code>[a-z]</code> or <code>\l</code>
        </td>
        <td> 
            <code>[a-z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[a-z]</code>
        </td>
        <td> 
            <code>[a-z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non lower-case <br> characters
        </td>
        <td> 
            <code>[^a-z]</code> or <code>\L</code>
        </td>
        <td> 
            <code>[^a-z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^a-z]</code>
        </td>
        <td> 
            <code>[^a-z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Upper-case <br> letters
        </td>
        <td> 
            <code>[A-Z]</code> or <code>\u</code>
        </td>
        <td> 
            <code>[A-Z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[A-Z]</code>
        </td>
        <td> 
            <code>[A-Z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non upper-case <br> characters
        </td>
        <td> 
            <code>[^A-Z]</code> or <code>\U</code>
        </td>
        <td> 
            <code>[^A-Z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^A-Z]</code>
        </td>
        <td> 
            <code>[^A-Z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Letters
        </td>
        <td> 
            <code>[a-zA-Z]</code> or <code>\a</code>
        </td>
        <td> 
            <code>[a-zA-Z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[a-zA-Z]</code>
        </td>
        <td> 
            <code>[a-zA-Z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non letters
        </td>
        <td> 
            <code>[^a-zA-Z]</code> or <code>\A</code>
        </td>
        <td> 
            <code>[^a-zA-Z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^a-zA-Z]</code>
        </td>
        <td> 
            <code>[^a-zA-Z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Digits
        </td>
        <td> 
            <code>\d</code>
        </td>
        <td> 
            <code> "\\d" or r"\d" </code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[[:digit:]]</code>
        </td>
        <td> 
            <code>\d</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non digits
        </td>
        <td> 
            <code>\D</code>
        </td>
        <td> 
            <code> "\\D" or r"\D" </code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^[:digit:]]</code>
        </td>
        <td> 
            <code>\D</code>
        </td>
    </tr>
    <tr>
        <td> 
            Hex digits
        </td>
        <td> 
            <code>[0-9a-fA-F]</code> or <code>\x</code>
        </td>
        <td> 
            <code>[0-9a-fA-F]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[0-9a-fA-F]</code>
        </td>
        <td> 
            <code>[0-9a-fA-F]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non-Hex digit <br> characters
        </td>
        <td> 
            <code>[^0-9a-fA-F]</code> or <code>\X</code>
        </td>
        <td> 
            <code>[^0-9a-fA-F]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^0-9a-fA-F]</code>
        </td>
        <td> 
            <code>[^0-9a-fA-F]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Octal digits
        </td>
        <td> 
            <code>[0-7]</code> or <code>\o</code>
        </td>
        <td> 
            <code>[0-7]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[0-7]</code>
        </td>
        <td> 
            <code>[0-7]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non-octal digit <br> Characters
        </td>
        <td> 
            <code>[^0-7]</code> or <code>\O</code>
        </td>
        <td> 
            <code>[^0-7]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^0-7]</code>
        </td>
        <td> 
            <code>[^0-7]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Head of word
        </td>
        <td> 
            <code>[a-zA-Z_]</code> or <code>\h</code>
        </td>
        <td> 
            <code>[a-zA-Z_]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[a-zA-Z_]</code>
        </td>
        <td> 
            <code>[a-zA-Z_]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non-head <br> of word
        </td>
        <td> 
            <code<code>[^a-zA-Z_]</code> or <code>\H</code>
        </td>
        <td> 
            <code>[^a-zA-Z_]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^a-zA-Z_]</code>
        </td>
        <td> 
            <code>[^a-zA-Z_]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Printable <br> Characters
        </td>
        <td> 
            <code>\p</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non printable <br> Characters
        </td>
        <td> 
            <code>\P</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Word characters
        </td>
        <td> 
            <code> \w</code>
        </td>
        <td> 
            <code> "\\w" or r"\w" </code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>\w</code>
        </td>
        <td> 
            <code>\w</code>
        </td>
    </tr>
    <tr>
        <td> 
            Word boundry
        </td>
        <td> 
            <code>\b</code>
        </td>
        <td> 
            <code> "\\b" or r"\b" </code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>\b</code>
        </td>
        <td> 
            <code>\b</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non word <br> characters
        </td>
        <td> 
            <code>\W</code>
        </td>
        <td> 
            <code>\W</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>\W</code>
        </td>
        <td> 
            <code>\W</code>
        </td>
    </tr>
    <tr>
        <td> 
            grouping
        </td>
        <td> 
            \(\)
        </td>
        <td> 
            ()
        </td>
        <td> 
            ()
        </td>
        <td> 
            ()
        </td>
        <td> 
            ()
        </td>
        <td> 
            \(\)
        </td>
        <td> 
            ()
        </td>
    </tr>
    <tr>
        <td> 
            0 or more 
            <br> matches
        </td>
        <td> 
            *
        </td>
        <td> 
            *
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            *
        </td>
        <td> 
            *
        </td>
    </tr>
    <tr>
        <td> 
            0 or more matches 
            <br> (as few as possible)
        </td>
        <td> 
            \\{-\\}
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            0 or 1 
            <br> matches
        </td>
        <td> 
            \=
        </td>
        <td> 
            ?
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            ?
        </td>
        <td> 
            ?
        </td>
    </tr>
    <tr>
        <td> 
            1 or more 
            <br> matches
        </td> 
        <td> 
            \+
        </td>
        <td> 
            +
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            +
        </td>
        <td> 
            +
        </td>
    </tr>
    <tr>
        <td> 
            Exactly m 
            <br> matches
        </td>
        <td> 
            \\{m\\}
        </td>
        <td> 
            {m}
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            {m}
        </td>
        <td> 
            {m}
        </td>
    </tr>
    <tr>
        <td> 
            m or more 
            <br> matches
        </td>
        <td> 
            \\{m,\\}
        </td>
        <td> 
            {m,}
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            {m,}
        </td>
        <td> 
            {m,}
        </td>
    </tr>
    <tr>
        <td> 
            m or more matches 
            <br> (as few as possible)
        </td>
        <td> 
            \\{-m,\\}
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            m to n 
            <br> matches
        </td>
        <td> 
            \\{m,n\\}
        </td>
        <td> 
            {m,n}
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            {m,n}
        </td>
        <td> 
            {m,n}
        </td>
    </tr>
    <tr>
        <td> 
            m to n matches 
            <br> (as few as possible)
        </td>
        <td> 
            \\{-m,n\\}
        </td> 
        <td> </td> 
        <td> </td> 
        <td> </td> 
        <td> </td> 
        <td> </td> 
        <td> </td>
    </tr>
    <tr>
        <td> 
            up to n 
            <br> matches
        </td>
        <td> 
            \\{,n\\}
        </td>
        <td> 
            {,n}
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            {,n}
        </td>
        <td> 
            {,n}
        </td>
    </tr>
    <tr>
        <td> 
            up to n matches 
            <br> (as few as possible)
        </td>
        <td> 
            \\{-,n\\}
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
    </tr>
    <tr>
        <td> 
            Any character 
            <br> except a newline
        </td>
        <td> 
            .
        </td>
        <td> 
            .
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            .
        </td>
        <td> 
            .
        </td>
    </tr>
    <tr>
        <td> 
            Start of 
            <br> a line
        </td>
        <td> 
            ^
        </td>
        <td> 
            ^
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            ^
        </td>
        <td> 
            ^
        </td>
    </tr>
    <tr>
        <td> 
            End of 
            <br> a line
        </td>
        <td> 
            $
        </td>
        <td> 
            $
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            $
        </td>
        <td> 
            $
        </td>
    </tr>
    <tr>
        <td> 
            Literal /
        </td>
        <td> 
        </td>
        <td> 
            \/ 
            <br> (need to escape)
        </td> 
        <td> 
        </td>
        <td> 
            / 
            <br> (no need to escape)
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Literal dot
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            \\.
        </td>
    </tr>
    <tr>
        <td> 
            Lookahead
        </td>
        <td> </td>
        <td> <a href="https://docs.python.org/3/library/re.html#index-20"> (?=...) </a> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            \\.
        </td>
    </tr>
    <tr>
        <td> 
            Negative lookahead
        </td>
        <td> </td>
        <td> <a href="https://docs.python.org/3/library/re.html#index-21"> (?!...) </a> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            \\.
        </td>
    </tr>
    <tr>
        <td> 
            Positive lookbehind
        </td>
        <td> </td>
        <td> <a href="https://docs.python.org/3/library/re.html#index-22"> (?&lt;=...) </a> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            \\.
        </td>
    </tr>
    <tr>
        <td> 
            Negative lookbehind
        </td>
        <td> </td>
        <td> <a href="https://docs.python.org/3/library/re.html#index-23"> (?&lt;!...) </a> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            \\.
        </td>
    </tr>
</table>
</div>

[1]: Python/JavaScript partially supports regular expression modifiers.
    To be more specifically,
    turning modifiers on is supported
    but turning modifiers off is not supported.
    Modifiers (once turned on) are applied to the entire regular expression
    and cannot be turned off.

[2]: Behavior of regular expressions in Oracle SQL 
    is control via parameters of regular expression  functions 
    instead of via regular expression modifiers.

[3]: `grep` fully supports regular expression modifiers 
    via Perl style regular (the `-P` option) expressions.

[4]: `grep` matches pattern greedly by default.
    However, 
    in Perl style syntax you can use the modifer `?` after a quantifier to perform a non-greedy match.
    For example, 
    instead of `.*` you can use `.*?` to do a non-greedy match.

[5]: As a matter of fact,
    `"\s"` also works in Python and it is equivalent to `"\\s"` and `r"\s"`.
    However,
    it is suggested that you avoid using `"\s"` as causes confusions
    especially when you call other programming languges (e.g., Spark SQL) 
    to run regular expression operations from Python.
    The raw string pattern `r"\s"` is preferred for its unambiguity and simplicity. 
    For more discussions on Python regular expressions,
    please refer to
    [Regular Expression in Python](http://www.legendu.net/en/blog/regular-expression-python)
    .

## References

- [Regular Expression Tester](https://regex101.com/)

- [Regular Expression in Python](http://www.legendu.net/en/blog/regular-expression-python)

- [Official Python Docs on Regular Expression](https://docs.python.org/3/library/re.html)

- [Regular Expression in Bash](http://www.legendu.net/misc/blog/regular-expression-in-bash/)

- [POSIX Extended Regular Expression Syntax](https://www.boost.org/doc/libs/1_56_0/libs/regex/doc/html/boost_regex/syntax/basic_extended.html#boost_regex.syntax.basic_extended.operator_precedence)

- [Operator Precedence of POSIX Extended Regular Expression](https://www.boost.org/doc/libs/1_56_0/libs/regex/doc/html/boost_regex/syntax/basic_extended.html#boost_regex.syntax.basic_extended.operator_precedence)