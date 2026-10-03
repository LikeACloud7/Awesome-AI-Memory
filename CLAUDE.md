# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an English-only fork of IAAR-Shanghai/Awesome-AI-Memory, a curated research paper collection covering AI memory and memory systems for large language models. It is not a typical software project — the primary content is research paper metadata stored in HTML tables within README.md.

## Repository Structure

- `README.md` — English paper list, regenerated from upstream's `README_en.md`; do not hand-edit paper entries (the next sync overwrites them)
- `CONTRIBUTING.md` — How the fork syncs, and the upstream workflow for adding papers
- `SCREENING.md` — Paper screening policy (English translation of upstream's)
- `scripts/sync_upstream.py` — Rebuilds README.md and `assets/` from an upstream git ref
- `scripts/update_paper_count.py` — Updates the paper count badge in README.md
- `.github/workflows/sync-upstream.yml` — Daily job: merges upstream with `-s ours`, runs the sync script, commits and pushes
- `assets/` — Images and resources (copied from upstream)

## Fork Rules

- Keep the repository English-only. Do not bring back upstream's Chinese files (`README_cn.md`, `README_en.md`, `screening/`, `scripts/check_screening.py`, `tests/`).
- Never merge upstream normally or use GitHub's "Sync fork" button: upstream's README.md is Chinese. Sync only through the workflow or `scripts/sync_upstream.py`.

## Paper Format

Papers are stored as HTML `<tr>` rows in README.md. Each paper consists of two rows:
1. First row: date, title, tags (shield.io badges), arXiv link
2. Second row: three bullet-point summaries

**Key pattern**: Each paper entry uses `rowspan="2"` on the date cell.

## Scripts

```bash
# Rebuild README.md from upstream's English list
git fetch upstream main && python3 scripts/sync_upstream.py upstream/main

# Update the paper count badge in README.md
python3 scripts/update_paper_count.py
```

Papers are added upstream, not here; see `CONTRIBUTING.md` for the upstream PR workflow.
