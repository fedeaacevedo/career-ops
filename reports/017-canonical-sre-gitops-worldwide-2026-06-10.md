# Evaluation: Canonical — Site Reliability / GitOps Engineer

**Date:** 2026-06-10
**URL:** https://job-boards.greenhouse.io/canonical/jobs/1747487
**Archetype:** DevOps/SRE/Platform
**Score:** 3.6/5
**Legitimacy:** Proceed with Caution
**PDF:** not generated (batch mode)
**Verification:** unconfirmed (batch mode — WebFetch used)

---

## A) Role Summary

| Field | Detail |
|---|---|
| Archetype | Site Reliability / GitOps Engineer |
| Domain | Cloud infrastructure, IS/IT operations, IaC, CI/CD |
| Function | Operate and automate cloud/container services for Canonical's internal IS team |
| Seniority | Mid-to-Senior IC (no explicit level stated, but peer review + mentoring implied) |
| Remote Policy | Home-based, worldwide — any timezone |
| Team | Internal IS team supporting 60M+ Ubuntu users |
| Travel | 2–4 in-person events/year, 1–2 weeks each, international |
| Compensation | Not disclosed |
| TL;DR | SRE/GitOps IC role inside Canonical's IS team: own automation, cloud/container reliability, IaC development, observability with Prometheus/Grafana, and incident response. Strong Python + Linux networking + Ceph required. GitOps and CI/CD are core. |

---

## B) Match with CV

| JD Requirement | Federico's Experience | Fit |
|---|---|---|
| Infrastructure as Code / GitOps | Terraform (production use at Seeker and Estudiantes), GitHub Actions, GitLab CI/CD | Strong |
| CI/CD pipeline development | GitHub Actions + GitLab CI/CD across multiple roles | Strong |
| Linux administration (enterprise) | Linux servers at Disney; Linux in AWS/DevOps stack across Seeker, Estudiantes | Strong |
| Cloud computing expertise | AWS production environments at Estudiantes and Seeker; AWS CCP + SAA certified | Strong |
| Prometheus + Grafana observability | Prometheus + Grafana in production (listed explicitly in CV skills) | Strong |
| Kubernetes | Kubernetes in CV skills and toolchain | Strong |
| Docker / containers | Docker in CV skills and active use | Strong |
| Python development (large projects) | Not explicitly evidenced in CV — infra/ops tooling background, not Python dev background | **Gap** |
| Linux networking, routing, firewall | Networking in CV (VPC, Route53, Nginx); not explicitly deep L2/L3 networking expertise | Partial |
| Storage systems (Ceph, databases) | PostgreSQL, MySQL, MariaDB present; Ceph not mentioned | **Gap** — Ceph specifically |
| Peer review / unit testing discipline | Not explicitly evidenced | Weak |
| Open-source / Ubuntu / Debian familiarity | Linux administration background; Ubuntu/Debian not explicitly called out | Moderate |
| Strong English communication | B1-B2 intermediate; technical environments comfortable | Partial — async/written English likely fine, spoken may be borderline |
| Bachelor's degree in CS or related | Not stated in CV | Unknown |
| Travel willingness (2–4 events/year) | Argentina-based, travel possible | Acceptable |
| Mentoring colleagues | Tech Lead at Seeker, CTO at Estudiantes | Strong |

**Summary of Gaps:**
- **Python development at project scale** is the most notable gap. The JD calls for Python experience "on large projects" — Federico's CV shows infra/ops tooling (Terraform, Docker, Kubernetes) but does not demonstrate Python development as a primary skill.
- **Ceph storage** is not present in Federico's stack. The JD lists it explicitly.
- **Deep Linux networking** (L2/L3, routing tables, firewall rulesets) is partially covered via AWS VPC and Nginx but is not explicitly evidenced at enterprise Linux level.
- **Open-source contribution** to Ubuntu/Debian ecosystem is not evidenced — Canonical weights this.
- **English** at B1-B2 is workable for async-first remote teams (Canonical is famous for async culture), but Canonical's interview process is entirely in English and technical — this is a real friction point.

**Mitigation:** Federico's IaC + CI/CD + Kubernetes + Prometheus/Grafana + Linux + AWS profile maps very well to the operational and automation core of the role. The Python and Ceph gaps are real but not necessarily dealbreakers if he can demonstrate scripting and automation work in Python (even basic). Canonical's interview process (tests + take-home assignments) rewards depth of reasoning over surface credentials.

---

## C) Level and Strategy

**JD Level:** Mid-to-Senior IC (SRE/GitOps contributor with mentoring expectation)
**Federico's Level:** Senior/Lead (DevOps Tech Lead at Seeker, CTO/Tech Manager at Estudiantes)

**Level fit:** Federico is likely slightly over-leveled as a pure IC here, but Canonical frequently hires strong engineers who prefer IC depth over management scope. His lead/CTO experience actually strengthens the application — it shows ownership, not just execution.

**"Sell senior" plan:**
- Lead with production reliability ownership: "I managed AWS production environments at Estudiantes de La Plata serving tens of thousands of users and led incident response, observability, and platform reliability improvements."
- Anchor on GitOps discipline: Terraform + GitHub Actions/GitLab CI/CD + Kubernetes is a direct match.
- Frame mentoring: as CTO and Tech Lead, Federico has already supported and mentored engineering and operations teams.
- Address Python: if Federico has any scripting or automation in Python (even infra tooling, Lambda, small automation scripts), surface it explicitly. If not, be honest that scripting/automation has primarily been in Bash/HCL/YAML and express willingness to deepen Python.
- Address Ceph: acknowledge it as a learning area; show database and storage administration depth as related signal.

**"If downleveled" plan:** Not likely — Canonical does not typically downlevel experienced engineers applying as ICs. The bigger risk is domain rejection on Python depth.

---

## D) Comp and Demand

**Canonical compensation context:**
- Canonical is known for globally competitive but not top-of-market compensation for SRE/IC roles.
- Based on comparable Canonical SRE/GitOps roles and public data: estimated USD 60,000–90,000/year (USD 5,000–7,500/month) for senior IC in most geographies.
- For Argentina-based remote candidates, Canonical typically pays market-competitive rates based on global bands rather than location-adjusted rates — this is a meaningful positive for LATAM applicants.
- Fully remote worldwide + travel budget is part of the total package.

**Demand signal:** Canonical regularly posts SRE and infrastructure roles. This specific posting (Greenhouse job ID 1747487) is active as of evaluation date but Greenhouse postings at Canonical can remain open for extended periods while they pipeline candidates through their multi-stage process.

**Assessment for Federico:** Estimated comp likely falls at or above his $4,000–6,000/month USD target. Canonical's global remote-first model is highly attractive for Argentina-based candidates given they do not typically apply significant geographic discounts.

---

## E) Customization Plan

**Top 3 CV/application changes:**

1. **Surface Python explicitly.** Even if Federico's Python use has been limited to scripts, Lambda functions, or automation tooling — add it. Canonical's JD specifically calls for Python "on large projects." If he has any Python-based infrastructure automation or tooling, document it. If not, acknowledge it as active learning in the cover letter.

2. **Strengthen the GitOps / IaC narrative.** Rewrite the Seeker Parking and Estudiantes bullet points to explicitly mention infrastructure-as-code disciplines: "Managed infrastructure as code using Terraform; deployed and operated containerized workloads via Kubernetes with automated CI/CD pipelines via GitHub Actions / GitLab CI/CD." Make the GitOps story unambiguous.

3. **Add Linux systems depth signals.** Emphasize Linux server administration specifics: distributions used, networking configuration, firewall management, system-level automation. Canonical is an Ubuntu company — any Ubuntu-specific experience (even personal) is worth mentioning.

---

## F) Interview Plan

Canonical uses a multi-stage process: application screening → written interview (async) → take-home technical assignment → technical panel → hiring manager review. Written English quality matters significantly.

**STAR Stories to prepare:**

1. **Production reliability ownership** — Estudiantes de La Plata: AWS production environment serving tens of thousands of users. Situation: responsible for reliability of critical club services. Task: ensure uptime, observability, and incident response. Action: implemented monitoring with Prometheus/Grafana/Zabbix; managed incident response. Result: stable platform supporting digital transformation initiatives. Reflection: learned to balance automation investment against operational urgency.

2. **Infrastructure as Code transformation** — Seeker Parking or Estudiantes: Situation: infrastructure managed inconsistently. Task: introduce IaC discipline. Action: implemented Terraform to codify cloud resources; integrated with GitHub Actions/GitLab CI/CD for automated deployments. Result: consistent, repeatable infrastructure across environments. Reflection: IaC as the foundation of operational reliability.

3. **Incident response under pressure** — Any role: Situation: production incident impacting users. Task: diagnose and restore service. Action: used observability stack (Prometheus/Grafana) to identify root cause; coordinated response; applied fix and post-mortem. Result: service restored; process improvement implemented. Reflection: the value of pre-built observability before incidents occur.

4. **Mentoring / knowledge transfer** — Seeker Parking (Tech Lead) or Estudiantes (CTO): Situation: team with mixed seniority levels. Task: improve operational consistency and lift team's infrastructure maturity. Action: introduced documentation practices, runbooks, and shared tooling. Result: reduced operational incidents; faster onboarding. Reflection: senior engineers multiply impact through others.

5. **Cross-team collaboration on architecture** — Mercedes-Benz or Estudiantes: Situation: infrastructure or integration decision required alignment across development, operations, and business stakeholders. Task: facilitate technical decision and documentation. Action: led architecture review, documented decision rationale, coordinated implementation. Result: aligned decision, fewer rework cycles. Reflection: documentation culture and async communication as force multipliers.

6. **Cloud cost and capacity planning** — Estudiantes or Seeker: Situation: cloud costs trending upward or capacity needed evaluation. Task: assess current resource usage and project future needs. Action: analyzed CloudWatch metrics, reviewed infrastructure allocation, proposed rightsizing or scaling strategy. Result: cost clarity and operational confidence. Reflection: capacity planning as a proactive reliability discipline.

---

## G) Posting Legitimacy

| Signal | Assessment |
|---|---|
| Source | Greenhouse ATS (job-boards.greenhouse.io/canonical) — Canonical's official ATS |
| Company verification | Canonical Ltd. is a well-established, legitimate company (Ubuntu publisher, founded 2004) |
| Job ID | 1747487 — specific numeric ID, not a generic or recycled posting |
| Role specificity | Detailed JD with specific technical requirements (Ceph, Python at project scale, Linux networking) — not a generic copy-paste |
| Compensation transparency | Not disclosed — typical for Canonical (they discuss comp later in process) |
| Red flags | None detected |
| Travel requirement | Disclosed upfront (2–4 events/year, international) — positive transparency signal |
| Remote policy | Worldwide, any timezone — consistent with Canonical's established global remote model |

**Legitimacy Tier: Legitimate** — Canonical is a well-known, established employer with a consistent hiring process on their official Greenhouse instance. No red flags. The undisclosed compensation is typical for Canonical (not a scam signal). The role description is specific and technically credible.

---

## Keywords Extracted

`GitOps`, `Infrastructure as Code`, `CI/CD`, `Kubernetes`, `Python`, `Prometheus`, `Grafana`, `Elasticsearch`, `Ceph`, `Linux networking`, `Cloud automation`, `SRE`, `Capacity planning`, `Incident response`, `Ubuntu`

---

## Machine Summary

```yaml
num: 17
date: 2026-06-10
company: Canonical
role: Site Reliability / GitOps Engineer
score: 3.6
status: Evaluated
pdf: false
url: https://job-boards.greenhouse.io/canonical/jobs/1747487
slug: canonical-sre-gitops-worldwide
```
