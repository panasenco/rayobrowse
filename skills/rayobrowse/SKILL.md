## Docker

A reliable way to run Rayobrowse locally is with Docker Compose. The steps below work even when the container needs to download the MaxMind GeoLite2 database.

```bash
# 1️⃣ Prepare the environment file (copy the example and accept the terms)
cp .env.example .env
# Add the required flag – the daemon will refuse to start without it
sed -i '/STEALTH_BROWSER_ACCEPT_TERMS/d' .env && echo "STEALTH_BROWSER_ACCEPT_TERMS=true" >> .env

# 2️⃣ (Optional) Pre‑download the GeoLite2 DB so the container does not have to fetch it at start‑up.
#    This avoids DNS‑related hangs inside the container.
mkdir -p data
curl -sL https://github.com/geoip/lite-db/releases/download/v202406/GeoLite2-City.mmdb -o data/GeoLite2-City.mmdb
curl -sL https://github.com/geoip/lite-db/releases/download/v202406/GeoLite2-Country.mmdb -o data/GeoLite2-Country.mmdb

# 3️⃣ Pull the latest image and (re)create the stack.
#    The bind‑mount (./data:/data) is used instead of a Docker volume so the DB files you placed above are visible to the daemon.
#    The DNS server 8.8.8.8 is injected to avoid host‑side DNS problems.

docker compose -f skills/rayobrowse/assets/docker-compose.yml pull

docker compose -f skills/rayobrowse/assets/docker-compose.yml up -d --force-recreate
```

# 4️⃣ Verify the service is healthy (wait a few seconds for the daemon to start).
curl -m 30 -s http://localhost:9222/health && echo "✅ healthy" || echo "❌ not healthy"
```

**Why the extra steps?**
- The daemon refuses to start without `STEALTH_BROWSER_ACCEPT_TERMS=true`.
- On first start it tries to download the MaxMind GeoLite2 database. If the container cannot resolve DNS, the start‑up hangs. Pre‑downloading the DB into `./data` (which is bind‑mounted to `/data`) circumvents this.
- Using a bind‑mount (`./data:/data`) makes the DB files persistent across container recreations without needing a named Docker volume.

If you still encounter DNS issues inside the container, you can force Docker to use a public DNS server by adding the `dns:` entry (already present in the compose file).
