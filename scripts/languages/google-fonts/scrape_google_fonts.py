#!/usr/bin/env python3
"""Scrape Google Fonts and typography knowledge for llm.txt."""

import json
import os
import re
import time
import urllib.request
from datetime import datetime

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "docs", "languages", "google-fonts")

KNOWLEDGE_PAGES = [
    ("introduction", "https://fonts.google.com/knowledge"),
    ("using_google_fonts", "https://fonts.google.com/knowledge/using_the_api/using_google_fonts"),
    ("managing_font_data", "https://fonts.google.com/knowledge/using_the_api/managing_font_data"),
    ("adding_font_styles", "https://fonts.google.com/knowledge/using_the_api/adding_font_styles"),
    ("use_cases", "https://fonts.google.com/knowledge/glossary/use_cases"),
    ("about_typefaces", "https://fonts.google.com/knowledge/glossary/about_typefaces"),
    ("typographic_basics", "https://fonts.google.com/knowledge/terminology/typographic_basics"),
    ("readability", "https://fonts.google.com/knowledge/readability_and_accessibility/readability"),
    ("pairing_typefaces", "https://fonts.google.com/knowledge/terminology/pairing_typefaces"),
    ("responsive_type", "https://fonts.google.com/knowledge/typographic_basics/responsive_type"),
    ("variable_fonts", "https://fonts.google.com/knowledge/using_the_api/variable_fonts"),
    ("choosing_typefaces", "https://fonts.google.com/knowledge/readability_and_accessibility/choosing_typefaces"),
    ("writing_systems", "https://fonts.google.com/knowledge/readability_and_accessibility/writing_systems"),
    ("font_subsets", "https://fonts.google.com/knowledge/using_the_api/font_subsets"),
]


def fetch_page(url):
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (compatible; LLMScraper/1.0)",
            "Accept": "text/html",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ERROR: {e}")
        return None


def extract_text(html):
    if not html:
        return ""
    html = re.sub(r'<(script|style|nav|footer|aside|header)[^>]*>.*?</\1>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    main_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if main_match:
        html = main_match.group(1)

    html = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n', html, flags=re.DOTALL)
    html = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html, flags=re.DOTALL)
    html = re.sub(r'<pre[^>]*>(.*?)</pre>', r'\n```\n\1\n```\n', html, flags=re.DOTALL)

    html = re.sub(r'<[^>]+>', ' ', html)
    html = html.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    html = html.replace('&quot;', '"').replace('&#39;', "'").replace('&nbsp;', ' ')
    html = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), html)
    html = re.sub(r'[ \t]+', ' ', html)
    html = re.sub(r'\n\s*\n\s*\n+', '\n\n', html)
    html = '\n'.join(line.rstrip() for line in html.split('\n'))
    return html.strip()


def fetch_font_stats():
    """Fetch font popularity data from Google Fonts metadata."""
    try:
        req = urllib.request.Request("https://fonts.google.com/metadata/stats", headers={
            "User-Agent": "Mozilla/5.0",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            # Strip )]}' prefix if present
            raw = re.sub(r'^\)\]\}\'\s*', '', raw)
            # Fix trailing commas
            raw = re.sub(r',(\s*[}\]])', r'\1', raw)
            return json.loads(raw)
    except Exception as e:
        print(f"  Error fetching font stats: {e}")
        return []


def scrape_knowledge():
    os.makedirs(DOCS_DIR, exist_ok=True)
    results = {}
    total = len(KNOWLEDGE_PAGES)
    done = 0

    for slug, url in KNOWLEDGE_PAGES:
        done += 1
        print(f"[{done}/{total}] {slug}...", end=" ", flush=True)
        html = fetch_page(url)
        if html:
            text = extract_text(html)
            results[slug] = text
            print(f"({len(text)} chars)")
        else:
            results[slug] = ""
            print("FAILED")
        time.sleep(0.3)

    return results


def generate_llm_txt(knowledge, fonts_data):
    lines = [
        "# Google Fonts - LLM Reference",
        "",
        f"Scraped: {datetime.now().strftime('%Y-%m-%d')}",
        f"Source: https://fonts.google.com",
        f"Total Fonts: {len(fonts_data)}",
        "",
        "---",
        "",
    ]

    # Top 100 fonts by popularity
    fonts_sorted = sorted(fonts_data, key=lambda x: x.get("totalViews", 0), reverse=True)
    lines.append("## Top 100 Fonts by Popularity\n")
    lines.append("| Rank | Font Family | Total Views | Designers |")
    lines.append("|------|------------|-------------|-----------|")
    for i, f in enumerate(fonts_sorted[:100], 1):
        name = f["family"]
        views = f"{f.get('totalViews', 0):,}"
        designers = ", ".join(f.get("designers", []))
        lines.append(f"| {i} | {name} | {views} | {designers} |")

    lines += [
        "",
        "---",
        "",
        "## All Fonts Alphabetical\n",
    ]

    fonts_alpha = sorted(fonts_data, key=lambda x: x["family"].lower())
    lines.append("| Font Family | Total Views | Designers |")
    lines.append("|------------|-------------|-----------|")
    for f in fonts_alpha:
        name = f["family"]
        views = f"{f.get('totalViews', 0):,}"
        designers = ", ".join(f.get("designers", []))
        lines.append(f"| {name} | {views} | {designers} |")

    lines += [
        "",
        "---",
        "",
        "## Typography Knowledge\n",
    ]

    for slug, content in knowledge.items():
        name = slug.replace("-", " ").title()
        lines.append(f"\n### {name}\n")
        if content:
            if len(content) > 4000:
                content = content[:4000] + "\n\n[... truncated]\n"
            lines.append(content)
        else:
            lines.append("[Content not available]")
        lines.append("")

    return "\n".join(lines)


def main():
    print("=== Google Fonts Scraper ===\n")

    print("Scraping typography knowledge pages...")
    knowledge = scrape_knowledge()

    print("\nFetching font popularity data...")
    fonts_data = fetch_font_stats()
    print(f"  Found {len(fonts_data)} fonts")

    llm_txt = generate_llm_txt(knowledge, fonts_data)
    llm_path = os.path.join(DOCS_DIR, "llm.txt")
    with open(llm_path, "w") as f:
        f.write(llm_txt)
    print(f"\nGenerated llm.txt ({len(llm_txt)} chars)")

    # Save knowledge section files
    for slug, content in knowledge.items():
        section_lines = [f"# Google Fonts - {slug.replace('-', ' ').title()}\n"]
        section_lines.append(content if content else "[Content not available]")
        with open(os.path.join(DOCS_DIR, f"{slug}.md"), "w") as f:
            f.write("\n".join(section_lines))
    print(f"Generated {len(knowledge)} section files")

    # Save top fonts as a separate quick reference
    fonts_sorted = sorted(fonts_data, key=lambda x: x.get("totalViews", 0), reverse=True)
    top_lines = [
        "# Google Fonts - Top 200 by Popularity\n",
        "| Rank | Font | Views | Designers |",
        "|------|------|-------|-----------|",
    ]
    for i, f in enumerate(fonts_sorted[:200], 1):
        name = f["family"]
        views = f"{f.get('totalViews', 0):,}"
        designers = ", ".join(f.get("designers", []))
        top_lines.append(f"| {i} | {name} | {views} | {designers} |")
    with open(os.path.join(DOCS_DIR, "top-fonts.md"), "w") as f:
        f.write("\n".join(top_lines))
    print("Generated top-fonts.md")

    print(f"\nDone! Files in {DOCS_DIR}")


if __name__ == "__main__":
    main()
