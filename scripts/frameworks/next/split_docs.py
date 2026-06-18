#!/usr/bin/env python3
"""
Split Next.js llms-full.txt into individual markdown files.
Input:  docs/frameworks/next/llms-full.txt (or cache)
Output: docs/frameworks/next/{slug}.md
"""

import re
import sys
from pathlib import Path

FULL_DOC = Path(__file__).parents[3] / "docs" / "frameworks" / "next" / "llms-full.txt"
OUTPUT_DIR = Path(__file__).parents[3] / "docs" / "frameworks" / "next"
LLM_INDEX = OUTPUT_DIR / "llm.txt"


def parse_frontmatter(text):
    """Extract title and url from YAML frontmatter."""
    fm = {}
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            block = text[3:end].strip()
            for line in block.split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')
    return fm


def slugify(title, url):
    """Create a filesystem-safe slug from title or URL."""
    if url:
        # Try to extract path from URL
        m = re.search(r'nextjs\.org/docs/(.+?)(?:\.md)?$', url)
        if m:
            path = m.group(1)
            # Remove common prefixes
            path = re.sub(r'^app/', '', path)
            path = re.sub(r'^pages/', 'pages-', path)
            # Clean up
            path = path.strip('/')
            slug = re.sub(r'[^a-zA-Z0-9_-]', '-', path)
            slug = re.sub(r'-+', '-', slug).strip('-')
            return slug.lower()

    # Fallback: use title
    slug = re.sub(r'[^a-zA-Z0-9_-]', '-', title)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug.lower()


def split_docs(content):
    """Split the full doc into sections by --- separator."""
    # Split on --- lines that are between sections
    parts = re.split(r'\n---\n', content)
    docs = []

    for part in parts:
        part = part.strip()
        if not part:
            continue

        fm = parse_frontmatter(part)
        title = fm.get("title", "")
        url = fm.get("url", "")

        # Skip the index/overview
        if title == "Getting Started" and not url:
            # Keep it but name it overview
            pass

        if not title:
            # Try to extract first heading
            m = re.match(r'^#\s+(.+)', part)
            if m:
                title = m.group(1)

        if title:
            slug = slugify(title, url)
            docs.append({
                "slug": slug,
                "title": title,
                "url": url,
                "content": part,
            })

    return docs


def deduplicate(docs):
    """Handle duplicate slugs by appending suffix."""
    seen = {}
    result = []
    for doc in docs:
        slug = doc["slug"]
        if slug in seen:
            seen[slug] += 1
            doc["slug"] = f"{slug}-{seen[slug]}"
        else:
            seen[slug] = 1
        result.append(doc)
    return result


def main():
    if not FULL_DOC.exists():
        print(f"File not found: {FULL_DOC}")
        print("Run the fetcher first to download llms-full.txt")
        sys.exit(1)

    content = FULL_DOC.read_text(encoding="utf-8")
    print(f"Read {len(content)} chars, {len(content.splitlines())} lines")

    docs = split_docs(content)
    print(f"Found {len(docs)} doc sections")

    docs = deduplicate(docs)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    written = 0
    index_lines = [
        "# Next.js Documentation",
        f"Scraped from nextjs.org/docs/llms-full.txt",
        "",
    ]

    for doc in docs:
        filename = f"{doc['slug']}.md"
        filepath = OUTPUT_DIR / filename

        filepath.write_text(doc["content"], encoding="utf-8")
        written += 1

        index_lines.append(f"- {doc['slug']}.md — {doc['title']}")

    LLM_INDEX.write_text("\n".join(index_lines), encoding="utf-8")
    print(f"Wrote {written} files to {OUTPUT_DIR}")
    print(f"Index: {LLM_INDEX}")


if __name__ == "__main__":
    main()
