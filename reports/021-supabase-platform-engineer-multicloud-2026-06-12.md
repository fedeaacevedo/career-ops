# Evaluación: Supabase — Platform Engineer - Multicloud

**Fecha:** 2026-06-12
**Arquetipo:** Cloud / Infrastructure Engineer + DevOps / Platform Engineer
**Score:** 2.5/5
**Legitimacy:** High Confidence
**URL:** https://jobs.ashbyhq.com/supabase/847a7bd7-6b75-444a-aeda-d0b28a11c764
**PDF:** not generated — run /career-ops pdf supabase to create on demand
**Batch ID:** 5

---

## Machine Summary

```yaml
company: "Supabase"
role: "Platform Engineer - Multicloud"
score: 2.5
legitimacy_tier: "High Confidence"
archetype: "Cloud / Infrastructure Engineer + DevOps / Platform Engineer"
final_decision: "Skip"
hard_stops:
  - "Multi-cloud gap: role requires AWS + GCP + Azure at scale; Federico has AWS only"
  - "Pulumi-specific IaC expertise required; Federico has Terraform (adjacent but not the same)"
  - "8+ years in platform/infra IC role — Federico's career is mixed management + hands-on"
soft_gaps:
  - "No developer tools product domain experience"
  - "Async globally distributed team experience not demonstrated in CV"
  - "No GCP or Azure certifications or listed projects"
top_strengths:
  - "Strong AWS foundation (EC2, RDS, S3, IAM, VPC, Lambda, CloudWatch, Route53)"
  - "Kubernetes listed in skills"
  - "Terraform (IaC adjacent to Pulumi)"
  - "Remote-first company aligns with location policy (Argentina)"
risk_level: "High"
confidence: "High"
next_action: "Skip — address multi-cloud gap first (GCP/Azure labs, certifications) before targeting similar roles"
```

---

## Paso 0 — Arquetipo Detectado

**Arquetipo primario:** Cloud / Infrastructure Engineer
**Arquetipo secundario:** DevOps / SRE / Platform Engineer

Supabase (Compute Team) busca un especialista IC profundo en **portabilidad multi-cloud**: auditoria de dependencias cloud-específicas, diseño de abstracciones cloud-agnósticas, orquestación Kubernetes cross-cloud. El rol es 100% hands-on plataforma, no tiene componente de liderazgo ni gestión de personas.

Esto encuadra en **Track A** del perfil de Federico — el arquetipo correcto, pero el rol exige una profundidad de IC platform engineering multi-cloud que el CV actual no acredita.

---

## A) Resumen del Rol

| Campo | Detalle |
|-------|---------|
| **Arquetipo** | Cloud / Infrastructure Engineer (Platform Engineering) |
| **Domain** | Developer Tools / Postgres Development Platform |
| **Function** | Platform Engineering IC — Compute Team |
| **Seniority** | Senior / Staff (8+ años; fuentes divergentes indican 3-5+ en otras variantes, pero el scope sugiere Senior/Staff) |
| **Remote** | Fully remote, worldwide — no oficinas físicas |
| **Team** | Compute Team (producto interno de infraestructura) |
| **Comp** | No listado; estimado $60K-$100K USD/año para LATAM con ajuste geográfico (~$5K-$8K/mes) |
| **TL;DR** | Construir infraestructura cloud-portable para Supabase: migrar dependencias AWS-específicas, diseñar abstracciones agnósticas, mantener Kubernetes multi-cloud. Core skill: AWS + GCP + Azure + Pulumi + K8s en producción a escala. |

**Empresa:** Supabase es el Postgres development platform (Database, Auth, Storage, Edge Functions, Realtime, Vector Search). Startup valuada en $2B+, $116M+ en funding. Sin oficinas físicas — equipo global distribuido. Ofrece WeWork o coworking allowance anywhere. ESOP para todos.

**Hiring process:** 4 etapas — application review → intro call → hasta 4 entrevistas con team y liderazgo → decisión final.

---

## B) Match con CV

### Mapping de Requisitos

| Requisito JD | Evidencia en CV | Nivel |
|---|---|---|
| Multi-cloud a escala (AWS + GCP + Azure) | Solo AWS (EC2, RDS, S3, IAM, VPC, Lambda, CloudWatch, etc.) — sin GCP ni Azure mencionados | ❌ **Hard blocker** |
| Kubernetes en múltiples plataformas cloud | cv.md: "Kubernetes" listado en DevOps skills | ⚠️ Listado, sin cross-cloud depth |
| Pulumi o IaC equivalente | cv.md: Terraform listado — Pulumi no aparece | ⚠️ Parcial (adjacent) |
| 8+ años en platform/infra engineering | Roles: Seeker (DevOps Lead), Estudiantes (CTO), MB (PM/Consultor), Disney (Infra/Sysadmin) — mix de management y hands-on | ⚠️ Parcial — no 8 años full IC platform |
| Experiencia en cloud abstraction / re-platforming | MB: "migration and integration projects"; Estudiantes: "cloud-based services and operational improvements" | ⚠️ Muy genérico, no cloud portability específica |
| Comunicación técnica / no técnica | Todos los roles: vendor management, stakeholder management, external providers | ✅ Fuerte |
| Async / globally distributed teams | No mencionado explícitamente en ningún rol | ⚠️ Neutral |
| Developer tools orientation | Ninguna experiencia en developer tooling companies | ❌ Gap |
| Contribuir a arquitectura de target cloud environments | MB: "participated in migration and integration projects" | ⚠️ Genérico |

**Coverage técnica directa:** ~25-30%. El gap multi-cloud es estructural y central al rol.

### Gaps y Estrategia de Mitigación

| Gap | Severidad | Mitigación |
|-----|-----------|------------|
| Multi-cloud (GCP + Azure) | **Hard blocker** — rol cuyo nombre es "Multicloud"; no hay forma de compensar | Labs GCP/Azure + cert (GCP ACE o AZ-900/104) mínimo 3-6 meses trabajo real |
| Pulumi | Soft — el JD dice "or similar IaC tooling" | Demostrar Terraform depth; mencionar que Pulumi usa mismos conceptos; aportar proyecto Pulumi en portfolio |
| Cross-cloud Kubernetes | Soft — Federico tiene K8s pero no cross-cloud | Desplegar cluster EKS+GKE en labs; documentar en portfolio |
| Developer tools domain | Soft | No hay compensación directa — Supabase es una empresa muy específica de dev tools |
| 8+ años IC platform | Parcial — Federico tiene experiencia pero incluye mucha gestión | Reencuadrar roles hands-on como platform ownership real |

**Diagnóstico:** El multi-cloud gap es una barrera real que no se puede superar con narrativa. El rol existe para migrar Supabase fuera de su dependencia AWS actual — quien lo ocupe debe haber operado GCP y Azure a escala real, no solo AWS. Federico necesita credenciales GCP/Azure antes de postular a este tipo de roles.

---

## C) Nivel y Estrategia

### Nivel detectado

| Aspecto | JD | Federico |
|---------|-----|---------|
| **Nivel** | Senior / Staff IC | Technical Leader / CTO + Senior DevOps IC |
| **Track** | Platform Engineering deep IC | Track A primario, pero con fuerte sesgo hacia leadership |
| **Scope** | Individual contributor platform architect | Lider técnico con ownership end-to-end de infra |

### Análisis

El rol de Supabase es un **IC platform engineering puro** — sin componente de gestión de personas o equipos. Buscan a alguien que pueda hacer hands-on:
- Diseñar abstracciones cloud-agnósticas
- Mantener Kubernetes multi-cloud
- Escribir Pulumi para infraestructura portable

El perfil natural de Federico es más fuerte como **Technical Lead / Infrastructure Manager** que como deep IC platform specialist. Su historial más relevante (CTO en Estudiantes, DevOps Lead en Seeker) mezcla ownership técnico con liderazgo — lo que diferencia a Federico positivamente en roles de liderazgo, no en este tipo de IC.

### Plan "si llegara a postular"

**Framing senior sin mentir:**
- "Diseñé y operé infraestructura AWS en producción para organizaciones con decenas de miles de usuarios"
- "Lideré la adopción de Terraform para infraestructura como código en entornos productivos"
- "Dirigí migraciones de sistemas y proyectos de integración en entornos enterprise complejos (Mercedes-Benz)"

**Debilidad estructural que no se puede ocultar:** no hay GCP ni Azure en el CV. En el primer screening técnico esto surgirá. No hay plan de mitigación narrativa para esto.

---

## D) Comp y Demanda

### Datos de Mercado

| Fuente | Dato | Rango |
|--------|------|-------|
| Levels.fyi (Supabase) | Software Engineer mediana total comp | $115K/año (~$9,600/mes) |
| Levels.fyi (Supabase top) | Postgres/infra experts | $160K-$205K/año |
| Supabase (general) | Geographic adjustments for remote | ~40-60% de rates SF para LATAM |
| Estimado Argentina-based | Platform Engineer Senior | $50K-$100K/año → **$4,200-$8,300/mes USD** |
| Target Federico | Preferred range | $4,000-$6,000/mes |

### Evaluación Comp

**Score comp: 4/5** — Supabase paga por encima del mercado incluso con ajuste geográfico. El rango estimado para Argentina está dentro o por encima del target de Federico. Adicionalmente ofrecen ESOP (equity pre-IPO en startup $2B+ valuada), health insurance 100% employee / 80% dependents, allowances de tecnología y desarrollo profesional.

**Riesgo:** Supabase no publica salario para este rol específico. El ajuste geográfico real puede variar. Preguntar en intro call antes de invertir tiempo en el proceso.

### Tendencia de Demanda

Supabase está activamente contratando (33+ posiciones abiertas en Glassdoor a junio 2026). El rol multicloud responde a una iniciativa estratégica de la compañía para desacoplarse de un solo cloud provider — lo que sugiere urgencia real. Supabase no aparece en ningún tracker de layoffs de 2026.

---

## E) Plan de Personalización

> **Nota:** Dado que el score es 2.5/5 y hay un hard blocker estructural (multi-cloud), la personalización solo aplica si Federico decide postular de todos modos después de considerar los gaps.

| # | Sección | Estado actual | Cambio propuesto | Por qué |
|---|---------|---------------|------------------|---------|
| 1 | Professional Summary | Genérico "technology leader and cloud infrastructure professional" | Agregar "hands-on cloud infrastructure engineer with focus on production reliability, IaC, and Kubernetes operations" | El rol busca un IC hands-on, no un leader |
| 2 | Skills — Cloud | AWS-only | Si se tienen laboratorios/experiencia GCP o Azure, agregarlos | El rol exige multi-cloud; sin GCP/Azure el CV se filtra automáticamente |
| 3 | Skills — DevOps | Terraform listado | Agregar "Pulumi (familiar)" o completar un Pulumi project real | Pulumi es el stack de Supabase; Terraform alone no es suficiente |
| 4 | Seeker Parking bullets | Muy genérico | Especificar Kubernetes usage: "Manage Kubernetes-based workload orchestration across production environments" | K8s es core al rol |
| 5 | Estudiantes de La Plata bullets | "Implemented cloud-based services and operational improvements" | Reescribir como: "Led cloud infrastructure migration and production environment modernization on AWS" | Re-platforming experience es específicamente lo que buscan |

**LinkedIn (si aplica):**
1. Headline: "Senior DevOps / Platform Engineer | AWS | Kubernetes | Terraform | Infrastructure at Scale"
2. About: Enfatizar hands-on infra ownership vs management
3. Skills: Agregar "Pulumi" (learner), "Multi-Cloud Architecture"
4. Featured: Agregar cualquier proyecto Kubernetes o Terraform público
5. Experience (Seeker): Especificar stack técnico con más detalle

---

## F) Plan de Entrevistas

> Solo relevante si Federico procede con la postulación.

### Historias STAR

| # | Requisito JD | Historia STAR | S | T | A | R |
|---|---|---|---|---|---|---|
| 1 | IaC / Terraform / re-platforming | Implementación de Terraform en Seeker/Estudiantes | Infra manual sin reproducibilidad, múltiples entornos | Estandarizar infra como código para dev/staging/prod | Diseñé Terraform modules, configuré state remoto, implementé CI/CD para infra | Entornos reproducibles, reducción de tiempo de provisioning |
| 2 | Kubernetes workload orchestration | Kubernetes en entornos de producción | Servicios sin orquestación o deployment manual | Migrar a contenedores con K8s para reliability y scaling | Diseñé manifests K8s, configuré deployments y servicios, implementé monitoreo | Mejora en uptime y deployment frequency |
| 3 | Cloud migration / re-platforming | Proyecto de migración en Mercedes-Benz | Sistemas legacy con integración SAP requerida | Coordinar migración técnica multi-stakeholder | Relevamiento de dependencias, plan de migración, coordinación de proveedores | Migración ejecutada sin disruption operativa |
| 4 | Production operations at scale | Gestión de producción en Estudiantes de La Plata | Infraestructura AWS sin observability madura | Implementar monitoring y incident management para servicio a decenas de miles de usuarios | Prometheus + Grafana deployment, alerting, runbooks | Reducción de tiempo de respuesta a incidentes |
| 5 | Stakeholder communication (technical/non-technical) | Cualquier project en Estudiantes o MB | Necesidad de alinear equipos técnicos y negocio | Comunicar decisiones de infra a stakeholders no-técnicos | Preparé arquitecturas visuales, presenté trade-offs en términos de negocio | Decisiones alineadas sin bloqueantes técnicos |

### Case Study Recomendado

**Seeker Parking — Platform Evolution:** Presentar como "ongoing platform modernization" — cómo se está construyendo la infraestructura que soporta múltiples productos y entornos. Enfatizar las decisiones de arquitectura cloud, el stack de observability, y cualquier trabajo de IaC o K8s.

### Preguntas Red-Flag y Respuestas

| Pregunta | Red flag | Respuesta recomendada |
|----------|----------|----------------------|
| "¿Cuánto trabajaste con GCP y Azure?" | El CV no los muestra | "Mi experiencia productiva principal es en AWS. Tengo familiaridad conceptual con GCP y Azure y estoy activamente expandiendo esa expertise. En roles de plataforma, los principios de networking, IAM, y workload orchestration son transferibles — ¿qué aspectos de GCP/Azure son más críticos en este rol?" |
| "¿Usaste Pulumi en producción?" | No está en el CV | "He trabajado extensivamente con Terraform, que cubre el mismo espacio conceptual. Estoy familiarizado con el modelo de Pulumi (programmatic IaC) y la curva de adopción es corta dado el contexto. ¿Qué partes del stack Pulumi de Supabase son las más complejas?" |
| "¿Dónde operaste Kubernetes en múltiples clouds?" | CV solo menciona K8s en general | "Mis despliegues de K8s han sido en AWS (EKS). El diseño cross-cloud de K8s es algo que estoy desarrollando activamente. Puedo hablar de los desafíos de networking y workload portability que he encontrado en producción." |

---

## G) Posting Legitimacy

**Assessment: High Confidence**

> Nota: Playwright no disponible en batch mode. Señales de frescura del posting no verificadas directamente.

### Señales

| Señal | Dato | Evaluación |
|-------|------|------------|
| Calidad del JD | Específico, requisitos realistas, responsabilidades claras, sin excessive boilerplate | ✅ Positivo |
| Transparencia salarial | No listado — común en startups bien financiadas | ⚠️ Neutral |
| Múltiples job boards | Ashby (ATS oficial), Accel, Glassdoor, Remotive, Remotech | ✅ Posting activo y distribuido |
| Historial de scan | Primer aparición: 2026-06-10 (hace 2 días) — no re-posting | ✅ Fresco |
| Noticias de layoffs | Supabase no aparece en ningún tracker de layoffs 2026 | ✅ No hay señales de freeze |
| Contexto de contratación | 33+ posiciones abiertas en Glassdoor; empresa en fase de crecimiento | ✅ Hiring activo |
| Coherencia estratégica | Rol de "Multicloud" consistente con posición de Supabase (Pulumi case study publicado, iniciativa estratégica documentada) | ✅ Rol genuino |

**Context Notes:**
- Supabase es una empresa en growth activo post Series C ($116M+, $2B+ valuación)
- El rol responde a una iniciativa estratégica real: desacoplarse de dependencia AWS
- La empresa tiene historial público de uso de Pulumi (case study en pulumi.com)
- No se detectó evidencia de freeze o layoffs
- Posting fue agregado el 2026-06-10 por el scanner — considerado fresco

---

## Score Global

| Dimensión | Score |
|-----------|-------|
| Match con CV | 1.5/5 |
| Alineación North Star (Track A) | 2.5/5 |
| Comp | 4.0/5 |
| Señales culturales | 3.5/5 |
| Red flags (multi-cloud gap estructural) | -0.5 |
| **Global** | **2.5/5** |

**Decisión final: SKIP**

El gap de multi-cloud (no GCP, no Azure en el CV de Federico) es un hard blocker para un rol cuyo nombre, misión, y requisitos principales giran en torno a AWS + GCP + Azure. El score técnico real no alcanza el mínimo recomendado de 4.0/5. La compensación y la cultura de la empresa son atractivas, pero no compensan una brecha de habilidades que sería evidente en el primer screening técnico.

**Camino recomendado:** Completar laboratorios o proyectos reales en GCP y Azure (incluyendo K8s cross-cloud), obtener una certificación adicional (GCP ACE o AZ-104), y volver a evaluar roles similares en 3-6 meses.

---

## Keywords extraídas

`multi-cloud`, `Kubernetes`, `Pulumi`, `cloud portability`, `infrastructure-as-code`, `cloud abstraction`, `platform engineering`, `Compute Team`, `cloud-agnostic`, `AWS`, `GCP`, `Azure`, `re-platforming`, `distributed systems`, `async team`, `developer tools`, `Postgres`, `infrastructure portability`, `workload orchestration`, `cloud dependencies`
