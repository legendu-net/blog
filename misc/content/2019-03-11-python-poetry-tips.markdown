Status: published
Date: 2019-12-12 12:24:34
Author: Benjamin Du
Slug: python-poetry-tips
Title: Python Poetry Tips
Category: Programming
Tags: programming, Python, poetry, build tool, dependency management

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.


[Poetry Documentation](https://poetry.eustace.io/docs/)

## Usage

```Bash
poetry new proj
```

```Bash
poetry init
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

## Run Test Suits Using Pytest
```bash
poetry run pytest
```
Or if you want to make it specific to collect test suits from the `test` directory 
under the root directory of the project.
```bash
poetry run pytest test
```

## Configuration

https://python-poetry.org/docs/cli/#config

https://python-poetry.org/docs/configuration/

## References

https://github.com/sdispater/poetry/issues/522

https://github.com/sdispater/poetry/issues/655

https://github.com/sdispater/poetry/issues/621


