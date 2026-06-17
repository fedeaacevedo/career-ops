# Evaluation: Canonical — Site Reliability Engineer

**Date:** 2026-06-10
**URL:** https://job-boards.greenhouse.io/canonical/jobs/4468036
**Archetype:** DevOps/SRE/Platform
**Score:** 3.4/5
**Legitimacy:** Tier 1 — Active, credible posting from a well-known open source company
**PDF:** not generated (batch mode)
**Verification:** unconfirmed (batch mode — WebFetch used)

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| **Company** | Canonical Ltd — publisher of Ubuntu, leading open source software and OS provider |
| **Role** | Site Reliability Engineer |
| **Location** | Home-based, Worldwide (fully remote) |
| **Team focus** | Deploying and operating OpenStack, Kubernetes, storage, and open source apps for enterprise customers |
| **Stack** | OpenStack, Kubernetes, Python, Linux, bare-metal networking, cloud (public + private) |
| **Employment** | Full-time, permanent |
| **Travel** | Twice yearly, 1-2 weeks each, international (mandatory) |
| **Comp** | Undisclosed base — adjusted every 6 months by location/experience/performance + annual bonus |
| **Benefits** | $2,000/year L&D budget, priority pass, maternity/paternity leave, EAP |

**Context:** Canonical is a globally distributed company (1,200+ people, 75+ countries, remote since 2004). The SRE team manages hundreds of private cloud clusters and customer deployments. The role spans the full infrastructure stack, with heavy emphasis on OpenStack and Python-based automation.

---

## B) Match with CV

| Requirement | Federico's Level | Evidence |
|------------|-----------------|----------|
| Linux operational experience | Strong | Walt Disney + Estudiantes + Seeker Parking (servers, VMs, production) |
| Kubernetes deployment/operations | Good | Kubernetes in DevOps stack; active hands-on (Seeker Parking) |
| Python software development | Partial | Not explicitly listed in CV; significant gap vs. JD emphasis |
| OpenStack deployment/operations | Weak | Not mentioned; no direct experience |
| Public cloud experience | Good | AWS environments (EC2, RDS, S3, IAM, VPC, CloudWatch, etc.) |
| Private cloud management | Partial | VMware/Proxmox at Disney; limited OpenStack |
| Observability and monitoring | Strong | Prometheus, Grafana, Zabbix across multiple roles |
| Automation / infrastructure-as-code | Good | Terraform, Docker, GitHub Actions, GitLab CI/CD |
| Incident response / production ops | Good | Estudiantes La Plata — large-scale user-facing production operations |
| Degree in CS/Software Engineering | Unknown | Not stated in CV; gap if degree is strictly required |
| English proficiency for global team | Moderate risk | B1-B2; Canonical is English-first async distributed culture |

**Key gaps:**
1. **Python development depth** — Canonical treats SRE as software engineering; the JD explicitly asks for Python experience as a coding/engineering skill, not just scripting. Federico's CV does not surface Python.
2. **OpenStack** — Core to Canonical's private cloud product. No exposure mentioned.
3. **Formal CS degree** — Listed as a requirement. Federico's educational background is not specified in the CV, which could be a disqualifier at application screening.
4. **English fluency** — Canonical operates as a globally distributed English-first company. Async written English is likely manageable at B1-B2, but live collaboration, on-call escalation, and technical interviews in English carry meaningful risk.

---

## C) Level & Strategy

**Level assessment:** This is a mid-to-senior individual contributor SRE role. Canonical does not differentiate by title in the posting — the team structure is flat with experienced engineers working across the full stack. Federico's experience aligns with the seniority band, but the technical profile skews infrastructure/cloud operations while Canonical needs someone closer to the software-engineering-meets-SRE boundary (Python, OpenStack).

**Strategy if applying:**
- Lead with Linux, Kubernetes, observability (Prometheus/Grafana), and production incident management. These are strong matches.
- Do not hide the OpenStack gap — acknowledge it as a learning curve but position VMware/Proxmox private cloud experience and cloud infrastructure depth as transferable.
- Add any Python experience (even scripting, automation, Ansible) to the CV before applying. The gap is critical.
- Prepare to demonstrate operational maturity at scale: Canonical evaluates how engineers think about automation, metrics-driven ops, and incident response, not just tool familiarity.
- English risk is real at Canonical — written async English is the daily operating mode. Prepare to demonstrate clear technical writing in the application and cover letter.

---

## D) Comp & Demand

| Dimension | Detail |
|-----------|--------|
| **Canonical published range** | Not disclosed — adjusted per location, experience, performance |
| **Market context (SRE, remote)** | SRE roles globally: $90k-$140k/year USD at senior level |
| **Argentina location adjustment** | Canonical adjusts pay by location; Argentina typically discounts vs. US/EU by 40-60% |
| **Estimated range for Argentina** | ~$2,000-$3,500/month USD (location-adjusted) |
| **Federico's target** | $4,000-$6,000/month USD |
| **Gap** | Likely below target — Canonical's location-based pay model typically places LATAM contributors below North American bands |
| **Benefits offset** | $2,000 L&D budget, international travel, stability, open source brand — meaningful but unlikely to close the comp gap |

**Verdict:** Compensation is a meaningful risk. Canonical's transparent location-adjusted pay model is well documented in the open source community. Argentina typically lands in a lower pay band. The role is technically interesting but likely falls below Federico's $4,000/month floor. This should be explicitly clarified at first contact. The open source brand and global exposure have career-development value, but do not substitute for base compensation.

---

## E) Customization Plan

**Top 3 CV/application changes before applying:**

1. **Surface Python work explicitly.** Add any Python scripting, automation, or tooling work to the CV (even lightweight examples from infrastructure automation or CI/CD pipelines). Canonical's SRE role is Python-heavy and will screen for this at the application question stage.

2. **Expand the private cloud narrative.** Reframe VMware/Proxmox experience from Disney as private cloud infrastructure management. Acknowledge OpenStack as a learning goal, not a blocker. Map existing bare-metal and virtualization experience to Canonical's infrastructure domain.

3. **Write a strong cover letter in English demonstrating async communication quality.** Canonical reads written English daily. The cover letter and application answers (which Canonical requires as part of the application — they ask technical competency questions about Python, Linux, and containerization) are the primary screening surface. Invest heavily here to compensate for the English risk.

---

## F) Interview Plan

**Likely Canonical SRE interview topics and recommended STAR stories:**

1. **Production incident at scale (Linux/cloud)** — Estudiantes La Plata: describe an incident affecting tens of thousands of users, how it was detected (Prometheus/Grafana), how it was resolved, and what automation was introduced to prevent recurrence. This directly maps to Canonical's metrics-driven operations culture.

2. **Infrastructure automation with code** — Seeker Parking: describe building or improving a CI/CD pipeline or Terraform module that reduced manual work. Emphasize the software engineering mindset (code review, testing, idempotency) not just tool usage.

3. **Kubernetes deployment and operations** — Describe a Kubernetes environment managed in production: cluster setup, pod management, resource constraints, upgrade strategy. Focus on operational discipline and incident response.

4. **Handling ambiguity in a distributed team** — Canonical is async-first. Prepare a story about independently diagnosing and resolving a complex infrastructure problem with minimal synchronous guidance — documenting findings and communicating clearly across timezones.

5. **Observability and monitoring design** — Describe the observability stack built or improved (Prometheus, Grafana, Zabbix). Explain the alerting philosophy, what signals matter, how false positives were reduced, and how dashboards drove decisions.

6. **Python/scripting for automation** — If any Python (or Bash/scripting) automation was built, describe it with the software engineering lens: modularity, error handling, testing, maintainability. If Python is thin, frame this as an active development area with concrete learning steps.

---

## G) Posting Legitimacy

| Signal | Assessment |
|--------|------------|
| **Source** | Greenhouse ATS — canonical.com official hiring platform |
| **Company verification** | Canonical Ltd is a well-established, profitable company; Ubuntu publisher; globally recognized |
| **Job board legitimacy** | greenhouse.io/canonical — verified company-owned ATS job board |
| **Posting specificity** | Detailed technical requirements, explicit travel policy, clear benefits structure |
| **Application mechanism** | Standard Greenhouse form with technical screening questions |
| **Red flags** | None |
| **Posting age** | Not determinable from WebFetch alone; Canonical regularly runs ongoing SRE hiring |

**Assessment:** Tier 1 — Legitimate, active posting from a well-known, established company on their official ATS. No concerns about posting authenticity. The role is real and the company is stable.

---

## Keywords Extracted

1. Site Reliability Engineering
2. OpenStack
3. Kubernetes
4. Python
5. Linux
6. Bare-metal infrastructure
7. Private cloud
8. Public cloud
9. Observability
10. Incident management
11. Metrics-driven operations
12. Infrastructure automation
13. Open source
14. Distributed systems
15. DevOps

---

## Machine Summary

```yaml
num: 16
date: 2026-06-10
company: Canonical
role: Site Reliability Engineer
score: 3.4
status: Evaluated
pdf: false
url: https://job-boards.greenhouse.io/canonical/jobs/4468036
slug: canonical-sre-worldwide
```
