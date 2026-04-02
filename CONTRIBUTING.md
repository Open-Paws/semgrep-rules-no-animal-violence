# Contributing to semgrep-rules-no-animal-violence

Rules in this repo are **auto-generated** by `project-compassionate-code`. Do not edit the rule YAML files directly — changes will be overwritten.

To add or modify rules, contribute to the canonical dictionary in [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) and the generator in [project-compassionate-code](https://github.com/Open-Paws/project-compassionate-code).

## What you can contribute here

- Improvements to the CI workflow (`.github/workflows/`)
- Pre-commit hook configuration (`.pre-commit-config.yaml`)
- Test improvements (`tests/`)
- Documentation updates

## Getting started

1. Fork and clone the repo
2. Install Python 3.11+
3. Install dependencies: `pip install -e ".[dev]"` (or `pip install pytest ruff` if no dev extras)
4. Run tests: `pytest`
5. Run lint: `ruff check .`

## Pull requests

- One PR per concern
- Describe what and why
- Run tests before submitting

## Code of conduct

Open Paws is building AI infrastructure for animal liberation. We expect all contributors to:
- Treat all participants with respect
- Use inclusive, non-speciesist language (see our [language guide](https://github.com/Open-Paws/no-animal-violence))
- Focus on constructive collaboration

## Questions?

Open an issue or reach out to the team.
