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

Check again with `curl --verbose --max-time 2 http://localhost:9222/health`.

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

If still broken, inspect the logs with `docker logs <container ID>` and do your best to troubleshoot from there.

# Using rayobrowse

## Proxy URL

If the user wants to use a proxy service, have them expose their proxy URL in the environment variable `AUTOMATION_PROXY`.
For example, in Rayobyte, they can go to Residential > Proxy Access and then copy their proxy URL from there.

To test that the automation proxy takes you through different IPs:

```sh
curl api.ipify.org
curl -x $AUTOMATION_PROXY api.ipify.org
```

## playwright-cli

[playwright-cli](https://github.com/microsoft/playwright-cli) is the preferred tool for an AI agent to interact directly with `rayobrowse`.
Ask the user to install `playwright-cli` if it's not available.

1.  Get the Chrome DevTools Protocol URL:
    ```sh
    CDP_URL=$(curl -s -D /tmp/rayoheaders.txt "http://localhost:9222/connect?os=windows&headless=false&vnc=true${AUTOMATION_PROXY:+&proxy=$AUTOMATION_PROXY}")
    ```
    If the user is interested in the VNC URL, extract it from the headers file:
    ```sh
    echo $(grep -i '^x-vnc-url:' /tmp/rayoheaders.txt | awk '{print $2}')
    ```
2.  Have`playwright-cli` use the Chrome DevTools Protocol URL:
    ```sh
    playwright-cli attach --cdp "$CDP_URL"
    ```
3.  Check that the exit IP address is different from the host:
    ```sh
    curl api.ipify.org
    playwright-cli goto "https://api.ipify.org"
    playwright-cli snapshot
    ```

To close the browser:
```bash
curl -X POST http://localhost:9222/api/browser/close -d "{\"sessionId\": \"${CDP_URL##*/}\"}"
```
