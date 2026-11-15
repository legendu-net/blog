---
title: Tips on the Ruby Programming Language
created: '2012-08-06T11:28:52-07:00'
date: '2026-11-15T09:29:43-08:00'
authors:
  - bendu
label: tips-on-the-ruby-programming-language
license: CC-BY-4.0
tags:
  - array
  - IO
  - Ruby
  - programming
  - string
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

<img src="/media/ruby/ruby.png" height="200" width="200" align="right"/>

## Array

1. The method `push` inserts an element to the back of the array;
   the method `insert` inserts an element to any place of the array.

1. The method `pop` removes the last element of the array;
   the method `delete` removes any specified element from the array.

1. The method `concat` combines the array with another one;
   the method `join` concatenates all elements in the array separated
   by the specified delimiter.

## String

1. Use the method `to_i` to convert a string to integer.

1. You use both single and double quotes to denote string.
   The difference is that single quotes preserves
   escape characters while double quotes interpret escape characters.

1. The method `end_with?` check whether a string ends with the specified string.

1. The method `upcase` returns a copy of the string with lower case letters
   replaced with their upper case letters;
   the method `downcase` returns a copy of the string with upper case letters
   replaced with their lower case letters;
   the method `swapcase` return a copy of the string with lower case letters
   replaced with their upper case letters and upper case character replaced with
   their lower case letters.

1. Use the method `strip` to remove leading and trailing white spaces.

## Input and Output

1. Both the function `puts` and `print` display the content of objects
   on the console. The difference is that the function `puts` add a new line
   to the end if their is no one while `print` not.

1. The function `gets` read in input from the console.
   You can use the `chomp` method to ignore new lines,
   i.e., you can use `gets.chomp` to read a single line from the console.

## File and Directory

1. You can use the method `Dir.entries` to query files and subdirectories in a directory.

1. The method `File.delete` removes files specified files.
   The number of files passed as arguments is returned.

## Flow Control

1. You cannot use `else if` in Ruby, instead you can use `elsif`.

## Object and Class

1. Use `methods` to query all methods of an object.

1. You'd not define a function with the same as some directly usable function/method in Ruby.

## References

- [Ruby Regular Expression Editor](http://rubular.com/)
- [Ruby Documentation](http://www.ruby-doc.org/)
- [Ruby User Guide](http://www.rubyist.net/~slagell/ruby/regexp.html)
- [Ruby Basic Tutorial](http://www.troubleshooters.com/codecorn/ruby/basictutorial.htm)
- [RubyLearning](http://rubylearning.com/satishtalim/tutorial.html)
