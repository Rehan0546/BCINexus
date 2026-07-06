# Contributing

Thank you for helping improve the BCINexus public developer ecosystem.

## Scope

This repository accepts contributions to:

- Public documentation.
- Examples and integration patterns.
- Public API contract feedback.
- JSON schema improvements.
- Typos, clarity fixes, and accessibility improvements.
- GitHub issue templates, workflows, and release metadata.

This repository does not accept proprietary BCINexus or BCILattice source code, private service logic, credentials, private datasets, internal infrastructure configuration, or closed-source product implementation details.

## Development Setup

```bash
git clone https://github.com/Rehan0546/BCINexus.git
cd BCINexus
python -m pip install --upgrade pip jsonschema pyyaml
```

## Validation

Run the lightweight checks before opening a pull request:

```bash
python scripts/validate_public_repo.py
```

If you have markdownlint installed:

```bash
markdownlint "**/*.md"
```

## Pull Request Guidelines

- Keep changes focused and reviewable.
- Use placeholders for future private or unreleased APIs.
- Do not include secrets, tokens, proprietary implementation, screenshots of private dashboards, private logs, or internal architecture diagrams.
- Prefer clear examples over broad marketing language.
- Update `CHANGELOG.md` when public contracts, schemas, or docs materially change.

## Commit Style

Use concise imperative commits:

```text
docs: add authentication guide
schemas: clarify pipeline metadata
examples: add REST project request
```

## Discussions

Use GitHub Discussions for design questions, ecosystem ideas, SDK feedback, and integration planning.
