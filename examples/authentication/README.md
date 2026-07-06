# Authentication Examples

BCINexus public API authentication is represented as bearer-token authentication in draft examples.

## Environment Variables

```bash
export BCINEXUS_API_KEY="replace_me"
export BCINEXUS_API_BASE_URL="https://api.bcinexus.xyz/v1"
```

## Request

```bash
curl "$BCINEXUS_API_BASE_URL/projects" \
  -H "Authorization: Bearer $BCINEXUS_API_KEY" \
  -H "Accept: application/json"
```

Do not commit credentials.
