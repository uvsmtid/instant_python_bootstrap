
# instant_python_bootstrap

A "drop-in" [bootstrap.py][bootstrap_script] script for ((pure) `python`) projects.

## Why?

It eliminates users' efforts by hiding "continuously evolving setup details":

*   single-click
*   zero thinking = no args
*   immediately usable:
    *   no deps
    *   no configs
*   simplicity **vs** flexibility:
    *   basic outside: no tooling knowledge required
    *   standard inside: native `pip` or fast `uv`
*   cross-platform: Linux, Mac, Windows
*   single lang: pure `python` even before `venv` is ready

## How?

*   Install:

    ```
    ./
    ├── bootstrap.py   <--- own copy
    ├── pyproject.toml
    └── *
    ```

    Add your **own copy** of `bootstrap.py` next to your `pyproject.toml`.

*   Run (click):

    ```sh
    ./bootstrap.py
    ```

## Next: continuously evolving setup details

This repo demonstrates a trivial use case (extend-able into any sophisticated bootstrap sequence).

When you need more - see [protoprimer][protoprimer_github]:
<details>
<summary>advanced features</summary>

<br>

*   handle environment-specific config
*   extend the bootstrap sequence by custom steps
*   configure any directory structure layout
*   maintain multiple `pyproject.toml` in a monorepo
*   support other pure `python` scripts even before `venv` is ready

</details>

---

[bootstrap_script]: bootstrap.py
[protoprimer_github]: https://github.com/uvsmtid/protoprimer
