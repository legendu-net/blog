---
name: html-table-to-list-table
description: Convert HTML tables in markdown files into list-tables in MyST Markdown. Use when a user asks to convert HTML `<table>` markup to MyST list-tables, or mentions list-table conversion in docs. Ask the user for the path of the markdown files to convert.
---

# Convert HTML Tables to MyST List-Tables

Convert each HTML `<table>` found in markdown files into a
[list-table](https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#list-tables)
in MyST Markdown.

## When to use

- The user wants HTML tables (`<table>`, `<tr>`, `<td>`, ...) inside markdown
  files converted to MyST list-tables.
- Trigger phrases: "convert HTML table to list-table", "MyST list-table".

## Steps

1. **Ask for the path** of the markdown file(s) to convert before doing anything.
2. Convert each HTML table into a MyST list-table following the guidelines below.
3. Refer to the official docs on list-tables if needed:
   <https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#list-tables>

## Conversion guidelines

- Delimit the `list-table` directive with a backtick fence instead of colons (`:::`).

- For both levels of the generated list-table, use `- `, which means the very
  first row of the table starts with `- - `.

- Properly convert HTML hyperlinks defined using the `<a>` tag into markdown
  syntax. For example,
  `<a href="https://play.vercel.ai">AI Playground - Collection of LLMs</a>`
  should be converted to
  `[AI Playground - Collection of LLMs](https://play.vercel.ai)`.

- Some cells in the HTML table might span across multiple columns or rows.
  Handle that properly:
  - If a cell spans across multiple rows and multiple columns at the same time,
    duplicate the value in all rows and columns that the cell spans to.
  - If a cell spans across multiple rows only, keep the value in the first row
    and leave it empty in the other rows.
  - If a cell spans across multiple columns only, duplicate the value in all
    columns.

- Properly convert HTML superscript into footnote syntax in markdown. For
  example, `<sup>[1]</sup>` should be converted to `[^1]`.

- Preserve `<span>` tags which define colored text.
