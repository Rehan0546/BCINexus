# Authentication Guide

BCINexus API authentication is expected to use bearer tokens or scoped API keys when public API access is released.

## Placeholder Request

```bash
curl "https://api.bcinexus.com/v1/projects" \
  -H "Authorization: Bearer $BCINEXUS_API_KEY" \
  -H "Accept: application/json"
```

## Security Requirements

- Store API keys in environment variables or a managed secret store.
- Never commit tokens to Git.
- Use least-privilege scopes.
- Rotate credentials regularly.
- Separate development, staging, and production credentials.

## Planned Token Scopes

| Scope | Purpose |
| --- | --- |
| `projects:read` | Read project metadata |
| `projects:write` | Create or update project metadata |
| `pipelines:read` | Read pipeline metadata |
| `pipelines:write` | Publish or update pipeline artifacts |
| `plugins:read` | Discover public plugins |

Scopes are placeholders until public API access is released.
