---
name: rayobrowse
description: Stealth Chromium browser (HTTP/CDP) for scraping and automation. Load this skill to start, fix, or connect to rayobrowse — especially on "Connection refused" on port 9222, docker/container issues, or when scripts import from rayobrowse or connect to localhost:9222. Covers setup (docker compose), fingerprinting, proxies, sessions, and human-like behavior.
---

## ⚡ Ad-hoc browsing: playwright-cli (token-efficient)

**For ad-hoc browsing (research, quick checks, one-off interactions), use
`playwright-cli` instead of writing Playwright scripts.** CLI commands save
massive tokens when an AI agent is driving the browser interactively.

For **scripted automation** (loops, conditionals, data pipelines, reusable
skills), Python + Playwright remains the best approach — see SDK sections below.

### Quick start with rayobrowse

```bash
# 1. Get a CDP URL from rayobrowse
CDP_URL=$(curl -s "http://localhost:9222/connect?os=windows&headless=false&vnc=true")

# 2. Attach playwright-cli to it
playwright-cli attach --cdp "$CDP_URL"

# 3. Browse with simple commands
playwright-cli goto "https://duckduckgo.com"
playwright-cli snapshot                    # see page structure (refs)
playwright-cli click "ref=e22"             # click by element ref
playwright-cli type "search query"
playwright-cli press Enter
playwright-cli screenshot                  # save screenshot
playwright-cli close                       # done
```

### Why playwright-cli > raw Playwright code

| | playwright-cli | Python/Node Playwright |
|---|---|---|
| **Tokens per action** | ~10 | ~50-200 |
| **Setup boilerplate** | 2 lines (curl + attach) | 15-30 lines |
| **Agent-friendly** | Yes — bash commands | Needs script files |
| **Snapshot** | Built-in YAML with element refs | Manual `page.content()` |
| **Sessions** | Automatic via `-s=name` | Manual session management |

### Key commands

| Command | What it does |
|---------|-------------|
| `attach --cdp <url>` | Connect to rayobrowse CDP session |
| `goto <url>` | Navigate |
| `snapshot [target]` | Page structure as YAML with clickable refs |
| `click <target>` | Click element (by ref, text, or CSS) |
| `fill <target> <text>` | Fill input field |
| `type <text>` | Type into focused element |
| `press <key>` | Keyboard key (Enter, Tab, etc.) |
| `screenshot [target]` | Save screenshot |
| `select <target> <val>` | Select dropdown option |
| `upload <file>` | Upload file |
| `tab-list` | List open tabs |
| `tab-new [url]` | Open new tab |
| `close` | Close browser |

### Multi-session example

```bash
# Session 1: research
CDP1=$(curl -s "http://localhost:9222/connect?os=windows&headless=false&vnc=true")
playwright-cli attach research --cdp "$CDP1"
playwright-cli -s=research goto "https://example.com"

# Session 2: different site, same time
CDP2=$(curl -s "http://localhost:9222/connect?os=windows&headless=false&vnc=true")
playwright-cli attach work --cdp "$CDP2"
playwright-cli -s=work goto "https://other-site.com"

# Switch between them freely
playwright-cli -s=research snapshot
playwright-cli -s=work click "Sign In"
```

### Install

```bash
npm install -g @playwright/cli@latest
playwright-cli install --skills   # optional: installs agent skills
```

---

## What rayobrowse is

> **When to use what**: `playwright-cli` (above) for ad-hoc browsing —
> research, quick checks, one-off interactions. Python/Node SDK (below)
> for scripted automation — loops, conditionals, data pipelines, reusable skills.

rayobrowse is a patched Chromium browser that runs inside Docker. It defeats bot
detection by spoofing 50+ fingerprint signals (User-Agent, WebGL, canvas, fonts,
screen, timezone, audio, WebRTC, …) so they tell a coherent story about a single
real device. You connect via the standard Chrome DevTools Protocol (CDP), so any
tool that speaks CDP — Playwright, Puppeteer, Selenium — works without changes.

**Two deployment modes:**

| Mode | Base URL | Auth |
|------|----------|------|
| Local (self-hosted, free) | `http://localhost:9222` | none |
| Cloud (managed, early access) | `https://cloud.rayobrowse.com` | `x-api-key` header |

---

## Prerequisites

<prereqs>
- Docker with Compose v2 (`docker compose`) installed.
- The current user must be able to run `docker` without `sudo`.
- Python 3.10+ **or** Node.js 18+ depending on which automation client is used.
- About 2 GB free RAM per browser instance.
</prereqs>

---

## Setup (local)

<setup>

1. **Start the container** using the bundled compose file in this skill's `assets/` folder.
   Resolve the absolute path before running:

   ```bash
   docker compose -f /path/to/skills/rayobrowse/assets/docker-compose.yml up -d
   ```

   Or, if working inside the `rayobrowse` repo:

   ```bash
   cp .env.example .env          # default .env.example works for local dev
   docker compose up -d
   ```

2. **Verify it is healthy:**

   ```bash
   curl http://localhost:9222/health
   # Expected: {"success": true, "data": {"status": "healthy", ...}}
   ```

   If the health check fails, wait a few seconds and retry, or check logs:

   ```bash
   docker compose logs -f
   ```

3. **Install the automation client** (choose one):

   ```bash
   # Playwright (Python)
   pip install httpx playwright && playwright install chromium

   # Playwright (Node)
   npm install playwright

   # Puppeteer (Node)
   npm install puppeteer-core
   ```

</setup>

---

## Core usage pattern

<core_pattern>

**Never connect Playwright/Puppeteer/Selenium directly to `/connect`.**
`/connect` is an HTTP endpoint, not a WebSocket. The correct flow is:

1. `GET /connect` → receive a CDP WebSocket URL as plain text.
2. Pass that CDP URL to your automation client.
3. The browser closes when the CDP session closes (unless `keepAlive=true`).

```
GET http://localhost:9222/connect?os=windows&headless=false
                                ↓ plain-text response body
ws://localhost:9222/cdp/<session-id>
                                ↓ connect your CDP client here
playwright.chromium.connect_over_cdp(cdp_url)
```

</core_pattern>

### Minimal end-to-end example

**Python (Playwright):**

```python
import os
import httpx
from playwright.sync_api import sync_playwright

# Optional: set AUTOMATION_PROXY=http://user:pass@host:port to route all traffic
# through a proxy (auto-matches timezone/locale to the proxy's geolocation).
proxy = os.environ.get("AUTOMATION_PROXY")

params = {"os": "windows", "headless": "false", "vnc": "true"}
if proxy:
    params["proxy"] = proxy

resp = httpx.get(
    "http://localhost:9222/connect",
    params=params,
    timeout=120,
)
resp.raise_for_status()

cdp_url = resp.text.strip()
vnc_url = resp.headers.get("x-vnc-url") or "http://localhost:6080/vnc.html"
print(f"\n👁  Watch live in your browser → {vnc_url}\n")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(cdp_url)
    context = browser.contexts[0] if browser.contexts else browser.new_context()
    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

**Node.js (Playwright):**

```js
const { chromium } = require('playwright');

// Optional: set AUTOMATION_PROXY=http://user:pass@host:port to route all traffic
// through a proxy (auto-matches timezone/locale to the proxy's geolocation).
const proxy = process.env.AUTOMATION_PROXY;
const params = new URLSearchParams({ os: 'windows', headless: 'false', vnc: 'true' });
if (proxy) params.set('proxy', proxy);

const resp = await fetch(`http://localhost:9222/connect?${params}`);
const cdpUrl = (await resp.text()).trim();
const vncUrl = resp.headers.get('x-vnc-url') || 'http://localhost:6080/vnc.html';
console.log(`\n👁  Watch live in your browser → ${vncUrl}\n`);

const browser = await chromium.connectOverCDP(cdpUrl);
const context = browser.contexts()[0] || await browser.newContext();
const page = context.pages()[0] || await context.newPage();
await page.goto('https://example.com');
console.log(await page.title());
await browser.close();
```

**Node.js (Puppeteer):**

```js
const puppeteer = require('puppeteer-core');

// Optional: set AUTOMATION_PROXY=http://user:pass@host:port to route all traffic
// through a proxy (auto-matches timezone/locale to the proxy's geolocation).
const proxy = process.env.AUTOMATION_PROXY;
const params = new URLSearchParams({ os: 'windows', headless: 'false', vnc: 'true' });
if (proxy) params.set('proxy', proxy);

const resp = await fetch(`http://localhost:9222/connect?${params}`);
const cdpUrl = (await resp.text()).trim();
const vncUrl = resp.headers.get('x-vnc-url') || 'http://localhost:6080/vnc.html';
console.log(`\n👁  Watch live in your browser → ${vncUrl}\n`);

const browser = await puppeteer.connect({ browserWSEndpoint: cdpUrl });
const page = (await browser.pages())[0] || await browser.newPage();
await page.goto('https://example.com');
console.log(await page.title());
await browser.disconnect();
```

---

## `/connect` parameters reference

| Parameter | Default | Description |
|-----------|---------|-------------|
| `headless` | `true` | `true` = headless (no display); `false` = headful with Xvnc — **use `false` in all scripts for realism and observability** |
| `os` | `linux` | Fingerprint OS: `windows` ✅ (recommended), `android` ✅, `linux`, `macos` |
| `browser_version_min` | latest | Min Chrome version to emulate (match to `146` for best results) |
| `browser_version_max` | latest | Max Chrome version to emulate (match to `146` for best results) |
| `proxy` | none | `http://user:pass@host:port` — routes all traffic and auto-matches timezone |
| `browser_language` | auto | `Accept-Language` value, e.g. `en-US` |
| `ui_language` | auto | Browser UI locale |
| `screen_width_min` | auto | Minimum screen width px, e.g. `1366` |
| `screen_height_min` | auto | Minimum screen height px, e.g. `768` |
| `vnc` | `false` | If `true`, response includes `x-vnc-url` header for live viewing |
| `keepAlive` | `false` | Keep browser alive after CDP disconnect; use with `sessionId` to reconnect |
| `sessionId` | none | Reconnect to an existing keep-alive session (`br_…`) |
| `maxLifetime` | none | Hard session TTL in seconds |
| `token` | none | API key as a query param (alternative to `x-api-key` header) |

**Recommended defaults for best stealth:**

```
os=windows&headless=false&vnc=true&browser_version_min=146&browser_version_max=146
```

Headful mode (`headless=false`) renders a real display, which avoids headless-detection
heuristics that many anti-bot systems check. Always pair it with `vnc=true` so you and
the user can observe the browser live.

---

## Stealth and human-like behavior

<stealth>

- **Always use `os=windows`** for the broadest, most tested fingerprint coverage.
- **Pin the browser version** (`browser_version_min=146&browser_version_max=146`) —
  a mismatched version is a cross-signal inconsistency detection systems flag immediately.
- **Route through a proxy** when targeting geo-restricted or heavily protected sites;
  rayobrowse auto-matches timezone and locale to the proxy's geolocation.
- **Do not do things only a bot would do:**
  - Don't navigate at machine speed from page to page; add short, random delays.
  - Don't skip pages a real user would land on (cookie consent, landing pages).
  - Don't batch hundreds of requests from the same session without pausing.
- **Mouse movements are automatic**: rayobrowse applies Bezier-curve trajectories and
  realistic click timing to standard `page.click()` / `page.mouse.move()` calls.
  No code changes are required to benefit from this.
- **Avoid CDP-only patterns** that leak automation intent (raw `evaluate()` injection
  of large scripts on every page, unthrottled network intercept, etc.).

</stealth>

---

## Common workflows

### Web scraping with a proxy

Set `AUTOMATION_PROXY=http://user:pass@proxy-host:port` in your environment before
running the script. rayobrowse will automatically match the timezone and locale to
the proxy's geolocation, strengthening fingerprint coherence.

```python
import os
import httpx
from playwright.sync_api import sync_playwright

proxy = os.environ.get("AUTOMATION_PROXY")  # e.g. http://user:pass@proxy-host:port

params = {
    "headless": "false",
    "os": "windows",
    "vnc": "true",
    "browser_version_min": "146",
    "browser_version_max": "146",
}
if proxy:
    params["proxy"] = proxy

resp = httpx.get(
    "http://localhost:9222/connect",
    params=params,
    timeout=120,
)
resp.raise_for_status()
cdp_url = resp.text.strip()
vnc_url = resp.headers.get("x-vnc-url") or "http://localhost:6080/vnc.html"
print(f"\n👁  Watch live in your browser → {vnc_url}\n")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(cdp_url)
    page = browser.contexts[0].pages[0]
    page.goto("https://target-site.com")
    print(page.content())
    browser.close()
```

### Keep-alive sessions (reconnectable browsers)

Useful for AI agents or multi-step workflows where you need the same browser state
across separate script invocations.

```bash
# Create a keep-alive headful browser
curl -i "http://localhost:9222/connect?os=windows&headless=false&keepAlive=true&vnc=true"
# Response headers:
#   x-session-id: br_59245e8658532863
#   x-vnc-url: http://localhost:6080/vnc.html?path=vnc/br_59245e8658532863&token=

# Reconnect to the same browser later
curl "http://localhost:9222/connect?sessionId=br_59245e8658532863"
```

Python SDK equivalent:

```python
import os
from rayobrowse import Rayobrowse
from playwright.sync_api import sync_playwright

proxy = os.environ.get("AUTOMATION_PROXY")  # optional: http://user:pass@host:port

client = Rayobrowse(endpoint="http://localhost:9222")
ws_url = client.connect_url(os="windows", headless=False, vnc=True, keep_alive=True,
                            **({"proxy": proxy} if proxy else {}))
session_id = client.last_session_id
print(f"\n👁  Watch live in your browser → {client.last_vnc_url}\n")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_url)
    page = browser.contexts[0].pages[0]
    page.goto("https://example.com")
    browser.close()

# Later — reconnect without losing browser state
# Note: reconnect_url() returns the CDP URL; VNC URL is unchanged from the original session.
ws_url = client.reconnect_url(session_id)
print(f"Resumed session {session_id}")
```

### Inspect and close sessions

```bash
# List all active browsers
curl "http://localhost:9222/api/browsers"

# Get status of a specific session
curl "http://localhost:9222/api/browser/br_59245e8658532863/status"

# Explicitly close a session
curl -X POST "http://localhost:9222/api/browser/close" \
  -H "Content-Type: application/json" \
  -d '{"sessionId": "br_59245e8658532863"}'
```

### Debugging with VNC

1. Start a headful browser with `headless=false&vnc=true`.
2. Read the `x-vnc-url` response header.
3. Open that URL in your local browser (noVNC, no install required).

> VNC stream may appear laggy — this is a display artifact only; the remote browser
> runs at full speed and appears fast to target sites.

---

## Cloud usage

Same `/connect` flow, different base URL and API key:

```python
resp = httpx.get(
    "https://cloud.rayobrowse.com/connect",
    params={"os": "windows", "headless": "false"},
    headers={"x-api-key": "YOUR_API_KEY"},
    timeout=120,
)
cdp_url = resp.text.strip()
```

The API key can also be passed as `?token=YOUR_API_KEY` in the query string.

---

## Configuration

| Env var | Default | Purpose |
|---------|---------|---------|
| `RAYOBROWSE_PORT` | `9222` | Host port for the HTTP daemon |
| `RAYOBYTE_ENDPOINT` | `http://localhost:9222` | Used by SDK and example scripts |
| `RAYOBYTE_API_KEY` | — | Cloud API key, used by SDK and example scripts |
| `AUTOMATION_PROXY` | — | Proxy URL (`http://user:pass@host:port`) forwarded to every `/connect` call; set once in the environment instead of hardcoding per script |

### AUTOMATION_PROXY — agent guidance

Whenever you write a script that calls `/connect`, read `AUTOMATION_PROXY` from the
environment and pass it as the `proxy` parameter if it is set. Tell the user:

> **Proxy:** If you want all browser traffic routed through a proxy, set
> `AUTOMATION_PROXY=http://user:pass@host:port` before running this script.
> rayobrowse will automatically match the timezone and locale to the proxy's
> geolocation, so you don't need to touch the script itself.
>
> Only HTTP proxies are supported (`http://…`). SOCKS proxies are not currently
> supported by rayobrowse.

The container requires `shm_size: 2g` and `seccomp=unconfined` (both set in the
bundled `assets/docker-compose.yml`). Budget ~300 MB RAM per concurrent browser.

---

## Common failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Connection refused` on port 9222 | Container not running | `docker compose up -d` |
| Health check fails | Daemon still starting or crashed | Wait, then `docker compose logs -f` |
| Playwright error: `/connect` is not a WebSocket | Connecting CDP client to the HTTP endpoint directly | Call HTTP `/connect` first, then connect to the returned CDP URL |
| Site blocks the session | Fingerprint mismatch or bot-like behavior | Use `os=windows`, pin `browser_version_min/max=146`, add a proxy, slow down navigation |
| noVNC unavailable | VNC not requested | Add `vnc=true` to the `/connect` call |
| `ERR_TUNNEL_CONNECTION_FAILED` | Proxy config broken | Test proxy directly with `curl -x` against `httpbin.org/ip`; check for missing `http://` scheme in `AUTOMATION_PROXY` |
| Rayobyte proxy returns `551 No Proxy` | Invalid geo-targeting suffix or state unavailable | Use `-region-statename` only — do **not** include `-country-XX` (Rayobyte doesn't support it and returns 551); if state is unavailable, try another or use bare credentials. See `014-features-proxy-support.md` |

---

## Reference files

Detailed documentation lives in `references/` next to this file:

| Topic | File |
|-------|------|
| Introduction & overview | `001-introduction.md` |
| Local quickstart | `002-quickstart-local.md` |
| Cloud quickstart | `003-quickstart-cloud.md` |
| `/connect` endpoint (all params) | `006-local-connect-endpoint.md` |
| Configuration & env vars | `007-local-configuration.md` |
| Fingerprint spoofing internals | `013-features-fingerprinting.md` |
| Proxy support | `014-features-proxy-support.md` |
| Headless vs headful & VNC | `015-features-headless-headful.md` |
| Session management | `016-features-session-management.md` |
| Human mouse behavior | `017-features-human-mouse.md` |
| Python SDK | `019-sdks-python-quickstart.md`, `020-sdks-python-reference.md` |
| Node.js SDK | `021-sdks-node-quickstart.md`, `022-sdks-node-reference.md` |
| Playwright integration | `024-integrations-playwright.md` |
| Puppeteer integration | `025-integrations-puppeteer.md` |
| Selenium integration | `026-integrations-selenium.md` |
| Scrapy integration | `028-integrations-scrapy.md` |
| API reference | `029-api-reference-overview.md` – `037-api-reference-cloud-browser-status.md` |
| Web scraping use case | `038-use-cases-web-scraping.md` |
| AI agents use case | `039-use-cases-ai-agents.md` |
