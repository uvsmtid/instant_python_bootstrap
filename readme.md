
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

will bootstrap the project `venv` on any platform in single click.

## Customization

```
./bootstrap.py --wizard
```

---

[bootstrap.py]: bootstrap.py
