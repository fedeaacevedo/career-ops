# Evaluation: Canonical — Senior Site Reliability Engineer

**Date:** 2026-06-10
**URL:** https://job-boards.greenhouse.io/canonical/jobs/3029798
**Archetype:** DevOps/SRE/Platform
**Score:** 3.6/5
**Legitimacy:** Credible — Active Listing
**PDF:** not generated (batch mode)
**Verification:** unconfirmed (batch mode — WebFetch used)

---

## A) Role Summary

| Field | Detail |
|---|---|
| Archetype | SRE / Platform / Infrastructure Automation |
| Domain | Open-source cloud infrastructure (OpenStack, Kubernetes, Canonical products) |
| Function | Operate and automate large-scale private cloud and Kubernetes clusters for enterprise customers |
| Seniority | Senior Individual Contributor |
| Remote Policy | Remote worldwide — strong positive for Federico |
| Travel | International twice yearly, 1-2 week company events (AllHands) |
| TL;DR | Senior SRE role managing hundreds of OpenStack/K8s clusters using Python-based infrastructure-as-code. Canonical product-centric, Linux and Python depth required. Compensation not published; market data suggests below Federico's target range. |

---

## B) Match with CV

| JD Requirement | Federico's Experience | Fit |
|---|---|---|
| Linux proficiency (networking, storage) | Walt Disney Infra/SysAdmin; Linux across all roles | Strong |
| Kubernetes operations | Kubernetes in current Seeker Parking role; used at Estudiantes La Plata | Solid |
| Cloud infrastructure operations | AWS (EC2, RDS, S3, IAM, VPC, Route53, Lambda, API GW, CloudWatch) at Estudiantes + Seeker | Strong |
| Python software development | Not listed as a primary skill in Federico's CV | Gap |
| OpenStack deployment/operations | No OpenStack experience apparent | Gap |
| Production operational experience | CTO/Tech Manager at Estudiantes La Plata: AWS production, observability, incident management | Strong |
| Automation / IaC | Terraform, GitHub Actions, GitLab CI/CD | Strong |
| Observability / monitoring | Prometheus, Grafana, Zabbix, CloudWatch | Strong |
| Degree in Software Engineering / CS | Not confirmed in candidate data — unverified | Risk |
| Interpersonal skills / async collaboration | International context across all roles; English B1-B2 | Adequate |

**Key gaps:**
1. **Python development depth** — JD explicitly requires Python as the primary IaC language; Federico's stack is Terraform/HCL-first. Python used operationally but not as a development discipline.
2. **OpenStack** — Canonical's core private cloud stack; Federico's cloud experience is AWS-native, not OpenStack.
3. **Canonical product ecosystem** — Juju, LXD, Charmed Kubernetes, Snaps are expected context; no exposure apparent.

**Strengths that carry weight:**
- AWS + Linux + Kubernetes combination is directly transferable to managing clusters.
- Strong observability stack (Prometheus, Grafana) matches SRE expectations.
- Incident management and production ownership at Estudiantes La Plata is directly relevant.
- Terraform IaC discipline shows the automation mindset; Python gap is learnable.

---

## C) Level & Strategy

**Level assessment:** The "Senior" SRE designation at Canonical is an IC role, not a management role. Federico's most recent trajectory (CTO, Tech Lead) means he would be stepping back from formal leadership into a senior IC position. This is a deliberate IC-track re-entry, which is viable but should be framed intentionally.

**Strategy:**
- Lead with production infrastructure ownership and incident management experience, not the management title.
- Reframe Terraform expertise as "infrastructure-as-code" that maps to Canonical's Python-first automation philosophy — and explicitly signal Python upskilling intent.
- Highlight the AWS + Kubernetes combination as directly applicable to multi-cluster management.
- Acknowledge the OpenStack gap proactively if asked; position AWS operational depth as transferable to private cloud operations.
- The twice-yearly travel requirement is minor and acceptable.

**Risk:** Canonical's SRE interview process is known to be rigorous (multiple technical rounds, coding/Python exercises). Python proficiency will be tested; Federico should prepare basic Python scripting for infra tasks before interviewing.

---

## D) Comp & Demand

| Dimension | Data |
|---|---|
| Published salary | Not disclosed — "competitive based on location, experience, performance" |
| Canonical SRE market reference (Glassdoor / Levels.fyi, ~2025) | USD $60K–$90K/year globally; LATAM-based employees typically in lower band (~$40K–$60K/year) |
| Monthly equivalent (LATAM band) | ~$3,300–$5,000/month |
| Federico's target | $4,000–$6,000/month |
| Annual learning budget | $2,000 — genuine and useful |
| Bonus | Performance-driven, not guaranteed |

**Verdict:** Compensation is a moderate risk. Canonical applies location-based pay; Argentina-based candidates historically land in the lower global band (~$3,300–$4,500/month), which may fall short of the $4–6K target. The $2K learning budget is a real positive. The role's technical scope (hundreds of clusters, open-source infrastructure at global scale) has significant career development value. Comp should be verified at the offer stage before committing.

**Demand signal:** Canonical hires continuously for SRE roles worldwide. This is a strong-demand archetype. The role is real and recurring; Canonical is profitable and hiring is not a red flag.

---

## E) Customization Plan

1. **Python and automation framing:** Rewrite the CV's IaC section to lead with "infrastructure automation" rather than just "Terraform." Add a brief Python scripting note if any Python has been used operationally (even simple scripts). This directly addresses the primary technical requirement.

2. **Production scale and reliability narrative:** The Estudiantes La Plata role should be expanded in the CV to highlight specific operational metrics: uptime, incident response times, number of services managed, AWS accounts/environments handled. Canonical SRE roles value quantified operational ownership.

3. **Observability stack prominence:** Move Prometheus, Grafana, Zabbix, and CloudWatch to a more visible position in the skills section or as a dedicated "Observability" category. This is a direct match to SRE expectations and differentiates Federico from generic DevOps candidates.

---

## F) Interview Plan

**Story 1 — Incident response at scale (Estudiantes La Plata)**
_Situation:_ AWS production outage or degraded service affecting club operations.
_Task:_ Restore service, identify root cause, prevent recurrence.
_Action:_ CloudWatch alerting, incident runbook execution, RDS/EC2 diagnosis, post-mortem.
_Result:_ Quantify: time to recovery, services restored, process improvements introduced.
_Relevance:_ Directly maps to SRE reliability ownership.

**Story 2 — Infrastructure automation (Seeker Parking or Estudiantes)**
_Situation:_ Manual or fragile deployment process for cloud infrastructure.
_Task:_ Automate provisioning to reduce risk and improve repeatability.
_Action:_ Terraform modules, GitHub Actions pipelines, environment parity.
_Result:_ Deployment frequency, error reduction, time saved.
_Relevance:_ Maps to Canonical's Python/IaC automation philosophy.

**Story 3 — Multi-environment Kubernetes management**
_Situation:_ Multiple Kubernetes clusters (dev/staging/prod) needing consistent management.
_Task:_ Standardize cluster configuration, observability, and deployment patterns.
_Action:_ Kubernetes manifests, Helm, monitoring integration (Prometheus/Grafana).
_Result:_ Reduced incidents, faster deployments, improved developer experience.
_Relevance:_ Direct parallel to managing "hundreds of Kubernetes clusters."

**Story 4 — Observability platform build (Estudiantes or Seeker)**
_Situation:_ Limited visibility into production systems; reactive incident detection.
_Task:_ Build proactive monitoring and alerting infrastructure.
_Action:_ Deployed Prometheus + Grafana stack; defined SLIs/SLOs; integrated Zabbix for legacy hosts.
_Result:_ Faster MTTD, reduced escalations, better capacity planning.
_Relevance:_ Core SRE discipline; Canonical values metric-driven operations explicitly.

**Story 5 — Cross-functional coordination under pressure (Mercedes-Benz)**
_Situation:_ Complex multi-vendor project with stakeholder alignment needs.
_Task:_ Coordinate technical delivery across teams and vendors.
_Action:_ Structured communication, risk tracking, clear ownership model.
_Result:_ On-time delivery or risk mitigation.
_Relevance:_ Canonical operates fully distributed; async coordination ability matters.

---

## G) Posting Legitimacy

| Signal | Assessment |
|---|---|
| Source | Greenhouse ATS — Canonical's official hiring platform |
| Company | Canonical Ltd — publisher of Ubuntu, profitable, 1200+ employees in 75+ countries |
| Role type | Recurring SRE hire — Canonical posts multiple SRE roles continuously |
| Compensation published | No — typical for Canonical (known for not publishing salaries) |
| Red flags | None — standard Canonical job structure |
| Legitimacy tier | **Credible — Active Listing** |

No ghost employer signals, no recruiter intermediary, no suspicious requirements. Canonical is a well-known open-source company with a documented hiring process. The absence of published comp is a known Canonical pattern, not a red flag.

---

## Keywords Extracted

1. Site Reliability Engineering (SRE)
2. Python infrastructure automation
3. OpenStack
4. Kubernetes (multi-cluster operations)
5. Linux (networking, storage)
6. Private cloud operations
7. DevSecOps
8. Software-defined storage
9. Infrastructure as code
10. Production operations at scale
11. Distributed systems
12. Open-source infrastructure
13. Prometheus / observability
14. Enterprise infrastructure
15. Remote worldwide

---

## Machine Summary

```yaml
num: 14
date: 2026-06-10
company: Canonical
role: Senior Site Reliability Engineer
score: 3.6
status: Evaluated
pdf: false
url: https://job-boards.greenhouse.io/canonical/jobs/3029798
slug: canonical-senior-sre-worldwide
```
