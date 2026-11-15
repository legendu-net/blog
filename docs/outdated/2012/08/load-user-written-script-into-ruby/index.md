---
title: Load User-written Script into Ruby
created: '2012-08-25T00:00:00-07:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: load-user-written-script-into-ruby
license: CC-BY-4.0
tags:
  - search path
  - require
  - programming
  - load
  - package
  - Ruby
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

<img src="/media/ruby/ruby.png" height="200" width="240" align="right"/>

By default the current working directoly is not in the search path of Ruby.
To load a user-written script named "script.rb" into Ruby,
you can use the command `require './script.rb'`.
