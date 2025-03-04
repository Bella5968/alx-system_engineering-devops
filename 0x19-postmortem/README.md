🚨 Postmortem: The Great Nginx Typo Apocalypse of February 28, 2025 🚨
📅 Issue Summary
Duration:
⏰ February 28, 2025, 14:10 - 15:05 UTC (55 minutes of pure chaos)

Impact:
💥 Our glorious e-commerce website took a 55-minute nap, leaving 85% of our users staring at error screens like this:

502 Bad Gateway
(a fancy way of saying "Something broke and we have no idea what")

📉 Result: Shopping carts abandoned, revenue tanked, and some users probably switched to our competitors. Ouch.

Root Cause:
A tiny typo (yes, a single wrong digit) in the Nginx upstream configuration sent traffic to a retired, outdated, and very confused server. That server had no idea what to do with modern requests and politely responded with a 502 Bad Gateway.

🕒 Timeline (a rollercoaster in bullet points)
14:10 UTC - PagerDuty screamed at the on-call engineer about high error rates.
14:12 UTC - On-call engineer grabs coffee and stares at Grafana like it’s a horror movie.
14:15 UTC - Initial theory: "The database is probably drunk again."
(Spoiler: It wasn’t.)
14:25 UTC - Server logs checked — everything looks innocent. Suspiciously innocent.
14:35 UTC - Nginx logs exposed the crime scene: repeated 502 Bad Gateway errors.
14:40 UTC - A typo in the upstream list was discovered. Plot twist: It was pointing to an ancient server.
14:45 UTC - DevOps team summoned like superheroes.
14:55 UTC - Correct config deployed, typo destroyed.
15:05 UTC - Service back online. Users rejoiced. On-call engineer went for more coffee.
😱 The Culprit — Illustrated
    +--------------------+
    |   Nginx Load Balancer   |
    +--------------------+
                |
                v
    +-----------------+           +-----------------+
    | Correct Server   | <-- YES  |  Old Retired Server  | <-- NOPE
    +-----------------+           +-----------------+
Actual config:
upstream app_servers { server 10.0.0.42; server 10.0.0.12; }

Broken config:
upstream app_servers { server 10.0.0.42; server 10.0.0.21; }
(That .21 server was retired last year. RIP.)

🐞 Root Cause & Fix
What went wrong?
During deployment, someone (naming no names, but it rhymes with "caffeine-starved engineer") manually edited the Nginx config and fat-fingered an IP address.
Nginx happily forwarded traffic to the wrong server — one that was too old to party with the new app.
How we fixed it
Immediately reverted to the last known good configuration.
Terminated the rogue old server to prevent future ghost sightings.
Set up pre-deployment validation to make sure this never happens again.
✅ Lessons & Action Items
What we learned
Typos are the devil.
Manual config edits are a dangerous sport.
Old servers should be decommissioned properly (not left lurking like zombies).
Concrete To-Do List
 Add syntax checks to the deployment pipeline.
 Improve Nginx health checks — no more blindly trusting old servers.
 Automate upstream IP validation.
 Update our runbooks to always check load balancer configs first.
 Conduct a blameless retro and buy donuts for the on-call team.
Final Thoughts
"To err is human, but to really mess things up requires a load balancer."
