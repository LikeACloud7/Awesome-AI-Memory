# Contributing Guide

## How This Fork Stays Updated

This is an English-only fork of [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory). Upstream keeps its English paper list in `README_en.md`; here it is published as `README.md`.

The **Sync English paper list from upstream** GitHub Action runs daily. It merges new upstream commits with `-s ours` (so upstream's Chinese files never come in), rebuilds `README.md` and `assets/` with `scripts/sync_upstream.py`, then commits and pushes. Manual edits to paper entries in `README.md` are overwritten on the next sync, so add papers upstream (steps below) and they will appear here automatically.

Do not use GitHub's **Sync fork** button; it would bring back upstream's Chinese `README.md`.

To sync right away, run the workflow from the Actions tab, or locally:

```bash
git remote add upstream https://github.com/IAAR-Shanghai/Awesome-AI-Memory.git
git fetch upstream main
git merge -s ours --no-commit upstream/main
python3 scripts/sync_upstream.py upstream/main
git add README.md assets
git commit -m "Sync English paper list from upstream"
```

## Adding a Paper (Upstream)

### 0. Check scope and evidence first

Read the [screening policy](SCREENING.md). Only work whose core contribution is Agent Memory or memory inside language models is included; adjacent topics, keyword matches and candidates with insufficient evidence cannot be added directly.

Save a per-paper human judgment with source evidence in upstream's `screening/YYYY-MM-DD-review.json`. Procedural skills must explain how experience is formed, persisted, reused later and validated/maintained. Resubmitting an excluded or held ID requires new evidence and a `reassessment`, and the historical record must be kept.

Before submitting, run `python3 scripts/check_screening.py --base origin/main --review screening/YYYY-MM-DD-review.json` in your upstream branch, and check the three summary bullets in both languages, descending date order, deduplication, counts and GitHub table rendering. The checker verifies evidence records; it does not replace human relevance judgment. Distinguish honestly between abstract verification and full-text reading.

### 1. Setup

Fork upstream and create a new branch from `upstream/main` (not from this fork's `main`):
```bash
git remote add upstream https://github.com/IAAR-Shanghai/Awesome-AI-Memory.git
git fetch upstream
git checkout -b add-paper-{paper-short-name} upstream/main
```

### 2. Find the insertion point

Papers are sorted by **date, newest first**. Insert the entry near its date.

### 3. Paper format

**HTML table rows**:

```html
<tr>
    <td rowspan="2" style="width: 15%;">[date, e.g. 2026-01-30]</td>
    <td style="width: 55%;"><strong>[paper title]</strong></td>
    <td style="width: 15%;">
        <img src="https://img.shields.io/badge/[tag1]-blue" alt="...">
        <img src="https://img.shields.io/badge/[tag2]-brightgreen" alt="...">
    </td>
    <td style="width: 15%;"><a href="[arXiv PDF link]">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
    </a></td>
</tr>
<tr>
    <td colspan="3">
        • [innovation]<br>
        • [task/method]<br>
        • [key result]
    </td>
</tr>
```

**Tag examples**: Behavior Tree, Policy Verifiability, Safety, Memory System, Agent Memory, Long-Term Memory, etc. (see existing entries)

### 4. Language requirements (upstream)

- **README.md**: Chinese description (upstream's default homepage)
- **README_en.md**: English description (the source of this fork's `README.md`)

### 5. Commit and open a PR

```bash
git add README.md README_en.md screening/YYYY-MM-DD-review.json
git commit -m "Add [paper short name] paper on [topic] for LLM Agents"
git push -u origin add-paper-{paper-short-name}
```

Create the PR with `gh pr create` or on the GitHub website:

```bash
gh pr create --repo IAAR-Shanghai/Awesome-AI-Memory \
  --title "Add [paper title]" \
  --body "## Summary
- Add paper: [paper title]
- [short description]

## Paper Details
- **Title**: [full title]
- **Authors**: [authors]
- **arXiv**: [ID](https://arxiv.org/abs/xxx)

## Test plan
- [x] Added entry to README.md
- [x] Added entry to README_en.md"
```

### 6. Issue template (optional)

If you are not submitting a PR, you can open an Issue first:
```
Title: [paper's title]
Head: [author name1] (, [author name2] ...)
Published: [arXiv / ACL / ICLR / NIPS / ...]
Summary:
  - Innovation:
  - Tasks:
  - Significant Result:
```
