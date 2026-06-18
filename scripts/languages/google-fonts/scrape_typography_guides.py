#!/usr/bin/env python3
"""Scrape typography guides from web.dev and NN/g for Google Fonts docs."""

import json
import os
import re
import time
import urllib.request
from datetime import datetime

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "docs", "languages", "google-fonts")

GUIDES = [
    ("webdev-accessible-typography", "https://web.dev/learn/accessibility/typography"),
    ("webdev-responsive-typography", "https://web.dev/learn/design/typography"),
    ("nngroup-pairing-typefaces", "https://www.nngroup.com/articles/pairing-typefaces/"),
    ("nngroup-typography-terms", "https://www.nngroup.com/articles/typography-terms-ux/"),
    ("nngroup-best-font-reading", "https://www.nngroup.com/articles/best-font-for-online-reading/"),
    ("designers-guide-choosing-fonts", "https://design.google/library/choosing-web-fonts-beginners-guide"),
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
    else:
        article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
        if article_match:
            html = article_match.group(1)

    html = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', html, flags=re.DOTALL)
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


def main():
    print("=== Typography Guides Scraper ===\n")
    results = {}
    total = len(GUIDES)
    done = 0

    for slug, url in GUIDES:
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

    # Append to existing llm.txt
    llm_path = os.path.join(DOCS_DIR, "llm.txt")
    existing = ""
    if os.path.exists(llm_path):
        with open(llm_path) as f:
            existing = f.read()

    new_section = "\n\n---\n\n## Typography Guides (from web.dev, NN/g, Google)\n\n"
    for slug, content in results.items():
        name = slug.replace("-", " ").title()
        new_section += f"\n### {name}\n\n"
        if content:
            if len(content) > 6000:
                content = content[:6000] + "\n\n[... truncated, see original source]\n"
            new_section += content + "\n"
        else:
            new_section += "[Content not available]\n"

    with open(llm_path, "w") as f:
        f.write(existing + new_section)
    print(f"\nAppended to llm.txt ({len(new_section)} chars added)")

    # Save individual files
    for slug, content in results.items():
        with open(os.path.join(DOCS_DIR, f"{slug}.md"), "w") as f:
            f.write(f"# {slug.replace('-', ' ').title()}\n\n{content if content else '[Content not available]'}")
    print(f"Saved {len(results)} guide files")

    print(f"\nDone! Files in {DOCS_DIR}")


if __name__ == "__main__":
    main()
