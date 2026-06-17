# Evaluation: Nubank — Lead Systems Engineer

**Date:** 2026-06-10
**URL:** https://job-boards.greenhouse.io/nubank/jobs/7248894
**Archetype:** DevOps/SRE/Platform
**Score:** 3.6/5
**Legitimacy:** Tier 1 — Direct ATS (Greenhouse)
**PDF:** not generated (batch mode)
**Verification:** unconfirmed (batch mode — WebFetch used)

---

## A) Role Summary

| Attribute | Detail |
|-----------|--------|
| Company | Nubank (Brazilian fintech, ~$17B valuation, publicly listed NYSE: NU) |
| Role | Lead Systems Engineer |
| Team | Computing Squad — foundational infrastructure |
| Location | Mexico City, Mexico (Hybrid 2-3 days/week in office) |
| Work Model | Hybrid — on-site required in CDMX |
| Focus | Kubernetes, AWS EKS, networking, service communications |
| Reporting | Not specified |
| Seniority | Lead (technical lead + mentoring responsibility) |
| Language | Advanced English required for daily documentation and communication |

**What this team does:** The Computing Squad owns foundational infrastructure — the Kubernetes platform, AWS networking, service mesh, and cloud compute that all other Nubank engineering teams depend on. A Lead Systems Engineer here is the go-to person for production reliability at platform level, drives technical direction, mentors others, and represents the team across the org.

---

## B) Match with CV

| Requirement | Federico Has | Fit |
|-------------|-------------|-----|
| AWS (EKS, VPC, EC2, IAM) | AWS CCP + SAA, production AWS at Estudiantes La Plata and Seeker | Strong |
| Kubernetes — production cluster lifecycle | Docker + Kubernetes in DevOps stack; production exposure at current role | Moderate |
| Autoscaling tools (Karpenter, KEDA, HPA) | General Kubernetes knowledge; specific tools not confirmed | Gap |
| Golang programming | Not listed in CV or skills | Hard gap |
| Technical lead role (2+ years minimum) | CTO at Estudiantes La Plata (2025-2026), Tech Lead at Seeker (2026-present) | Strong |
| Mentoring junior engineers | Tech manager experience, team leadership listed | Strong |
| Advanced English (daily documentation + comms) | B1-B2, comfortable in technical environments | Partial risk |
| Infrastructure performance/cost/governance | Cloud operations background across roles | Moderate |
| Stakeholder communication across org levels | Mercedes-Benz PM role, vendor coordination, cross-functional leadership | Strong |

**Key gaps:**

- **Golang is a hard requirement.** The JD explicitly states "Golang programming experience." Federico's CV has no Go experience whatsoever. This is likely a dealbreaker for a Lead-level role where code contribution is expected.
- **Advanced autoscaling tools gap (Karpenter, KEDA).** These are production-grade Kubernetes scaling tools. General Kubernetes experience is relevant but these specific tools are not demonstrated.
- **English level risk.** The role requires "Advanced English proficiency for daily documentation and communication." B1-B2 is intermediate, and the JD's wording suggests this is a genuine daily working requirement, not just a nice-to-have.

---

## C) Level & Strategy

**Level fit assessment:**

The title "Lead Systems Engineer" at Nubank signals a senior-plus individual contributor with formal technical lead responsibilities — roughly equivalent to Staff/Senior Lead in other companies. Federico has genuine lead credentials: CTO at Estudiantes La Plata and current Tech Lead at Seeker. The lead dimension is not a concern.

The technical depth concern is the Golang requirement. At Nubank's engineering maturity (Go-heavy backend, open-source contributors), a Lead in the Computing Squad will be expected to write and review Go code for infrastructure tooling, controllers, and automation. This is not a stretch item — it is core to the role.

**Recommended framing if applying:**

- Lead with the CTO and Tech Lead narrative: two consecutive technical leadership roles in production AWS environments.
- Emphasize Kubernetes in production: EKS experience (from AWS SAA and production exposure), cluster operations, and observability stack (Prometheus + Grafana).
- Acknowledge Golang gap honestly if screened. Frame it as "active learning area" only if Federico genuinely has any exposure (even tutorials). Do not fabricate.
- Position the LATAM angle as a cultural and business fit: Federico targets LATAM opportunities, Nubank is a LATAM-native company expanding in Mexico.

**Risk:** Without Go, the screening filter at a technical lead level is likely to reject early. This should be treated as a stretch application unless Federico has undisclosed Go exposure.

---

## D) Comp & Demand

| Metric | Detail |
|--------|--------|
| Federico's target range | $4,000–$6,000 USD/month |
| Nubank Mexico City (Lead level) | Estimated $5,000–$8,000 USD/month (competitive LATAM fintech, equity included) |
| Role includes equity | Yes — RSUs, 3-year vest (33.3% annually) |
| Benefits package quality | High: health/dental/vision, 17 vacation days + 25% bonus, food allowance, gym, WFH stipend, mental health program, language learning program |
| Location premium | Mexico City pricing — likely higher than Argentina remote but requires relocation/presence |
| Comp verdict | Likely within or above Federico's range at base; equity adds long-term upside |

**Demand signal:** Nubank's Computing Squad hires are competitive globally. They have a strong engineering brand in LATAM. The role is open (active ATS posting on Greenhouse). Mexico City office expansion is ongoing. Market demand for platform/infra leads with Kubernetes and AWS EKS is consistently strong in LATAM fintech.

**Comp verdict:** Compensation is likely favorable, but the hybrid requirement in Mexico City introduces a practical constraint — Federico is based in Argentina and the role requires 2-3 days/week in CDMX. This is not remote. Relocation assistance is mentioned but is a significant life decision.

---

## E) Customization Plan

**Top 3 CV changes if applying:**

1. **Elevate Kubernetes and EKS explicitly.** Current CV lists Kubernetes generically. Rewrite the Seeker and Estudiantes bullets to call out EKS specifically, cluster management, and any autoscaling or cost optimization work done in production.

2. **Add a computing/platform infrastructure bullet.** The Computing Squad role is about owning foundational infra that other teams depend on. Add a bullet at Estudiantes or Seeker framing Federico's work as "platform-level infrastructure" — not just individual apps but shared services, networking, and compute layers.

3. **Address English and Go gaps in cover letter (not CV).** In a cover note, briefly acknowledge that Golang is a learning priority (if true), and that English proficiency has been exercised in international technical coordination. Do not adjust the CV for what isn't there.

---

## F) Interview Plan

**STAR stories to prepare:**

1. **Kubernetes production incident (AWS EKS):** Situation — cluster degradation or node failure. Task — restore service. Action — diagnosis, node replacement or pod rescheduling. Result — RTO achieved, post-mortem completed. (Anchor to Estudiantes or Seeker.)

2. **Infrastructure cost optimization:** Situation — cloud cost spike or waste identified. Task — reduce spend without impacting reliability. Action — rightsizing, reserved instances, or architecture change. Result — measurable cost reduction. (Estudiantes La Plata AWS production.)

3. **Leading a cross-functional technical initiative:** Situation — complex infrastructure project touching multiple teams. Task — technical lead and delivery. Action — planning, coordination, technical decisions, stakeholder comms. Result — successful delivery. (Mercedes-Benz migration project or Estudiantes transformation.)

4. **Mentoring a junior engineer through a production problem:** Situation — junior team member facing escalating issue. Task — guide without taking over. Action — coaching through diagnosis steps, structured pair debugging. Result — junior resolved it, gained confidence. (Seeker or Estudiantes teams.)

5. **Autoscaling or capacity planning decision:** Situation — growth event approaching (product launch, user spike). Task — ensure the platform could handle load. Action — implemented HPA or load testing, tuned thresholds. Result — zero downtime during event. (Production context at either current role.)

6. **Communicating technical risk to non-technical stakeholders:** Situation — infrastructure debt or critical dependency at risk. Task — get buy-in for remediation from leadership. Action — translated technical severity into business impact, proposed roadmap. Result — prioritized and funded. (CTO experience at Estudiantes or PM role at Mercedes-Benz.)

---

## G) Posting Legitimacy

| Signal | Assessment |
|--------|------------|
| ATS platform | Greenhouse — enterprise-grade, direct company posting |
| Company | Nubank — publicly listed (NYSE: NU), established LATAM fintech |
| Posting specificity | High — detailed tech stack, named tools (Karpenter, KEDA, HPA, EKS), team context |
| Salary disclosed | No — typical for LATAM/Mexico tech postings |
| Benefits disclosed | Yes — detailed, company-standard package |
| Red flags | None |
| Legitimacy verdict | **Tier 1 — Legitimate direct posting from a public company via verified ATS** |

---

## Keywords Extracted

1. Kubernetes
2. AWS EKS
3. VPC
4. IAM
5. EC2
6. Golang
7. Karpenter
8. KEDA
9. HPA (Horizontal Pod Autoscaler)
10. Technical Lead
11. Platform Infrastructure
12. Autoscaling
13. Service Communications
14. Production Cluster Lifecycle
15. Computing Squad

---

## Machine Summary

```yaml
num: 9
date: 2026-06-10
company: Nubank
role: Lead Systems Engineer
score: 3.6
status: Evaluated
pdf: false
url: https://job-boards.greenhouse.io/nubank/jobs/7248894
slug: nubank-lead-systems-engineer-mexico
```
