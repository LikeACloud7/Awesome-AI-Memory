#!/usr/bin/env python3
"""
Regenerate the English-only README.md from an upstream git ref.

Upstream (IAAR-Shanghai/Awesome-AI-Memory) keeps its English paper list in
README_en.md and its Chinese list in README.md. This fork publishes English
only, so README.md is rebuilt from upstream's English file and upstream's
Chinese files are never copied in.

Usage: python3 scripts/sync_upstream.py [git-ref]   (default: upstream/main)
"""

import re
import subprocess
import sys
from pathlib import Path

from update_paper_count import count_papers, update_badge_count

UPSTREAM_BLOB = 'https://github.com/IAAR-Shanghai/Awesome-AI-Memory/blob/main/'
# Upstream file names that may hold the English list; the one with the least CJK text wins.
CANDIDATES = ('README_en.md', 'README.md')
CJK = re.compile(r'[\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uff00-\uffef]')
LINK = re.compile(r'(\]\(|(?:href|src)=")([^)"\s]+)')


def git(root: Path, *args: str) -> str:
    return subprocess.run(['git', *args], cwd=root, check=True, capture_output=True, text=True).stdout


def read_english(root: Path, ref: str) -> str:
    """Return the upstream README with the least Chinese text"""
    texts = []
    for name in CANDIDATES:
        try:
            texts.append(git(root, 'show', f'{ref}:{name}'))
        except subprocess.CalledProcessError:
            continue
    if not texts:
        raise SystemExit(f'No README found at {ref}')
    return min(texts, key=lambda t: len(CJK.findall(t)))


def to_english(text: str, root: Path) -> str:
    # Drop the language switcher line linking to the Chinese page; this fork has none.
    text = re.sub(r'<p align="center">\s*\u3010[^\u3011]*\u3011\s*</p>\n+', '', text)

    # Full-width punctuation (e.g. the colon in "M+\uff1aExtending") -> ASCII
    text = re.sub(r'([\uff1a\uff0c\uff1b])(?=\S)', r'\1 ', text)
    text = re.sub(r'[\uff01-\uff5e]', lambda m: chr(ord(m.group()) - 0xfee0), text)

    # Relative links to files this fork does not keep (e.g. Chinese screening reports) point upstream.
    def relink(m: re.Match) -> str:
        prefix, target = m.groups()
        if re.match(r'[a-z]+:|#', target):
            return m.group()
        path = target.split('#')[0].split('?')[0]
        if path in CANDIDATES:
            return prefix + 'README.md' + target[len(path):]
        if (root / path).exists():
            return m.group()
        return prefix + UPSTREAM_BLOB + target
    return LINK.sub(relink, text)


def main():
    ref = sys.argv[1] if len(sys.argv) > 1 else 'upstream/main'
    root = Path(__file__).resolve().parents[1]

    git(root, 'checkout', ref, '--', 'assets')
    readme = root / 'README.md'
    readme.write_text(to_english(read_english(root, ref), root), encoding='utf-8')
    update_badge_count(readme, count_papers(readme))
    print(f'README.md regenerated from {ref}: {count_papers(readme)} papers')

    leftovers = [i for i, line in enumerate(readme.read_text(encoding='utf-8').splitlines(), 1) if CJK.search(line)]
    if leftovers:
        print(f'warning: non-English text remains on README.md lines {leftovers[:20]}')


if __name__ == '__main__':
    main()
