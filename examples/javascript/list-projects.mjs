const apiBaseUrl = process.env.BCINEXUS_API_BASE_URL ?? "https://api.bcinexus.xyz/v1";
const apiKey = process.env.BCINEXUS_API_KEY;

if (!apiKey) {
  throw new Error("Set BCINEXUS_API_KEY before running this example.");
}

const response = await fetch(`${apiBaseUrl}/projects`, {
  headers: {
    Authorization: `Bearer ${apiKey}`,
    Accept: "application/json",
  },
});

if (!response.ok) {
  throw new Error(`Request failed with status ${response.status}`);
}

console.log(JSON.stringify(await response.json(), null, 2));
