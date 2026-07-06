"""Validate public BCINexus developer repository files."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - exercised on minimal local machines.
    yaml = None

try:
    from jsonschema.validators import validator_for
except ImportError:  # pragma: no cover - exercised on minimal local machines.
    validator_for = None


ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".json", ".yaml", ".yml", ".py", ".mjs", ".svg"}
PROHIBITED_MARKERS = [
    "BEGIN " + "PRIVATE KEY",
    "BCINEXUS" + "_SECRET",
    "BCILATTICE" + "_SECRET",
    "DATABASE" + "_URL=",
    "JWT" + "_SECRET",
    "OPENAI" + "_API_KEY=",
    "ANTHROPIC" + "_API_KEY=",
]


def validate_json_file(path: Path) -> None:
    with path.open("r", encoding="utf-8") as handle:
        json.load(handle)


def validate_yaml_file(path: Path) -> None:
    if yaml is None:
        return
    with path.open("r", encoding="utf-8") as handle:
        yaml.safe_load(handle)


def validate_json_schema(path: Path) -> None:
    if validator_for is None:
        return
    with path.open("r", encoding="utf-8") as handle:
        schema = json.load(handle)
    validator_cls = validator_for(schema)
    validator_cls.check_schema(schema)


def scan_text(path: Path) -> list[str]:
    findings: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for marker in PROHIBITED_MARKERS:
        if marker in text:
            findings.append(f"{path.relative_to(ROOT)} contains prohibited marker {marker!r}")
    return findings


def main() -> int:
    errors: list[str] = []

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue

        try:
            if path.suffix == ".json":
                validate_json_file(path)
            elif path.suffix in {".yaml", ".yml"}:
                validate_yaml_file(path)
            if path.name.endswith(".schema.json"):
                validate_json_schema(path)
            if path.suffix in TEXT_EXTENSIONS:
                errors.extend(scan_text(path))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Public repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

