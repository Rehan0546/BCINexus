# BCINexus Developer Hub

[![Status](https://img.shields.io/badge/status-public%20developer%20preview-0f766e.svg)](#status)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-6BA539.svg)](api/openapi.yaml)
[![Security](https://img.shields.io/badge/security-responsible%20disclosure-111827.svg)](SECURITY.md)
[![Discussions](https://img.shields.io/badge/GitHub-Discussions-7c3aed.svg)](https://github.com/Rehan0546/BCINexus/discussions)

BCINexus is the public developer ecosystem for BCILattice: APIs, schemas, examples, documentation, integration guidance, and community workflows for neuroscience, BCI, AI/ML, and research tooling.

This repository is not the source code for BCINexus or BCILattice. It contains public resources only. Commercial services, hosted infrastructure, desktop application source code, internal services, model implementations, private datasets, and proprietary product logic remain closed source.

## Status

This repository is the official public GitHub home for BCINexus developer resources. The production API is built and running; public developer access is launching soon. Public SDKs, plugin registries, and hardware integration packages will follow over time. Until each surface is public, this repository uses explicit placeholders and stable draft schemas so integrators can plan safely.

## Table of Contents

- [What Is BCINexus?](#what-is-bcinexus)
- [What Is BCILattice?](#what-is-bcilattice)
- [Repository Contents](#repository-contents)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Examples](#examples)
- [API and Schemas](#api-and-schemas)
- [Brand Assets](#brand-assets)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)

## What Is BCINexus?

BCINexus is the cloud and developer layer around the BCILattice research workflow. It is designed for account management, project publishing, collaboration, reproducibility metadata, workflow exchange, API integrations, and community resources.

BCINexus is intended to help developers and researchers connect external tools to the ecosystem without exposing proprietary application internals.

## What Is BCILattice?

BCILattice is the local research application for building and managing BCI and neuroscience workflows. It focuses on local-first analysis, preprocessing, pipeline composition, ML workflows, experiment organization, and research utilities.

The public contract is intentionally limited to documented formats, schemas, examples, and future API/SDK surfaces. The desktop source code is not part of this repository.

## Repository Contents

```text
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── docs/
├── examples/
├── api/
├── schemas/
├── assets/
└── .github/
```

## Installation

Clone the public developer repository:

```bash
git clone https://github.com/Rehan0546/BCINexus.git
cd BCINexus
```

Optional local validation tools:

```bash
python -m pip install --upgrade pip jsonschema pyyaml
npm install -g markdownlint-cli
```

No BCINexus or BCILattice proprietary dependencies are required to use this repository.

## Quick Start

1. Read the ecosystem overview in [docs/ecosystem-overview.md](docs/ecosystem-overview.md).
2. Review the draft OpenAPI contract in [api/openapi.yaml](api/openapi.yaml).
3. Inspect public data contracts in [schemas/](schemas/).
4. Run or adapt examples from [examples/](examples/).
5. Open a GitHub Discussion for integration design questions.

Example REST request:

```bash
curl -X GET "https://api.bcinexus.com/v1/projects" \
  -H "Authorization: Bearer $BCINEXUS_API_KEY" \
  -H "Accept: application/json"
```

The endpoint above reflects the production API contract. Public developer access (API keys, docs sign-up) is launching soon.

## Documentation

- [What is BCINexus?](docs/what-is-bcinexus.md)
- [What is BCILattice?](docs/what-is-bcilattice.md)
- [Ecosystem Overview](docs/ecosystem-overview.md)
- [API Documentation](docs/api.md)
- [Authentication Guide](docs/authentication.md)
- [SDK Guide](docs/sdk-guide.md)
- [Plugin Guide](docs/plugin-guide.md)
- [Hardware Integration Guide](docs/hardware-integration.md)
- [Research Workflow Examples](docs/research-workflows.md)
- [FAQ](docs/faq.md)

## Examples

- [Python](examples/python/)
- [JavaScript and TypeScript](examples/javascript/)
- [REST API](examples/rest/)
- [Authentication](examples/authentication/)
- [Pipeline Import and Export](examples/pipeline-import-export/)
- [Plugin Development](examples/plugin-development/)

## API and Schemas

- [OpenAPI specification](api/openapi.yaml)
- [Example API requests](api/requests/)
- [Example API responses](api/responses/)
- [Pipeline schema](schemas/pipeline.schema.json)
- [Project schema](schemas/project.schema.json)
- [Plugin manifest schema](schemas/plugin-manifest.schema.json)

## Brand Assets

Public brand assets live in [assets/](assets/), including logos, icons, screenshots placeholders, and brand usage guidelines. Do not imply partnership, endorsement, certification, or official hardware support unless explicitly approved in writing by BCINexus.

## Contributing

Contributions are welcome for public documentation, examples, schema feedback, and integration guidance. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

Please do not open public issues for vulnerabilities. Follow [SECURITY.md](SECURITY.md) for responsible disclosure.

## License

This repository is licensed under the [MIT License](LICENSE), except for brand assets and trademarks, which are governed by the brand guidelines in [assets/brand-guidelines.md](assets/brand-guidelines.md).
