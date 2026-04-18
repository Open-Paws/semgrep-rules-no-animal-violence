<!-- tech_stack: semgrep, yaml, python, javascript, go -->
<!-- project_status: active -->
<!-- difficulty: beginner -->
<!-- skill_tags: static-analysis, inclusive-language, ci-cd, semgrep -->
<!-- related_repos: no-animal-violence, eslint-plugin-no-animal-violence, vale-no-animal-violence, no-animal-violence-pre-commit, no-animal-violence-action, vscode-no-animal-violence, reviewdog-no-animal-violence, danger-plugin-no-animal-violence -->

# semgrep-rules-no-animal-violence

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Semgrep](https://img.shields.io/badge/semgrep-rules-blue)](https://semgrep.dev)
[![Rules](https://img.shields.io/badge/rules-62%2B%20patterns-green)](rules/)
[![Languages](https://img.shields.io/badge/languages-generic%20%7C%20Python%20%7C%20JS%2FTS%20%7C%20Go-informational)](rules/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)](https://pre-commit.com)
[![Open Paws](https://img.shields.io/badge/Open%20Paws-AI%20for%20animal%20liberation-orange)](https://openpaws.ai)

Semgrep rules for detecting speciesist language — idioms, metaphors, and tech jargon that normalize harm to animals — in code, comments, documentation, and configuration files. Covers 62+ patterns across four severity levels for generic text, Python, JavaScript/TypeScript, and Go.

Language-specific rules support `--autofix` for automated replacement. All rules are auto-generated from the canonical [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) dictionary and run in production CI.

> [!NOTE]
> This project is part of the [Open Paws](https://openpaws.ai) ecosystem — AI infrastructure for the animal liberation movement. [Explore the full platform →](https://github.com/Open-Paws)

## Example match

Running the generic rule against a Python file that contains a common idiom:

```
$ semgrep --config rules/animal-violence-generic.yaml example.py

example.py
  7:result = "We killed two birds with one stone here."
          ERROR  animal-violence.kill-two-birds-with-one-stone
                 "kill two birds with one stone" uses violence against animals as a metaphor.
                 Use "accomplish two things at once" instead.
```

Running with autofix on a Python file:

```
$ semgrep --config rules/animal-violence-python.yaml --autofix example.py

example.py
  7:result = "We accomplished two things at once here."
```

## Quickstart

**1. Install Semgrep**

```bash
pip install semgrep
```

**2. Run all rules against your project (no clone needed)**

```bash
semgrep --config https://raw.githubusercontent.com/Open-Paws/semgrep-rules-no-animal-violence/master/rules/animal-violence-generic.yaml \
        --config https://raw.githubusercontent.com/Open-Paws/semgrep-rules-no-animal-violence/master/rules/animal-violence-python.yaml \
        --config https://raw.githubusercontent.com/Open-Paws/semgrep-rules-no-animal-violence/master/rules/animal-violence-javascript.yaml \
        --config https://raw.githubusercontent.com/Open-Paws/semgrep-rules-no-animal-violence/master/rules/animal-violence-go.yaml \
        /path/to/your/project
```

**3. Run with autofix (language-specific rules only)**

```bash
semgrep --config https://raw.githubusercontent.com/Open-Paws/semgrep-rules-no-animal-violence/master/rules/animal-violence-python.yaml \
        --autofix /path/to/your/project
```

**4. Validate rule syntax**

```bash
git clone https://github.com/Open-Paws/semgrep-rules-no-animal-violence.git
cd semgrep-rules-no-animal-violence
semgrep --config rules/ --validate
```

**5. Add to CI via the dedicated GitHub Action**

```yaml
# .github/workflows/inclusive-language.yml
name: Inclusive Language Check
on: [pull_request]

jobs:
  nav-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: Open-Paws/no-animal-violence-action@v1
```

## Features

**Rule files**

| File | Mode | Target | Autofix | Pattern count |
|------|------|--------|---------|---------------|
| `rules/animal-violence-generic.yaml` | Generic (plain text) | All file types: comments, strings, docs, configs | No | 62+ |
| `rules/animal-violence-python.yaml` | Python AST | String literals | Yes | 62+ |
| `rules/animal-violence-javascript.yaml` | JS/TS AST | String literals | Yes | 62+ |
| `rules/animal-violence-go.yaml` | Go AST | String literals | Yes | 62+ |

**Severity levels**

- `ERROR` — direct animal-harming idioms (e.g. "kill two birds with one stone", "skin a cat") — fix required
- `WARNING` — speciesist idioms and tech jargon (e.g. "guinea pig", "cattle vs. pets") — replacement recommended
- `INFO` — deeply embedded phrases where alternatives are still gaining adoption (e.g. "red herring") — flagged for awareness

**Pattern categories**

- Violent idioms: "kill two birds with one stone", "beat a dead horse", "skin a cat", "shooting fish in a barrel", and more
- Speciesist idioms: "guinea pig", "herding cats", "sacred cow", "cash cow", "scapegoat", "rat race", and more
- Tech jargon: "cattle vs. pets", "dogfooding", "canary in a coal mine", "master/slave", "whitelist/blacklist", "kill process", and more
- Embedded phrases: "the elephant in the room", "red herring", "pet project"

**Two-mode approach**

Generic rules (`languages: [generic]`) treat files as plain text and catch speciesist language in comments, documentation, and configs. Language-specific rules use Semgrep's AST parser to target only string literals, reducing false positives and enabling `--autofix`. Combine both for full coverage:

```bash
semgrep \
  --config rules/animal-violence-generic.yaml \
  --config rules/animal-violence-python.yaml \
  /path/to/python/project
```

## Documentation

- [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) — canonical pattern dictionary (source of truth for all rules)
- [no-animal-violence-action](https://github.com/Open-Paws/no-animal-violence-action) — GitHub Action wrapping these rules
- [no-animal-violence-pre-commit](https://github.com/Open-Paws/no-animal-violence-pre-commit) — pre-commit hook
- [eslint-plugin-no-animal-violence](https://github.com/Open-Paws/eslint-plugin-no-animal-violence) — ESLint plugin for JS/TS
- [vale-no-animal-violence](https://github.com/Open-Paws/vale-no-animal-violence) — Vale rules for prose
- [vscode-no-animal-violence](https://github.com/Open-Paws/vscode-no-animal-violence) — VS Code extension
- [reviewdog-no-animal-violence](https://github.com/Open-Paws/reviewdog-no-animal-violence) — inline PR annotations
- [danger-plugin-no-animal-violence](https://github.com/Open-Paws/danger-plugin-no-animal-violence) — Danger.js integration
- [Coghlan & Parker (2023)](https://doi.org/10.1007/s43681-023-00380-w) — research on speciesist language in AI training data

## Architecture

<details>
<summary>Rule structure and generation pipeline</summary>

**Rule ID naming convention**

```
animal-violence.<idiom-slug>                          # generic
animal-violence.python.string.<idiom-slug>            # Python
animal-violence.js.string.<idiom-slug>                # JS/TS
animal-violence.go.string.<idiom-slug>                # Go
```

**Generic rule anatomy**

```yaml
rules:
  - id: animal-violence.kill-two-birds-with-one-stone
    languages: [generic]
    severity: ERROR
    message: |
      "kill two birds with one stone" uses violence against animals as a metaphor.
      Use "accomplish two things at once" instead.
    patterns:
      - pattern-regex: (?i)kill(ing)?\s+two\s+birds\s+with\s+one\s+stone
    metadata:
      category: inclusive-language
      subcategory: animal-violence
      alternative: accomplish two things at once
      references:
        - https://doi.org/10.1007/s43681-023-00380-w
```

**Language-specific rule anatomy (with autofix)**

```yaml
rules:
  - id: animal-violence.python.string.kill-two-birds-with-one-stone
    languages: [python]
    severity: ERROR
    message: ...
    patterns:
      - pattern: $STR
        metavariable-regex:
          metavariable: $STR
          regex: (?i)".*kill(ing)?\s+two\s+birds\s+with\s+one\s+stone.*"
    fix-regex:
      regex: (?i)kill(ing)?\s+two\s+birds\s+with\s+one\s+stone
      replacement: accomplish two things at once
    metadata:
      category: inclusive-language
      subcategory: animal-violence
      alternative: accomplish two things at once
```

**Generation pipeline**

The four `rules/*.yaml` files are auto-generated by [project-compassionate-code](https://github.com/Open-Paws/project-compassionate-code) from the canonical dictionary in [no-animal-violence](https://github.com/Open-Paws/no-animal-violence). Do not edit rule YAML files directly — changes will be overwritten on the next sync.

**Testing**

Semgrep's built-in test framework uses annotation comments in test files:

```python
# ruleid: animal-violence.python.string.guinea-pig
label = "guinea pig test"

# ok: animal-violence.python.string.guinea-pig
comment = "the guinea pig is a small animal"
```

Run tests:

```bash
semgrep --config rules/ --test       # Semgrep rule tests
pytest tests/ -v                      # Structural YAML tests
yamllint -c .yamllint.yml rules/      # YAML lint
```

</details>

## Contributing

Rule YAML files are auto-generated — do not edit them directly. To add or change a pattern:

1. Submit a PR to [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) to update the canonical dictionary.
2. [project-compassionate-code](https://github.com/Open-Paws/project-compassionate-code) regenerates all four rule files.
3. A PR is opened in this repo with the updated rules.

Contributions welcome in these areas:

- CI workflows (`.github/workflows/`)
- Pre-commit configuration (`.pre-commit-config.yaml`)
- Test coverage (`tests/`)
- Documentation

**Development setup**

```bash
git clone https://github.com/Open-Paws/semgrep-rules-no-animal-violence.git
cd semgrep-rules-no-animal-violence
pip install pytest pyyaml yamllint ruff semgrep
pre-commit install
```

**Before submitting a PR**

```bash
semgrep --config rules/ --validate   # rule syntax
pytest tests/ -v                      # structural tests
yamllint -c .yamllint.yml rules/      # YAML lint
ruff check . --config ruff.toml      # Python lint
```

All contributions must use non-speciesist language in code, comments, commit messages, and documentation. See the [canonical language guide](https://github.com/Open-Paws/no-animal-violence) for the full pattern list.

## Impact / Adoption

<!-- TODO: add adoption numbers when available (e.g. stars, downloads, repos using the action) -->

This rule set runs in production CI across Open Paws repositories. The no-animal-violence ecosystem spans nine integration points covering Semgrep, ESLint, Vale, pre-commit, GitHub Actions, VS Code, Reviewdog, and Danger.js.

Research supports the approach: speciesist language in AI training data encodes anthropocentric biases into language models (Coghlan & Parker, 2023). Removing this language from codebases contributes to less biased systems.

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgments

Built by [Open Paws](https://openpaws.ai), a 501(c)(3) nonprofit building AI infrastructure for the animal liberation movement.

- [Coghlan, S., & Parker, C. (2023). "Harm to nonhuman animals from AI: a systematic account and framework." *Philosophy & Technology*, 36(2).](https://doi.org/10.1007/s43681-023-00380-w)
- [Dunayer, J. (2001). *Animal Equality: Language and Liberation*. Ryce Publishing.](https://www.rycepress.com)
- [PETA. "Not Your Metaphor: Speciesist Language and How to Avoid It."](https://www.peta.org/features/animal-friendly-idioms/)

---

[Donate](https://openpaws.ai/donate) · [Discord](https://discord.gg/openpaws) · [openpaws.ai](https://openpaws.ai) · [Volunteer](https://openpaws.ai/volunteer)
