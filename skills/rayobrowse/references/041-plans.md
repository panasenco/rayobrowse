# Self-Hosted and Cloud

> Source: https://docs.rayobrowse.com/plans/

Self-hosted rayobrowse is free and unlimited. rayobrowse Cloud is in early access for teams that want managed infrastructure, orchestration, one-click proxies, observability, and less fleet maintenance.

## Self-hosted

Section titled “Self-hosted”

  - Free and unlimited self-hosted use.
  - No registration required.
  - Bring your own infrastructure and proxies.
  - Same core stealth engine included in every release.
  - MIT-licensed wrapper with a separately licensed rayobrowse Browser Binary.

## Cloud early access

Section titled “Cloud early access”

Cloud is for teams that want to scale without operating their own browser fleet:

  - Managed browser infrastructure.
  - Auto-scaling and orchestration.
  - Session queuing instead of failed creates at capacity.
  - Managed datacenter, ISP, and residential proxies.
  - Central dashboard, VNC viewing, usage reporting, and debugging tools.
  - A path to move from local development to production with the same `/connect` flow.

We have optimized our infrastructure so that, for many teams, using rayobrowse Cloud can be cheaper than running your own servers, proxies, monitoring, and DevOps effort.

Cloud is currently in early access. Contact [[email protected]](https://docs.rayobrowse.com/cdn-cgi/l/email-protection#8af9ebe6eff9caf8ebf3e5e8f3feefa4e9e5e7) if you want to test it.

## Self-hosted vs Cloud

Section titled “Self-hosted vs Cloud”

| Self-Hosted (Free)| Cloud  
---|---|---  
**Core Browser Engine**| |   
Full stealth engine (50+ spoofed signals)| ✅| ✅  
Fingerprint spoofing (UA, WebGL, Canvas, fonts, timezone, audio, and more) from real-world devices| ✅| ✅  
Patent-pending Canvas Fingerprint Spoofing that provides real canvas data (not noise, which is detectable)| ❌ - Noise, works for 90% of websites| ✅ - Patent-pending technology makes you look like a real user  
CDP compatible — Playwright, Puppeteer, Selenium, and more| ✅| ✅  
Desktop fingerprints (Windows, Linux, macOS)| ✅| ✅  
Headless & headful modes| ✅| ✅  
Proxy support (bring your own)| ✅| ✅  
Human mouse movement| ✅| ✅  
**Infrastructure & Operations**| |   
Central dashboard — start, stop, VNC view, traffic usage, and more| ❌| ✅  
Orchestration — auto-scaling, zombie cleanup, OOM protection| ❌| ✅  
Session queuing — requests queue at capacity instead of failing| ❌| ✅  
Automatic engine & software updates| ❌| ✅  
**Proxy & Network**| |   
Managed proxy — datacenter, ISP, and residential in one click| ❌| ✅  
Proxies optimized for browser use — long sessions, low ban rates| ❌| ✅  
**Monitoring & Debugging**| |   
Live VNC from anywhere — no reverse proxy or tunneling needed| ❌| ✅  
Usage analytics & cost reporting| ❌| ✅  
Budget & proxy cost alerts (email, webhook)| ❌| Soon  
Session replay — record and replay browser sessions| ❌| Soon  
Remote Dev Tools — inspect any browser from the dashboard| ❌| Soon  
**Advanced Features**| |   
Real-world fingerprints - captured exactly how the anti-bot companies do it| ✅ Limited fingerprints available| ✅ Tens of thousands of real-world fingerprints  
Android mobile fingerprint| ❌| ✅  
Persistent browser profiles — save & restore state across sessions| ❌| Beta  
Smart Cache — speed up runs and save up to 90% on proxy costs| ❌| Soon  
**Collaboration**| |   
Team accounts with role-based access| ❌| 🔜  
Audit logs| ❌| 🔜  
  
## Next steps

Section titled “Next steps”

  - [Local quickstart](https://docs.rayobrowse.com/quickstart-local)
  - [Cloud quickstart](https://docs.rayobrowse.com/quickstart-cloud)
  - [Licensing](https://docs.rayobrowse.com/licensing)
