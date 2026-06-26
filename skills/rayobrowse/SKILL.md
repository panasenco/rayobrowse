---
name: rayobrowse
description: Stealth Chromium browser for scraping and automation, running in Docker.
---

# Start rayobrowse

## Check if already running

Run this command to check the service health:
```sh
curl --verbose --max-time 2 http://localhost:9222/health
```

If unsuccessful, check whether anything is running with `docker compose ls`.

## Prerequisites
- Ensure Docker is installed.
- Locate the directory of this skill file.

Note that starting the stack for the first time will download a 2.5GB Docker image so set a timeout of no less than 10 mins for the command.

## Port forward mode

Start `rayobrowse` in port forward mode by default:

```sh
docker compose -f /path/to/skills/rayobrowse/assets/docker-compose-port-forward.yml up -d
```

## Host network mode

If experiencing networking issues in port forward mode or explicitly requested, start in host network mode:

```sh
docker compose -f /path/to/skills/rayobrowse/assets/docker-compose-host-network.yml up -d
```

## Checking health

```sh
curl --verbose --max-time 2 http://localhost:9222/health
```

"Connection refused" is normal within the first ~3 mins as the service starts up.

Getting a timeout points to networking issues.
The user is likely running Tailscale or similar software interfering with Docker networking.

To check for sure:
1.  Run `docker ps` to get the container ID.
2.  Run `docker exec <container ID> curl --verbose --max-time 2 http://localhost:9222/health`.

If the curl is timing out on the host but not in the container, you likely need to switch to host networking:
```sh
docker compose -f /path/to/skills/rayobrowse/assets/docker-compose-port-forward.yml down
docker compose -f /path/to/skills/rayobrowse/assets/docker-compose-host-network.yml up -d
```
