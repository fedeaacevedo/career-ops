# Evaluación: Resend — Security Engineer, Platform

**Fecha:** 2026-06-12
**Arquetipo:** DevOps / SRE / Platform Engineer (superficial match — security specialization is primary, outside all target tracks)
**Score:** 2.0/5
**Legitimacy:** High Confidence
**URL:** https://jobs.ashbyhq.com/resend/cde17f7c-4c70-435f-be38-ef5abe94ff22
**PDF:** not generated — run /career-ops pdf resend to create on demand
**Batch ID:** 6

---

## Machine Summary

```yaml
company: "Resend"
role: "Security Engineer, Platform"
score: 2.0
legitimacy_tier: "High Confidence"
archetype: "DevOps / SRE / Platform Engineer (partial) — AppSec / Platform Security (primary, not in target tracks)"
final_decision: "Skip"
hard_stops:
  - "No hands-on security engineering experience (AppSec, secrets management, tenant isolation, access control design)"
  - "Role is a specialized security IC position — outside all three target tracks (A, B, C)"
  - "No detection/response or SIEM/SOAR background"
soft_gaps:
  - "No developer tools / SaaS startup experience"
  - "Comp not disclosed — startup with no salary data"
  - "No English-first remote company experience (writing-driven culture)"
top_strengths:
  - "AWS IAM and cloud access management experience (partial relevance)"
  - "Remote Americas timezone match"
  - "Some cybersecurity team oversight at Estudiantes de La Plata"
risk_level: "High"
confidence: "Medium"
next_action: "Skip — role requires deep security engineering specialization not present in CV. Monitor Resend for future DevOps/SRE/Platform roles on the Platform Squad."
```

---

## A) Resumen del Rol

| Campo | Detalle |
|-------|---------|
| **Arquetipo detectado** | AppSec / Platform Security Engineer (IC, specialized) — closest Federico archetype: DevOps/SRE/Platform (superficial) |
| **Domain** | Developer Tools / Email API Infrastructure |
| **Function** | Security Engineering — Platform Squad |
| **Seniority** | IC, likely Senior (not specified explicitly) |
| **Remote** | Yes — Americas timezone ✅ |
| **Company size** | ~74 people (Series A, $21M raised, Dec 2024) |
| **TL;DR** | Resend is building security foundations for its developer email API platform. This role sits on the Platform Squad and owns API key security, secrets management, tenant isolation, audit logs, and detection/response for suspicious activity. It's a specialized IC security engineering role, not infrastructure operations or DevOps. |

**Context:** Resend is a fast-growing developer tools startup (email API, 2M+ developers, $21M Series A). Engineering culture: small senior teams, extreme ownership, writing-driven, zero tolerance for quality debt. The Platform Squad owns internal platform reliability and security foundations. This is a hands-on individual contributor role requiring deep, specialized security engineering knowledge — not management of a security team.

---

## B) Match con CV

### JD Requirements → CV Mapping

| Requisito JD | Match | Evidencia en CV / Notas |
|--------------|-------|------------------------|
| API keys, service permissions, secrets management | ❌ Gap | No hands-on secrets management tooling (Vault, AWS Secrets Manager at engineering depth). IAM listed but as admin config, not security engineering. |
| Tenant isolation design | ❌ Hard blocker | Not mentioned anywhere in cv.md. Requires multi-tenant SaaS architecture security experience. |
| Audit logs architecture | ❌ Hard blocker | No audit log engineering. CloudTrail listed as AWS skill (monitoring), not security audit design. |
| Internal access controls design | ⚠️ Weak partial | AWS IAM in cv.md skills. Management-level cybersecurity oversight at Estudiantes de La Plata. Not the same as designing access control systems. |
| Detection & response for suspicious access / leaked credentials | ❌ Hard blocker | No SIEM, SOAR, threat detection, or incident response tooling experience in CV. |
| Abnormal sending behavior detection | ❌ N/A | Domain-specific to email infrastructure security. No background. |
| Secure defaults for services, workers, queues, databases, pipelines | ⚠️ Weak partial | DevOps and CI/CD experience (GitHub Actions, GitLab) gives partial exposure to pipeline security, but not security-by-design at engineering level. |
| Security review of deployment pipelines | ⚠️ Partial | CI/CD experience (GitHub Actions, GitLab, Docker, Kubernetes). Could contribute at basic level but not as primary security engineer. |
| Small senior team, extreme ownership | ✅ Fit | Current role at Seeker Parking and CTO at Estudiantes show ownership across multiple functions. |
| Remote Americas timezone | ✅ Fit | Argentina (UTC-3). Americas timezone match. |
| Writing-driven culture | ⚠️ Unknown | Not evidenced in CV. English B1-B2 may be a challenge for a writing-first culture. |

### Gap Analysis

| Gap | Severity | Mitigation? |
|-----|----------|-------------|
| No hands-on security engineering background | **Hard blocker** | Management of cybersecurity teams ≠ security engineering. No mitigation path for this role. |
| No tenant isolation / multi-tenant security design | **Hard blocker** | Requires SaaS security architecture experience that doesn't exist in CV. |
| No detection & response / SIEM tooling | **Hard blocker** | This is a core part of the role, not a nice-to-have. |
| No secrets management engineering (Vault, etc.) | **Hard blocker** | AWS IAM is tangentially relevant but not sufficient. |
| English B1-B2 at writing-driven company | **Soft blocker** | Resend's culture is writing-first, async English. B1-B2 is manageable for technical work but creates friction. |
| No developer tools / SaaS startup experience | Medium | Not a hard blocker but adds to overall mismatch. |

**Summary:** 4 hard blockers. The fundamental problem is that Federico is a cloud infrastructure and technology leadership professional — not a security engineer. Managing a cybersecurity team is categorically different from building security systems. This role requires deep, hands-on specialization in application and platform security that is not present in the CV.

---

## C) Nivel y Estrategia

**Nivel detectado en JD:** IC Senior Security Engineer (individual contributor, specialized)

**Nivel natural de Federico:** Technical Leader / IT Manager / DevOps Lead — generalist with cloud operations depth, management experience, but not a deep-specialization IC.

**Mismatch:** Federico has grown into management and leadership. This role goes the other direction: it's a highly specialized IC role requiring deep security engineering knowledge. The level mismatch is compounded by a domain mismatch.

**"Vender senior sin mentir" — No viable path:**
The gap here is domain (security engineering specialization), not seniority. There is no honest framing that turns cloud infrastructure management into security engineering credibility for a role like this. The cybersecurity oversight at Estudiantes de La Plata could be mentioned but would not be competitive against candidates with 5+ years of hands-on AppSec or platform security engineering.

**"Si me downlevelan" — Not applicable:**
This is not a leveling question. The issue is that the required domain expertise (security engineering) is absent regardless of level.

**Recommendation:** Do not apply. This role is outside all three target tracks and would require a 2-3 year career pivot into security specialization to be genuinely competitive.

---

## D) Comp y Demanda

### Salary Data

| Fuente | Dato | Confianza |
|--------|------|-----------|
| Levels.fyi (Resend) | $99,500 median total comp — only 1 role reported (Customer Service). No engineering data. | Low |
| Built-In (Remote Security Engineer, 2026) | Average $178,307 base + $27,508 bonus = ~$205,815 total | Medium (market benchmark) |
| Glassdoor (Platform Security Engineer) | $147K-$236K (25th-75th percentile) in the US | Medium |
| ZipRecruiter (Remote Security Engineer) | $143K-$342K range | Medium |
| Resend careers page | No salary posted | — |

**Comp score: 2.5/5**

Resend does not disclose salary ranges. As a ~74-person Series A startup (raised $21M in Dec 2024), compensation is likely below large-company security engineer rates but potentially competitive for its stage. For remote candidates from Argentina, the key unknown is whether they pay US-rate or apply geographic adjustment. Without data, this is speculative.

Even if comp is strong, the domain mismatch makes this moot. Score capped at 2.5 due to undisclosed comp and no public data for engineering roles at Resend.

### Market Demand Assessment

Security engineering roles are in high demand in 2026, particularly for developer tools companies handling sensitive data (emails, API keys). Resend is a legitimate and growing company. However, this demand is for *specialized security engineers*, not cloud/infrastructure generalists.

---

## E) Plan de Personalización

**Score is below threshold for application. Personalization plan provided for reference only — not recommended to apply.**

| # | Sección | Estado actual | Cambio propuesto | Por qué |
|---|---------|---------------|------------------|---------|
| 1 | Professional Summary | Cloud infrastructure / IT leadership focus | Add explicit security awareness framing: "AWS IAM governance, CI/CD pipeline security controls, multi-cloud access management" | Closest honest bridge to JD |
| 2 | Estudiantes de La Plata bullet | "Led technology, infrastructure, software development, cybersecurity, and support teams" | Expand to: "Directed cybersecurity function including access control policies, incident response coordination, and audit compliance" | Only honest security-related proof point |
| 3 | Skills | AWS IAM, CloudTrail, CloudWatch listed | Group under "Security-Adjacent" heading: IAM, CloudTrail, GuardDuty (if applicable), VPC security groups | Signals security awareness even if not deep |
| 4 | Projects section | None | Add any security-related project or process improvement (e.g., implemented MFA org-wide, configured AWS SCPs) | Even small proof points matter for weak match |
| 5 | LinkedIn | Standard cloud/infra headline | Not recommended to change for this role — risk of misrepresenting specialization | N/A |

**Bottom line:** Even a fully optimized CV cannot honestly bridge the gap here. This would require fabricating security engineering depth that doesn't exist.

---

## F) Plan de Entrevistas

**Not recommended to reach interview stage. Stories provided if candidate decides to explore anyway.**

| # | Requisito del JD | Historia STAR | S | T | A | R |
|---|-----------------|---------------|---|---|---|---|
| 1 | Access controls design | Cybersecurity function at Estudiantes de La Plata | Large org with multiple access layers | Ensure secure access across infrastructure, applications, and user systems | Implemented IAM policies, AD governance, access control reviews | Reduced unauthorized access incidents, documented access control policies |
| 2 | Audit and compliance | IT governance at Estudiantes or Mercedes-Benz | Complex enterprise environment | Required auditability for technology access and operations | Implemented monitoring and logging (CloudWatch, CloudTrail, Zabbix) | Traceability for audit purposes |
| 3 | Detection for abnormal behavior | Observability and monitoring background | Production environment monitoring | Early detection of incidents | Prometheus/Grafana/Zabbix alerting pipeline | Reduced MTTR on production incidents |
| 4 | Secrets management | AWS environment management | Cloud production management | Secure credentials and keys for services | AWS Secrets Manager and IAM roles for service authentication | Reduced credential exposure in pipeline configurations |

**Case study recommendation:** Estudiantes de La Plata cybersecurity oversight — frame as "building security foundations from scratch for a large production environment." Emphasize scope (tens of thousands of users), not depth of security engineering.

**Red flag questions:**
- *"Tell me about your experience with secrets management tooling like HashiCorp Vault"* → Honest answer: limited to AWS Secrets Manager. This will likely end the interview.
- *"Walk me through how you'd design tenant isolation for a multi-tenant API"* → No direct experience. Can reason through principles but no implementation track record.
- *"What's your experience with threat detection and SIEM tools?"* → No experience. This is a dealbreaker question.

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Value | Source |
|--------|-------|--------|
| URL in scan-history.tsv | ✅ Found — added 2026-06-10 (Americas version) | scan-history.tsv |
| Both Americas + Europe versions exist | ✅ Two active Ashby listings | search results + scan-history |
| Company status | ✅ Active startup, Series A Dec 2024, ~74 people | Tracxn, getlatka.com |
| JD specificity | ✅ High — specific technical scope (API keys, tenant isolation, audit logs, detection/response) | JD text |
| Boilerplate ratio | Low — reads like a real team's written requirements | JD text |
| Salary disclosed | ❌ No salary published | Ashby listing |
| Repost detection | No prior Resend evaluations in tracker | applications.md |

**Context Notes:** Resend is a legitimate, well-funded developer tools startup. Both the Americas and Europe versions of this role are in the scan-history as of 2026-06-10. The posting is fresh (2 days old), specific in scope, and consistent with the company's Platform Squad responsibilities described in their careers page. Posting freshness verification via Playwright not available in batch mode — marked as unconfirmed.

---

## Score Global

| Dimensión | Score | Notas |
|-----------|-------|-------|
| Match con CV | 1.5/5 | 4 hard blockers; only tangential AWS IAM relevance |
| Alineación North Star | 1.0/5 | Not in any target track (A, B, or C) |
| Comp | 2.5/5 | Unknown; US-rate potential but undisclosed; startup risk |
| Señales culturales | 3.0/5 | Remote Americas ✅, small team ✅, but English-first writing culture is a friction point |
| Red flags | -0.5 | Severe domain mismatch — role requires security specialization depth absent from CV |
| **Global** | **2.0/5** | **SKIP** |

**Final Recommendation: SKIP**

This is a specialized IC security engineering role that requires deep hands-on experience in AppSec, secrets management, tenant isolation, and threat detection. Federico's background is in cloud infrastructure operations, DevOps, and technology leadership — a fundamentally different domain. The cybersecurity oversight at Estudiantes de La Plata does not translate to security engineering specialization.

**What to watch for instead:** If Resend posts a DevOps Engineer, SRE, Platform Infrastructure Engineer, or similar cloud/infrastructure role on the Platform Squad, that would be a much better fit given the technical context and remote Americas setup.

---

## Keywords extraídas

`platform security`, `secrets management`, `tenant isolation`, `audit logs`, `API key management`, `access controls`, `detection and response`, `privilege escalation`, `security engineering`, `service permissions`, `leaked credentials`, `abnormal behavior detection`, `deployment pipeline security`, `internal access controls`, `developer tools security`, `SaaS platform security`, `security defaults`, `AppSec`
