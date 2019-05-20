Status: published
Date: 2019-05-20 19:37:23
Author: Benjamin Du
Slug: python-poetry-tips
Title: Python Poetry Tips
Category: Programming
Tags: programming, Python, poetry, build tool, dependency management

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.


https://poetry.eustace.io/docs/

## Usage
```Bash
poetry new proj
```

## Updating poetry

Updating poetry to the latest stable version is as simple as calling the self:update command.

```Bash
poetry self:update
```

If you want to install prerelease versions, you can use the --preview option.

```Bash
poetry self:update --preview
```

https://codingdose.info/2018/08/02/develop-and-publish-with-poetry/

https://hackersandslackers.com/poetic-python-project-packaging/

## User Tasks

https://github.com/sdispater/poetry/pull/591

https://github.com/sdispater/poetry/issues/241

## Python Version

Poetry supports the `env` subcomamnd starting from version 1.0.0.
You can use `poetry env use python_version` to specify the Python version to use for the project.
```Bash
poetry env use python3
```
## Activate Virtual Environment

`poetry shell` does not activate virtual environment currently, 
which is a bug. 
However, 
one alternative is to run the following command (starting from poetry 1.0.0beta2).
```Bash
source $(poetry env info -p)/bin/activate
```

## References

https://github.com/sdispater/poetry/issues/522

https://github.com/sdispater/poetry/issues/655

https://github.com/sdispater/poetry/issues/621


