Status: published
Date: 2020-03-03 15:04:23
Author: Ben Chuanlong Du
Slug: shell-alternatives
Title: Python Alternatives to Shell
Category: Programming
Tags: programming, IPython, shell, bash, xonsh, plumbum, Python, shell alternatives

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.


## Python Equivalent of Shell Commands

<table style="width:100%">
  <tr>
    <th> Shell Command </th>
    <th> Alternative </th>
    <th> Python </th>
  </tr>
  <tr>
    <td> mkdir -p /path/to/some/file </td>
    <td> Path("path/to/some/file").mkdir(exist_ok=True) </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> mkdir -p /path/to/some/file </td>
    <td> os.makedirs("/path/to/some/file", exist_ok=True) </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> mkdir -p /path/to/some/file </td>
    <td> !mkdir -p /path/to/some/file </td>
    <td> IPython </td>
  </tr>
  <tr>
    <td> mkdir -p /path/to/some/file </td>
    <td> mkdir -p /path/to/some/file </td>
    <td> xonsh </td>
  </tr>
  <tr>
    <td> cp file1 file2 </td>
    <td> shutil.copy2("file1", "file2") </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> cp file1 file2 </td>
    <td> shutil.copyfile("file1", "file2") </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> cp file1 file2 </td>
    <td> !cp file1 file2 </td>
    <td> IPython </td>
  </tr>
  <tr>
    <td> cp file1 file2 </td>
    <td> cp file1 file2 </td>
    <td> xonsh </td>
  </tr>
  <tr>
    <td> ln -s file1 file2 </td>
    <td> Path("file1").symlink_to("file2", target_is_directory=True) </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> ln -s file1 file2 </td>
    <td> os.symlink("file1", "file2", target_is_directory=True) </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> ln -s file1 file2 </td>
    <td> !ln -s file1 file2 </td>
    <td> IPython </td>
  </tr>
  <tr>
    <td> ln -s file1 file2 </td>
    <td> ln -s file1 file2 </td>
    <td> xonsh </td>
  </tr>
  <tr>
    <td> ln -sT file1 file2 </td>
    <td> Path("file1").symlink_to("file2", target_is_directory=False) </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> ln -sT file1 file2 </td>
    <td> os.symlink("file1", "file2", target_is_directory=False) </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> ln -sT file1 file2 </td>
    <td> !ln -sT file1 file2 </td>
    <td> IPython </td>
  </tr>
  <tr>
    <td> ln -sT file1 file2 </td>
    <td> ln -sT file1 file2 </td>
    <td> xonsh </td>
  </tr>
  <tr>
    <td> rm file </td>
    <td> os.remove(file) </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> rm file </td>
    <td> !rm file </td>
    <td> IPython </td>
  </tr>
  <tr>
    <td> rm file </td>
    <td> rm file </td>
    <td> xonsh </td>
  </tr>
  <tr>
    <td> rm -rf dir </td>
    <td> shutil.rmtree(dir) </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> rm -rf dir </td>
    <td> !rm -rf dir </td>
    <td> IPython </td>
  </tr>
  <tr>
    <td> rm -rf dir </td>
    <td> rm -rf dir </td>
    <td> xonsh </td>
  </tr>
  <tr>
    <td> mv file1 file2 </td>
    <td> Path("file1").rename("file2") </td>
    <td> pathlib </td>
  </tr>
  <tr>
    <td> mv file1 file2 </td>
    <td> shutil.move("file1", "file2") </td>
    <td> shutil </td>
  </tr>
  <tr>
    <td> mv file1 file2 </td>
    <td> os.rename("file1", "file2") </td>
    <td> Python </td>
  </tr>
  <tr>
    <td> mv file1 file2 </td>
    <td> !mv file1 file2 </td>
    <td> IPython </td>
  </tr>
  <tr>
    <td> mv file1 file2 </td>
    <td> mv file1 file2 </td>
    <td> xonsh </td>
  </tr>
</table>

## [xonsh](https://github.com/xonsh/xonsh)

xonsh is the best and simplest Python approach to replace (most part of) shell so far.

## [IPython](https://github.com/ipython/ipython)

IPython is the best and simpliest Python approach to replace (all part of) shell so far.

https://ipython.readthedocs.io/en/stable/interactive/magics.html

https://github.com/ivanov/vim-ipython

1. Use the IPython shell or JupyterLab notebook (preferred) instead of Shell for complicated interactive operations.

2. Be careful about illegal shell commands.
    For example,
    `ls )` in Bash shell throws the error message `bash: syntax error near unexpected token )`.
    If you have a equivalent IPython command,
    it will throw the same error message.
    For example,
    suppose `file` is path of a file which contains `)`
    then `!ls {file}` in IPython will throws the same error message as above.
    However,
    this is definitely trickier to debug than the original Bash shell command `ls )`.
    There are several ways to avoid this.
    First,
    you can use Python script
    ([xonsh](https://github.com/xonsh/xonsh) is a great choice is vanilla Python script is too verbose)
    instead Shell as underlying commands.
    Second,
    you can show the underlying Shell commands for debugging.

3. You can even run Shell commands on a remote server (via `ssh` or a remote kernel) in JupyterLab notebook.
    This provide the advantage of leveraging the JupyterLab notebook UI.


## [plumbum](https://github.com/tomerfiliba/plumbum)

Yet another Python approach as a replacement of shell.
I personally prefer IPython and xonsh to plumbum.



## References

https://github.com/ninjaaron/replacing-bash-scripting-with-python

https://stackoverflow.com/questions/209470/how-to-implement-common-bash-idioms-in-python

https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python

https://docs.python.org/3/library/pathlib.html#module-pathlib