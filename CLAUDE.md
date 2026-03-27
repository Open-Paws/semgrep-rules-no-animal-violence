# semgrep-rules-no-animal-violence

Semgrep rules for detecting speciesist language in code comments, strings, and documentation. Part of the [Open Paws](https://github.com/Open-Paws) speciesist language detection suite.

## Quick Start

```bash
# Run all rules against a project
semgrep --config rules/ /path/to/project

# Run with autofix (language-specific rules only)
semgrep --config rules/animal-violence-python.yaml --autofix /path/to/project

# Test rules
semgrep --config rules/ --test
```

## Architecture

The ruleset has two layers:

- **Generic rules** (`generic` mode) — plain-text scanning across all file types (comments, docs, configs). No autofix.
- **Language-specific rules** (Python, JS/TS, Go) — AST-aware string literal matching with `fix-regex` autofix support.

The canonical dictionary contains 62 entries across four severity categories: violent idioms (ERROR), speciesist idioms (WARNING), low-severity idioms (INFO), and tech jargon (WARNING/INFO).

## Key Files

| File | Description |
|------|-------------|
| `rules/animal-violence-generic.yaml` | Generic (all languages) pattern rules |
| `rules/animal-violence-python.yaml` | Python AST-aware rules with autofix |
| `rules/animal-violence-javascript.yaml` | JS/TS AST-aware rules with autofix |
| `rules/animal-violence-go.yaml` | Go AST-aware rules with autofix |
| `README.md` | Full pattern dictionary, CI/CD integration examples |

## Development

```bash
# Add a new pattern
# 1. Add to rules/animal-violence-generic.yaml (always)
# 2. Add AST-aware version to relevant language file(s)
# 3. Include message with speciesist term + alternative
# 4. Include metadata: category: inclusive-language, subcategory: speciesism

# Validate rules
semgrep --config rules/ --validate

# Test against sample files
semgrep --config rules/ --test
```

## Related Repos

- [vscode-no-animal-violence](https://github.com/Open-Paws/vscode-no-animal-violence) — VS Code extension
- [danger-plugin-no-animal-violence](https://github.com/Open-Paws/danger-plugin-no-animal-violence) — Danger.js plugin for PR checks
