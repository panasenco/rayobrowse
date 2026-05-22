# Proxy Support

> Source: https://docs.rayobrowse.com/features/proxy-support/

rayobrowse supports HTTP proxies at the browser level. All traffic from the session is routed through the proxy, and the fingerprint’s timezone and locale are automatically matched to the proxy’s geolocation.

## Usage

Section titled “Usage”

### Via HTTP /connect

Section titled “Via HTTP /connect”

Terminal window
    
    
    curl "http://localhost:9222/connect?headless=true&os;=windows&proxy;=http://user:pass@host:port"

### Via SDK

Section titled “Via SDK”
    
    
    client = Rayobrowse()
    
    ws_url = client.connect_url(os="windows", proxy="http://user:pass@host:port")
    
    
    const wsUrl = await client.connectUrl({
    
      os: 'windows',
    
      proxy: 'http://user:pass@host:port',
    
    });

## Self-hosted usage

Section titled “Self-hosted usage”

Self-hosted rayobrowse is free and unlimited whether you bring your own proxies or use [Rayobyte rotating proxies](https://rayobyte.com/products/). Cloud early access includes managed proxy options for teams that want browser infrastructure and proxies in one place.

## Proxy format

Section titled “Proxy format”
    
    
    http://username:password@hostname:port

SOCKS proxies are not currently supported.

## Rayobyte residential proxies — geo-targeting

> Source: https://portal.rayobyte.com/en/support/solutions/articles/64000283559-how-to-use-geo-targeting-by-state-with-residential-proxies

Rayobyte residential proxies support state-level geo-targeting by appending a suffix
to the **password** field:

```
username:password-region-statename@la.residential.rayobyte.com:8000
```

For multi-word states use underscores: `-region-New_York`.

**Full example (correct):**

```
http://rayobyte_user:mypassword-region-colorado@la.residential.rayobyte.com:8000
```

### Common Rayobyte mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Missing `http://` scheme | `ERR_TUNNEL_CONNECTION_FAILED` or silent failure | Prefix with `http://` — rayobrowse requires `http://user:pass@host:port` |
| `-country-XX` prefix in password (e.g. copied from some dashboards) | `551 No Proxy` from Rayobyte | Remove `-country-XX` entirely — Rayobyte only supports `-region-statename`, not country targeting |
| State not available on account | `551 No Proxy` | Try a different state or contact Rayobyte support; bare credentials (no targeting) work as a fallback |

### Diagnosing `551 No Proxy` vs other failures

Test with `curl` to isolate where the failure is:

```bash
# 1. Test bare credentials (no geo-targeting) — should return 200 if account is valid
curl -s -o /dev/null -w "%{http_code}" \
  -x "http://user:password@la.residential.rayobyte.com:8000" \
  --max-time 15 https://httpbin.org/ip

# 2. Test with geo-targeting appended
curl -s -o /dev/null -w "%{http_code}" \
  -x "http://user:password-region-colorado@la.residential.rayobyte.com:8000" \
  --max-time 15 https://httpbin.org/ip
```

- Bare = 200, targeted = 551 → wrong targeting syntax or state unavailable on plan
- Both fail → credentials invalid or account suspended
- Both = 200 → proxy is healthy; issue is elsewhere (e.g. missing `http://` in `AUTOMATION_PROXY`)

[ Previous   
Overview ](https://docs.rayobrowse.com/features/fingerprinting/) [ Next   
Headless & Headful ](https://docs.rayobrowse.com/features/headless-headful/)
