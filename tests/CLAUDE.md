# tests/

Structural tests for the Semgrep rule YAML files. These are not Semgrep integration tests — they verify that each rule file is valid YAML and that every rule contains the four fields Semgrep requires to run: `id`, `message`, `languages`, and `severity`.

## Files

| File | Description |
|------|-------------|
| `test_placeholder.py` | Parametrized pytest suite: YAML validity, `rules` key presence, and required field checks across all four rule files |
| `__init__.py` | Empty marker making `tests/` a Python package |

## Running

```bash
pip install pytest pyyaml
pytest tests/ -v
```

The suite parametrizes over every `*.yaml` file in `rules/`, so new rule files are automatically picked up without changing the test code.

## What Is and Isn't Tested

**Tested:** YAML parse validity, top-level `rules` list exists and is non-empty, every rule has `id` + `message` + `languages` + `severity`.

**Not tested:** Whether Semgrep actually executes the rules correctly, whether `fix-regex` replacements produce correct output, whether patterns match the intended phrases. Those require `semgrep --config rules/ --test` with dedicated test fixture files. Adding Semgrep-native test fixtures (`.semgrep_test` files) is backlog work.
