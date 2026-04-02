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

## Organizational Context

**Strategic role (Lever 1 + Lever 3):** Multi-language CI scanner for speciesist language. Upstream dependency: `no-animal-violence` (canonical rule dictionary). Downstream consumers: `desloppify` (embeds as scoring dimension), `project-compassionate-code` (uses to identify and fix speciesist language in open-source repos), `open-paws-platform` CI.

**Current org priorities relevant to this repo:**
- Platform CI integration planned but not yet shipped. This ruleset should be added to `open-paws-platform` CI and bootcamp setup instructions. See `ecosystem/integration-todos.md` §27a.
- Suite maintenance has **no named owner** as of 2026-04-02. Rule additions, false-positive tuning, and new language coverage (Rust, Ruby, Java) are F/E-rank Guild quests.
- Language coverage gap: Python, JS/TS, Go, and generic exist. Other popular open-source languages are missing.

**Decisions affecting this repo:**
- 2026-03-25: Every org repo runs `semgrep --config semgrep-no-animal-violence.yaml` on all code/docs edits as a universal quality gate.
- 2026-04-01: Rule maintenance should sync from the `no-animal-violence` canonical dictionary — avoid independent drift.

## Related Repos

- [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) — Canonical rule dictionary (upstream dependency)
- [vscode-no-animal-violence](https://github.com/Open-Paws/vscode-no-animal-violence) — VS Code extension
- [eslint-plugin-no-animal-violence](https://github.com/Open-Paws/eslint-plugin-no-animal-violence) — ESLint plugin for JS/TS
- [no-animal-violence-action](https://github.com/Open-Paws/no-animal-violence-action) — GitHub Action
- [danger-plugin-no-animal-violence](https://github.com/Open-Paws/danger-plugin-no-animal-violence) — Danger.js plugin for PR checks

## Development Standards

### 10-Point Review Checklist (ranked by AI violation frequency)

1. **DRY** — Before adding a new pattern, verify it isn't already in `animal-violence-generic.yaml` or the language-specific files.
2. **Deep modules** — Generic rules and language-specific rules serve different purposes. Keep them separate.
3. **Single responsibility** — One rule = one pattern with one message and one fix suggestion.
4. **Error handling** — Run `semgrep --config rules/ --validate` before committing. Never ship invalid YAML.
5. **Information hiding** — Rule metadata (category, subcategory, severity) must be consistent across all files.
6. **Ubiquitous language** — "farmed animal" not "livestock," "factory farm" not "farm." Never introduce synonyms for domain terms.
7. **Design for change** — Autofix patterns (`fix-regex`) must be tested against real code before merging.
8. **Legacy velocity** — Before modifying existing rules, run `semgrep --config rules/ --test` against the full test suite.
9. **Over-patterning** — Generic ruleset catches most patterns. Add language-specific rules only when AST-aware matching provides meaningful false-positive reduction.
10. **Test quality** — Every new rule must have a `# ruleid:` true-positive test case and a `# ok:` false-positive suppression case.

### Quality Gates

- **Validate**: `semgrep --config rules/ --validate` before every commit.
- **Test**: `semgrep --config rules/ --test`
- **Desloppify**: `desloppify scan --path .` — minimum score ≥85.
- **Two-failure rule**: After two failed fixes on the same problem, stop and restart.

### Testing Methodology

- Spec-first: define what a new rule catches before writing YAML.
- Every rule needs a `# ruleid:` true-positive and `# ok:` false-positive test case.
- Three questions per rule: (1) Does it catch the target phrase in real code? (2) Does autofix produce valid code? (3) Does it avoid flagging POSIX calls, system terms, or quoted strings?

### Seven Concerns — Repo-Specific Notes

1. **Testing** — Semgrep's built-in `--test` framework is the primary mechanism. Gap: not all existing rules have test cases.
2. **Security** — False positives on security-relevant system calls must be aggressively suppressed. A rule that flags legitimate security code erodes developer trust.
3. **Privacy** — Not applicable.
4. **Cost optimization** — Semgrep OSS is free. Avoid rules requiring Semgrep Pro features.
5. **Advocacy domain** — Consistent with canonical dictionary. "farmed animal," "factory farm," "slaughterhouse." Never euphemisms.
6. **Accessibility** — Rule messages must be clear to developers unfamiliar with advocacy context. Explain why the phrase is problematic.
7. **Emotional safety** — Rule messages should not contain graphic content.

### Structured Coding Reference

For tool-specific AI coding instructions (Claude Code rules, Cursor MDC, Copilot, Windsurf, etc.), copy the corresponding directory from `structured-coding-with-ai` into this project root.
