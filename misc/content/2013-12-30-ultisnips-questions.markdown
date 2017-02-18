UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2015-08-02 12:12:38
Slug: snippet
Title: Questions About UltiSnips
Category: Software
Tags: Software, UltiSnips, questions

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 

1. command :UltiSnipsListSnippets doesn't work?

6. how to remove file types added to an opened file for editing?

4. It seems that when you use multiple snippets for a file type (e.g., Python),
there's no main snippet? 
what I'm looking for that functions defined in one snippet file can be used in other files.


2. it seems that snippet.snippet doesn't support symbolic link? 
That is if I have "UltiSnip" point to a folder, then expansion won't work! 
It seems that only in a empy file? It seems that ... works in an empty file 
even if not open using the UltiSnipsEditor command.

4. UltiSnips 
	a. how to default to edit private snippets?
	b. why snippets (snip) doesn't trigger when edit directly?
ultisnips auto indent problem?

6. SnippetSyntaxError: Invalid multiword trigger: 'pa' in git/config/linux/common/vim/UltiSnips/r.snippets:5
Possibly because you used option `r` for a non-regular expression trigger, or miss '' for regular expression triggers.

9. fuzz complete and case-insensitive compelete has problem. 
One way to avoid this is to user later completions to correct them. 
fuzz matching, regular expression, etc. ...

11. The $0 tabstop is special: it defines the final position of the cursor, 
regardless of how many tabstops you specify.

1. why tex files are not recognized automatically?
Currently I have to manually add filetype, how to fix the problem?

2. it seems that there's a bug in UltiSnips when using mirror, 
if the typed text is shorter than the default one ..., 
the mirros are automatically extended using following characters ... 

3. how to set different keys for expand and ultisnip trigger

## Tricks and Traps

3. unbalanced parentheses in regular expression triggers causes tricky problems. 

ultisnips, can triggers be nested? that is, can I trigger use another trigger/
this is generally speaking not a good idea, you can manully invoke another snippet trigger ...

ultisnips: see how you can check whether a snippet is inside some procedure ...
