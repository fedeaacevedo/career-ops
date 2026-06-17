# Evaluation: Cabify — Senior Site Reliability Engineer

**Date:** 2026-06-10
**URL:** https://job-boards.greenhouse.io/cabify/jobs/8367951002
**Archetype:** DevOps/SRE/Platform
**Score:** 3.6/5
**Legitimacy:** High Confidence
**PDF:** not generated (batch mode)
**Verification:** unconfirmed (batch mode — WebFetch used)

---

## A) Role Summary
| Field | Value |
|-------|-------|
| Archetype | SRE / Platform Engineering |
| Domain | Ride-hailing / Mobility tech |
| Seniority | Senior (L4) |
| Remote | Hybrid — 3 days/week onsite in Madrid |
| Location | Madrid, Spain |
| TL;DR | Build and operate platform infrastructure for Cabify's mobility services, focusing on Kubernetes/AWS, observability, and SLO-based reliability. |

## B) Match with CV
| JD Requirement | Federico's Match | Gap? |
|---------------|-----------------|------|
| Kubernetes (AWS EKS) | Kubernetes in CV + AWS EKS implied via AWS stack | Minor — no explicit EKS projects cited |
| Terraform IaC | Terraform explicitly listed | No gap |
| GitLab CI/CD | GitLab CI/CD explicitly listed | No gap |
| Observability (Grafana, Cortex) | Prometheus + Grafana + Zabbix listed | Minor — Cortex not mentioned, but Grafana stack covered |
| Deep Unix/networking knowledge | Linux + networking in CV, Disney/Estudiantes ops experience | Moderate — OSI/CAP theorem depth not demonstrated in CV |
| Strong programming skills (at least one language) | Not evidenced in CV | Gap — scripting/coding skills not highlighted |
| Defining SLIs/SLOs/SLAs | Implied via reliability work at Estudiantes | Moderate — not explicitly framed as SLO ownership |
| On-call participation | Implied via incident management and operations | No gap |
| Fluent English for international team | B1-B2 (intermediate) | Gap — role mentions "fluent English"; B1-B2 is borderline |
| AWS (EKS, services) | AWS CCP + SAA + full service list | No gap |
| SQL/NoSQL DB operations | PostgreSQL, MySQL, MariaDB listed | No gap |

**Key gaps and mitigation:**
- **English fluency:** The JD asks for fluent English for an international team; B1-B2 is borderline. Federico should emphasize his technical English communication in interviews and on the CV (e.g., "comfortable conducting technical discussions in English").
- **Programming/scripting:** No scripting language is mentioned in the CV. Adding even basic Python/Bash automation examples (from any infra automation done at Seeker or Estudiantes) would address this gap directly.
- **SLO ownership framing:** Federico's observability work (Prometheus, Grafana) and incident management experience can be reframed explicitly around SLI/SLO definition — the experience is there, the vocabulary is missing.

## C) Level & Strategy
- **JD level:** Senior (L4)
- **Federico's fit:** Good fit — current Tech Lead/CTO-level experience at Estudiantes maps well to L4 SRE; not over-leveled, not under-leveled
- **Sell senior plan:**
  1. Lead with the Estudiantes La Plata scope — CTO managing tens of thousands of users on AWS production = credibility at scale for an L4 role
  2. Frame Seeker Parking DevOps/Tech Lead as hands-on platform ownership (CI/CD, infra, monitoring), not just management
  3. AWS SAA cert + Kubernetes + Terraform = the exact stack Cabify runs; lead with tools alignment in cover/CV summary
- **If downleveled:** L3/Mid is unlikely given Federico's tenure — if raised, position as "I'm targeting senior impact from day one, open to discussing scope during the process"

## D) Comp & Demand
| Source | Range | Notes |
|--------|-------|-------|
| Cabify JD (stated) | Up to €75,000/year | L4 level — stated explicitly in the posting |
| Madrid SRE market benchmark | €55,000–€80,000/year (Senior) | Based on general Spanish tech market data for senior infra/SRE roles |
| Federico's target | ~$4,000–$6,000 USD/month | ≈ €44,000–€66,000/year at 1.1 USD/EUR |

**Verdict:** The €75,000 ceiling is **at or slightly above** Federico's target range when converted ($5,500–$6,800/month depending on exchange rate). This is favorable. However, Madrid cost of living and Spain's tax burden should be factored in — net take-home on €75k in Spain is roughly €48,000–€52,000/year (~€4,000–4,300/month net). For a remote-from-Argentina arrangement this would be excellent; for relocation to Madrid it's competitive but not exceptional.

**Note:** The hybrid policy (3 days/week in Madrid) is a significant constraint for Federico based in Argentina. This would likely require relocation or the role to offer full remote as an exception. This is the primary score downgrade factor.

## E) Customization Plan
Top 3 CV changes for this role:
1. **Add a scripting/automation line** under DevOps skills — even "Bash/Python scripting for infrastructure automation" to close the programming gap that Cabify explicitly requires.
2. **Reframe Estudiantes La Plata experience** to include SLI/SLO language: e.g., "Defined and maintained SLOs for AWS production services serving 50,000+ users; led on-call incident response and post-mortems."
3. **Add AWS EKS explicitly** to the AWS skills section (it's implied but not stated); also add "Grafana + Cortex / Prometheus" as a named observability stack to mirror Cabify's tooling.

## F) Interview Plan
| JD Requirement | STAR Story | Key Point |
|---------------|-----------|-----------|
| Building self-service infra for dev teams | Estudiantes: deployed internal tooling/CI pipelines for dev teams | Reduced deployment friction; engineers shipped independently |
| SLI/SLO definition | Estudiantes: set up Grafana+Prometheus monitoring for production AWS | Map dashboards to uptime commitments; frame as implicit SLOs |
| On-call and incident response | Any production incident at Estudiantes or Seeker | Walk through timeline, root cause, resolution, prevention |
| Kubernetes cluster operations | Kubernetes work at Seeker/Estudiantes | Focus on operational challenges: scaling, networking, upgrades |
| Terraform IaC at scale | Infrastructure-as-code adoption at Estudiantes | Before/after: manual vs. Terraform; idempotency and drift |
| Influencing other teams on reliability | Estudiantes: cross-functional tech leadership as CTO | Led non-tech stakeholders; drove reliability culture in dev teams |

## G) Posting Legitimacy
| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Greenhouse job board — active and rendering full JD | High |
| Posting age | Not visible in fetched content | Medium |
| Description quality | Very specific: named tech (EKS, Cortex, Grafana), named practices (SLI/SLO/SLA), culture cues (KISS, async) — high-quality, authentic JD | High |
| Compensation stated | Explicit €75k cap listed — rare and a strong legitimacy signal | High |
| Company news | Cabify is an established Madrid-based ride-hailing company; active in Spain and LATAM | Medium |

**Assessment:** High Confidence — The posting is specific, compensation is stated, and it's on Cabify's own Greenhouse board. No red flags. The primary risk is the hybrid Madrid requirement, not legitimacy.

---

## Keywords Extracted
Kubernetes, EKS, Terraform, AWS, SRE, SLI, SLO, SLA, Grafana, Prometheus, GitLab CI/CD, observability, incident response, on-call, platform engineering, service mesh, networking, reliability, scalability, Unix

---

## Machine Summary
```yaml
num: 4
date: 2026-06-10
company: Cabify
role: Senior Site Reliability Engineer
score: 3.6
status: Evaluated
pdf: false
url: https://job-boards.greenhouse.io/cabify/jobs/8367951002
slug: cabify-senior-sre-madrid
```
