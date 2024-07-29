Status: published
Date: 2024-07-22 13:39:40
Modified: 2024-07-22 13:39:40
Author: Benjamin Du
Slug: editing-shell-commands-using-vim
Title: Editing Shell Commands Using Vim
Category: Computer Science
Tags: Computer Science, programming

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


3. Bash supports both Vi mode and Emacs mode.
    The default is Emacs mode.
    You can turn on the Vim mode by `set -o vi` in `.bashrc`.

export EDITOR=vim

A better way is to use ctrl+x ctrl+e

And if you need previous command, you can read them into vim using
:r ! tail -20 ~/.bash_history

tail -n 20 ~/.bash_history | egrep -v '^#'

## References
How do I edit current shell command in VI
https://apple.stackexchange.com/questions/88515/how-do-i-edit-current-shell-command-in-vi

Recall the Previous Command or Its Arguments in Bash
https://www.baeldung.com/linux/bash-recall-previous-command

After years of bash, I actually found a shortcut I never heard about.

https://www.reddit.com/r/linux/comments/13q4l4s/after_years_of_bash_i_actually_found_a_shortcut_i/

Edit any command line in vim
https://www.reddit.com/r/vim/comments/9atgsj/edit_any_command_line_in_vim/