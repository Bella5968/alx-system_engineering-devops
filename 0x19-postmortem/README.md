Postmortem: Web Application Outage on February 28, 2025

Issue Summary
Duration:
February 28, 2025, 14:10 - 15:05 UTC (55 minutes)
Impact:
Our primary e-commerce application was unavailable for 55 minutes. During this period, approximately 85% of users were unable to load product pages, and checkout API calls were timing out. This led to a significant revenue drop, as customers could not complete their purchases.
Root Cause:
A misconfiguration in the Nginx load balancer, introduced during a routine deployment, caused traffic to be routed to an unhealthy and outdated server. This server was not fully compatible with the current application version, leading to a cascade of 502 Bad Gateway errors.

Timeline
14:10 UTC - Monitoring system triggered an alert for increased error rates and degraded response times.
14:12 UTC - On-call engineer began investigating using Grafana and Kibana dashboards.
14:15 UTC - Initial suspicion focused on a possible database connectivity issue, leading to a database health check.
14:25 UTC - Application server logs were inspected, but no direct errors were observed.
14:35 UTC - Further review of Nginx logs uncovered repeated 502 Bad Gateway errors.
14:40 UTC - The Nginx configuration was reviewed, and a typo in the upstream server list was identified.
14:45 UTC - The incident was escalated to the DevOps team for immediate rollback.
14:55 UTC - Correct configuration was redeployed.
15:05 UTC - Service was fully restored and error rates returned to normal.

Root Cause and Resolution
Root Cause
The root cause was a typo in the Nginx upstream configuration file. During a recent deployment, an incorrect IP address was added to the upstream list, pointing to an old and unused server that still hosted an outdated version of the application. Nginx’s basic health checks were insufficient to detect the incompatibility, so it continued sending traffic to this server, causing 502 errors.
Resolution
The Nginx configuration was rolled back to the previous, correct version. The faulty server was immediately decommissioned to avoid future accidental usage. Once Nginx began routing requests to the correct servers, error rates dropped and the service was fully restored.

Corrective and Preventative Measures
Improvements Needed
Strengthen the review process for load balancer configuration changes.
Improve health checks to detect version mismatches and application health more effectively.
Enhance alerting and dashboards to highlight upstream routing errors sooner.
Introduce pre-deployment validation to test upstream reachability and compatibility.
Specific Tasks (TODO)
Implement automated syntax validation for Nginx configurations in the CI/CD pipeline.
Add comprehensive health checks to ensure upstream servers are running the expected version.
Introduce a pre-deployment test that verifies upstream servers are responsive and compatible.
Update incident response runbooks to prioritize reviewing load balancer configurations.
Schedule a blameless postmortem review to share findings and recommendations across teams.
