# Ecosystem Overview

The BCINexus ecosystem is organized around public contracts and closed commercial products.

## Components

| Component | Role | Public in this repository |
| --- | --- | --- |
| BCILattice | Local research application | Public schemas and workflow examples only |
| BCINexus | Cloud and developer layer | API contracts (production API live, public access launching soon), docs, examples |
| SDKs | Future language-specific clients | Roadmap and placeholder docs |
| Plugins | Future extension mechanism | Draft manifest schema and guide |
| Hardware integrations | Device and acquisition guidance | Public integration patterns only |

## Integration Model

1. Developers build against documented schemas and API contracts.
2. BCILattice exports public workflow or pipeline artifacts.
3. BCINexus validates, stores, shares, or publishes supported public artifacts.
4. Third-party tools integrate through documented authentication and API surfaces.

## Non-Goals

- Publishing proprietary source code.
- Replacing the commercial BCINexus service.
- Exposing private infrastructure, credentials, internal models, or product internals.
- Treating draft schemas as final regulatory or clinical guarantees.
