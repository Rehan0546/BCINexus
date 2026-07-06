"""Public placeholder example for listing BCINexus projects."""

from __future__ import annotations

import json
import os
import urllib.request


API_BASE_URL = os.getenv("BCINEXUS_API_BASE_URL", "https://api.bcinexus.xyz/v1")
API_KEY = os.getenv("BCINEXUS_API_KEY")


def main() -> None:
    if not API_KEY:
        raise SystemExit("Set BCINEXUS_API_KEY before running this example.")

    request = urllib.request.Request(
        f"{API_BASE_URL}/projects",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "application/json",
        },
        method="GET",
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
