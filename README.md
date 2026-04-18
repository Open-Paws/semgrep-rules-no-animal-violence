# semgrep-rules-no-animal-violence

> **Status: Active Development** — Rules are auto-generated from the canonical [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) dictionary and live in production CI. The toolset has no named maintainer; new language coverage (Rust, Ruby, Java) is an open contribution opportunity.

Part of the [Open Paws no-animal-violence ecosystem](https://github.com/Open-Paws/no-animal-violence).

---

## What is this?

[Semgrep](https://semgrep.dev/) is an open-source static analysis tool that runs pattern-matching rules against source code. Unlike linters that require language-specific plugins, Semgrep can scan **any file type** using generic text patterns, and can also do **AST-aware** matching for precise detection within specific programming languages.

This repo provides a set of Semgrep rules that detect **speciesist language** — idioms, metaphors, and tech jargon that normalize harm to animals — in codebases, documentation, comments, and configuration files. The rules cover 62+ patterns across four severity levels and four target languages.

Language shapes thought. When a codebase treats phrases like "kill two birds with one stone" or "cattle vs. pets" as neutral technical vocabulary, it reinforces assumptions worth questioning. These rules help teams identify and replace that language with clear, inclusive alternatives.

Research supports this: speciesist language in AI training data encodes anthropocentric biases into language models (Coghlan & Parker, 2023). Cleaner language in code contributes to less biased systems.

---

## The no-animal-violence ecosystem

This repo is one of nine tools in the no-animal-violence suite. Each tool targets a different integration point:

| Tool | Integration point |
|------|------------------|
| [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) | Canonical pattern dictionary — source of truth |
| **semgrep-rules-no-animal-violence** (this repo) | Semgrep CI scanner — multi-language, all file types |
| [eslint-plugin-no-animal-violence](https://github.com/Open-Paws/eslint-plugin-no-animal-violence) | ESLint — JavaScript/TypeScript only |
| [vale-no-animal-violence](https://github.com/Open-Paws/vale-no-animal-violence) | Vale — prose and documentation |
| [no-animal-violence-pre-commit](https://github.com/Open-Paws/no-animal-violence-pre-commit) | Pre-commit hook wrapping these Semgrep rules |
| [no-animal-violence-action](https://github.com/Open-Paws/no-animal-violence-action) | GitHub Action wrapping these rules for PR checks |
| [vscode-no-animal-violence](https://github.com/Open-Paws/vscode-no-animal-violence) | VS Code extension for real-time detection |
| [reviewdog-no-animal-violence](https://github.com/Open-Paws/reviewdog-no-animal-violence) | Reviewdog — inline PR annotations |
| [danger-plugin-no-animal-violence](https://github.com/Open-Paws/danger-plugin-no-animal-violence) | Danger.js — PR review automation |

---

## Quick start

### Prerequisites

```bash
pip install semgrep
```

### Run directly from GitHub (no clone needed)

```bash
# Scan with all rules (generic + all language-specific)
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/ /path/to/your/project

# Generic rules only — works across all file types (comments, strings, docs, configs)
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/animal-violence-generic.yaml /path/to/project

# Python projects
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/animal-violence-python.yaml /path/to/project

# JavaScript / TypeScript projects
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/animal-violence-javascript.yaml /path/to/project

# Go projects
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/animal-violence-go.yaml /path/to/project
```

### Clone and run locally

```bash
git clone https://github.com/Open-Paws/semgrep-rules-no-animal-violence.git
cd semgrep-rules-no-animal-violence

# Scan a project
semgrep --config rules/ /path/to/your/project

# Validate rule syntax (no project needed)
semgrep --config rules/ --validate

# Run with autofix (language-specific rules only)
semgrep --config rules/animal-violence-python.yaml --autofix /path/to/project
semgrep --config rules/animal-violence-javascript.yaml --autofix /path/to/project
semgrep --config rules/animal-violence-go.yaml --autofix /path/to/project
```

### Maximum coverage: always combine generic + language-specific

```bash
semgrep \
  --config rules/animal-violence-generic.yaml \
  --config rules/animal-violence-python.yaml \
  /path/to/python/project
```

The generic rules catch language in comments and docs. The language-specific rules catch language in string literals with autofix. Together they give full coverage.

---

## Rule files

| File | Mode | Targets | Autofix | Rules |
|------|------|---------|---------|-------|
| `rules/animal-violence-generic.yaml` | Generic (plain text) | All file types: comments, strings, docs, configs | No | 62+ |
| `rules/animal-violence-python.yaml` | Python AST | String literals only | Yes | 62+ |
| `rules/animal-violence-javascript.yaml` | JS/TS AST | String literals only | Yes | 62+ |
| `rules/animal-violence-go.yaml` | Go AST | String literals only | Yes | 62+ |

**Why two modes?**

- **Generic rules** (`languages: [generic]`) treat files as plain text. They catch speciesist language everywhere — comments, documentation, config files, Markdown. They produce more matches because they are not AST-aware.
- **Language-specific rules** use Semgrep's AST parser with `metavariable-regex` to target only string literals. This reduces false positives (no matches inside comments or import paths) and enables `fix-regex` autofix. However, AST mode cannot match inside comments — that is why combining both modes gives full coverage.

**Note on rule generation:** All four rule YAML files are auto-generated by [project-compassionate-code](https://github.com/Open-Paws/project-compassionate-code) from the canonical dictionary in [no-animal-violence](https://github.com/Open-Paws/no-animal-violence). Do not edit them directly — changes will be overwritten on the next sync.

---

## Detected patterns

The full canonical dictionary contains 62+ entries across four categories.

### Violent idioms (severity: ERROR)

These phrases directly invoke harm to animals as metaphors. They have clear, widely-accepted alternatives.

| Phrase | Suggested alternative |
|--------|-----------------------|
| kill two birds with one stone | accomplish two things at once |
| beat a dead horse | belabor the point |
| flog a dead horse | belabor the point |
| more than one way to skin a cat | more than one way to solve this |
| like shooting fish in a barrel | trivially easy |
| bring home the bacon | bring home the results |
| like lambs to the slaughter | without resistance |
| curiosity killed the cat | curiosity backfired |
| like a chicken with its head cut off | in a panic |
| your goose is cooked | you're in trouble |
| throw someone to the wolves | abandon to criticism |

### Speciesist idioms (severity: WARNING)

These phrases treat animals as instruments or objects without moral consideration.

| Phrase | Suggested alternative |
|--------|-----------------------|
| let the cat out of the bag | reveal the secret |
| open a can of worms | create a complicated situation |
| wild goose chase | futile search |
| guinea pig | test subject |
| hold your horses | wait a moment |
| straight from the horse's mouth | directly from the source |
| take the bull by the horns | face the challenge head-on |
| no room to swing a cat | very cramped |
| hook, line, and sinker | completely |
| clip someone's wings | restrict someone's freedom |
| the straw that broke the camel's back | the tipping point |
| a bird in the hand is worth two in the bush | a sure thing beats a possibility |
| eat crow | admit being wrong |
| fight like cats and dogs | constantly argue |
| take the bait | fall for it |
| don't count your chickens before they hatch | don't assume success prematurely |
| don't be a chicken | don't hesitate |
| bigger fish to fry | more important matters to address |
| herding cats | coordinating independent contributors |
| sacred cow | unquestioned belief |
| scapegoat | blame target |
| rat race | daily grind |
| dead cat bounce | temporary rebound |
| dog-eat-dog | ruthlessly competitive |
| whack-a-mole | recurring problem |
| cash cow | profit center |
| sacrificial lamb | expendable person |
| sitting duck | easy target |
| open season | free-for-all |
| put out to pasture | retire |
| dead duck | lost cause |
| fishing expedition | exploratory investigation |
| badger someone | pester |
| ferret out | uncover |
| pig (as insult) | resource-intensive |

### Embedded idioms (severity: INFO)

Deeply embedded in everyday language; alternatives exist but adoption is still growing. Flagged for awareness rather than enforcement.

| Phrase | Suggested alternative |
|--------|-----------------------|
| the elephant in the room | the obvious issue |
| red herring | distraction |
| pet project | side project |

### Tech and infrastructure jargon (severity: WARNING or INFO)

Industry terms that use animal metaphors or treat animals as commodities.

| Term | Suggested alternative |
|------|-----------------------|
| cattle vs. pets | ephemeral vs. persistent |
| canary in a coal mine | early warning signal |
| dogfooding | self-hosting |
| cowboy coding | undisciplined coding |
| code monkey | developer |
| kill process | terminate the process |
| kill the server | stop the server |
| nuke (it/the/everything) | delete completely |
| cull | remove |
| master/slave | primary/replica |
| whitelist/blacklist | allowlist/denylist |
| grandfathered | legacy |
| abort | cancel |

---

## Severity levels

- **ERROR** — Direct animal-harming idioms. These have clear, widely-accepted alternatives and should be fixed.
- **WARNING** — Speciesist idioms and tech jargon. These have well-established alternatives and are recommended for replacement.
- **INFO** — Deeply embedded jargon where alternatives exist but adoption is still growing. Flagged for awareness.

---

## CI integration

### GitHub Actions — using the official action

```yaml
name: Inclusive Language Check
on: [pull_request]

jobs:
  semgrep:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/animal-violence-generic.yaml
            https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/animal-violence-python.yaml
            https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/animal-violence-javascript.yaml
            https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/animal-violence-go.yaml
```

### GitHub Actions — using the dedicated wrapper action

The [no-animal-violence-action](https://github.com/Open-Paws/no-animal-violence-action) wraps these rules in a purpose-built GitHub Action:

```yaml
name: Inclusive Language Check
on: [pull_request]

jobs:
  nav-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: Open-Paws/no-animal-violence-action@v1
```

### Pre-commit hook

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/Open-Paws/no-animal-violence-pre-commit
    rev: v1.0.0
    hooks:
      - id: no-animal-violence
        files: \.(py|ts|js|md|yaml|yml)$
```

Or use Semgrep's own pre-commit integration directly:

```yaml
repos:
  - repo: https://github.com/returntocorp/semgrep
    rev: v1.56.0
    hooks:
      - id: semgrep
        args:
          - --config
          - https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/master/rules/animal-violence-generic.yaml
          - --error
```

### Install pre-commit hooks for this repo

```bash
pip install pre-commit
pre-commit install
```

---

## Rule anatomy

Each rule follows this structure:

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

Language-specific rules add `fix-regex` for autofix:

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

### Rule ID naming convention

```
animal-violence.<language>.<target>.<idiom-slug>
```

- Generic: `animal-violence.kill-two-birds-with-one-stone`
- Python: `animal-violence.python.string.kill-two-birds-with-one-stone`
- JS/TS: `animal-violence.js.string.kill-two-birds-with-one-stone`
- Go: `animal-violence.go.string.kill-two-birds-with-one-stone`

---

## Relationship to the canonical dictionary

The canonical list of speciesist terms lives in [no-animal-violence](https://github.com/Open-Paws/no-animal-violence). This repo's rule files are generated from that dictionary by [project-compassionate-code](https://github.com/Open-Paws/project-compassionate-code).

To add a new pattern or change an existing one:

1. Submit a PR to [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) to update the canonical dictionary.
2. The [project-compassionate-code](https://github.com/Open-Paws/project-compassionate-code) generator will regenerate all four rule YAML files.
3. A PR will be opened in this repo with the updated rules.

Do not edit `rules/*.yaml` files directly — they will be overwritten.

---

## Testing rules

Semgrep has a built-in test framework. Test files live alongside rule files and use annotation comments:

```python
# Good: no issue
result = process_items(tasks)

# ruleid: animal-violence.python.string.guinea-pig
label = "guinea pig test"

# ok: animal-violence.python.string.guinea-pig
comment = "the guinea pig is a small animal"  # in a biological context
```

Run the tests:

```bash
semgrep --config rules/ --test
```

Run structural tests (YAML validity, required fields):

```bash
pip install pytest pyyaml
pytest tests/ -v
```

---

## Contributing

Rule YAML files are auto-generated — do not edit them directly. What you can contribute:

- Improvements to CI (`.github/workflows/`)
- Pre-commit hook configuration (`.pre-commit-config.yaml`)
- Test improvements (`tests/`)
- Documentation updates

### Development setup

```bash
git clone https://github.com/Open-Paws/semgrep-rules-no-animal-violence.git
cd semgrep-rules-no-animal-violence
pip install pytest pyyaml yamllint ruff semgrep
pre-commit install
```

### Before submitting a PR

```bash
semgrep --config rules/ --validate    # Rule syntax check
pytest tests/ -v                       # Structural tests
yamllint -c .yamllint.yml rules/       # YAML lint
ruff check . --config ruff.toml       # Python lint
```

### Language guide

All contributions must use non-speciesist language in code, comments, commit messages, and documentation. See the [canonical language guide](https://github.com/Open-Paws/no-animal-violence) for the full pattern list.

---

## References

- Coghlan, S., & Parker, C. (2023). "Harm to nonhuman animals from AI: a systematic account and framework." *Philosophy & Technology*, 36(2). [DOI: 10.1007/s43681-023-00380-w](https://doi.org/10.1007/s43681-023-00380-w)
- PETA. "Not Your Metaphor: Speciesist Language and How to Avoid It." [peta.org](https://www.peta.org/features/animal-friendly-idioms/)
- Dunayer, J. (2001). *Animal Equality: Language and Liberation*. Ryce Publishing.

---

## License

MIT. See [LICENSE](LICENSE).

---

Built by [Open Paws](https://github.com/Open-Paws) — AI infrastructure for animal liberation.
