---
name: rayobrowse
description: Stealth Chromium browser (HTTP/CDP) for scraping and automation. Load this skill to start, fix, or connect to rayobrowse — especially on "Connection refused" on port 9222, docker/container issues, or when scripts import from rayobrowse or connect to localhost:9222. Covers setup (docker compose), fingerprinting, proxies, sessions, and human-like behavior.
---

## ⚡ Ad-hoc browsing: playwright-cli (token-efficient)

**For ad-hoc browsing (research, quick checks, one-off interactions), use
`playwright-cli` instead of writing Playwright scripts.** For scripted automation
(loops, conditionals, data pipelines), use Python + Playwright (see below).

```bash
CDP_URL=$(curl -s "http://localhost:9222/connect?os=windows&headless=false&vnc=true")
playwright-cli attach --cdp "$CDP_URL"
playwright-cli goto "https://duckduckgo.com"
playwright-cli snapshot          # page structure with clickable refs
playwright-cli click "ref=e22"
playwright-cli screenshot
playwright-cli close
```

| Command | What it does |
|---------|-------------|
| `attach --cdp <url>` | Connect to rayobrowse CDP session |
| `goto <url>` | Navigate |
| `snapshot [target]` | Page structure as YAML with element refs |
| `click <target>` | Click element (by ref, text, or CSS) |
| `fill <target> <text>` | Fill input field |
| `type <text>` | Type into focused element |
| `press <key>` | Keyboard key (Enter, Tab, etc.) |
| `screenshot [target]` | Save screenshot |
| `select <target> <val>` | Select dropdown option |
| `upload <file>` | Upload file |
| `tab-list` / `tab-new [url]` | Manage tabs |
| `close` | Close browser |

---

## What rayobrowse is

rayobrowse is a patched Chromium in Docker that defeats bot detection by spoofing
50+ fingerprint signals coherently. Connect via CDP — Playwright, Puppeteer, or
Selenium all work without changes.

| Mode | Base URL | Auth |
|------|----------|------|
| Local (self-hosted) | `http://localhost:9222` | none |
| Cloud (managed) | `https://cloud.rayobrowse.com` | `x-api-key` header or `?token=` |

## Prerequisites

- Docker with Compose v2, user can run `docker` without `sudo`
- Python 3.10+ or Node.js 18+
- ~2 GB free RAM per browser instance

## Setup (local)

1. **Start the container:**
   ```bash
   docker compose -f /path/to/skills/rayobrowse/assets/docker-compose.yml up -d
   ```

2. **Verify health:**
   ```bash
   curl http://localhost:9222/health
   ```
   If unhealthy, wait a few seconds or check `docker compose logs -f`.

3. **Install client:**
   On most OSes:
   ```bash
   pip install httpx playwright
   ```
   
   On NixOS - run your scripts with:
   ```sh
   nix-shell -p python3Packages.playwright python3Packages.httpx
   ```
   
---

## Core usage pattern

**Never connect CDP clients directly to `/connect`.** It's an HTTP endpoint:

1. `GET /connect` → returns a CDP WebSocket URL as plain text
2. Pass that URL to `connect_over_cdp()` / `puppeteer.connect()`
3. Browser closes when CDP disconnects (unless `keepAlive=true`)

### Python example (Playwright)

```python
import os
import httpx
from playwright.sync_api import sync_playwright

proxy = os.environ.get("AUTOMATION_PROXY")  # http://user:pass@host:port

params = {
    "os": "windows", "headless": "false", "vnc": "true",
    "browser_version_min": "146", "browser_version_max": "146",
}
if proxy:
    params["proxy"] = proxy

resp = httpx.get("http://localhost:9222/connect", params=params, timeout=120)
resp.raise_for_status()
cdp_url = resp.text.strip()
vnc_url = resp.headers.get("x-vnc-url", "")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(cdp_url)
    context = browser.contexts[0] if browser.contexts else browser.new_context()
    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

For Node.js (Playwright/Puppeteer) examples, see `024-integrations-playwright.md`
and `025-integrations-puppeteer.md` in the references section.

---

## `/connect` parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `headless` | `true` | `false` = headful with Xvnc — **use for realism + observability** |
| `os` | `linux` | `windows` ✅ (recommended), `android` ✅, `linux`, `macos` |
| `browser_version_min` | latest | Pin to `146` for best results |
| `browser_version_max` | latest | Pin to `146` for best results |
| `proxy` | none | `http://user:pass@host:port` — auto-matches timezone/locale |
| `browser_language` | auto | `Accept-Language` value |
| `ui_language` | auto | Browser UI locale |
| `screen_width_min` | auto | Minimum screen width px |
| `screen_height_min` | auto | Minimum screen height px |
| `vnc` | `false` | Response includes `x-vnc-url` header for live viewing |
| `keepAlive` | `false` | Keep browser alive after CDP disconnect |
| `sessionId` | none | Reconnect to existing keep-alive session (`br_…`) |
| `maxLifetime` | none | Hard session TTL in seconds |
| `token` | none | API key as query param (alternative to `x-api-key` header) |

**Recommended:** `os=windows&headless=false&vnc=true&browser_version_min=146&browser_version_max=146`

---

## Stealth and human-like behavior

- **Always use `os=windows`** — broadest, most tested fingerprint coverage.
- **Pin browser version** to `146` — mismatches are flagged by detection systems.
- **Route through a proxy** for geo-restricted/protected sites (auto-matches tz/locale).
- **Don't act like a bot:** add random delays, don't skip pages, don't batch hundreds of requests.
- **Mouse movements are automatic:** Bezier curves + realistic click timing on all `page.click()` calls.
- **Avoid CDP-only patterns** that leak intent (large `evaluate()` injections, unthrottled intercepts).

---

## Common workflows

### Keep-alive sessions

```bash
# Create — response headers include x-session-id and x-vnc-url
curl -i "http://localhost:9222/connect?os=windows&headless=false&keepAlive=true&vnc=true"

# Reconnect later
curl "http://localhost:9222/connect?sessionId=br_59245e8658532863"
```

### Session management

```bash
curl "http://localhost:9222/api/browsers"                          # list active
curl "http://localhost:9222/api/browser/br_59245e8658532863/status" # status
curl -X POST "http://localhost:9222/api/browser/close" \
  -H "Content-Type: application/json" \
  -d '{"sessionId": "br_59245e8658532863"}'                        # close
```

### Debugging with VNC

Start with `headless=false&vnc=true`, open the `x-vnc-url` in your browser (noVNC).
VNC stream may appear laggy — display artifact only; the remote browser runs full speed.

### Retrying on proxy tunnel failures

Residential proxies rotate exit IPs per connection. Some may be dead/blocked, causing
`ERR_TUNNEL_CONNECTION_FAILED`. The proxy IP is fixed **per `/connect` session**, so
retrying `page.goto()` won't help — wrap the **entire session** so each retry gets a
new browser with a fresh exit IP:

```python
from tenacity import retry, retry_if_exception_message, stop_after_attempt, wait_fixed

@retry(
    retry=retry_if_exception_message(match=r".*ERR_TUNNEL_CONNECTION_FAILED"),
    stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True,
)
def scrape(url: str) -> str:
    resp = httpx.get("http://localhost:9222/connect",
                     params={"os": "windows", "headless": "false",
                             "proxy": os.environ["AUTOMATION_PROXY"]},
                     timeout=120)
    resp.raise_for_status()
    with sync_playwright() as pw:
        browser = pw.chromium.connect_over_cdp(resp.text.strip())
        page = browser.contexts[0].pages[0]
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)
        content = page.content()
        browser.close()
    return content
```

**Note:** `tenacity`'s `match=` uses `re.match()` (anchored to start), so always
prefix patterns with `.*` to match mid-string.

---

## Configuration

| Env var | Default | Purpose |
|---------|---------|---------|
| `RAYOBROWSE_PORT` | `9222` | Host port for the HTTP daemon |
| `AUTOMATION_PROXY` | — | Proxy URL forwarded to every `/connect` call |

When writing scripts, always read `AUTOMATION_PROXY` from the environment and pass
it as the `proxy` parameter if set. Only HTTP proxies are supported (not SOCKS).

Container requires `shm_size: 2g` and `seccomp=unconfined` (set in bundled
`assets/docker-compose.yml`). Budget ~300 MB RAM per concurrent browser.

---

## Common failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Connection refused` on 9222 | Container not running | `docker compose up -d` |
| Health check fails | Daemon starting or crashed | Wait, then `docker compose logs -f` |
| `/connect` is not a WebSocket | CDP client pointed at HTTP endpoint | Call `/connect` first, connect to returned CDP URL |
| Site blocks session | Fingerprint mismatch / bot behavior | Use `os=windows`, pin version `146`, add proxy, slow down |
| `ERR_TUNNEL_CONNECTION_FAILED` | Proxy exit IP dead/blocked | Retry with **new `/connect` session** for fresh IP; if persistent, test with `curl -x`; check `http://` scheme |
| `551 No Proxy` (Rayobyte) | Invalid geo-targeting suffix | Use `-region-statename` only — no `-country-XX`; try another state or bare credentials |
| noVNC unavailable | VNC not requested | Add `vnc=true` to `/connect` |

---

## Reference files

Detailed docs in `references/` next to this file:

| Topic | File |
|-------|------|
| Introduction | `001-introduction.md` |
| Local quickstart | `002-quickstart-local.md` |
| Cloud quickstart | `003-quickstart-cloud.md` |
| `/connect` endpoint | `006-local-connect-endpoint.md` |
| Configuration | `007-local-configuration.md` |
| Fingerprinting | `013-features-fingerprinting.md` |
| Proxy support | `014-features-proxy-support.md` |
| Headless/headful & VNC | `015-features-headless-headful.md` |
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
