# Career Ops Automation

Daily automation layer for Federico Acevedo's Career Ops workflow. It is isolated under `automation/` and starts in `DRY_RUN=true`.

## Commands

```bash
python3 automation/run_daily.py
python3 automation/email_sender.py --dry-run
python3 automation/scorer.py --test
python3 -m py_compile automation/*.py
```

## What It Does

- Runs `npm run scan` and keeps going if scanning fails.
- Reads `data/pipeline.md`.
- Ignores checked, skipped, and expired pipeline rows.
- Scores pending offers from 0 to 100.
- Penalizes advanced English and bad geography.
- Generates daily Markdown and JSON reports in `automation/reports/`.
- Generates fully tailored artifacts per JD in `automation/generated/YYYY-MM-DD/company-title/`:
  - `cv.md` (full rewrite, not just summary)
  - `cv.pdf` (rendered from template)
  - `cover_letter.md` (JD-specific)
  - `email.txt` (short, professional)
  - `metadata.json` (JD analysis JSON + match metrics + missing skills)
- Tracks jobs, generated documents, and email sends in SQLite at `automation/data/applications.db`.
- Uses Gmail SMTP only when explicitly configured and `DRY_RUN=false`.

## Configuration

Edit `automation/config/settings.yml` for scoring thresholds, keywords, locations, and categories.

Copy `automation/config/.env.example` to `automation/config/.env` if you want to configure Gmail:

```bash
GMAIL_USER=your.email@gmail.com
GMAIL_APP_PASSWORD=your-app-password
EMAIL_FROM_NAME=Federico Acevedo
DRY_RUN=true
DAILY_EMAIL_LIMIT=10
```

Do not store real passwords in source control.

## Safety

The sender never submits applications or fills forms. In dry-run mode it prints what it would send and records that dry run in `automation/sent/sent_emails.log` so duplicates are avoided by URL.
