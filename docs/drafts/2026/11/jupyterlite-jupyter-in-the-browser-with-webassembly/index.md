---
title: 'JupyterLite: Jupyter in the Browser with WebAssembly'
created: '2026-11-25T02:55:28.060416-08:00'
date: '2026-11-25T02:55:28.060425-08:00'
authors:
  - bendu
label: jupyterlite-jupyter-in-the-browser-with-webassembly
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Python
  - Jupyter
  - JupyterLite
  - WebAssembly
  - WASM
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Overview

[JupyterLite](https://github.com/jupyterlite/jupyterlite) is a JupyterLab and Jupyter Notebook distribution that runs **entirely in the browser** via WebAssembly (Wasm) and Web Workers. Because code execution, file storage, and the UI all live client-side, a compiled JupyterLite deployment consists purely of static assets—no Python server, container orchestrator, or backend kernel is required.

## Architecture & Kernels

Core JupyterLite ships without a default kernel; you bundle one or more browser-compatible kernels when building the static site:

1. **Pyodide (`jupyterlite-pyodide-kernel`)**:
   - Runs CPython compiled to WebAssembly via Emscripten, backed by IPython (supporting IPython magics and inline Matplotlib).
   - Pure-Python wheels from PyPI can be installed at runtime using `piplite` (built on `micropip`), e.g., `await piplite.install("ipywidgets")`.
2. **Xeus (`jupyterlite-xeus` / `jupyterlite-xeus-python`)**:
   - Loader for Xeus-based kernels (including `xeus-python`, C++, Lua, and SQLite) compiled to WebAssembly.
   - Pre-built scientific packages (including many C/C++ extensions) are pulled from [`emscripten-forge`](https://emscripten-forge.org/) via Conda/Mamba tooling, and environments can be pre-configured at build time with an `environment.yml` file.
3. **Client-Side Storage**:
   - Notebooks and workspace files are persisted in the browser's `IndexedDB` / `localStorage`.
   - Storage is per-origin and ephemeral if browser site data is cleared, so important `.ipynb` files should be downloaded or synced externally.

## Quick Start & Static Deployment

Install `jupyterlite-core` along with a kernel package, build the static site, and preview it locally:

```bash
pip install jupyterlite-core jupyterlite-pyodide-kernel
# Or use xeus-python instead:
# pip install jupyterlite-xeus-python

jupyter lite build --contents ./notebooks
jupyter lite serve
```

`jupyter lite build` outputs a self-contained static directory (`_output/` by default) that can be deployed directly to GitHub Pages, GitLab Pages, Read the Docs, Netlify, or embedded alongside documentation in Jupyter Book / MyST sites.

## Strengths & Limitations

**Strengths**

- **Zero server cost & effortless scaling**: Static hosting handles arbitrary concurrent users without provisioning containers or GPUs.
- **Instant sharing & onboarding**: Interactive tutorials, documentation examples, and classrooms open with a single URL.
- **Client-side privacy**: Code and local data never leave the user's browser.

**Limitations**

- **Package compatibility**: Libraries with native C/C++/Fortran/Rust extensions (e.g., `torch`, `psycopg2`, `h5py`) only work if pre-compiled for Pyodide or `emscripten-forge`.
- **No raw sockets or subprocesses**: Browser sandboxing blocks arbitrary TCP/UDP sockets, database drivers requiring raw sockets, and `subprocess` spawning.
- **CORS restrictions**: HTTP requests from inside the kernel are subject to browser Cross-Origin Resource Sharing (CORS) policies.
- **Memory & compute caps**: Execution is constrained by browser tab memory limits (typically ~2–4 GB) and lacks native CUDA/GPU access.

## Comparison with Alternatives

| Feature / Dimension | JupyterLite | Binder | JupyterHub | Marimo (Wasm) |
| :--- | :--- | :--- | :--- | :--- |
| **Execution location** | Browser (Wasm) | Cloud containers | Managed server / K8s | Browser (Wasm / Pyodide) |
| **Backend required** | No (static files) | Yes (ephemeral) | Yes (persistent) | No (static files) |
| **Startup latency** | Fast (browser cache) | Slow (image pull/build) | Fast–Medium | Fast (browser cache) |
| **Native C/GPU/sockets** | No | Yes (CPU; limited) | Yes | No |
| **Notebook format** | Standard `.ipynb` | Standard `.ipynb` | Standard `.ipynb` | Reactive `.py` |

## References

- [JupyterLite: Jupyter ❤️ WebAssembly ❤️ Python (Jupyter Blog)](https://blog.jupyter.org/jupyterlite-jupyter-%EF%B8%8F-webassembly-%EF%B8%8F-python-f6e2e41ab3fa)
- [JupyterLite GitHub Repository](https://github.com/jupyterlite/jupyterlite)
- [JupyterLite Official Documentation](https://jupyterlite.readthedocs.io)
- [](#tips-on-wasm)
- [](#tips-on-jupyterlab)
- [](#tips-on-jupyter-binder)
- [](#tips-on-jupyterhub)
- [](#tips-on-jupyter-book)
