---
title: Manage Python Projects Using uv
created: '2025-04-30T06:16:38-07:00'
date: '2026-11-15T09:27:59-08:00'
authors:
  - bendu
label: manage-python-projects-using-uv
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Python
  - uv
  - project
  - management
  - virtualenv
  - dependency
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local/bin" sh

curl -LsSf https://astral.sh/uv/install.sh | sudo env UV_INSTALL_DIR="/usr/local/bin" sh
```

## Usage

### Run Executable Scripts of Python Packages

1. Format `pyproject.toml`.

   uvx pyproject-fmt pyproject.toml

1. Run `python -m http.server` to start a simple http server.

   ```
   uvx python -m http.server
   ```

1. Run the ruff tool.

   ```
   uvx ruff -h
   ```

1. Run `snb` from the aiutil package.

   ```
   uvx --from aiutil snb -h
   ```

### Ad-hoc Python Shell & Scripts

1. You can start an ad-hoc Python shell (
   e.g., Python 3.14 with 3rd-party packages dockeree and aituil
   ) using the following command.

   ```
   uv run --python 3.13 --with dockeree --with aiutil python
   ```

1. Similar to the above but start an IPython shell instead.

   ```
   uv run --python 3.13 --with dockeree --with aiutil --with IPython python -m IPython
   ```

1. Initialize a uv managed Python script.

   ```
   uv init --python 3.14 --script example.py 
   ```

   Notice that if the script `example.py` already exists,
   uv will just append metadata lines into it.

1. You can add dependencies to a uv managed Python scripts
   using the following command.

   ```
   uv add --script example.py 'requests<3' 'rich'
   ```

1. You can run a uv managed Python script using

   ```
   uv run /path/to/uv_managed_script.py
   ```

   or

   ```
   # preferred
   uv run --script /path/to/uv_managed_script.py
   ```

   Those 2 commands will automatically resolve and install dependencies specified in the script.
   This can be simplified by add the shebang
   `#!/usr/bin/env -S uv run`
   or `#!/usr/bin/env -S uv run --script`
   into the Python script,
   so that you can invoke the script as an executable directly.

1. You might want to pass Python interpreter options (e.g., the `-P` option)
   while running a script using `uv`.
   This can be done using the command below.

   ```
   uv run python -P /path/to/uv_managed_script.py
   ```

   However,
   it has one drawback.
   It doesn't automatically resolve and install dependencies specified in the script.
   Luckily,
   with [PR](https://github.com/astral-sh/uv/pull/12763) merged,
   this is possible through the option `--with-requirements script_with_deps.py`
   which includes inline dependency metadata from `script_with_deps.py`.
   So,
   you can use the following command (though it's verbose).

   ```
   uv run python -P /path/to/uv_managed_script.py --with-requirements uv_managed_script.py
   ```

### Manage Projects

1. Migrate from other Python projects to uv.

   ```
   uvx migrate-to-uv
   ```

1. Initialize a new uv project with the given name.

   ```
   uv init --package new_project_name
   ```

1. Initialize the current project as a uv project.

   ```
   uv init --package
   ```

1. Update the lock file (changing as little as possible).

   ```
   uv lock
   ```

1. Update the lock file ensuring that dependencies are the newest version allowed by the spec.

   ```
   uv lock --upgrade
   ```

1. Create a virtual environment if one doesn't already exist
   and install all dependencies.

   ```
   uv sync
   ```

   Install all dependencies including optional ones.

   ```
   uv sync --all-extras
   ```

   Install all dependencies but not the current project.

   ```
   uv sync --no-install-project
   ```

1. Build the project.

   ```
   uv build
   ```

1. Publish the project.

   ```
   uv publish
   ```

## References

- [uv Docs](https://docs.astral.sh/uv/)

- [uv @ GitHub](https://github.com/astral-sh/uv)

- [Adding a Trusted Publisher to an existing PyPI project](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)

- [How to Run a Python REPL with uv](https://pydevtools.com/handbook/how-to/how-to-run-a-python-repl-with-uv/)

- [Using uv as your shebang line](https://akrabat.com/using-uv-as-your-shebang-line/)
