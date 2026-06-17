#!/usr/bin/env node

import { appendFileSync, existsSync, readFileSync, writeFileSync } from 'fs';

const DATE = new Date().toISOString().slice(0, 10);
const PIPELINE_PATH = 'data/pipeline.md';
const APPLICATIONS_PATH = existsSync('data/applications.md') ? 'data/applications.md' : 'applications.md';
const HISTORY_PATH = 'data/scan-history.tsv';

const queries = [
  'DevOps',
  'Cloud Engineer',
  'Project Manager IT',
  'Analista Funcional',
  'Analista de Sistemas',
  'Soporte IT',
  'Infraestructura',
  'Product Owner',
  'Gerente de Sistemas',
  'IT Manager',
];

const titleAllow = [
  'devops',
  'cloud',
  'project manager',
  'analista funcional',
  'analista de sistemas',
  'soporte it',
  'infraestructura',
  'product owner',
  'gerente de sistemas',
  'jefe de sistemas',
  'it manager',
  'sistemas',
  'security',
  'seguridad',
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

function seenSources() {
  const chunks = [];
  for (const file of [PIPELINE_PATH, APPLICATIONS_PATH, HISTORY_PATH]) {
    if (existsSync(file)) chunks.push(readFileSync(file, 'utf8'));
  }
  return chunks.join('\n');
}

function parseCards(html, queryName) {
  const cards = html.split(/<li>/i).slice(1);
  const out = [];

  for (const card of cards) {
    const urlMatch = card.match(/href="([^"]*\/jobs\/view\/[^"]+)"/i);
    const titleMatch = card.match(/base-search-card__title[^>]*>([\s\S]*?)<\/h3>/i);
    const companyMatch = card.match(/base-search-card__subtitle[^>]*>([\s\S]*?)<\/h4>/i);
    const locationMatch = card.match(/job-search-card__location[^>]*>([\s\S]*?)<\/span>/i);

    const url = urlMatch ? canonicalUrl(urlMatch[1]) : '';
    const title = titleMatch ? stripTags(titleMatch[1]) : '';
    const company = companyMatch ? stripTags(companyMatch[1]) : 'LinkedIn';
    const location = locationMatch ? stripTags(locationMatch[1]) : 'Argentina';

    if (!url || !title) continue;

    const nTitle = normalize(title);
    if (!titleAllow.some((term) => nTitle.includes(normalize(term)))) continue;
    if (titleBlock.some((term) => nTitle.includes(normalize(term)))) continue;

    out.push({ url, title, company, location, queryName });
  }

  return out;
}

async function fetchQuery(query) {
  const url = new URL('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search');
  url.searchParams.set('keywords', query);
  url.searchParams.set('location', 'Argentina');
  url.searchParams.set('start', '0');

  const res = await fetch(url, {
    headers: {
      'user-agent': 'Mozilla/5.0 career-ops public jobs scanner',
      accept: 'text/html',
    },
  });

  if (!res.ok) throw new Error(`${query}: HTTP ${res.status}`);
  return parseCards(await res.text(), `linkedin-public:${query}`);
}

async function main() {
  const seen = seenSources();
  const found = [];
  const errors = [];

  for (const query of queries) {
    try {
      found.push(...await fetchQuery(query));
    } catch (err) {
      errors.push(err.message);
    }
  }

  const byUrl = new Map();
  for (const job of found) {
    if (!byUrl.has(job.url)) byUrl.set(job.url, job);
  }

  const added = [];
  const skippedDup = [];
  const pipelineLines = [];
  const historyLines = [];
  for (const job of byUrl.values()) {
    if (seen.includes(job.url)) {
      skippedDup.push(job);
      continue;
    }

    pipelineLines.push(`- [ ] ${job.url} | ${job.company} | ${job.title}`);
    historyLines.push(`${job.url}\t${DATE}\t${job.queryName}\t${job.title}\t${job.company}\tadded\t${job.location}`);
    added.push(job);
  }

  if (pipelineLines.length) {
    const pipeline = readFileSync(PIPELINE_PATH, 'utf8');
    const marker = '\n## Procesadas';
    const insert = `${pipelineLines.join('\n')}\n`;
    const next = pipeline.includes(marker)
      ? pipeline.replace(marker, `\n${insert}${marker}`)
      : `${pipeline.replace(/\s*$/, '')}\n${insert}`;
    appendFileSync(HISTORY_PATH, `${historyLines.join('\n')}\n`);
    writeFileSync(PIPELINE_PATH, next);
  }

  console.log(`LinkedIn public scan — ${DATE}`);
  console.log(`Queries: ${queries.length}`);
  console.log(`Found: ${found.length}`);
  console.log(`Unique: ${byUrl.size}`);
  console.log(`Duplicates: ${skippedDup.length}`);
  console.log(`Added: ${added.length}`);
  if (errors.length) {
    console.log('\nErrors:');
    for (const err of errors) console.log(`- ${err}`);
  }
  if (added.length) {
    console.log('\nNew offers:');
    for (const job of added) {
      console.log(`+ ${job.company} | ${job.title} | ${job.location} | ${job.url}`);
    }
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
