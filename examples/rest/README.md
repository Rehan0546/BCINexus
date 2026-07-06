# REST API Examples

Example placeholder REST calls.

## List Projects

```bash
curl "https://api.bcinexus.xyz/v1/projects" \
  -H "Authorization: Bearer $BCINEXUS_API_KEY" \
  -H "Accept: application/json"
```

## Create Project

```bash
curl -X POST "https://api.bcinexus.xyz/v1/projects" \
  -H "Authorization: Bearer $BCINEXUS_API_KEY" \
  -H "Content-Type: application/json" \
  --data @../../api/requests/create-project.json
```
