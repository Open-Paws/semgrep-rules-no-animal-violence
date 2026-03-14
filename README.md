# semgrep-rules-no-animal-violence

Semgrep rules for detecting speciesist language in code comments, strings, and documentation.

Language shapes thought. Speciesist idioms — "kill two birds with one stone", "beat a dead horse", "guinea pig" — normalize violence against animals. These rules help development teams identify and replace speciesist language with inclusive alternatives.

## Quick Start

### Run directly from GitHub

```bash
# Scan your project with all rules (generic + language-specific)
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/main/rules/

# Generic rules only (works across all file types — comments, strings, docs)
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/main/rules/animal-violence-generic.yaml

# Language-specific rules (AST-aware string matching with autofix support)
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/main/rules/animal-violence-python.yaml
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/main/rules/animal-violence-javascript.yaml
semgrep --config https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/main/rules/animal-violence-go.yaml
```

### Clone and run locally

```bash
git clone https://github.com/Open-Paws/semgrep-rules-no-animal-violence.git
semgrep --config semgrep-rules-no-animal-violence/rules/ /path/to/your/project
```

### With autofix

The language-specific rules (Python, JavaScript/TypeScript, Go) include `fix-regex` autofixes for many patterns. Run with `--autofix` to apply them:

```bash
semgrep --config semgrep-rules-no-animal-violence/rules/animal-violence-python.yaml --autofix /path/to/your/project
```

## Rule Files

| File | Languages | Targets | Autofix |
|------|-----------|---------|---------|
| `animal-violence-generic.yaml` | All (generic mode) | Comments, strings, docs, any text | No |
| `animal-violence-python.yaml` | Python | String literals (AST-aware) | Yes |
| `animal-violence-javascript.yaml` | JavaScript, TypeScript | String literals (AST-aware) | Yes |
| `animal-violence-go.yaml` | Go | String literals (AST-aware) | Yes |

**Why both generic and language-specific rules?**

- **Generic rules** use `languages: [generic]` which treats files as plain text. This catches speciesist language in comments, documentation, config files, and any text. However, it may produce more matches.
- **Language-specific rules** use Semgrep's AST parsing to target only string literals. This is more precise and supports autofix, but cannot match comments (Semgrep's language mode excludes comments from the AST).

For maximum coverage, use both:

```bash
semgrep --config semgrep-rules-no-animal-violence/rules/ /path/to/your/project
```

## Detected Patterns

The full canonical dictionary contains 62 entries across four categories.

### Violent Idioms (ERROR)

| Phrase | Suggested Alternative |
|---|---|
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

### Speciesist Idioms (WARNING)

| Phrase | Suggested Alternative |
|---|---|
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

### Speciesist Idioms (INFO)

| Phrase | Suggested Alternative |
|---|---|
| the elephant in the room | the obvious issue |
| red herring | distraction |
| pet project | side project |

### Tech & Infrastructure Jargon (WARNING/INFO)

| Term | Suggested Alternative |
|---|---|
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

## CI/CD Integration

### GitHub Actions

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
            https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/main/rules/animal-violence-generic.yaml
            https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/main/rules/animal-violence-python.yaml
            https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/main/rules/animal-violence-javascript.yaml
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
          - https://github.com/Open-Paws/semgrep-rules-no-animal-violence/blob/main/rules/animal-violence-generic.yaml
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

1. Add the pattern to `rules/animal-violence-generic.yaml` (always)
2. Add AST-aware versions to the relevant language files (if applicable)
3. Include `message` with the speciesist term and at least one alternative
4. Include `metadata` with `category: inclusive-language` and `subcategory: speciesism`
5. Test your rule: `semgrep --config your-rule.yaml --test`

## License

MIT. See [LICENSE](LICENSE).

---

Built by [Open Paws](https://github.com/Open-Paws) — AI infrastructure for animal liberation.
