# Evaluation: Nubank — Senior Systems Engineer (Service Provisioning)

**Date:** 2026-06-10
**URL:** https://job-boards.greenhouse.io/nubank/jobs/7658493
**Archetype:** DevOps/Platform Engineering
**Score:** 3.6/5
**Legitimacy:** High Confidence
**PDF:** not generated (batch mode) — run `/career-ops pdf nubank-senior-systems-engineer-service-provisioning` if needed
**Verification:** unconfirmed (batch mode — WebFetch used)

---

## A) Role Summary

| Field | Detail |
|---|---|
| **Archetype** | Platform Engineering / Internal Developer Platform (IDP) |
| **Domain** | Fintech / Financial Services |
| **Function** | Build & own internal Service Provisioning platform (~3,000 microservices); Infrastructure Control Plane design |
| **Seniority** | Senior (IC, no explicit people-management) |
| **Remote Policy** | Hybrid — 2-3 days/week in Buenos Aires office |
| **TL;DR** | Build the internal platform that manages microservice provisioning, deployment, and cross-region infra topology for Nubank. Heavy Kubernetes/AWS EKS + software engineering (Java/Python/Go). Not pure ops — closer to Platform Engineering SWE. |

---

## B) Match with CV

| JD Requirement | Federico's Experience | Gap? |
|---|---|---|
| Deep AWS experience | AWS CCP + SAA certs; EC2, RDS, S3, IAM, VPC, Route53, Lambda, API GW, CloudWatch | Strong match |
| Strong Kubernetes / EKS mastery | Kubernetes listed in skills; EKS implied via AWS expertise | Partial — depth unclear; no EKS-at-scale projects documented |
| Java, Python, or Golang proficiency | Not listed in CV; no software dev background stated | **Gap** — significant |
| Distributed systems (queues, concurrency) | Not explicitly listed | **Gap** — no evidence in CV |
| High-scale platform experience | Estudiantes de La Plata: tens of thousands of users; Seeker Parking: multiple products | Partial — ops/infra scale, not SWE-level platform |
| Internal Developer Platform / IDP experience | No explicit IDP work documented | **Gap** |
| Intermediate-to-advanced English | B1-B2 per candidate profile | Meets minimum stated ("Intermediate-to-advanced") |
| Autonomous in ambiguous environments | CTO role at Estudiantes, Technology Lead at Seeker — proven leadership in ambiguity | Strong match |
| CI/CD pipelines | GitHub Actions, GitLab CI/CD | Strong match |

**Key gaps:** Software engineering proficiency (Java/Python/Go) is the primary risk. This role leans more toward a Platform SWE than a DevOps/SRE. Federico's background is infrastructure-ops, not application development. Kubernetes depth at EKS scale is unverified.

**Mitigation:** Emphasize Terraform automation and CI/CD pipeline work. Highlight Kubernetes usage in current role. If Python scripting has been used in any automation context, surface it prominently.

---

## C) Level & Strategy

**JD Level:** Senior IC — equivalent to 5-8 years, software-heavy platform engineering.
**Federico's Level:** Senior/Lead — technically aligned in seniority, but from an ops/infrastructure track rather than SWE track.

**Sell Senior plan:** Lead with the Infrastructure Control Plane angle — Federico's experience designing multi-product cloud infra at Seeker and AWS production at Estudiantes maps to the cross-region, multi-account provisioning challenge. Frame the CTO role as proof of ownership over platform decisions at scale.

**If downleveled:** The role is already positioned as "Senior" with no explicit Staff/Principal above. Downlevel risk is low. Bigger risk is being screened out for insufficient SWE background in the language assessment phase.

**Red flag:** The JD explicitly requires Java/Python/Go. Without demonstrable code-writing ability, passing the technical screen will be difficult. Recommend preparing Python scripting examples (infrastructure automation, Lambda functions) before applying.

---

## D) Comp & Demand

*WebSearch unavailable — estimates based on training data and market knowledge.*

| Source | Role | Location | Range (USD/month) |
|---|---|---|---|
| Glassdoor estimates (training data) | Senior Engineer, Nubank Argentina | Buenos Aires | ~$3,500–$5,500 |
| General LATAM fintech senior eng market | Senior SWE/Platform Eng | Argentina remote | ~$4,000–$6,000 |
| Nubank public ranges (Brazil base) | Senior Engineer | LATAM | ~$4,500–$7,000 equivalent |

Nubank pays competitively vs LATAM market. Equity (stock options) is mentioned. Likely meets Federico's $4,000–$6,000 target. Min $2,500 threshold easily exceeded.

---

## E) Customization Plan

**Top 5 CV changes:**
1. Add a dedicated "Platform Engineering" section or bullet highlighting any IDP-adjacent work (service catalog, internal tooling, deployment automation)
2. Expand Kubernetes section: mention cluster management, Helm, namespaces, or any EKS-specific work at current role
3. Surface any Python scripting (Lambda functions, automation scripts, monitoring hooks) — even light scripting counts
4. Quantify Seeker Parking platform scope: number of services/environments managed, deployment frequency
5. Add "distributed systems" framing to Estudiantes: mention event-driven architecture, queues, or any async patterns used

**Top 5 LinkedIn changes:**
1. Add "Internal Developer Platform" and "Platform Engineering" to Skills section
2. Update Seeker Parking headline to mention "multi-service platform" or "infrastructure control plane"
3. Add Kubernetes/EKS as featured skill with endorsements
4. Post or share content about AWS EKS / Kubernetes automation to signal active interest
5. Add AWS SAA certification badge to profile (if not already visible)

---

## F) Interview Plan

**STAR+R Stories mapped to JD requirements:**

1. **Infrastructure Control Plane (Cross-region deployment):**
   *Situation:* Estudiantes de La Plata needed AWS infrastructure across multiple environments for tens of thousands of users. *Task:* Design and implement cloud architecture. *Action:* Architected multi-account/VPC structure with IAM policies, CloudWatch monitoring, RDS. *Result:* Stable production with monitoring. *Relevance:* Maps to cross-region, multi-account design requirement.

2. **CI/CD Pipeline Automation:**
   *S:* Seeker Parking required repeatable deployments across multiple products. *T:* Standardize deployment process. *A:* Implemented GitHub Actions/GitLab CI/CD pipelines with Docker containers. *R:* Reduced deployment time, eliminated manual steps. *Relevance:* Direct match to "manifest generation integrated into CI/CD."

3. **Handling Circular Dependencies / Systemic Issues:**
   *S:* [Candidate to prepare: any incident at Seeker or Estudiantes involving interdependent systems, infra ordering dependencies, or deployment sequencing]. *T/A/R/Rel:* Frame as solving systemic provisioning issues.

4. **Large-scale Infrastructure Change Safety:**
   *S:* At Estudiantes managing digital transformation for tens of thousands of users. *T:* Roll out new infrastructure without downtime. *A:* Used staged rollouts, CloudWatch alarms, rollback plans. *R:* Zero major incidents during transition. *Relevance:* Safety mechanisms for large-scale changes.

5. **Kubernetes Adoption:**
   *S:* [Candidate to prepare: context for adopting or managing Kubernetes at current role]. *T:* Deploy containerized workloads at scale. *A:* Set up EKS/K8s cluster, configured namespaces, Helm charts, resource limits. *R:* Improved deployment reliability. *Relevance:* Core K8s mastery requirement.

6. **Vendor/Stakeholder Coordination at Scale (Software Engineering Alignment):**
   *S:* Mercedes-Benz: large enterprise SAP/technology projects. *T:* Align engineering teams, vendors, and business stakeholders. *A:* Led cross-functional delivery. *R:* On-time delivery of enterprise platform changes. *Relevance:* Working autonomously in ambiguous environments.

7. **Operating at Scale — High Traffic Events:**
   *S:* Estudiantes de La Plata: peak events (match days, ticketing surges). *T:* Ensure platform stability under load. *A:* Implemented auto-scaling (EC2/ECS), set CloudWatch alarms, pre-scaled before events. *R:* No service degradation during peak load. *Relevance:* High-scale platform experience.

---

## G) Posting Legitimacy

- **Posting freshness:** Active Greenhouse board listing; no expiry signals detected in page content.
- **Description quality:** High — specific team context (3,000+ microservices), concrete technical challenges (circular dependencies, cross-region provisioning), clear engineering culture signals. Not a generic posting.
- **Company signals:** Nubank is a publicly traded fintech (NYSE: NU), one of the largest in Latin America. Buenos Aires office is established and actively hiring.
- **Reposting signals:** None detected. Greenhouse URLs are typically unique per requisition.
- **Legitimacy Tier: High Confidence**

---

## Keywords Extracted

Kubernetes, EKS, AWS, Infrastructure Control Plane, Service Provisioning, Internal Developer Platform, IDP, CI/CD, Terraform, Docker, microservices, distributed systems, Java, Python, Golang, GitOps, multi-account, cross-region, Platform Engineering, SRE

---

## Machine Summary

```yaml
num: 1
date: 2026-06-10
company: Nubank
role: Senior Systems Engineer (Service Provisioning)
score: 3.6
status: Evaluated
pdf: false
url: https://job-boards.greenhouse.io/nubank/jobs/7658493
slug: nubank-senior-systems-engineer-service-provisioning
```
