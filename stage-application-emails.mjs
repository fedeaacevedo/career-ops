#!/usr/bin/env node

/**
 * stage-application-emails.mjs
 *
 * Creates reviewable application email drafts for high-fit evaluated roles.
 * This script intentionally does not send email. career-ops is human-in-the-loop:
 * the candidate reviews and sends the final application.
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const PROFILE_PATH = 'config/profile.yml';
const APPLICATIONS_PATH = existsSync('data/applications.md') ? 'data/applications.md' : 'applications.md';

function slugify(value) {
  return String(value || '')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80);
}

function parseScore(score) {
  const match = String(score || '').match(/(\d+(?:\.\d+)?)\s*\/\s*5/);
  return match ? Number(match[1]) : 0;
}

function parseApplications(markdown) {
  return markdown
    .split('\n')
    .filter((line) => line.startsWith('| ') && !line.includes('---'))
    .slice(1)
    .map((line) => {
      const cols = line.split('|').slice(1, -1).map((c) => c.trim());
      const [num, date, company, role, score, status, pdf, report, notes] = cols;
      const reportMatch = report?.match(/\]\(([^)]+)\)/);
      return {
        num,
        date,
        company,
        role,
        score,
        scoreValue: parseScore(score),
        status,
        pdf,
        reportPath: reportMatch ? reportMatch[1].replace(/^\.\.\//, '') : '',
        notes: notes || '',
      };
    })
    .filter((entry) => entry.num && entry.company && entry.role);
}

function extractReportHeader(reportText) {
  const get = (label) => {
    const match = reportText.match(new RegExp(`^\\*\\*${label}:\\*\\*\\s*(.*)$`, 'mi'));
    return match ? match[1].trim() : '';
  };
  return {
    url: get('URL'),
    pdf: get('PDF'),
    score: get('Score'),
  };
}

function findContactEmail(...texts) {
  const joined = texts.join('\n');
  const emails = joined.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi) || [];
  const own = new Set(['fedeaacevedo@gmail.com']);
  return emails.find((email) => !own.has(email.toLowerCase())) || '';
}

function buildBody({ candidate, entry, reportHeader, contactEmail }) {
  const greeting = contactEmail ? 'Hola,' : 'Hola,';
  return `${greeting}

Me interesa postularme al rol de ${entry.role}. Mi perfil combina liderazgo tecnologico, gestion de sistemas, infraestructura, cloud, seguridad, proveedores y transformacion digital.

Vengo de roles de Technology Manager / CTO y Technology Lead, liderando tecnologia, infraestructura, software delivery, ciberseguridad, soporte, proveedores y operaciones. Tambien trabaje en proyectos empresariales con procesos SAP, migraciones e integraciones, coordinando stakeholders de negocio, equipos tecnicos y consultoras externas.

Creo que puedo aportar valor en un rol donde tecnologia debe conectar objetivos de negocio, continuidad operativa, integracion de sistemas y mejora de procesos.

Adjunto mi CV para que puedan evaluarlo.

Quedo atento para conversar.

${candidate.full_name}
${candidate.email}
${candidate.linkedin || ''}

Referencia de la busqueda: ${reportHeader.url || 'URL no detectada en reporte'}
`;
}

function main() {
  if (!existsSync(PROFILE_PATH)) throw new Error(`Missing ${PROFILE_PATH}`);
  if (!existsSync(APPLICATIONS_PATH)) throw new Error(`Missing ${APPLICATIONS_PATH}`);

  const profile = yaml.load(readFileSync(PROFILE_PATH, 'utf-8'));
  const cfg = profile.application_email || {};

  if (!cfg.enabled) {
    console.log('application_email.enabled=false; nothing to do.');
    return;
  }
  if (cfg.mode !== 'draft_only') {
    throw new Error('Only application_email.mode="draft_only" is supported. Auto-send is intentionally blocked.');
  }

  const threshold = Number(cfg.score_threshold || 4.2);
  const requirePdf = cfg.require_pdf !== false;
  const outDir = cfg.output_dir || 'output/email-drafts';
  mkdirSync(outDir, { recursive: true });

  const apps = parseApplications(readFileSync(APPLICATIONS_PATH, 'utf-8'));
  const eligible = apps.filter((entry) => (
    entry.scoreValue >= threshold &&
    entry.status === 'Evaluated' &&
    (!requirePdf || entry.pdf.includes('✅'))
  ));

  let created = 0;
  for (const entry of eligible) {
    const reportText = entry.reportPath && existsSync(entry.reportPath)
      ? readFileSync(entry.reportPath, 'utf-8')
      : '';
    const reportHeader = extractReportHeader(reportText);
    const contactEmail = findContactEmail(entry.notes, reportText);
    const subject = (cfg.default_subject_template || 'Postulación - {role} - Federico Acevedo')
      .replaceAll('{role}', entry.role)
      .replaceAll('{company}', entry.company);
    const body = buildBody({
      candidate: profile.candidate || {},
      entry,
      reportHeader,
      contactEmail,
    });

    const review = `# Email Draft - #${entry.num} ${entry.company} - ${entry.role}

**Status:** review_required
**Safety:** Draft only. Do not send automatically.
**To:** ${contactEmail || 'PENDING - completar email del recruiter o portal'}
**Subject:** ${subject}
**Attach:** ${reportHeader.pdf || 'PENDING - PDF no detectado en reporte'}
**Application URL:** ${reportHeader.url || 'PENDING'}
**Score:** ${entry.score}

---

${body}
`;

    const file = path.join(outDir, `${String(entry.num).padStart(3, '0')}-${slugify(entry.company)}-${slugify(entry.role)}.md`);
    writeFileSync(file, review);
    created++;
    console.log(`Draft staged: ${file}`);
  }

  console.log(`\nEligible: ${eligible.length}. Drafts staged: ${created}.`);
  if (requirePdf) {
    const skippedHighFit = apps.filter((entry) => (
      entry.scoreValue >= threshold &&
      entry.status === 'Evaluated' &&
      !entry.pdf.includes('✅')
    ));
    if (skippedHighFit.length) {
      console.log('\nHigh-fit roles skipped because PDF is missing:');
      for (const entry of skippedHighFit) {
        console.log(`- #${entry.num} ${entry.company} — ${entry.role} (${entry.score})`);
      }
    }
  }
}

try {
  main();
} catch (err) {
  console.error(`Error: ${err.message}`);
  process.exit(1);
}
