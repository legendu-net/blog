Status: published
Date: 2023-03-05 21:24:58
Modified: 2023-03-05 21:24:58
Author: Benjamin Du
Slug: tips-on-visualize-sqlite
Title: Tips on Visualize-Sqlite
Category: Computer Science
Tags: Computer Science, programming, Rust, visualize, SQLite3, DOT, GraphViz

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


[visualize-sqlite](https://github.com/UhhhWaitWhat/visualize-sqlite)
is a Rust crate for creating simple visualizations 
of SQLite databases in GraphViz dot format.

## Installation

    wajig install libsqlite3-dev graphviz
    cargo install visualize-sqlite

## Usage

    visualize-sqlite your_sqlite_database.db | dot -Tpng -Gfontname='Fira Mono' -Gfontcolor='#586e75' -Gbgcolor='#fdf6e3' -Nfontname='Fira Mono' -Nfontcolor='#586e75' -Efontname='Fira Mono' > output.png

