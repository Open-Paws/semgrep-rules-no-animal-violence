# semgrep-rules-speciesism

Semgrep rules for detecting speciesist language in code comments, strings, and documentation.

Language shapes thought. Speciesist idioms — "kill two birds with one stone", "beat a dead horse", "guinea pig" — normalize violence against animals. These rules help development teams identify and replace speciesist language with inclusive alternatives.

## Quick Start

### Run directly from GitHub

```bash
# Scan your project with all rules (generic + language-specific)
semgrep --config https://github.com/Open-Paws/semgrep-rules-speciesism/blob/main/rules/

# Generic rules only (works across all file types — comments, strings, docs)
semgrep --config https://github.com/Open-Paws/semgrep-rules-speciesism/blob/main/rules/speciesism-generic.yaml

# Language-specific rules (AST-aware string matching with autofix support)
semgrep --config https://github.com/Open-Paws/semgrep-rules-speciesism/blob/main/rules/speciesism-python.yaml
semgrep --config https://github.com/Open-Paws/semgrep-rules-speciesism/blob/main/rules/speciesism-javascript.yaml
semgrep --config https://github.com/Open-Paws/semgrep-rules-speciesism/blob/main/rules/speciesism-go.yaml
```

### Clone and run locally

```bash
git clone https://github.com/Open-Paws/semgrep-rules-speciesism.git
semgrep --config semgrep-rules-speciesism/rules/ /path/to/your/project
```

### With autofix

The language-specific rules (Python, JavaScript/TypeScript, Go) include `fix-regex` autofixes for many patterns. Run with `--autofix` to apply them:

```bash
semgrep --config semgrep-rules-speciesism/rules/speciesism-python.yaml --autofix /path/to/your/project
```

## Rule Files

| File | Languages | Targets | Autofix |
|------|-----------|---------|---------|
| `speciesism-generic.yaml` | All (generic mode) | Comments, strings, docs, any text | No |
| `speciesism-python.yaml` | Python | String literals (AST-aware) | Yes |
| `speciesism-javascript.yaml` | JavaScript, TypeScript | String literals (AST-aware) | Yes |
| `speciesism-go.yaml` | Go | String literals (AST-aware) | Yes |

**Why both generic and language-specific rules?**

- **Generic rules** use `languages: [generic]` which treats files as plain text. This catches speciesist language in comments, documentation, config files, and any text. However, it may produce more matches.
- **Language-specific rules** use Semgrep's AST parsing to target only string literals. This is more precise and supports autofix, but cannot match comments (Semgrep's language mode excludes comments from the AST).

For maximum coverage, use both:

```bash
semgrep --config semgrep-rules-speciesism/rules/ /path/to/your/project
```

## Detected Patterns

### Idioms & Phrases (WARNING)

| Speciesist Phrase | Suggested Alternative |
|---|---|
| kill two birds with one stone | accomplish two things at once |
| beat/flog a dead horse | belaboring the point |
| guinea pig (as metaphor) | test subject, beta tester |
| more than one way to skin a cat | more than one way to solve this |
| let the cat out of the bag | spill the beans, reveal the secret |
| open a can of worms | open Pandora's box |
| wild goose chase | pointless pursuit |
| hold your horses | hold on, slow down |
| straight from the horse's mouth | from the original source |
| elephant in the room | the obvious issue |
| like herding cats | like organizing chaos |
| take the bull by the horns | face the challenge head-on |
| bring home the bacon | bring home the bagels |
| sacred cow | protected assumption |
| like lambs to the slaughter | without resistance |
| bigger fish to fry | bigger problems to solve |
| shooting fish in a barrel | trivially simple |
| no room to swing a cat | very cramped |
| dead cat bounce | temporary rebound |
| open season on | unrestricted criticism of |

### Tech Jargon (INFO/WARNING)

| Speciesist Term | Suggested Alternative |
|---|---|
| canary deployment | incremental rollout, phased deployment |
| monkey patch | runtime patch, dynamic patch |
| monkey testing | random testing, fuzz testing |
| dogfooding | self-hosting, internal testing |
| cattle vs pets | ephemeral vs persistent, fleet vs snowflake |
| duck typing | structural typing, behavioral typing |
| rubber duck debugging | talk-through debugging |
| bug hunting | defect discovery, issue triage |

### Derogatory Animal Comparisons (WARNING)

| Pattern | Note |
|---|---|
| "pig" as insult | Using animal names as insults devalues them as sentient beings |
| "chicken" as coward | Using animal names as insults devalues them as sentient beings |

## CI/CD Integration

### GitHub Actions

```yaml
name: Speciesist Language Check
on: [pull_request]

jobs:
  semgrep:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            https://github.com/Open-Paws/semgrep-rules-speciesism/blob/main/rules/speciesism-generic.yaml
            https://github.com/Open-Paws/semgrep-rules-speciesism/blob/main/rules/speciesism-python.yaml
            https://github.com/Open-Paws/semgrep-rules-speciesism/blob/main/rules/speciesism-javascript.yaml
```

### Pre-commit hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/returntocorp/semgrep
    rev: v1.56.0
    hooks:
      - id: semgrep
        args:
          - --config
          - https://github.com/Open-Paws/semgrep-rules-speciesism/blob/main/rules/speciesism-generic.yaml
          - --error
```

## Severity Levels

- **WARNING** — Direct speciesist idioms and violence-normalizing phrases. These have clear, widely-accepted alternatives.
- **INFO** — Deeply embedded tech jargon where alternatives exist but adoption is still growing. Flagged for awareness rather than enforcement.

## Why This Matters

Research has shown that speciesist language in AI training data and codebases reinforces anthropocentric biases in language models (Coghlan & Parker, 2023). By detecting and replacing speciesist language in code, we:

1. **Reduce harm** — Language that normalizes violence against animals contributes to their exploitation
2. **Improve inclusivity** — Many people find speciesist language alienating or offensive
3. **Set precedent** — Just as the tech industry moved away from "master/slave" and "whitelist/blacklist", we can move past speciesist metaphors
4. **Build better AI** — Cleaner training data means less biased models

## References

- Coghlan, S., & Parker, C. (2023). "Harm to nonhuman animals from AI: a systematic account and framework." *Philosophy & Technology*, 36(2). [DOI: 10.1007/s43681-023-00380-w](https://doi.org/10.1007/s43681-023-00380-w)
- PETA. "Not Your Metaphor: Speciesist Language and How to Avoid It." [peta.org](https://www.peta.org/features/animal-friendly-idioms/)
- Dunayer, J. (2001). *Animal Equality: Language and Liberation*. Ryce Publishing.

## Contributing

Contributions welcome. To add new rules:

1. Add the pattern to `rules/speciesism-generic.yaml` (always)
2. Add AST-aware versions to the relevant language files (if applicable)
3. Include `message` with the speciesist term and at least one alternative
4. Include `metadata` with `category: inclusive-language` and `subcategory: speciesism`
5. Test your rule: `semgrep --config your-rule.yaml --test`

## License

MIT. See [LICENSE](LICENSE).

---

Built by [Open Paws](https://github.com/Open-Paws) — AI infrastructure for animal liberation.
