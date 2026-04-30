# AGENTS.md

Setup, verification, and usage notes for AI agents and automated pipelines
working with the public rayobrowse repository.

## What This Project Is

rayobrowse is a Chromium-based stealth browser that runs inside Docker. It
exposes an HTTP daemon on port `9222`. Your automation code calls
`GET /connect`, receives a CDP WebSocket URL as plain text, and passes that URL
to Playwright, Puppeteer, Selenium, or any other CDP client.

The local and cloud usage model is intentionally the same. For local work, use
`http://localhost:9222`. For rayobrowse Cloud, use
`https://cloud.rayobrowse.com` with an API key.

## Prerequisites

- Docker with Compose v2 (`docker compose`)
- Python 3.10+ for Python examples
- Node.js 18+ for Node examples
- About 2 GB free RAM for a basic local run

## Local Setup

```bash
cp .env.example .env
docker compose up -d
curl http://localhost:9222/health
```

By using rayobrowse, you agree to the licenses in `LICENSE` and
`BROWSER_BINARY_LICENSE.md`.

## Primary Usage Pattern

Do not connect Playwright or Puppeteer directly to `/connect`. `/connect` is an
HTTP endpoint, not a CDP WebSocket endpoint.

Correct flow:

1. Call `GET http://localhost:9222/connect`.
2. Read the CDP WebSocket URL from the response body.
3. Connect your CDP client to that returned URL.
4. Let the browser close when the CDP session closes, unless the task requires
   explicit lifecycle control.

Python example:

```python
import httpx
from playwright.sync_api import sync_playwright

resp = httpx.get(
    "http://localhost:9222/connect",
    params={"os": "windows", "headless": "false", "vnc": "true"},
    timeout=120,
)
resp.raise_for_status()

cdp_url = resp.text.strip()
vnc_url = resp.headers.get("x-vnc-url") or "http://localhost:6080/vnc.html"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(cdp_url)
    context = browser.contexts[0] if browser.contexts else browser.new_context()
    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://example.com")
    print(page.title())
    print(f"To view your browser in VNC go to: {vnc_url}")
    browser.close()
```

## Cloud Usage

Cloud is early access. Use the same `/connect` flow with a different endpoint
and an API key:

```python
resp = httpx.get(
    "https://cloud.rayobrowse.com/connect",
    params={"os": "windows", "headless": "false"},
    headers={"x-api-key": "YOUR_API_KEY"},
    timeout=120,
)
cdp_url = resp.text.strip()
```

## SDK Usage

The SDKs are optional wrappers around the same HTTP API.

Python:

```python
from rayobrowse import Rayobrowse

client = Rayobrowse(endpoint="http://localhost:9222")
cdp_url = client.connect_url(os="windows", headless=False, vnc=True)
```

Node.js:

```typescript
import { Rayobrowse } from 'rayobrowse';

const client = new Rayobrowse({ endpoint: 'http://localhost:9222' });
const cdpUrl = await client.connectUrl({ os: 'windows', headless: false, vnc: true });
```

Use the SDK when you need session IDs, reconnects, VNC URL tracking, typed
errors, browser listing, or explicit close/status calls.

## Ports

| Port | Purpose |
| --- | --- |
| `9222` | HTTP daemon and CDP proxy |
| `6080` | noVNC viewer when requested with `vnc=true` |

## Common Failures

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `Connection refused` on port `9222` | Container is not running | `docker compose up -d` |
| Health check fails | Daemon still starting or container crashed | `docker compose logs -f` |
| Playwright says `/connect` is not a WebSocket | Using the old direct connect flow | Call HTTP `/connect`, then connect to the returned CDP URL |
| noVNC is unavailable | VNC was not requested for that browser | Add `vnc=true` to the `/connect` call and read `x-vnc-url` |
| Browser exits after script finishes | Normal cleanup after CDP disconnect | Use SDK/session APIs for keep-alive or reconnect workflows |
