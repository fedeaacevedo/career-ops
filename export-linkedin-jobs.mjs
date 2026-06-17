#!/usr/bin/env node

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';

const DATE = new Date().toISOString().slice(0, 10);
const OUT_DIR = 'output';
const OUT_PATH = `${OUT_DIR}/ofertas-tecnologia-argentina-linkedin-${DATE}.xls`;

const queries = [
  'IT Manager',
  'Gerente de Sistemas',
  'Jefe de Infraestructura',
  'Cloud Infrastructure Lead',
  'DevOps',
  'Cloud Engineer',
  'Project Manager IT',
  'Technical Project Manager',
  'Analista Funcional',
  'Analista de Sistemas',
  'Infraestructura',
  'Soporte IT',
  'Product Owner',
  'Security Engineer',
  'Administrador de Sistemas',
];

const starts = [0, 10, 20, 30, 40, 50];

const titleAllow = [
  'devops',
  'cloud',
  'project manager',
  'technical project manager',
  'analista funcional',
  'analista de sistemas',
  'soporte it',
  'infraestructura',
  'product owner',
  'gerente de sistemas',
  'jefe de sistemas',
  'jefe de infraestructura',
  'it manager',
  'sistemas',
  'security',
  'seguridad',
  'administrador de sistemas',
  'sysadmin',
];

const titleBlock = [
  'sales',
  'account executive',
  'business development',
  'marketing',
  'recruiter',
  'talent acquisition',
  'customer success',
  'comercial',
  'vendedor',
  'pasante',
  'trainee',
];

const priorityTerms = [
  ['Gerencia/Liderazgo', 100, ['gerente de sistemas', 'it manager', 'jefe de infraestructura', 'cloud infrastructure lead', 'coordinador de infraestructura']],
  ['Cloud/DevOps', 90, ['devops', 'cloud engineer', 'aws cloud', 'cloud administrator', 'infrastructure consulting cloud']],
  ['Infraestructura/Sistemas', 80, ['infraestructura', 'administrador de sistemas', 'analista de infraestructura', 'sistemas']],
  ['PM/Delivery IT', 70, ['project manager it', 'technical project manager', 'senior project manager', 'pmo']],
  ['Funcional/ERP', 60, ['analista funcional', 'erp', 'crm']],
  ['Producto Tech', 50, ['product owner']],
  ['Soporte IT', 40, ['soporte it', 'field support']],
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

function canonicalUrl(url) {
  return decodeHtml(url).split('?')[0];
}

function normalize(value) {
  return String(value || '')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();
}

function parseCards(html, sourceQuery) {
  const cards = html.split(/<li>/i).slice(1);
  const out = [];

  for (const card of cards) {
    const urlMatch = card.match(/href="([^"]*\/jobs\/view\/[^"]+)"/i);
    const titleMatch = card.match(/base-search-card__title[^>]*>([\s\S]*?)<\/h3>/i);
    const companyMatch = card.match(/base-search-card__subtitle[^>]*>([\s\S]*?)<\/h4>/i);
    const locationMatch = card.match(/job-search-card__location[^>]*>([\s\S]*?)<\/span>/i);
    const postedMatch = card.match(/job-search-card__listdate[^>]* datetime="([^"]+)"/i)
      || card.match(/job-search-card__listdate--new[^>]* datetime="([^"]+)"/i);

    const url = urlMatch ? canonicalUrl(urlMatch[1]) : '';
    const title = titleMatch ? stripTags(titleMatch[1]) : '';
    const company = companyMatch ? stripTags(companyMatch[1]) : 'LinkedIn';
    const location = locationMatch ? stripTags(locationMatch[1]) : 'Argentina';
    const posted = postedMatch ? postedMatch[1] : '';

    if (!url || !title) continue;

    const nTitle = normalize(title);
    if (!titleAllow.some((term) => nTitle.includes(normalize(term)))) continue;
    if (titleBlock.some((term) => nTitle.includes(normalize(term)))) continue;

    out.push({ url, title, company, location, posted, sourceQuery });
  }

  return out;
}

function classify(job) {
  const title = normalize(`${job.title} ${job.company}`);
  for (const [category, baseScore, terms] of priorityTerms) {
    if (terms.some((term) => title.includes(normalize(term)))) {
      return { category, score: baseScore };
    }
  }
  return { category: 'Tecnologia', score: 30 };
}

async function fetchQuery(query, start) {
  const url = new URL('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search');
  url.searchParams.set('keywords', query);
  url.searchParams.set('location', 'Argentina');
  url.searchParams.set('start', String(start));

  const res = await fetch(url, {
    headers: {
      'user-agent': 'Mozilla/5.0 career-ops public jobs export',
      accept: 'text/html',
    },
  });
  if (!res.ok) throw new Error(`${query} start=${start}: HTTP ${res.status}`);

  return parseCards(await res.text(), query);
}

function htmlWorkbook(rows) {
  const body = rows.map((job, idx) => `
    <tr>
      <td>${idx + 1}</td>
      <td>${escapeHtml(job.category)}</td>
      <td>${escapeHtml(job.company)}</td>
      <td>${escapeHtml(job.title)}</td>
      <td>${escapeHtml(job.location)}</td>
      <td>${escapeHtml(job.posted)}</td>
      <td>${escapeHtml(job.sourceQuery)}</td>
      <td><a href="${escapeHtml(job.url)}">${escapeHtml(job.url)}</a></td>
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
        <th>Categoria</th>
        <th>Empresa</th>
        <th>Rol</th>
        <th>Ubicacion</th>
        <th>Publicado</th>
        <th>Busqueda</th>
        <th>URL</th>
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
  const found = [];
  const errors = [];

  for (const query of queries) {
    for (const start of starts) {
      try {
        found.push(...await fetchQuery(query, start));
      } catch (err) {
        errors.push(err.message);
      }
    }
  }

  const byUrl = new Map();
  for (const job of found) {
    if (!byUrl.has(job.url)) {
      const cls = classify(job);
      byUrl.set(job.url, { ...job, ...cls });
    }
  }

  const rows = [...byUrl.values()]
    .sort((a, b) => b.score - a.score || a.company.localeCompare(b.company) || a.title.localeCompare(b.title))
    .slice(0, 50);

  mkdirSync(OUT_DIR, { recursive: true });
  writeFileSync(OUT_PATH, htmlWorkbook(rows));

  console.log(`LinkedIn export — ${DATE}`);
  console.log(`Queries: ${queries.length}`);
  console.log(`Pages per query: ${starts.length}`);
  console.log(`Found raw: ${found.length}`);
  console.log(`Unique filtered: ${byUrl.size}`);
  console.log(`Exported: ${rows.length}`);
  console.log(`File: ${OUT_PATH}`);

  if (errors.length) {
    console.log('\nErrors:');
    for (const err of errors.slice(0, 10)) console.log(`- ${err}`);
    if (errors.length > 10) console.log(`- ... ${errors.length - 10} more`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
