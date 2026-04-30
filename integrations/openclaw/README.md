# OpenClaw + rayobrowse

Run [OpenClaw](https://openclaw.ai) with a stealth Chromium session that uses a
realistic device fingerprint.

## How It Works

rayobrowse uses an HTTP-first connection flow:

1. Call `GET /connect` with the browser and fingerprint options you want.
2. Read the returned CDP WebSocket URL from the response body.
3. Give that CDP URL to OpenClaw as its browser endpoint.

```text
curl /connect  --->  CDP WebSocket URL  --->  OpenClaw  --->  rayobrowse browser
```

## Start rayobrowse

From the repo root:

```bash
cp .env.example .env
docker compose up -d
curl -s http://localhost:9222/health
```

## Configure OpenClaw

Request a browser and store the returned CDP URL:

```bash
CDP_URL=$(curl -fsS "http://localhost:9222/connect?headless=true&os=windows")
```

Add a `rayobrowse` profile:

```bash
openclaw config set browser.enabled true
openclaw config set browser.defaultProfile rayobrowse
openclaw config set "browser.profiles.rayobrowse.cdpUrl" "$CDP_URL"
```

Or set it directly in `~/.openclaw/openclaw.json`:

```json5
{
  browser: {
    enabled: true,
    defaultProfile: "rayobrowse",
    profiles: {
      rayobrowse: {
        cdpUrl: "ws://localhost:9222/cdp/br_59245e8658532863",
      },
    },
  },
}
```

The CDP URL is session-specific. If OpenClaw closes the browser and you want a
new session, call `/connect` again and update the profile.

## Options

Pass options as query parameters to `/connect`:

```bash
curl -fsS "http://localhost:9222/connect?headless=true&os=android&proxy=http://user:pass@proxy.example.com:8080"
```

Common parameters:

| Parameter | Example | Description |
| --- | --- | --- |
| `headless` | `headless=true` | Run with or without a visible browser window. |
| `os` | `os=windows` | Target OS fingerprint: `windows`, `linux`, `android`, or `macos`. |
| `proxy` | `proxy=http://user:pass@host:port` | Browser-level proxy. |
| `browser_version_min` | `browser_version_min=146` | Minimum Chrome fingerprint version. |
| `browser_version_max` | `browser_version_max=146` | Maximum Chrome fingerprint version. |
| `keepAlive` | `keepAlive=true` | Keep the browser open across CDP disconnects. |

## Watch With VNC

Request VNC in the `/connect` call and read the `x-vnc-url` response header:

```bash
curl -i "http://localhost:9222/connect?headless=false&os=windows&vnc=true"
```

Open the returned VNC URL in your browser.

## Cloud

rayobrowse Cloud is in early access. The flow is the same, but the endpoint is
`https://cloud.rayobrowse.com` and requests use an API key.

```bash
CDP_URL=$(curl -fsS "https://cloud.rayobrowse.com/connect?headless=true&os=windows" \
  -H "x-api-key: YOUR_API_KEY")
```

Contact `sales@rayobyte.com` for access.

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| `Connection refused` on port 9222 | Container not running | `docker compose up -d` |
| OpenClaw says the browser is unavailable | Profile not set or session closed | Request a fresh `/connect` URL and update the profile |
| User-Agent mismatch detected | Another layer is overriding headers | Let rayobrowse control browser request headers |
| Can't see the browser | Browser was started headless or without VNC | Use `headless=false&vnc=true` and open `x-vnc-url` |
