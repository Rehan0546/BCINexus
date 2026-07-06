# API Documentation

The public BCINexus API contract is currently represented by a draft OpenAPI specification in [`../api/openapi.yaml`](../api/openapi.yaml).

## Base URL

```text
https://api.bcinexus.xyz/v1
```

This base URL reflects the production API. Public developer access is launching soon.

## Public API Areas

- Projects.
- Pipelines.
- Authentication.
- Artifact import and export.
- Plugin discovery.
- Research workflow metadata.

## Versioning

Public APIs should use explicit version prefixes, such as `/v1`. Breaking changes must be documented in `CHANGELOG.md` and reflected in OpenAPI updates.

## Stability Labels

- `draft`: Proposed contract. Subject to change.
- `preview`: Available to selected developers. May change with notice.
- `stable`: Supported public contract.

Current status: `preview`. The production API is live and running; public developer access is launching soon.
