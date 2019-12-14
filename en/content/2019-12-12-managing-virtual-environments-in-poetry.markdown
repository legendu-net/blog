Status: published
Date: 2019-12-14 12:35:10
Author: Benjamin Du
Slug: managing-virtual-environments-in-poetry
Title: Managing Virtual Environments in Poetry
Category: Programming
Tags: programming, Python, Poetry, virtual environment

## Where to Create Virtual Environments

By default,
Poetry create virtual environment in `$HOME/.poetry` for cahcing/sharing purpose.
However,
it is inconvenient if you use Docker-based web IDE for a Python project 
as you will lose the created virtual environment once the Docker container is restarted.
In that situation, 
you have to create a new virtual environment, 
set up the Python interpreter again,
which is tedious.
Fortunately, 
Poetry allows to create virtual environment in th root directory of a Python project,
and it is recommended to do so for the situation described above.
Run the following command to configure Poetry to create virtual environment in the root directory of the current project.
```bash
poetry config --local virtualenvs.in-project true
```
Notice that the above configure works for the current project only.
Use the following command
if you want to make Poetry always create virtual environment in the root directory of a project.
```bash
poetry config virtualenvs.in-project true
```


## Create a Virtual Environment

Poetry supports the `env` subcomamnd starting from version 1.0.0.
You can use `poetry env use python_version` to specify the Python version to use for the project.
```Bash
poetry env use python3
```

## Activate Vitual Environment

The virtual environment shell can be activated using the following command.
```bash
poetry shell
```

## Show Information of the Vitual Environment
```bash
poetry env info
```

## References

https://github.com/python-poetry/poetry/issues/108