"""Structural tests for semgrep rule YAML files.

Each rule file must be valid YAML and contain at least one rule with
the required semgrep fields: id, message, languages, and severity.
"""

from pathlib import Path

import pytest
import yaml

RULES_DIR = Path(__file__).parent.parent / "rules"
RULE_FILES = list(RULES_DIR.glob("*.yaml"))


@pytest.mark.parametrize("rule_file", RULE_FILES, ids=lambda p: p.name)
def test_rule_file_is_valid_yaml(rule_file: Path) -> None:
    """Each rules file must parse as valid YAML without errors."""
    content = yaml.safe_load(rule_file.read_text())
    assert content is not None, f"{rule_file.name} must not be empty"


@pytest.mark.parametrize("rule_file", RULE_FILES, ids=lambda p: p.name)
def test_rule_file_has_rules_key(rule_file: Path) -> None:
    """Each rules file must have a top-level 'rules' list."""
    content = yaml.safe_load(rule_file.read_text())
    assert "rules" in content, f"{rule_file.name} must contain a 'rules' key"
    assert isinstance(content["rules"], list), f"{rule_file.name} 'rules' must be a list"
    assert len(content["rules"]) > 0, f"{rule_file.name} must contain at least one rule"


@pytest.mark.parametrize("rule_file", RULE_FILES, ids=lambda p: p.name)
def test_each_rule_has_required_fields(rule_file: Path) -> None:
    """Each individual rule must declare id, message, languages, and severity."""
    content = yaml.safe_load(rule_file.read_text())
    required = {"id", "message", "languages", "severity"}
    for rule in content["rules"]:
        missing = required - rule.keys()
        assert not missing, (
            f"Rule '{rule.get('id', '?')}' in {rule_file.name} is missing fields: {missing}"
        )
