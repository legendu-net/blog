UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2015-08-02 12:16:49
Slug: ultisnips-tips
Title: UltiSnips Tips
Category: Software
Tags: snippet, UltiSnips, tips, software

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. ultisnips list snippet does not show regex snippet. 
however, YouCompleteMe solves this problem perfectly!!!
It is suggested that you always use UltiSnips together with YouCompleteMe.

1. when use user-defined modules (e.g., complete), 
you have to make sure that all modules imported in the user-defined modules are installed.
Otherwise, you will get an error message 
"ImportError: no module named complete"
This can be miss leading as you might think that something is wrong with the path settings for the user-defined moduel, however, it is really a missing module used in the user-defined module (complete) which causes the problem.
And a fix can be really easy:
just install the missing module used in the user-defined module (complete).

1. It is suggested that you make a separate folder for snippet of each kind.
Split snippets into smaller parts according to functionalities.

2. When creating auto complete triggers, e.g., continue, 
do not use the full word. 
There are 2 reasons. 
First, auto complete is not needed if you have typed the full word. 
Second, if you use the full word as trigger for itself, it causes problems. 
The cursor will be trapped and never being able to jump to the next tab stop.

1. g:UltiSnipsSnippetsDir set private snip dir

2. extends sql loads sql snippets automatically

3.  snippet filename filetype ~
ruby.snippets ruby
perl.snippets perl
c.snippets c
c_my.snippets c
c/a c
c/b.snippets c
all.snippets *all
all/a.snippets *all

my question is that will they all get used or not?
and if we add snippets, which one is used?

1. Use `:UltiSnipsAddFiletypes` to assocate more snippets with current file. 
For example, `:UltiSnipsAddFiletypes text.markdown` associate text.snippets and markdown.snippets with current file.
Note that you can type in `:U` and then press up/down key to quick navigate to a previous UltiSnips command.

4. The suggested way to edit snippets is to open a (temp) file 
using vim and use the `:UltiSnipsEdit` command.

10. ultisnips $1 does not have to be continuous!!!

1. You can use the option `r` with other options. 
For example, you can use `rb`. 
However, `r` together with `w` does not work well. 
You should avoid using this combination.
To achieve "rw", use "\bTrigger".
r is dominant and drowns out all other options, so the w does nothing in your example. Reason is that regular expressions offer you all you want and more already. use \b(tolower|lcase) as your trigger.

4. A regular expression trigger (or part of it) can be used in a snippet using `match.group` in Python script.

2. It is suggested that you do not overuse regular expressions in UltiSnips.
Simpler solutions are usually better and more robust.
For example, instead of using regular expression `'write.table|wt'`, 
you can define two non-regular expression triggers `write.table` and `wt`. 
Though it seems that the latter rquires more work, 
it is more robust and less trouble-making.
If you use regular expression, 
you may soon come across issues of word bundary, white spaces, begin of line, etc.

3. If you defined a regular expression trigger `'\s*be'` with option `!r`,
you will find that when it is triggered the leading white spaces are eaten by the trigger.
One way is to solve this problem is to define `'(\s*)be'` 
with option `!r` and recover white spaces using `match.group(1)` in Python script.
A more convenient and elegant way is to define trigger `'be'` with option `!rb`.

4. If you use only one snippets directory, 
you must use the default "UltiSnips" directory 
in order for snippets for snippets (i.e., snippets.snippets) to work well.

5. Regular expression `/*` is represented as `'\/\*'` in UltiSnips but `'\\/\\*'` in Python. 

6. Both MATLAB and Mathematica has ".m" as file extensions,
however, ".m" is only recognized as file extension for MATLAB m-files. 
"mma.snippets" is the snippets file for Mathematica ".nb" files. 
You can manually add "mma.snippets" when you edit a Mathematica ".m" file.

7. A trigger should be quoted with `""` when it contains white spaces.

4. ignoring case and adjust accordingly is interesting in AutoHotkey and AutoKey. Can we do that in UltiSnips? you can do it using regular expression

11. it's better to use .markdown instead of .md

8. s.m or s. give options of str object methods, and also for other types of objects
or use .s .f, etc. to indicate ..., this is great!

12. I suggest that you use suffix _o 
to indicate that an argument is optional for python snippet

13. use python code to generate snippets for you!

14. a good way is to end variable names with "_s.". 
This make it easy for auto complete. 
another good way is to prompt for all funtions, supporting fuzz search, etc. ...

19. the vim module is not availble in a usual python session, 
but when you use python code in vim, it is avalaible. 


## Fantastic Ideas (not work)

9. an even cooler way is to use fuzz match for completing methods of ojects!!! 
And you should just copy and paste a page and then write code to parse the text to extract method and argument information

15. using vimscript to delete $1, etc. this give you the ability to use fuzz match, etc.

10. I think it's better to allow alias in UltiSnips. If the author don't add this, do it yourself!

1. use `extends file_type` to automatically include another snippet file.

2. if ultisnips fails to associate a file with the corresponding snippets,
you can do it manually.
for example, tex files

2. you can use tab stop to force the snippet jumps to a place.
this is very help when you want to use multi-step triggers

## Tricky Mistakes

1. Unmatched parenthesis when using regular expression triggers.

3. when using the "r" option, do not use other 
do not use the "r" option together with other options.
use regular expression to achive what you want.
"^\s*" for "b"
"\b" for "w"

1. Sometime the trigger `snip` (for snippets) does not expand in a snippet files.
This is probably due to the name you used for the snippet file 
contains special characters (e.g., underscore).
Vim highlight mode does not work if a snippet file is not recognized correctly.

2. "[" in regular expression, you should use "\[" instead

3. ultisnips: it seems that nested snippets causes troubles ...
it suggest that you manually type in nest snippets

ultisnips: it seems that problem occurs, 
if you delete some part of the snippets, 
but go back and then go forward can problem resolve the issue ...

ultisnips: it seems that if you put select there, it causes problem, but if you manually type it in, no problem ... very strange ...

4.  ultisnips: see whether you can resolve the tab completion vs snippet trigger issue: 
define different keys can definite solve the problem, check if superTab ...
you can define different keys and then use superTab to help you

5. Ultisnips import Multiple files ..., one compelete
the author does not like this idea
