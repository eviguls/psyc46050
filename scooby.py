"""Read the Mystery Inc. team from a YAML file and print each member's role."""

from pathlib import Path

import yaml

# Look for test.yml next to this script, so it works from any folder.
DEFAULT_FILE = Path(__file__).parent / "test.yml"


def load_members(path=DEFAULT_FILE):
    """Return the list of members (dicts with 'name' and 'role') from a YAML file."""
    with open(path) as f:
        data = yaml.safe_load(f)

    # An empty file loads as None; fail with a clear message instead of a TypeError.
    if not data or "mystery-inc" not in data:
        raise ValueError(f"{path} has no 'mystery-inc' list")
    return data["mystery-inc"]


def format_roster(members):
    """Return one 'name: role' line per member."""
    return [f"{member['name']}: {member['role']}" for member in members]


if __name__ == "__main__":
    members = load_members()
    print("Leader:", members[0]["name"])   # Fred
    for line in format_roster(members):
        print(line)
