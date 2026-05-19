# Fingerprint Spoofing

> Source: https://docs.rayobrowse.com/features/fingerprinting/

Stealth fingerprinting is the core of rayobrowse. We spend more engineering time on this than anything else in the product, because we think the math is simple: if your browser can’t get past detection, none of your downstream code matters. You can’t scrape data you can’t reach.

Every rayobrowse session gets assigned a full device profile from a database of thousands of real fingerprints. These profiles are collected using the same techniques that the major anti-bot vendors use. Each session spoofs **over 50 individual signals** , and those signals all match each other.

## Why cross-signal consistency matters

Section titled “Why cross-signal consistency matters”

Most stealth tools will set a valid User-Agent, spoof a few canvas/WebGL values, and call it a day. That worked in 2020. Modern detection systems are smarter than that.

Anti-bot platforms cross-reference your fingerprint signals against each other. They look at whether your User-Agent, OS platform, navigator properties, GPU renderer, installed fonts, screen size, timezone, and everything else actually belong to the same device. A Windows User-Agent with macOS fonts? Flagged. A mobile screen resolution with a desktop GPU? Flagged. A European timezone with a US locale and no proxy? Flagged.

Getting individual values right is the easy part. Getting 50+ signals to tell a coherent story about a single real device is the hard part, and it’s what we focus on.

How detection actually works 

Detection systems don’t just check if your User-Agent is valid. They build a profile from dozens of signals and check whether the whole thing is self-consistent. A real Windows desktop has a specific set of fonts, a specific range of screen resolutions, specific WebGL renderers, and so on. If any of those are wrong for the claimed device, you’re caught.

## What we spoof

Section titled “What we spoof”

This table covers the high-level categories. Each one includes multiple individual signals and sub-properties.

Category| What’s covered  
---|---  
**User-Agent & Client Hints**| Full UA string, `Sec-CH-UA` headers, `userAgentData` API, platform and architecture hints  
**OS / Platform**| `navigator.platform`, `oscpu`, platform-specific behavioral differences  
**Screen & Display**| Resolution, color depth, device pixel ratio, available screen area, multi-monitor consistency  
**WebGL**|  GPU renderer, vendor, extensions, shader precision, parameter limits, all matched to real hardware  
**Canvas**|  Noise-adjusted canvas fingerprint with realistic per-device variance  
**Fonts**|  Enumerable font list matched to target OS and locale  
**WebRTC**|  Local/public IP leak protection, media device enumeration, SDP munging  
**Timezone**|  Auto-matched to proxy geolocation via MaxMind GeoLite2, `DateTimeFormat` consistency  
**CPU & Memory**| `hardwareConcurrency`, `deviceMemory`, matched to realistic hardware profiles  
**Audio**|  AudioContext fingerprint noise, sample rate, channel configuration  
**Locale & Language**| `navigator.language`, `languages`, `Intl` API configuration, accept-language headers  
**Media Devices**|  Realistic camera/microphone device enumeration  
**Battery**|  Battery API status consistent with device type  
**Network & Connection**| `navigator.connection` properties, downlink, effective type  
**Permissions & Feature Policy**| Consistent permission states, feature policy responses  
**Plugin & MIME Types**| Chromium-accurate plugin list, MIME type support  
**Automation Signals**|  No `navigator.webdriver`, no leaked Playwright/Puppeteer artifacts, no CDP traces  
  
Note 

This is the summary, not the full list. Many categories contain several sub-signals. WebGL alone covers the renderer string, vendor string, supported extensions, max texture size, max viewport dimensions, shader precision format, and more. All internally consistent per profile.

## How fingerprints are selected

Section titled “How fingerprints are selected”

  - Profiles are selected dynamically based on the `os` and `browser_version_min`/`max` parameters
  - Each session gets a unique, internally consistent combination from the profile database
  - For deterministic environments, you can load a static fingerprint file. Contact [[email protected]](https://docs.rayobrowse.com/cdn-cgi/l/email-protection#76050306061904023604170f19140f02135815191b) for templates.

## Our Chromium fork

Section titled “Our Chromium fork”

This isn’t a JavaScript wrapper on top of stock Chromium. We maintain a patched fork of Chromium that we track against upstream releases:

  - Browser APIs are normalized and hardened at the C++ level
  - Fingerprint entropy leaks that stock Chromium exposes are eliminated
  - Automation artifacts that detection systems scan for are removed
  - Native Chromium behavior is preserved everywhere else so sites see a real browser

We validate every release against internal test targets before shipping. When Chromium pushes a new version, we typically patch, test, and release within days.

## OS recommendations

Section titled “OS recommendations”

`os` value| Status| Notes  
---|---|---  
`windows`| **Recommended**|  Most thoroughly tested, best detection avoidance  
`android`| **Recommended**|  Well tested for mobile fingerprints  
`linux`| Experimental| Available but not primary focus  
`macos`| Experimental| Available but not primary focus  
  
## Version matching

Section titled “Version matching”

Set `browser_version_min` and `browser_version_max` to match the current Chromium version (currently **146**) for the best results. A mismatched version is exactly the kind of cross-signal inconsistency that detection systems look for.
