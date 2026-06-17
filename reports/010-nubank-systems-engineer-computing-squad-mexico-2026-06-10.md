# Evaluation: Nubank — Systems Engineer - Computing Squad

**Date:** 2026-06-10
**URL:** https://job-boards.greenhouse.io/nubank/jobs/7572803
**Archetype:** Cloud/Infrastructure Engineer
**Score:** 3.2/5
**Legitimacy:** High Confidence
**PDF:** not generated (batch mode)
**Verification:** unconfirmed (batch mode — WebFetch used)

---

## A) Role Summary

| Field | Detail |
|---|---|
| **Company** | Nubank (Nu Holdings — NYSE: NU) |
| **Team** | Computing Squad |
| **Domain** | Fintech / Digital Banking |
| **Function** | Infrastructure improvement (performance, cost, governance); AWS + Kubernetes platform operations; scaling and access management |
| **Seniority** | Mid-Senior IC (no explicit people-management mentioned) |
| **Location** | Mexico City, Mexico — Hybrid (2-3 days/week in office) |
| **Relocation** | Relocation assistance mentioned ("if applicable") |
| **Remote Policy** | Hybrid — not fully remote; physical presence in Mexico City expected |
| **TL;DR** | Cloud/infrastructure engineering role focused on AWS EKS, Kubernetes autoscaling (Karpenter/KEDA/HPA), IAM/access management, and infrastructure governance at Nubank's Mexico operation. Requires Golang and advanced English. Strong brand, but on-site hybrid in Mexico City is a real barrier for a candidate in Argentina. |

---

## B) Match with CV

| JD Requirement | Federico's Experience | Gap? |
|---|---|---|
| AWS cloud platform experience | AWS CCP + SAA; EC2, RDS, S3, IAM, VPC, Route53, Lambda, API GW, CloudWatch, CloudFront | Strong match |
| Kubernetes + AWS EKS (hands-on) | Kubernetes listed in skills; EKS implied via AWS + K8s combination | Partial — EKS at Nubank scale (high-load fintech) unverified |
| Access management (AWS IAM, roles) | IAM explicitly listed; role/policy management part of AWS practice | Strong match |
| Karpenter, KEDA, HPA (scaling tools) | HPA is standard Kubernetes; Karpenter/KEDA not documented in CV | **Gap** — Karpenter and KEDA are advanced/specific; need to surface or acquire |
| Golang programming proficiency | Not listed in CV; no software development background documented | **Gap** — hard requirement; not mitigatable without real Golang experience |
| Advanced English (daily docs, meetings) | B1-B2 intermediate level | **Borderline gap** — JD says "Advanced English"; B1-B2 is below this bar |
| Infrastructure improvement (perf, cost, governance) | Led cloud environments at Estudiantes and Seeker; observability with Prometheus/Grafana/Zabbix | Strong match on intent |
| Root cause analysis and medium/long-term design | DevOps/Tech Lead at Seeker; CTO at Estudiantes — proven ownership of infra decisions | Strong match |
| Technical documentation and stakeholder negotiation | CTO and PM/Consultant experience across Estudiantes and Mercedes-Benz | Strong match |
| Passion for knowledge sharing / mentoring | Leadership roles at Estudiantes and Seeker imply mentoring | Inferred — not explicitly stated in CV |

**Key gaps summary:**
1. **Golang** — explicitly required, not in Federico's skill set. No workaround.
2. **Karpenter / KEDA** — advanced Kubernetes autoscaling tools not documented. Can be self-studied, but no proof point.
3. **Advanced English** — JD requires it for daily written and spoken work; B1-B2 is borderline.
4. **On-site hybrid Mexico City** — Federico is in Argentina; relocation required for this role.

**Strengths:**
- AWS breadth and certifications are a strong foundation
- IAM and access management directly addressed
- Infrastructure governance, observability, and cost-awareness align with role scope
- Leadership experience adds credibility for the stakeholder/documentation dimension

---

## C) Level & Strategy

**JD Level:** Senior IC — inferred from scope (contributing to product strategy, representing in technical forums, medium-to-long-term design decisions).

**Federico's Level:** Senior/Lead — seniority aligns, but track is ops/infrastructure, not SWE. Golang requirement puts this closer to a hybrid SWE-infra role.

**Sell Senior plan:**
- Lead with AWS IAM depth and infrastructure governance experience — "Access management expertise" is a headline requirement and Federico has documented IAM work.
- Frame Kubernetes usage at current roles as hands-on EKS-adjacent experience; highlight HPA configuration if done.
- Position the cost/performance improvement angle from Estudiantes (managing production AWS environments efficiently) as direct experience.
- Acknowledge Golang gap honestly; show learning trajectory if any Go scripts or tools have been used.

**Key risk:** Golang is a hard technical screen filter at Nubank. Without demonstrable Go code, passing a technical interview is unlikely regardless of infra strength.

**Location risk:** Hybrid Mexico City means physical relocation from Argentina. Even with relocation assistance, this is a life decision. If Federico is open to relocating to Mexico City, this is a viable path; if not, the role is not practical regardless of technical fit.

---

## D) Comp & Demand

*WebSearch unavailable — estimates based on market knowledge and prior Nubank evaluations in this pipeline.*

| Source | Role | Location | Range (USD/month) |
|---|---|---|---|
| Nubank LATAM market data (training) | Systems/Senior Engineer | Mexico City | ~$3,500–$6,000 |
| General LATAM fintech infra market | Cloud/Infra Engineer | Mexico (hybrid) | ~$4,000–$6,500 |
| Nubank benefits package | Stock equity, health/dental/vision, food card, gym, WFH allowance | LATAM | Adds meaningful value |
| Prior Nubank report (#001) comp estimate | Senior Engineer LATAM | Buenos Aires | ~$3,500–$5,500 |

**Verdict:** Comp likely meets Federico's $4,000–$6,000/month target at the midpoint. Equity upside (NYSE: NU) is a real differentiator. The benefits package — health insurance, food card, language training, 30-day holiday bonus, 17+ vacation days — is competitive for LATAM standards.

**Net comp note:** Mexico City cost of living is higher than Argentina. If relocating, take-home purchasing power may be lower than the gross USD figure suggests.

---

## E) Customization Plan

**Top 3 CV/application changes if applying:**

1. **Expand IAM and access management section** — this is a headline requirement. Add specific examples: cross-account role assumptions, service control policies (SCPs), least-privilege policy design, identity federation. Even one concrete IAM architecture story will stand out.

2. **Surface Kubernetes autoscaling work** — add any HPA configuration or resource limit tuning done at Seeker or Estudiantes. If Karpenter or KEDA have not been used, do not fabricate — but note familiarity with the scaling problem space and willingness to ramp.

3. **Address Golang gap directly** — either surface any Go tooling used (even CLI tools or basic scripts), or note it as active learning in the CV's training section. Do not leave it as a blank — Nubank's tech screen will probe it.

**Additional notes:**
- If Federico is open to Mexico City relocation, mention it explicitly in the application cover note.
- The language training benefit is a positive signal — Nubank invests in English development, which may indicate B1-B2 candidates can grow into the requirement.

---

## F) Interview Plan

**STAR+R Stories mapped to JD requirements:**

1. **AWS IAM and Access Management at Scale:**
   *Situation:* Estudiantes de La Plata needed secure, governed AWS access for a multi-team cloud environment serving tens of thousands of users. *Task:* Design IAM structure for production. *Action:* Created role hierarchies, enforced least-privilege policies, configured CloudTrail for audit trails. *Result:* Compliant, auditable access model with no privilege escalation incidents. *Relevance:* Direct match to "Access management expertise (AWS IAM, Role management)."

2. **Infrastructure Cost and Performance Improvement:**
   *Situation:* At Seeker Parking, multiple product environments were running with unoptimized AWS resource usage. *Task:* Identify and reduce infrastructure costs without impacting availability. *Action:* Audited EC2 sizing, reviewed RDS instance types, rightsized resources, implemented CloudWatch cost alarms. *Result:* [Candidate to quantify: % reduction in monthly AWS spend]. *Relevance:* "Identify and pursue infrastructure improvement opportunities in performance, costs, and governance."

3. **Kubernetes Deployment and Container Orchestration:**
   *Situation:* [Candidate to prepare: Kubernetes adoption or management context at Seeker or Estudiantes]. *Task:* Deploy and manage containerized workloads. *Action:* Configured Kubernetes cluster (or EKS), defined namespaces, resource requests/limits, HPA for auto-scaling. *Result:* Stable, scalable container platform. *Relevance:* "Strong hands-on experience with Kubernetes and AWS EKS."

4. **Root Cause Analysis — Production Incident:**
   *Situation:* Production environment at Estudiantes experienced an unplanned degradation during a high-traffic event (e.g., match day). *Task:* Identify root cause and restore service. *Action:* Used CloudWatch + Prometheus/Grafana to trace the issue; identified bottleneck; applied fix and post-incident review. *Result:* Service restored; preventive measures implemented. *Relevance:* "Conduct deep analysis to identify root causes and develop solutions with medium to long-term impact."

5. **Technical Documentation and Stakeholder Communication:**
   *Situation:* At Mercedes-Benz, a complex enterprise technology project required alignment across internal teams, vendors, and senior stakeholders. *Task:* Document and negotiate technical decisions. *Action:* Produced architecture decision records, presented trade-offs to non-technical executives, facilitated vendor negotiations. *Result:* Project delivered on scope and timeline. *Relevance:* "Represent the team in technical forums while documenting and negotiating with stakeholders."

6. **Platform Strategy Contribution:**
   *Situation:* As CTO at Estudiantes, needed to define the cloud technology roadmap for the organization. *Task:* Contribute to infrastructure product strategy. *Action:* Collaborated with stakeholders to prioritize reliability, modernization, and cost goals; documented decisions. *Result:* Roadmap adopted and executed across teams. *Relevance:* "Contribute to Computing product strategy alongside peers and Product Managers."

---

## G) Posting Legitimacy

- **Posting freshness:** Active Greenhouse job board listing; no expiry signals in page content. Greenhouse URLs are unique per requisition and typically reflect live openings.
- **Description quality:** High — specific team name (Computing Squad), concrete technical stack (Karpenter, KEDA, HPA, EKS), specific competency language. Not a generic posting; written by someone with real platform context.
- **Company signals:** Nubank is NYSE-listed (ticker: NU), one of the world's largest digital banks (122M+ customers). Mexico City office is established and central to LATAM expansion strategy.
- **Reposting signals:** None detected.
- **Compensation transparency:** No salary range published (common for LATAM roles), but benefits are explicitly listed — a positive legitimacy signal.
- **Legitimacy Tier: High Confidence**

---

## Keywords Extracted

AWS EKS, Kubernetes, Karpenter, KEDA, HPA, IAM, access management, role management, Golang, infrastructure governance, cost optimization, performance engineering, cloud platform, Computing Squad, fintech, LATAM, hybrid, Mexico City, Systems Engineer, auto-scaling

---

## Machine Summary

```yaml
num: 10
date: 2026-06-10
company: Nubank
role: Systems Engineer - Computing Squad
score: 3.2
status: Evaluated
pdf: false
url: https://job-boards.greenhouse.io/nubank/jobs/7572803
slug: nubank-systems-engineer-computing-squad-mexico
```
