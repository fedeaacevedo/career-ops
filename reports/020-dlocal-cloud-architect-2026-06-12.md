# Evaluación: dLocal — Cloud Architect

**Fecha:** 2026-06-12
**Arquetipo:** Cloud / Infrastructure Engineer (secondary: Cloud Architect / Solutions Architect)
**Score:** 2.6/5
**Legitimacy:** Suspicious
**URL:** https://jobs.lever.co/dlocal/1244cc72-c553-40ce-ac1a-afc2a5bb4dc3
**PDF:** not generated — run `/career-ops pdf dlocal-cloud-architect` to create on demand
**Batch ID:** 1
**Verification:** unconfirmed (batch mode — Lever retorna HTTP 403; JD no recuperable)

---

> **NOTA DE EVALUACIÓN:** La URL de la oferta retorna HTTP 403 (Forbidden) — igual patrón que el rol dLocal Head of Platform Engineering del 2026-06-10. La oferta fue indexada en scan-history el 2026-06-10 con título "Cloud Architect" y ubicación "Spain". Esta evaluación se basa en el título del rol, el perfil público de dLocal como empresa, y las normas de industria para roles de Cloud Architect en fintechs. Tratar como evaluación parcial/especulativa.

---

## Machine Summary

```yaml
company: "dLocal"
role: "Cloud Architect"
score: 2.6
legitimacy_tier: "Suspicious"
archetype: "Cloud Architect / Solutions Architect"
final_decision: "Skip"
hard_stops:
  - "Posting returns HTTP 403 — likely expired or geo-blocked (2 days since indexing, persists)"
  - "Location Spain — fuera de la geografía preferida LATAM de Federico"
soft_gaps:
  - "No fintech/payments domain experience"
  - "AWS Associate-level certifications vs. Professional typically expected for Architect title"
  - "Cloud Architect es arquetipo secundario — rol IC puro vs. fuerza de Federico en liderazgo + operaciones"
top_strengths:
  - "AWS production depth (EC2, RDS, S3, IAM, VPC, Route53, Lambda, CloudWatch, CloudFront)"
  - "Terraform + Kubernetes + Docker + CI/CD — stack completo de IaC y plataforma"
  - "Observability stack (Prometheus, Grafana, Zabbix) con experiencia en production ownership"
risk_level: "High"
confidence: "Low"
next_action: "No aplicar — posting probablemente cerrado. Si el rol reaparece con URL activa y configuración remote-LATAM, re-evaluar con JD completo."
```

---

## A) Resumen del Rol

| Campo | Detalle |
|-------|---------|
| Arquetipo | Cloud Architect / Solutions Architect (secondary para Federico) |
| Empresa | dLocal (NASDAQ: DLO) — fintech de pagos en mercados emergentes, ~700 empleados, HQ Uruguay |
| Dominio | Fintech / Payments Infrastructure |
| Función | Diseño de arquitectura cloud, implementación y gobierno — típicamente: AWS, IaC, networking, seguridad, escalabilidad |
| Seniority | Senior/Lead (Cloud Architect = 5-8+ años típicamente, con profundidad en arquitectura y diseño) |
| Ubicación | Spain (source: scan-history — si es on-site o hybrid, fuera de la geografía de Federico) |
| Remote policy | Desconocida (URL 403 — dLocal tiene equipos distribuidos en LATAM y Europa) |
| Comp visible | No disponible (JD no recuperable) |
| TL;DR | Cloud Architect en fintech NASDAQ en España. Posting probablemente cerrado (403 persistente). Arquetipo secundario para Federico con location mismatch importante. Evaluar solo si el rol reaparece con URL activa y política remote-LATAM confirmada. |

**Sobre dLocal:**
dLocal es una empresa uruguaya cotizada en NASDAQ (símbolo: DLO) que procesa pagos en mercados emergentes (LATAM, África, Asia). Cultura de ingeniería cloud-native sobre AWS. Tiene presencia en Uruguay, Brasil, España, y otros mercados. En Glassdoor: 3.5/5 con 138 reviews; 62% recomendarían trabajar allí; comentarios frecuentes sobre salario por debajo de mercado, presión alta, y procesos de HR caóticos.

---

## B) Match con CV

**Nota:** JD no disponible (403). Match inferido de normas de industria para Cloud Architect en fintech y del perfil público de dLocal.

### Requisitos típicos para Cloud Architect en fintech vs. Federico

| Requisito del JD (inferido) | Match en CV | Línea / evidencia | Nivel de match |
|-----------------------------|-------------|-------------------|---------------|
| AWS avanzado (EC2, VPC, IAM, RDS, S3, Lambda, CloudFront) | cv.md — Core Skills / Cloud | Lista completa de servicios AWS relevantes | ✅ Fuerte |
| Terraform / IaC | cv.md — Core Skills / DevOps | "Terraform" en DevOps skills | ✅ Fuerte |
| Kubernetes / Docker / contenedores | cv.md — Core Skills / DevOps | "Kubernetes", "Docker" | ✅ Fuerte |
| CI/CD pipelines | cv.md — Core Skills / DevOps | "GitHub Actions", "GitLab CI/CD" | ✅ Fuerte |
| Observabilidad y monitoreo | cv.md — Core Skills / Observability | "Prometheus", "Grafana", "Zabbix" | ✅ Fuerte |
| Networking (VPC, Route53, load balancers) | cv.md — Core Skills / Cloud + Infrastructure | VPC, Route53, Nginx incluidos | ✅ Fuerte |
| Diseño de arquitecturas cloud end-to-end | cv.md — Experience (inferred) | Operacional, no explícitamente arquitectónico | ⚠️ Parcial |
| Seguridad cloud (IAM, compliance) | cv.md — Core Skills / Cloud + Estudiantes CTO exp | IAM incluido; cybersecurity gestionado en EDLP | ⚠️ Parcial |
| Dominio fintech / pagos / PCI-DSS | cv.md — No hay experiencia fintech | — | ❌ Gap |
| AWS Professional Certification (SA Pro) | cv.md — Certifications | "AWS Solutions Architect Associate" únicamente | ⚠️ Parcial |
| Documentación de arquitectura y ADRs | cv.md — No evidencia explícita | — | ⚠️ Parcial |
| Comunicación técnica en inglés | cv.md — Languages | "Intermediate (B1-B2)" | ⚠️ Parcial |

### Gaps y mitigación

| Gap | ¿Hard blocker? | Experiencia adyacente | Plan de mitigación |
|-----|---------------|----------------------|-------------------|
| Fintech/payments domain | Soft blocker (para esta empresa, mayor riesgo) | Operaciones complejas en entornos regulados (Mercedes-Benz, EDLP) | Enmarcar experiencia en compliance, vendor governance, y entornos de alta responsabilidad |
| AWS SA Professional | Nice-to-have typical | Associate + experiencia práctica en producción | Mencionar plan de certificación; usar experiencia real como compensador |
| Experiencia de arquitectura pura | Soft blocker | Diseño de plataforma en Seeker y EDLP (infraestructura desde cero) | Reposicionar experiencia operacional como "arquitectura emergente desde la práctica" |
| Inglés avanzado (España puede requerir B2+) | Depende del equipo | Español nativo → ventaja en empresa de origen latinoamericano | Confirmar idioma de trabajo antes de aplicar |
| Location (España, posiblemente on-site) | Hard blocker si no es fully remote | Preferencia declarada remote LATAM/worldwide | Solo aplicar si se confirma remote desde Argentina |

---

## C) Nivel y Estrategia

**Nivel detectado en JD:** Senior / Lead (Cloud Architect en fintech NASDAQ suele requerir 5-8 años con foco en arquitectura, no solo operaciones).

**Nivel natural de Federico:** Senior IC con fuerte componente de liderazgo (CTO, Technology Manager) y profundidad operacional en AWS. Competitivo para el nivel técnico, pero con énfasis en gestión y operaciones más que en diseño de arquitecturas formales.

**Riesgo de nivel:**
- Si el rol busca un IC puro con foco en documentar architectures, definir estándares, y liderar decisiones de diseño sin gestión directa de equipos → Federico está levemente por encima en scope de liderazgo, lo que puede ser un desfasaje.
- Si el rol busca alguien que combine profundidad técnica con liderazgo de equipo o práctica → Federico encaja mejor.

**Plan "vender Cloud Architect sin inflar":**
- Enfatizar decisiones de arquitectura reales tomadas en Seeker Parking y Estudiantes de La Plata (selección de servicios AWS, diseño de redes, adoption de IaC, observability stack)
- Posicionar experiencia CTO/Technology Manager como "arquitectura bajo presión real" — no teoría, sino decisiones de diseño con consecuencias de producción
- Usar AWS Solutions Architect Associate como señal de conocimiento formal, con plan explícito de Professional

**Plan "si bajan nivel a Senior Cloud Engineer":**
- Aceptar si comp es justa (≥ $4,000/mes) y scope técnico es sólido
- Pedir revisión de título + comp a 6 meses con criterios claros (delivery de arquitecturas clave, reducción de deuda técnica)

---

## D) Comp y Demanda

**Datos de mercado para Cloud Architect en España:**

| Fuente | Rango | Notas |
|--------|-------|-------|
| Glassdoor (España, 2026) | €43K–€65K/año | Percentil 25–75 |
| ERIeri / SalaryExpert (España, 2026) | €53K–€91K/año | Media: €75K/año |
| Jobicy (España, Cloud Architect) | $62K–$188K/año | Alta varianza por seniority |
| dLocal (Levels.fyi — Solution Architect España) | hasta $103K/año | Dato anecdótico único |
| dLocal Glassdoor feedback | "Salary below market average" | 10 de 138 reviews lo mencionan explícitamente |

**Para Federico:**
- Target mensual: $4,000–$6,000/mes USD
- Equivalente anual: ~$48K–$72K USD / año
- Mercado España para este rol: ~€53K–€91K/año ≈ ~$58K–$100K USD/año
- Si dLocal paga por debajo de mercado y Federico recibe paquete para Argentina (no para España), podría estar en el rango inferior

**Score de comp:** 2.5/5
- dLocal tiene reputación de pagar por debajo de mercado
- Federico podría recibir un paquete LATAM, no español
- Sin datos concretos de la oferta (JD 403)

**Tendencia de demanda para Cloud Architect:**
- Demanda alta y sostenida en 2025–2026 en el sector fintech
- dLocal activamente contratando en España (~40 roles en Glassdoor España a febrero 2026)
- No hay señales de freeze ni layoffs recientes para dLocal en los resultados disponibles

---

## E) Plan de Personalización

*(Relevante solo si el rol reaparece con URL activa y política remote-LATAM confirmada)*

| # | Sección | Estado actual | Cambio propuesto | Por qué |
|---|---------|---------------|------------------|---------|
| 1 | Professional Summary | Genérico: "technology leader and cloud infrastructure professional" | Insertar: "Cloud Architect with hands-on AWS production depth across EC2, VPC, Terraform, Kubernetes, and observability stacks — driving platform reliability and infrastructure scalability in complex multi-product environments" | Alinear framing al título exacto del rol |
| 2 | Skills / Cloud | Lista plana | Reagrupar en: Architecture (AWS SA patterns, VPC design, multi-AZ), IaC (Terraform), Containers (Kubernetes, Docker), Observability, Security | Cloud Architect exige categorización arquitectónica, no solo enumeración |
| 3 | Seeker Parking bullet top | Genérico: "Leading technology initiatives" | Reescribir: "Architecting multi-product cloud platform on AWS — designing VPC topology, Terraform module strategy, Kubernetes workload orchestration, and CI/CD delivery pipelines from scratch" | Inyectar vocabulario de arquitectura con ownership real |
| 4 | Estudiantes de La Plata | Enfocado en gestión | Añadir bullet: "Designed and operationalized AWS production environments for large-scale user-facing services — VPC architecture, IAM governance, RDS multi-AZ, observability stack, and CloudTrail audit trails" | Demostrar decisiones de arquitectura con impacto |
| 5 | Certifications | "AWS Solutions Architect Associate + Cloud Practitioner" | Añadir: "AWS Solutions Architect Professional — in progress" | Señalizar evolución hacia nivel Professional |

**Top 5 cambios LinkedIn:**
1. Headline: "Cloud Architect | AWS • Terraform • Kubernetes | Infrastructure reliability & platform design"
2. About: Párrafo que mencione explícitamente "cloud architecture decisions", "IaC strategy", y "production-grade AWS platform design"
3. Skills sección: Priorizar "Cloud Architecture", "AWS Solutions Architect", "Terraform", "Kubernetes", "Platform Engineering"
4. Seeker Parking experience: Añadir "Architecting" en el primer bullet visible
5. Featured: Agregar enlace a GitHub o portfolio si existe; si no, añadir AWS SA Associate como featured certification

---

## F) Plan de Entrevistas

*(Adaptado al arquetipo Cloud Architect — énfasis en decisiones de arquitectura, trade-offs técnicos, y ownership de plataforma)*

| # | Requisito del JD (inferido) | Historia STAR | S | T | A | R |
|---|-----------------------------|---------------|---|---|---|---|
| 1 | Diseño de arquitectura AWS desde cero | Seeker Parking — arquitectura de plataforma multi-producto | Startup de parkings sin infraestructura cloud definida | Diseñar y desplegar plataforma AWS para múltiples productos | Definí VPC, subnets, IAM roles, selección de servicios (EC2, RDS, S3, Lambda, API GW), Terraform modules, K8s cluster, GitLab CI/CD pipelines | Plataforma operativa en producción; equipo puede operar y escalar sin intervención ad-hoc |
| 2 | Reliability y observability en producción | EDLP — observabilidad para operaciones a gran escala | Organización con decenas de miles de usuarios sin stack de monitoreo unificado | Implementar observabilidad end-to-end para cloud, apps, y soporte | Desplegué Prometheus + Grafana para métricas de infraestructura; Zabbix para alertas; CloudWatch para AWS; definí SLIs y alertas de producción | Visibilidad completa de producción; reducción de tiempo de detección de incidentes |
| 3 | IaC y estandarización de infraestructura | Migración y modernización con Terraform | Entornos provisioned manualmente, sin reproducibilidad | Migrar a IaC para reducir drift y habilitar consistencia entre envs | Diseñé módulos Terraform para networking, compute, y bases de datos; pipeline de CI/CD para plan/apply; documenté convenciones | Infraestructura reproducible; onboarding más rápido de nuevos entornos; fewer configuration drift incidents |
| 4 | Seguridad y governance en AWS | EDLP — cybersecurity y AWS governance como CTO | Entorno sin IAM granular ni auditoría formal | Implementar governance de IAM y auditoría en entornos cloud | Definí políticas IAM por rol, habilitamos CloudTrail, revisé grupos de seguridad, coordiné con proveedores de cybersecurity | Entorno auditado; alineación con requisitos de compliance organizacional |
| 5 | Coordinación de decisiones técnicas con múltiples stakeholders | Mercedes-Benz — coordinación de proyectos de integración | Proyectos enterprise con múltiples vendors y sistemas SAP | Gestionar decisión técnica de migración/integración con stakeholders cruzados | Facilité workshops de requirements, alineé equipo técnico con consultoras externas, documenté decisiones y criterios de aceptación | Proyecto ejecutado dentro de scope; stakeholders alineados en criterios técnicos |
| 6 | Selección de tecnología y trade-off de plataforma | Seeker Parking — decisión K8s vs ECS vs serverless | Plataforma nueva, múltiples opciones de orquestación | Elegir el stack de contenedores correcto para el equipo y el presupuesto | Evalué ECS Fargate (managed, costo), K8s en EC2 (control, complejidad), serverless Lambda (costo, limitaciones); elegí K8s con plan de abstracción gradual | Equipo adoptó K8s con curva de aprendizaje manejable; decisión documentada para futuros ingenieros |

**Case study recomendado:** Plataforma cloud de Seeker Parking — narrar el proceso completo de diseño e implementación como "greenfield cloud architecture project": desde la selección de región AWS, diseño de VPC, decisiones de orquestación, IaC strategy, hasta el modelo de operaciones (observability + CI/CD + on-call).

**Preguntas red-flag y respuestas:**
- *"¿Tenés experiencia en pagos o PCI-DSS?"* → "No tengo experiencia directa en fintech ni PCI-DSS, pero he gestionado entornos con requerimientos de compliance, auditoría de IAM, y CloudTrail en entornos regulated. Estoy activamente aprendiendo sobre el espacio de pagos y entiendo que hay curva de aprendizaje en el dominio."
- *"¿Cómo trabajarías con un equipo basado en España si estás en Argentina?"* → "He coordinado con equipos distribuidos y proveedores internacionales en roles anteriores. La diferencia horaria España-Argentina es de 4-5hs, lo que permite un overlap operativo sólido. Trabajo en remoto con alta autonomía y comunicación asíncrona efectiva."
- *"¿Tenés experiencia diseñando arquitecturas para alta disponibilidad en pagos?"* → Reposicionar: "He diseñado entornos AWS multi-AZ con RDS y EC2 Auto Scaling en producción real. El pattern de alta disponibilidad es trasladable; el dominio de pagos es lo que tendría que profundizar."

---

## G) Posting Legitimacy

**Assessment: Suspicious**

| Señal | Valor | Confianza |
|-------|-------|-----------|
| URL responde con contenido de JD | ❌ HTTP 403 Forbidden | Verificado |
| Tiempo desde indexación en scan-history | 2026-06-10 → 2026-06-12 (2 días con 403) | Verificado |
| Patrón previo en dLocal | Head of Platform Engineering (diferente URL) también retornó 403 el 2026-06-10 | Verificado |
| Empresa activa contratando | ✅ dLocal tiene ~40 roles en España según Glassdoor España (Feb 2026) | Verificado (web search) |
| Reposting / duplicado | No hay duplicado en applications.md para este URL específico | Verificado |
| Calidad de la descripción | ❌ No recuperable | No disponible |
| Señales de freeze/layoff | No hay noticias de freeze en resultados disponibles | Baja confianza |

**Context Notes:**
- La oferta fue indexada el 2026-06-10 mediante la API de Lever. Lever a veces retorna 403 cuando una oferta está activa pero geo-restricted, o cuando fue cerrada recientemente. El hecho de que el otro rol de dLocal también retorne 403 sugiere que podría ser una restricción de geo-bloqueo (Argentina → España) más que cierre definitivo.
- dLocal como empresa es legítima y activamente contratante. El problema es la accesibilidad del posting específico, no la empresa.
- Acción recomendada: Verificar en jobs.lever.co/dlocal directamente desde un browser con VPN en España (o preguntarle a alguien con IP española) si el rol está activo. Si está activo, re-evaluar con JD completo.

---

## Score Global

| Dimensión | Score |
|-----------|-------|
| Match con CV | 3.5/5 |
| Alineación North Star | 2.5/5 |
| Comp | 2.5/5 |
| Señales culturales | 2.5/5 |
| Red flags | -0.4 (403 persistente + location mismatch) |
| **Global** | **2.6/5** |

**Decisión final: Skip**

Razones en orden de peso:
1. Posting probablemente cerrado o geo-bloqueado (403 persiste 2 días)
2. Ubicación España — fuera de la geografía preferida; si es on-site, es un hard blocker desde Argentina
3. Cloud Architect es arquetipo secundario para Federico (primary: DevOps/Cloud/SRE IC o Leadership/Management)
4. No hay fintech domain experience
5. Sin JD completo no se puede hacer una evaluación de calidad para aplicar

**Si el rol reaparece con URL activa:** Re-evaluar con JD completo. Si el rol es fully remote y el scope es AWS cloud architecture hands-on, el match técnico justificaría un 3.5+ y potencial aplicación.

---

## Keywords extraídas

*(inferidas de normas de industria para Cloud Architect en fintech — no del JD directamente)*

cloud architecture, AWS, infrastructure as code, Terraform, Kubernetes, Docker, VPC design, IAM governance, CI/CD, observability, Prometheus, Grafana, multi-AZ, high availability, cost optimization, platform engineering, security compliance, networking, cloud operations, fintech infrastructure
