# Scrapy + rayobrowse

Use [Scrapy](https://scrapy.org) with a stealth browser that passes modern bot
detection.

Scrapy on its own does not render JavaScript. `scrapy-playwright` adds browser
rendering, and rayobrowse provides the browser: a Chromium session with a
realistic device fingerprint and standard CDP support.

## How It Works

rayobrowse exposes an HTTP `/connect` endpoint. Call it once to create a
browser and get a CDP WebSocket URL, then pass that returned URL to
`scrapy-playwright` through `PLAYWRIGHT_CDP_URL`.

```text
Scrapy spider
  |
  | scrapy-playwright download handler
  |
  v
Playwright  ---CDP--->  returned rayobrowse CDP URL  --->  stealth Chromium
```

## Start rayobrowse

```bash
git clone https://github.com/rayobyte-data/rayobrowse.git
cd rayobrowse
cp .env.example .env
docker compose up -d
curl -s http://localhost:9222/health
```

## Install dependencies

```bash
pip install scrapy scrapy-playwright httpx
```

You do not need `playwright install`; the browser runs inside the rayobrowse
container.

## Configure `settings.py`

```python
import httpx

_resp = httpx.get(
    "http://localhost:9222/connect",
    params={"headless": "true", "os": "windows"},
    timeout=120,
)
_resp.raise_for_status()
PLAYWRIGHT_CDP_URL = _resp.text.strip()

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
PLAYWRIGHT_PROCESS_REQUEST_HEADERS = None
```

`PLAYWRIGHT_PROCESS_REQUEST_HEADERS = None` is important. It prevents Scrapy
from overriding the User-Agent that rayobrowse set on the fingerprint.

## Use a Proxy

```python
_resp = httpx.get(
    "http://localhost:9222/connect",
    params={
        "headless": "true",
        "os": "windows",
        "proxy": "http://user:pass@proxy.example.com:8080",
    },
    timeout=120,
)
_resp.raise_for_status()
PLAYWRIGHT_CDP_URL = _resp.text.strip()
```

## Watch With VNC

Request a visible browser and VNC URL:

```python
_resp = httpx.get(
    "http://localhost:9222/connect",
    params={"headless": "false", "os": "windows", "vnc": "true"},
    timeout=120,
)
_resp.raise_for_status()
PLAYWRIGHT_CDP_URL = _resp.text.strip()
print("VNC:", _resp.headers.get("x-vnc-url"))
```

## Run the Example Project

From inside `example_project/`:

```bash
pip install -r requirements.txt
scrapy crawl quotes -o quotes.json
```

The `quotes` spider renders [quotes.toscrape.com/js](https://quotes.toscrape.com/js/)
through rayobrowse. The `books` spider is also available:

```bash
scrapy crawl books -o books.json
```

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| `Connection refused` on 9222 | Container not running | `docker compose up -d` |
| Empty page or no quotes | Missing `playwright: True` in request metadata | Add `meta={"playwright": True}` |
| User-Agent mismatch detected | Scrapy is overriding headers | Set `PLAYWRIGHT_PROCESS_REQUEST_HEADERS = None` |
| `ReactorNotRestartable` | Wrong Twisted reactor | Set `TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"` |
