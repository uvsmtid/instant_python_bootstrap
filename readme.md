
# instant_python_bootstrap

This [bootstrap.py][bootstrap_script] script hides "evolving setup details" from your users behind a **single click**.

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

## Why?

*   one-click
*   by default:
    *   no args
    *   no deps
    *   no configs
*   user-friendly: no tooling knowledge required
*   cross-platform: Linux, Mac, Windows
*   backed by: native `pip` or fast `uv`
*   pure `python` even before `venv` is ready

## Next: evolving setup details

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
