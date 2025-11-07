
# instant_python_bootstrap

Place your own `bootstrap.py` verbatim copy next to `pyproject.toml`:

```
.
├── *
├── bootstrap.py
└── pyproject.toml
```

and this command:

```sh
./bootstrap.py
```

will bootstrap the project `venv`:
*   on any platform
*   in single click
*   with no args
*   with no deps
*   with no configs

## More info

This repo is a demo of a trivial setup for the [protoprimer][protoprimer_github]
extensible into any sophisticated bootstrap sequence with pure `python`.

---

[bootstrap.py]: bootstrap.py
[protoprimer_github]: https://github.com/uvsmtid/protoprimer
