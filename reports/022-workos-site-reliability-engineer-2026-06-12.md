# Evaluación: WorkOS — Site Reliability Engineer

**Fecha:** 2026-06-12
**Arquetipo:** DevOps / SRE / Platform Engineer
**Score:** 2.5/5
**Legitimacy:** High Confidence (posting) / Proceed with Caution (geographic access)
**URL:** https://jobs.ashbyhq.com/workos/cff5a16f-fd1c-4b64-9b66-8a8321122375
**PDF:** not generated — run /career-ops pdf workos to create on demand
**Batch ID:** 7

---

## Machine Summary

```yaml
company: "WorkOS"
role: "Site Reliability Engineer"
score: 2.5
legitimacy_tier: "Proceed with Caution"
archetype: "DevOps / SRE / Platform Engineer"
final_decision: "Skip"
hard_stops:
  - "Geographic restriction: posting explicitly states United States & Canada only; Federico is Argentina-based with no relocation/visa path"
  - "TypeScript coding requirement: role requires writing and optimizing backend systems in TypeScript — not in Federico's profile"
  - "English level: US-based team requiring daily English for on-call, postmortems, and design discussions; B1-B2 may be insufficient"
soft_gaps:
  - "No formal SLI/SLO definition experience documented in CV"
  - "No production scale metrics (requests/sec, uptime %, service count) in CV"
  - "Postmortem leadership not explicitly mentioned"
top_strengths:
  - "AWS production stack (EC2, RDS, S3, IAM, VPC, CloudWatch, CloudTrail, Lambda, Route53) — direct match to primary requirement"
  - "Kubernetes, Prometheus, Grafana — all nice-to-have skills explicitly covered"
  - "Production operations and incident management ownership across Seeker Parking and Estudiantes de La Plata"
risk_level: "High"
confidence: "Medium"
next_action: "Skip — verify if WorkOS hires LATAM contractors before reconsidering; if confirmed LATAM-open, address TypeScript gap first (3-6 month roadmap)"
```

---

## A) Resumen del Rol

### Arquetipo: DevOps / SRE / Platform Engineer (primary)

| Campo | Valor |
|-------|-------|
| **Arquetipo** | DevOps / SRE / Platform Engineer |
| **Domain** | Developer Infrastructure / B2B SaaS (enterprise auth: SSO, SCIM, AuthKit, MFA) |
| **Function** | Site Reliability Engineering — IC contributor role |
| **Seniority** | Senior IC (no explicit level; scope implies 5+ years production systems experience) |
| **Remote** | Remote — United States & Canada only (hard geographic restriction) |
| **Team size** | Small SRE team within ~120-person company |
| **Comp (estimated)** | US market: $140K–$200K+/year total; no LATAM comp signal |
| **TL;DR** | IC SRE at a $2B developer tools company building auth infrastructure. Federico's technical profile (AWS, K8s, Prometheus/Grafana) maps extremely well to the technical requirements, but two hard blockers exist: geographic restriction (US/Canada only) and TypeScript coding requirement (not in CV). Without a LATAM-remote exception, this role is inaccessible regardless of technical fit. |

### About WorkOS

WorkOS provides enterprise-grade authentication primitives for developers: SSO, SCIM directory sync, MFA, and AuthKit. It is positioned as the "Stripe for enterprise auth." Funding: $198M+ raised, Series C at $100M closed at $2B valuation. ~120 employees as of April 2026. Backed by Sequoia, Battery Ventures. Building toward "agentic software security and reliability by default" per their Series C announcement. Active hiring — careers page live.

---

## B) Match con CV

### Requirement mapping

| JD Requirement | Type | Federico's CV match |
|----------------|------|---------------------|
| Operating and scaling production systems in AWS | **Must** | AWS Core Skills: EC2, RDS, S3, IAM, VPC, Route53, Lambda, API Gateway, CloudWatch, CloudTrail, CloudFront. "Managing production environments and application reliability" (Seeker Parking). "Oversaw AWS production environments" (Estudiantes de La Plata). Direct match. |
| Service reliability: monitoring, alerting, incident response, RCA | **Must** | Prometheus, Grafana, Zabbix in Observability skills. "Incident Management" in Management skills. "Managing monitoring, observability, and operational support" (Estudiantes de La Plata). Strong match. |
| Comfortable across infrastructure layers (compute, networking, storage, observability) | **Must** | Linux, Windows Server, Networking, Docker, Kubernetes, VMware, Proxmox. Full AWS stack covers storage (S3, RDS) and compute (EC2). Well covered. |
| Strong debugging and systems thinking | **Must** | CTO and Tech Lead roles imply cross-system ownership and incident triage. Not documented with specific debugging examples, but implied through production ops scope. Soft match. |
| Work independently, drive projects from discovery to resolution | **Must** | CTO at Estudiantes de La Plata, Tech Lead at Seeker Parking — clear pattern of autonomous ownership. Strong match. |
| Write and optimize backend systems in TypeScript | **Functionally required** | **NOT in CV.** No TypeScript, JavaScript, or Node.js experience documented. Hard gap. |
| Kubernetes or similar orchestration | Nice | Kubernetes explicitly in Core Skills. ✅ |
| Prometheus, Grafana, Datadog, OpenTelemetry | Nice | Prometheus + Grafana in Observability. Zabbix is adjacent. OpenTelemetry not mentioned but Prometheus covers the concept. ✅ (partial) |
| Define and measure SLIs/SLOs | Core responsibility | Not explicitly documented. Implied through production ops work, but absent from CV language. Soft gap. |
| Lead incident response and postmortems | Core responsibility | Incident management is in CV. No explicit postmortem leadership mentioned. Close but not documented. |

### Gaps and mitigation

| Gap | Blocker level | Mitigation |
|-----|--------------|------------|
| **Geographic restriction: US & Canada only** | **HARD BLOCKER** | Federico is Argentina-based. No visa or relocation path documented. Before any other action, verify if WorkOS makes exceptions for LATAM contractors. If no exception, role is inaccessible. |
| **TypeScript backend development** | **HARD BLOCKER** | The role explicitly requires writing and optimizing backend systems in TypeScript. Infra-layer tooling in shell/Python is adjacent but does not meet the bar. Cannot be bridged without actual TypeScript development experience. 3–6 month gap to develop credibly. |
| **English level for US team** | **Moderate blocker** | US company with SF, NY, and remote team. B1-B2 is functional for technical work and async communication, but on-call handoffs, postmortems, and architecture discussions in a US startup likely require higher fluency. Downgrade per profile policy. |
| **SLI/SLO formal definition** | Soft | Implicit in production ops work. Can be bridged with framing: "managed service uptime and reliability targets through dashboards and alerting thresholds." No action needed unless role is pursued. |
| **Production scale metrics** | Soft | CV lacks numbers (RPS, uptime %, services monitored). Add approximate figures during application if proceeding. |
| **Postmortem culture** | Soft | Not documented. If pursuing: reference any major incident response as an informal postmortem equivalent. |

---

## C) Nivel y Estrategia

### Level analysis

| Dimension | JD expectation | Federico's profile |
|-----------|----------------|--------------------|
| Level | Senior IC SRE | Senior IC with CTO-level leadership track — over-qualified for IC |
| Coding | TypeScript backend development | Ops/infra tooling; no app-layer TypeScript |
| Scope | Production reliability, SLIs, on-call | Production ops, incident management, cloud infra ownership |
| Leadership | IC contributor, no management signal | Has led 8+ person tech orgs as CTO |

Federico is an exceptionally strong fit from an infrastructure and operations perspective. The role's coding expectation (TypeScript) represents a genuine skill gap, not just a nice-to-have. As written, this is not a pure-infra SRE role — it's a hybrid SRE/backend-engineer role at a TypeScript-first company.

**Plan "vender senior sin mentir" (if blockers resolved):**

Lead with observability and production ownership, not management:

> "I've owned the full reliability lifecycle across production AWS environments: infrastructure provisioning with Terraform and Docker/K8s, observability stack with Prometheus and Grafana, incident response and operational support at scale. I work independently and drive reliability improvements from problem detection to resolution."

On TypeScript:
> "My primary tooling is infrastructure-layer — shell, Terraform, CI/CD pipelines. TypeScript backend development is not my current depth, and I want to be transparent about that. My systems-thinking and debugging strengths transfer, and I'd ramp on TypeScript, but I'm starting from a learning position rather than experience."

**Plan "si me downlevelan":** This is already an IC role. The real risk is being asked to contribute TypeScript code on Day 1, which Federico cannot do credibly. A downlevel isn't the concern — a scope mismatch is.

---

## D) Comp y Demanda

### Compensation data

| Source | Data | Notes |
|--------|------|-------|
| Levels.fyi (WorkOS SWE, US) | Median $137K/year total; max $377K | US market; equity included; not SRE-specific |
| Glassdoor (US SRE market) | P25: $132K / Median: $176K / P75: $244K | General US SRE market; WorkOS-specific data not available |
| WorkOS company profile | $2B valuation, $198M+ raised, 120 employees, Series C | Healthy, growth-stage company — above-median comp expected |

**Estimated WorkOS SRE total comp (US):** $140,000–$200,000/year (~$11,700–$16,700/month USD)

**Federico's target:** $4,000–$6,000/month USD

**Comp scenario analysis:**

| Scenario | Likelihood | Comp outcome |
|----------|------------|--------------|
| WorkOS hires LATAM contractors at US rates | Very unlikely | $11,700–$16,700/month — well above target |
| WorkOS hires LATAM contractors at LATAM market rates | Plausible (some US startups do this) | ~$3,000–$5,500/month — at or below Federico's target |
| WorkOS only hires US/Canada residents | Most likely (posting says US & Canada) | Inaccessible without relocation |

**Comp score: 2.5/5** — Theoretically attractive US compensation exists, but the geographic restriction makes it likely inaccessible. If WorkOS accepts LATAM contractors, LATAM-adjusted rates may fall at or below Federico's minimum.

### Demand signals

- WorkOS is in active growth post-Series C; no layoff or hiring freeze signals found
- SRE demand at developer infrastructure companies is stable and strong
- The specific posting was added 2026-06-10 — 2 days ago — fresh listing
- WorkOS has 3 open engineering-adjacent roles detected in the same scan (SRE, Infrastructure Engineer, Systems Engineer) — suggests genuine team build-out

---

## E) Plan de Personalización

If geographic and TypeScript blockers were resolved, these are the recommended changes:

### Top 5 CV changes

| # | Section | Current state | Proposed change | Why |
|---|---------|---------------|-----------------|-----|
| 1 | Professional Summary | Generic technology leader framing | Add SRE vocabulary: "production reliability, observability stack ownership, and incident response in cloud-native AWS environments" | Matches role vocabulary directly |
| 2 | Seeker Parking bullets | "Managing production environments and application reliability" | Expand: "maintained service uptime through Prometheus/Grafana monitoring, led incident response and RCA, managed Kubernetes-based workloads" | Evidence + SRE terminology |
| 3 | Observability section | Tool names only (Prometheus, Grafana, Zabbix) | Add context line: "Built monitoring dashboards for production AWS services; supported incident triage, alerting configuration, and reliability workflows" | Tools + outcomes, not just a list |
| 4 | Metrics / scale | No numbers anywhere | Add approximate figures: user scale at Estudiantes de La Plata, services monitored, uptime targets | Strengthens "scaling production systems" claim |
| 5 | TypeScript / Node.js | Not present | Add only if genuine exposure exists; do not fabricate | Fills the primary functional gap; only if honest |

### Top 5 LinkedIn changes

| # | Section | Proposed change |
|---|---------|-----------------|
| 1 | Headline | Include "SRE / Site Reliability / Production Operations" alongside current title |
| 2 | About section | Lead with reliability and observability angle, not management titles |
| 3 | Seeker Parking description | Add SRE framing: on-call, incident response, observability ownership |
| 4 | Skills endorsements | Prioritize: Prometheus, Grafana, Kubernetes, AWS, Incident Management, Terraform |
| 5 | Open to work | Explicitly add "Site Reliability Engineer" to visible target roles |

---

## F) Plan de Entrevistas

Applicable if geographic and TypeScript concerns are resolved:

| # | JD Requirement | Historia STAR | S | T | A | R |
|---|----------------|---------------|---|---|---|---|
| 1 | Operating and scaling production systems in AWS | Seeker Parking — production AWS management across multiple products | Led technology across multiple products and environments | Ensure stable and reliable production services | Managed EC2, RDS, S3, CloudWatch, IAM, VPC across environments; built alerting and monitoring pipelines | Stable production operations; proactive alerting reduced reactive incidents |
| 2 | Incident response and RCA | Estudiantes de La Plata — incident management for large user-facing platform | Managing AWS production serving tens of thousands of users | Critical service incident requiring fast detection and RCA | Led incident response cross-functionally, performed root cause analysis, coordinated restore procedures | Service restored; implemented observability improvements to prevent recurrence |
| 3 | SLI/SLO ownership | Estudiantes de La Plata — built observability for CTO-level tech org | No formal reliability monitoring existed when joining | Define service health baselines for 8+ person tech org | Deployed Prometheus + Grafana stack; defined key service metrics and alerting thresholds; established operational runbooks | Improved production visibility; enabled proactive capacity planning and reliability decisions |
| 4 | Kubernetes orchestration | Seeker Parking / platform evolution | Managing container infrastructure across multiple products | Need consistent, reliable workload orchestration | Adopted Kubernetes for containerized workloads; managed deployment lifecycle | More predictable, reliable deployments; reduced environment drift |
| 5 | Driving projects end-to-end independently | Mercedes-Benz — technology projects from discovery to delivery | Independent technical PM and delivery coordinator | Led migration and integration initiatives with minimal direct authority | Managed full project lifecycle: requirements → stakeholder coordination → vendor management → delivery | Projects delivered on scope; enterprise stakeholder confidence built |
| 6 | CI/CD and automation | GitHub Actions / GitLab CI/CD implementation | Improving delivery reliability at Seeker Parking | Unstructured deployment processes causing reliability risk | Implemented CI/CD pipelines with GitHub Actions and GitLab; standardized build and deploy workflows | Reduced deployment incidents; improved delivery velocity and traceability |

**Case study recommendation:** Seeker Parking — full reliability lifecycle. Frame as:
> "At Seeker Parking I own the complete reliability picture: Terraform for infra provisioning, Docker and Kubernetes for workload management, Prometheus and Grafana for observability, CI/CD for delivery, and incident response for production issues. I'll walk you through how I think about reliability at each layer."

**Red flag Q&A:**

| Question | How to respond |
|----------|----------------|
| "Are you based in the US?" | "I'm based in Argentina, working remote-first. Before proceeding, I'd want to confirm whether WorkOS is open to LATAM contractors or if the US-only requirement is a firm policy — I don't want to waste either of our time if it's a hard geographic constraint." |
| "Do you have TypeScript experience?" | "My primary stack is infrastructure and operations tooling — shell scripting, Terraform, CI/CD pipeline configuration. TypeScript application development is not my current depth, and I want to be transparent about that. I'd ramp quickly given strong systems fundamentals, but I'm starting from a learning position." |
| "What's your English level?" | "Intermediate-advanced for technical work. I communicate well in writing, documentation, code reviews, and technical meetings. On-call verbal handoffs and high-pressure postmortem discussions are where I'd be building more comfort." |

---

## G) Posting Legitimacy

**Assessment: High Confidence (posting is genuine and active)**

| Signal | Status | Detail |
|--------|--------|--------|
| Posting freshness | ✅ Fresh | Detected by scanner on 2026-06-10 via Ashby API — 2 days ago |
| Prior appearances in scan history | ✅ First appearance | Only one entry for this URL in scan-history.tsv; no reposting detected |
| JD specificity | ✅ High | SLIs/SLOs, TypeScript backend, observability stack terminology — specific, not boilerplate |
| Company hiring signals | ✅ Active growth | Series C $100M, $2B valuation, 120 employees, 3 concurrent engineering roles detected |
| Layoff / freeze news | ✅ None found | No negative signals in search results for WorkOS 2026 |
| Salary transparency | ⚠️ None | No compensation range disclosed in the posting |
| Geographic restriction | 🔴 US & Canada only | Confirmed in scan history location field; hard filter for LATAM-based candidates |
| Apply button state | ⚠️ Unverified (batch mode) | Playwright not available; cannot confirm button state directly |

**Context notes:**

This is a genuine, active posting at a well-funded company. The legitimacy concern here is not fraud, ghost posting, or expired role — it is the geographic restriction. WorkOS lists the role as "United States & Canada" and their team appears primarily US-based. Before permanently discarding, one concrete action: check workos.com/careers or reach out to a WorkOS recruiter on LinkedIn to ask directly whether they hire LATAM contractors for SRE roles. This takes 5 minutes and could change the picture entirely.

---

## Score Global

| Dimensión | Score |
|-----------|-------|
| Match con CV | 3.5/5 |
| Alineación North Star | 2.0/5 |
| Comp | 2.5/5 |
| Señales culturales | 3.5/5 |
| Red flags | -1.5 |
| **Global** | **2.5/5** |

**Recomendación: SKIP**

Three converging hard blockers — geographic restriction (US & Canada only), TypeScript coding requirement, and English fluency for a US-native team — make this role inaccessible at this time. The underlying technical fit is genuinely strong: AWS stack, Kubernetes, Prometheus/Grafana, and production operations ownership all map directly to what WorkOS is buying. If Federico addresses the TypeScript gap (3–6 months) and confirms WorkOS accepts LATAM contractors, this archetype of role becomes a strong target.

---

## Keywords extraídas

SRE, Site Reliability Engineer, TypeScript, SLI, SLO, AWS, Kubernetes, Prometheus, Grafana, OpenTelemetry, observability, incident response, on-call rotation, postmortem, production systems, reliability engineering, monitoring, alerting, root cause analysis, infrastructure layers, cloud operations, B2B SaaS, developer tools, service ownership, graceful degradation
