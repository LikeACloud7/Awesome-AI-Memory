#!/usr/bin/env python3
"""
Count the papers and update the paper count badge in README.md
"""

import re
from pathlib import Path


def count_papers(readme_path: Path) -> int:
    """Count the papers in a README file (via the rowspan="2" pattern)"""
    content = readme_path.read_text(encoding='utf-8')

    # Strip HTML comments first so commented-out papers are not counted
    content_without_comments = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    # Each paper in the table uses rowspan="2" to merge its date cell
    pattern = r'rowspan="2"'
    matches = re.findall(pattern, content_without_comments)
    return len(matches)


def update_badge_count(readme_path: Path, paper_count: int) -> bool:
    """Update the paper count badge in a README file"""
    content = readme_path.read_text(encoding='utf-8')

    # Match badges in the Papers-N-blue format
    pattern = r'(Papers-)\d+(-blue\.svg)'
    replacement = rf'\g<1>{paper_count}\g<2>'

    new_content, count = re.subn(pattern, replacement, content)

    if count > 0:
        readme_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def main():
    # Locate the project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    readme_files = [
        project_root / 'README.md',
    ]

    print("📊 Counting papers...")
    print("-" * 40)

    for readme_path in readme_files:
        if not readme_path.exists():
            print(f"⚠️  File not found: {readme_path.name}")
            continue

        paper_count = count_papers(readme_path)
        print(f"📄 {readme_path.name}: {paper_count} papers")

        if update_badge_count(readme_path, paper_count):
            print(f"   ✅ Badge count updated to {paper_count}")
        else:
            print(f"   ⚠️  Badge not found or no update needed")

    print("-" * 40)
    print("✨ Done!")


if __name__ == '__main__':
    main()
