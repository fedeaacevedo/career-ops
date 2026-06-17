#!/usr/bin/env node

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';

const DATE = new Date().toISOString().slice(0, 10);
const OUT_DIR = 'output';
const OUT_PATH = `${OUT_DIR}/ofertas-tecnologia-argentina-multiportal-${DATE}.xls`;
const PIPELINE_PATH = 'data/pipeline.md';

const getOnBoardQueries = [
  'devops',
  'cloud',
  'project manager',
  'it manager',
  'infraestructura',
  'product owner',
  'analista funcional',
  'sistemas',
];

const remotiveQueries = [
  'devops',
  'cloud',
  'project manager',
  'product owner',
  'systems',
  'infrastructure',
];

const allowTerms = [
  'devops',
  'cloud',
  'aws',
  'infrastructure',
  'infraestructura',
  'project manager',
  'technical project manager',
  'it manager',
  'gerente',
  'jefe',
  'lead',
  'product owner',
  'analista funcional',
  'sistemas',
  'sysadmin',
  'security',
  'seguridad',
  'support engineer',
  'soporte',
  'platform',
];

const blockTerms = [
  'sales',
  'account executive',
  'business development',
  'marketing',
  'recruiter',
  'talent acquisition',
  'customer success',
  'comercial',
  'vendedor',
  'trainee',
  'intern',
  'pasante',
];

const priorityRules = [
  ['Gerencia/Liderazgo', 100, ['gerente', 'it manager', 'jefe', 'lead', 'manager']],
  ['Cloud/DevOps', 90, ['devops', 'cloud', 'aws', 'platform']],
  ['Infraestructura/Sistemas', 80, ['infraestructura', 'infrastructure', 'sistemas', 'sysadmin']],
  ['PM/Delivery IT', 70, ['project manager', 'technical project manager', 'pmo']],
  ['Producto Tech', 60, ['product owner']],
  ['Funcional/ERP', 55, ['analista funcional', 'erp', 'crm']],
  ['Soporte IT', 40, ['soporte', 'support engineer']],
];

function decodeHtml(value) {
  return String(value || '')
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/\s+/g, ' ')
    .trim();
}

function escapeHtml(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function stripTags(value) {
  return decodeHtml(String(value || '').replace(/<[^>]*>/g, ' '));
}

function normalize(value) {
  return String(value || '')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();
}

function passes(job) {
  const text = normalize(`${job.title} ${job.company} ${job.category}`);
  return allowTerms.some((term) => text.includes(normalize(term)))
    && !blockTerms.some((term) => text.includes(normalize(term)));
}

function classify(job) {
  const text = normalize(`${job.title} ${job.company} ${job.category}`);
  for (const [category, score, terms] of priorityRules) {
    if (terms.some((term) => text.includes(normalize(term)))) return { category, score };
  }
  return { category: 'Tecnologia', score: 30 };
}

function parseGetOnBoard(html, sourceQuery) {
  const cards = html.split('class="results-item').slice(1);
  const jobs = [];
  for (const card of cards) {
    const urlMatch = card.match(/href="([^"]+)"/i);
    const titleMatch = card.match(/<h4 class="results-list-title">([\s\S]*?)<\/h4>/i);
    const companyMatch = card.match(/class="gb-results-list__company">([\s\S]*?)<\/span>/i)
      || card.match(/class="opacity-half">([\s\S]*?)<\/span>/i);
    const summaryMatch = card.match(/title="([^"]+)"/i);
    const rawUrl = urlMatch ? decodeHtml(urlMatch[1]) : '';
    const url = rawUrl.startsWith('http') ? rawUrl : `https://www.getonbrd.com${rawUrl}`;
    const title = titleMatch ? stripTags(titleMatch[1]).replace(/\s+Full time.*$/i, '') : '';
    const company = companyMatch ? stripTags(companyMatch[1]) : 'Get on Board';
    const summary = summaryMatch ? decodeHtml(summaryMatch[1]) : '';
    if (!url || !title) continue;
    jobs.push({
      portal: 'Get on Board',
      company,
      title,
      location: 'Remote/LATAM or Argentina eligible',
      category: 'Tecnologia',
      url,
      sourceQuery,
      summary,
    });
  }
  return jobs;
}

async function fetchGetOnBoard() {
  const out = [];
  for (const query of getOnBoardQueries) {
    const url = new URL('https://www.getonbrd.com/empleos');
    url.searchParams.set('query', query);
    url.searchParams.set('country', 'Argentina');
    const res = await fetch(url, { headers: { 'user-agent': 'Mozilla/5.0 career-ops' } });
    if (!res.ok) continue;
    out.push(...parseGetOnBoard(await res.text(), query));
  }
  return out;
}

async function fetchRemotive() {
  const out = [];
  for (const query of remotiveQueries) {
    const url = new URL('https://remotive.com/api/remote-jobs');
    url.searchParams.set('search', query);
    const res = await fetch(url, { headers: { 'user-agent': 'career-ops job search' } });
    if (!res.ok) continue;
    const data = await res.json();
    for (const job of data.jobs || []) {
      out.push({
        portal: 'Remotive',
        company: job.company_name || '',
        title: job.title || '',
        location: job.candidate_required_location || 'Remote',
        category: job.category || '',
        url: job.url || '',
        sourceQuery: query,
        summary: stripTags(job.description || '').slice(0, 220),
      });
    }
  }
  return out;
}

function pipelineJobs() {
  if (!existsSync(PIPELINE_PATH)) return [];
  return readFileSync(PIPELINE_PATH, 'utf8')
    .split('\n')
    .filter((line) => line.startsWith('- [ ] '))
    .map((line) => {
      const cols = line.replace(/^- \[ \] /, '').split('|').map((part) => part.trim());
      const [url, company, title] = cols;
      let portal = 'Pipeline';
      if (url.includes('computrabajo')) portal = 'Computrabajo';
      if (url.includes('linkedin')) portal = 'LinkedIn';
      if (url.includes('greenhouse') || url.includes('ashbyhq') || url.includes('lever.co')) portal = 'ATS directo';
      return {
        portal,
        company,
        title,
        location: 'Ver oferta',
        category: 'Tecnologia',
        url,
        sourceQuery: 'pipeline',
        summary: '',
      };
    });
}

function htmlWorkbook(rows) {
  const body = rows.map((job, idx) => `
    <tr>
      <td>${idx + 1}</td>
      <td>${escapeHtml(job.portal)}</td>
      <td>${escapeHtml(job.category)}</td>
      <td>${escapeHtml(job.company)}</td>
      <td>${escapeHtml(job.title)}</td>
      <td>${escapeHtml(job.location)}</td>
      <td>${escapeHtml(job.sourceQuery)}</td>
      <td><a href="${escapeHtml(job.url)}">${escapeHtml(job.url)}</a></td>
      <td>${escapeHtml(job.summary)}</td>
    </tr>`).join('\n');

  return `<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    table { border-collapse: collapse; font-family: Arial, sans-serif; font-size: 12px; }
    th { background: #1f4e78; color: white; font-weight: bold; }
    th, td { border: 1px solid #d0d7de; padding: 6px 8px; vertical-align: top; }
  </style>
</head>
<body>
  <table>
    <thead>
      <tr>
        <th>#</th>
        <th>Portal</th>
        <th>Categoria</th>
        <th>Empresa</th>
        <th>Rol</th>
        <th>Ubicacion</th>
        <th>Busqueda</th>
        <th>URL</th>
        <th>Resumen</th>
      </tr>
    </thead>
    <tbody>
${body}
    </tbody>
  </table>
</body>
</html>
`;
}

async function main() {
  const raw = [
    ...pipelineJobs(),
    ...await fetchGetOnBoard(),
    ...await fetchRemotive(),
  ].filter((job) => job.url && job.title && passes(job));

  const byUrl = new Map();
  for (const job of raw) {
    if (!byUrl.has(job.url)) {
      const cls = classify(job);
      byUrl.set(job.url, { ...job, ...cls });
    }
  }

  const rows = [...byUrl.values()]
    .sort((a, b) => b.score - a.score || a.portal.localeCompare(b.portal) || a.company.localeCompare(b.company))
    .slice(0, 80);

  mkdirSync(OUT_DIR, { recursive: true });
  writeFileSync(OUT_PATH, htmlWorkbook(rows));

  console.log(`Multiportal export — ${DATE}`);
  console.log(`Raw candidates: ${raw.length}`);
  console.log(`Unique: ${byUrl.size}`);
  console.log(`Exported: ${rows.length}`);
  console.log(`File: ${OUT_PATH}`);
  const portals = rows.reduce((acc, job) => {
    acc[job.portal] = (acc[job.portal] || 0) + 1;
    return acc;
  }, {});
  console.log(`Portals: ${Object.entries(portals).map(([k, v]) => `${k}=${v}`).join(', ')}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
