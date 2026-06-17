# Evaluación: Canonical — Cloud Solutions Architect - Alliances

**Fecha:** 2026-06-12
**Arquetipo:** Cloud Architect / Solutions Architect (secondary)
**Score:** 2.4/5
**Legitimacy:** High Confidence
**URL:** https://job-boards.greenhouse.io/canonical/jobs/5915936
**PDF:** not generated — run /career-ops pdf canonical-cloud-sa-alliances to create on demand
**Batch ID:** 4

---

## Machine Summary

```yaml
company: "Canonical"
role: "Cloud Solutions Architect - Alliances"
score: 2.4
legitimacy_tier: "High Confidence"
archetype: "Cloud Architect / Solutions Architect"
final_decision: "Skip"
hard_stops:
  - "Fluent written and spoken English explicitly required — Federico is B1-B2"
  - "Ceph not in CV; listed as core requirement with 'extensive experience'"
  - "OpenStack not in CV; core to the Canonical solutions portfolio"
  - "Kubeflow / MLOps stack not in CV"
  - "30% global travel from Argentina is a material lifestyle constraint"
soft_gaps:
  - "Python not explicitly listed in CV"
  - "No partner/alliance SA experience"
  - "Canonical-specific stack (Juju, LXD, Snaps) absent"
  - "Degree requirement (CS/Math/Physics) not mentioned in CV"
top_strengths:
  - "Linux and Kubernetes are genuine matches to core requirements"
  - "Cloud infrastructure design experience (AWS) translates partially"
  - "Remote-first company with worldwide home-based policy"
risk_level: "High"
confidence: "High"
next_action: "Skip — second Canonical SKIP in this batch; English fluency + Canonical stack are hard blockers"
```

---

## A) Resumen del Rol

| Campo | Detalle |
|-------|---------|
| **Arquetipo detectado** | Cloud Architect / Solutions Architect (secondary archetype for Federico) |
| **Domain** | Open source infrastructure, cloud platforms, partner/alliances engineering |
| **Function** | Solutions Architecture, Field Engineering, Alliance Technical Enablement |
| **Seniority** | Senior IC (no direct reports mentioned; partner-facing technical ownership) |
| **Remote** | Home-based, worldwide — strong remote signal |
| **Team size** | Worldwide Alliances / Field Engineering team; partners include Intel, Nvidia, Google, Dell, HP, Accenture, Tata |
| **TL;DR** | Technical SA role embedded in Canonical's Alliances team. The job is to help major technology partners understand, adopt, and architect solutions around Ubuntu, OpenStack, Kubernetes, Ceph, Kubeflow, and the broader Canonical open-source portfolio. Requires deep Canonical-stack expertise, fluent English for partner workshops and presentations, and 30% global travel. |

**What they're buying:** A field engineer who already knows the Canonical stack (Ubuntu, OpenStack, Ceph, Kubernetes, Kubeflow) and can translate it into joint reference architectures and onboarding programs for strategic partners. English fluency is not a soft preference — it's operationally required for every partner interaction.

---

## B) Match con CV

### Requirements → CV Mapping

| Requisito JD | Estado | CV Match | Notas |
|---|---|---|---|
| Extensive experience with Linux (Ubuntu preferred) | ✅ Match | `cv.md: "Linux" in Core Skills → Infrastructure` | Strong general Linux background; Ubuntu-specific depth unverified |
| Kubernetes | ✅ Match | `cv.md: "Kubernetes" in DevOps skills` | Present but depth is operational (Seeker Parking), not deep SA/design |
| Experience designing solutions on public or private clouds | ✅ Partial | `cv.md: AWS environments across all roles` | AWS-centric; no OpenStack or private cloud design experience |
| Python and bash understanding | ⚠️ Partial | `cv.md: no explicit Python; GitHub Actions / CI/CD scripts imply bash` | Python absent from CV; bash implied |
| Fluent written and spoken English | ❌ Hard gap | `config/profile.yml: english_level: "Intermediate (B1-B2)"` | JD explicitly requires fluency; profile policy: downgrade when fluency is daily operational requirement |
| Excellent communication and presentation abilities | ⚠️ Partial | Leadership history supports this; presentations not documented | No partner workshop or public presentation references |
| Ability to travel globally up to 30% | ❌ Risk | Argentina-based; no travel history mentioned in CV | 30% = ~70 days/year globally; significant from LATAM |
| Degree in CS, Mathematics, Physics, or related field | ❌ Gap | Not mentioned in CV | No university degree referenced |
| Ceph (block storage / distributed systems) | ❌ Hard gap | Not in CV | Core to Canonical storage and private cloud offerings |
| OpenStack | ❌ Hard gap | Not in CV | Core to Canonical private cloud portfolio |
| Kubeflow / AI/MLOps stack | ❌ Hard gap | Not in CV | Canonical positions this as a key growth area |
| Software automation | ✅ Partial | `cv.md: Terraform, GitHub Actions, GitLab CI/CD` | Good automation toolchain, but not infrastructure-as-code for Canonical stack |
| Integrate PostgreSQL, MongoDB, Kafka, Cassandra, NGINX | ⚠️ Partial | `cv.md: PostgreSQL, MySQL, MariaDB in Databases` | Relational DB familiarity; no Kafka, Cassandra, MongoDB |
| Partner-facing engagement (Alliances context) | ❌ Gap | No alliance or partner SA experience in CV | No vendor-partner technical work documented |

**Nice-to-have missing:** LXD, Juju, Snaps — none in CV. These signal Canonical ecosystem depth that Federico doesn't have.

### Gaps Analysis

| Gap | Type | Blocker? | Mitigation |
|-----|------|----------|------------|
| Fluent English | Profile rule | **Hard blocker** | None — B1-B2 is insufficient for daily partner workshops; profile policy triggers SKIP |
| Ceph | Technical | **Hard blocker** | No adjacent experience to bridge; not learnable in application window |
| OpenStack | Technical | **Hard blocker** | No private cloud / OpenStack exposure in any role |
| Kubeflow / MLOps | Technical | Hard | No ML infrastructure background; Federico's stack is AWS/infra, not ML platform |
| 30% global travel | Lifestyle | Hard for Argentina | Could be negotiated to regional travel, but JD states "globally" explicitly |
| Python | Technical | Soft | Can be addressed in cover letter referencing scripting/automation context |
| Alliance/partner SA | Experience | Soft | Leadership experience with vendors/stakeholders is adjacent, not identical |
| Degree requirement | Credential | Soft | Canonical rarely hard-blocks on this in practice, but it's listed |
| Reference architectures | Deliverable | Soft | No published architecture documentation in portfolio |

---

## C) Nivel y Estrategia

**Nivel detectado en JD:** Senior IC — the role owns technical relationships with named strategic partners. It's not a manager role; it's an individual contributor SA with significant scope. Canonical typically doesn't distinguish between L4/L5/L6 publicly.

**Federico's natural level:** Senior individual contributor with leadership history. This is his secondary archetype (SA), not primary.

**Plan "vender senior sin mentir":**
If pursuing despite hard stops:
- Lead with Kubernetes + Linux operational depth rather than Canonical-specific stack
- Frame AWS cloud architecture work as "public cloud SA" to establish design credibility
- Emphasize technical leadership at Estudiantes de La Plata as evidence of partner/stakeholder-facing technical ownership
- Do not attempt to position Ceph or OpenStack — recruiters at Canonical know these tools deeply

**Plan "si me downlevelan":** Not applicable — the primary barrier is technical and language, not level.

**Honest assessment:** Even with a strong presentation, the technical gap on Ceph + OpenStack + Kubeflow alongside the English requirement makes this an unlikely outcome. Canonical's Alliances team interviews are technical-deep on the Ubuntu stack.

---

## D) Comp y Demanda

### Market Data

| Fuente | Datos | Notas |
|--------|-------|-------|
| Glassdoor (Canonical Cloud SA) | ~$231K/yr avg — but US-centric data | Likely inflated by US-based respondents |
| Levels.fyi (Canonical SA) | €81.7K–€114K+ | European data; not LATAM-adjusted |
| Glassdoor (Canonical overall 2026) | $102K median total comp | Global average; likely not representative for remote LATAM |
| Canonical historical (LATAM remote reports) | $50K–$80K/yr estimate for LATAM remote | No salary stated in JD; Canonical is known for below-market base but solid benefits |
| Federico's target | $48K–$72K/yr ($4K–6K/month) | Canonical LATAM range likely intersects lower half |

**Score de comp: 3.0/5** — Canonical pays decent for remote but is known to be below market vs US peers. No salary stated in JD. Based on LATAM remote reports, the role likely lands in Federico's target range but not the top of it. The $2K/year learning budget and performance bonus improve total value.

**Demand context:** Solutions Architect roles at open-source infrastructure companies are in steady demand. Canonical hires continuously for this team globally. Competition is high from candidates with Ubuntu/OpenStack/Ceph depth.

**Canonical hiring posture:** Company appears to be actively hiring (multiple roles in scan history from 2026-06-10). Profitable, founder-led, growing. Low layoff risk based on available signals.

---

## E) Plan de Personalización

*Provided for reference — not recommended for application given hard stops.*

| # | Sección | Estado actual | Cambio propuesto | Por qué |
|---|---------|---------------|------------------|---------|
| 1 | Professional Summary | Generic tech leader framing | Add "cloud infrastructure architect" framing, mention Linux/K8s/cloud-native explicitly | SA roles look for design-first framing |
| 2 | Kubernetes bullet (Seeker Parking) | Operational management | Add architecture/design signal: "designed Kubernetes workload topology for X" | JD requires SA-level K8s, not just ops |
| 3 | Skills section | No Python listed | Add Python under DevOps/scripting if candidate has any Python scripting exposure | Explicit requirement in JD |
| 4 | AWS bullets | Infrastructure ops framing | Reframe as "architecture decisions" where applicable | Positions Federico as SA, not just operator |
| 5 | Languages | English: B1-B2 | No change — do not misrepresent | Honesty is non-negotiable |

**LinkedIn:** Not recommended for this application. If pursuing, add "Solutions Architecture" and "Open Source Infrastructure" to skills.

---

## F) Plan de Entrevistas

*Provided for reference — not recommended given hard stops. Canonical SA interviews are multi-round and heavily technical on the Ubuntu/Canonical stack.*

| # | Requisito del JD | Historia STAR | S | T | A | R |
|---|---|---|---|---|---|---|
| 1 | Cloud infrastructure architecture | Kubernetes platform design at Seeker Parking | Leading infra across multiple products | Architect reliable, observable K8s workloads | Designed workload topology, CI/CD pipelines, monitoring | Stable production environments |
| 2 | Linux systems administration | Server management at Walt Disney / Estudiantes | Multi-org Linux environments | Keep production Linux infra stable across diverse teams | Managed Linux servers, AD, virtualization, monitoring | Operational continuity for thousands of users |
| 3 | Integration of open source software | AWS + observability stack at Estudiantes | Cloud infra for digital transformation | Integrate monitoring (Prometheus, Grafana, Zabbix) with AWS production | Deployed multi-tool observability stack | Improved incident visibility and response time |
| 4 | Partner/stakeholder-facing engagement | Vendor coordination at Mercedes-Benz | Complex multi-vendor technology program | Coordinate SAP-adjacent migration with external consultants | Managed requirements, communication, execution across firms | Delivered integration programs on schedule |
| 5 | Solutions design and documentation | Cloud modernization at Estudiantes | CTO of org serving tens of thousands of users | Modernize infrastructure and document cloud strategy | Implemented cloud services, defined operational processes | Improved reliability and scalability of user-facing operations |

**Case study recomendado:** The Kubernetes platform at Seeker Parking — most relevant SA signal Federico has. Frame it as "architected the workload orchestration layer" rather than "managed Kubernetes."

**Preguntas red-flag:**
- *"What's your experience with Ceph?"* → Honest answer: "I don't have production Ceph experience. I'm familiar with distributed storage concepts from Kubernetes persistent volumes and AWS EBS/EFS. I'd need to ramp on Ceph specifically."
- *"How comfortable are you running partner workshops in English?"* → Honest answer: "My English is intermediate/B1-B2. I'm comfortable in technical discussions and async collaboration, but highly fluent partner workshop facilitation would be a growth area for me."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Resultado | Fuente |
|--------|-----------|--------|
| JD quality | High — specific tech requirements (Ceph, OpenStack, Kubeflow), realistic seniority, named partner ecosystem | JD text |
| ATS platform | Greenhouse — Canonical's standard; active and well-maintained | URL structure |
| First seen | 2026-06-10 (2 days ago) | data/scan-history.tsv |
| Prior appearances | First appearance in scan history | data/scan-history.tsv |
| Company hiring signals | Canonical appears actively hiring — 8+ roles found in scan-history.tsv on 2026-06-10 | scan-history.tsv |
| Salary transparency | Not provided — consistent with Canonical's standard practice | JD |
| Boilerplate ratio | Low — JD is specific to the Alliances team context and Canonical tech stack | JD text |
| Posting freshness | Unverified (batch mode) — Playwright not available | Batch mode limitation |
| Layoff/freeze signals | None found — Canonical is profitable, growing, founder-led | WebSearch |

**Context notes:** This is the third Canonical role encountered in this batch. All three were posted on 2026-06-10 via Greenhouse. Canonical runs a persistent open hiring pipeline for its field engineering teams globally. High confidence this is a real, actively-staffed opening.

---

## Score Global

| Dimensión | Score |
|-----------|-------|
| Match con CV | 2.0/5 |
| Alineación North Star | 2.5/5 |
| Comp | 3.0/5 |
| Señales culturales | 3.0/5 |
| Red flags | -0.5 |
| **Global** | **2.4/5** |

**Recomendación: SKIP**

Three compounding hard stops: (1) "Fluent written and spoken English" is operationally central to every partner interaction in this role — not negotiable at B1-B2; (2) Ceph and OpenStack are explicitly core and absent from the CV; (3) Kubeflow/MLOps stack is a third hard technical gap. The Kubernetes and Linux match is real but insufficient to bridge these. This is the second Canonical SKIP in today's batch (after #019 Observability EM). Canonical roles systematically require fluent English for their distributed global teams.

---

## Keywords extraídas

Ubuntu, Linux, Kubernetes, Ceph, OpenStack, Kubeflow, Spark, Python, Bash, Cloud Solutions Architecture, Reference Architectures, Alliance Engineering, Field Engineering, Partner Onboarding, MLOps, AI/ML Infrastructure, Open Source, PostgreSQL, Kafka, NGINX, LXD, Juju, Snaps, Public Cloud, Private Cloud, Partner Enablement
