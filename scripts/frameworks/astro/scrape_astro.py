#!/usr/bin/env python3
"""Scrape Astro framework docs and generate llm.txt."""

import json
import os
import re
import time
import urllib.request
from datetime import datetime

BASE_URL = "https://docs.astro.build/en"
DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "docs", "frameworks", "astro")

SECTIONS = {
    "Getting Started": [
        "install-and-setup/",
        "concepts/why-astro/",
        "concepts/islands/",
        "basics/project-structure/",
        "develop-and-build/",
    ],
    "Configuration": [
        "guides/configuring-astro/",
        "editor-setup/",
        "guides/typescript/",
        "guides/environment-variables/",
        "guides/integrations/",
        "guides/build-with-ai/",
        "guides/dev-toolbar/",
    ],
    "Routing & Navigation": [
        "basics/astro-pages/",
        "guides/routing/",
        "guides/endpoints/",
        "guides/middleware/",
        "guides/internationalization/",
        "guides/prefetch/",
        "guides/view-transitions/",
    ],
    "UI & Components": [
        "basics/astro-components/",
        "basics/layouts/",
        "guides/styling/",
        "guides/fonts/",
        "guides/syntax-highlighting/",
        "guides/client-side-scripts/",
        "guides/framework-components/",
    ],
    "Content": [
        "guides/markdown-content/",
        "guides/content-collections/",
        "guides/images/",
        "guides/data-fetching/",
        "guides/astro-db/",
    ],
    "Server Rendering": [
        "guides/on-demand-rendering/",
        "guides/server-islands/",
        "guides/actions/",
        "guides/sessions/",
    ],
    "Template Syntax": [
        "reference/astro-syntax/",
        "reference/directives-reference/",
    ],
    "Reference": [
        "reference/configuration-reference/",
        "reference/cli-reference/",
        "guides/imports/",
        "reference/routing-reference/",
        "reference/api-reference/",
    ],
    "API Modules": [
        "reference/modules/astro-actions/",
        "reference/modules/astro-assets/",
        "reference/modules/astro-config/",
        "reference/modules/astro-content/",
        "reference/modules/astro-env/",
        "reference/modules/astro-i18n/",
        "reference/modules/astro-middleware/",
        "reference/modules/astro-static-paths/",
        "reference/modules/astro-transitions/",
        "reference/modules/astro-zod/",
    ],
    "Integrations": [
        "guides/integrations-guide/react/",
        "guides/integrations-guide/vue/",
        "guides/integrations-guide/svelte/",
        "guides/integrations-guide/solid-js/",
        "guides/integrations-guide/preact/",
        "guides/integrations-guide/alpinejs/",
        "guides/integrations-guide/cloudflare/",
        "guides/integrations-guide/netlify/",
        "guides/integrations-guide/node/",
        "guides/integrations-guide/vercel/",
        "guides/integrations-guide/db/",
        "guides/integrations-guide/mdx/",
        "guides/integrations-guide/markdoc/",
        "guides/integrations-guide/sitemap/",
        "guides/integrations-guide/partytown/",
    ],
    "Deployment": [
        "guides/deploy/",
        "guides/deploy/cloudflare/",
        "guides/deploy/netlify/",
        "guides/deploy/vercel/",
        "guides/deploy/github/",
        "guides/deploy/aws/",
        "guides/deploy/flyio/",
        "guides/deploy/deno/",
        "guides/deploy/firebase/",
    ],
    "How-to Recipes": [
        "recipes/",
        "recipes/build-forms/",
        "recipes/build-forms-api/",
        "recipes/sharing-state/",
        "recipes/sharing-state-islands/",
        "recipes/rss/",
        "recipes/docker/",
        "recipes/tailwind-rendered-markdown/",
        "recipes/reading-time/",
        "recipes/modified-time/",
        "recipes/bun/",
    ],
    "Migration Guides": [
        "guides/migrate-to-astro/",
        "guides/upgrade-to/v6/",
        "guides/upgrade-to/v5/",
        "guides/upgrade-to/v4/",
    ],
}


def fetch_page(path):
    url = f"{BASE_URL}/{path}"
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
    # Remove nav, footer, sidebar, scripts, styles
    html = re.sub(r'<(script|style|nav|footer|aside|header)[^>]*>.*?</\1>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    # Keep main content area
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if main_match:
        html = main_match.group(1)

    # Convert elements
    html = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html, flags=re.DOTALL)
    html = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n', html, flags=re.DOTALL)
    html = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html, flags=re.DOTALL)
    html = re.sub(r'<pre[^>]*>(.*?)</pre>', r'\n```\n\1\n```\n', html, flags=re.DOTALL)
    html = re.sub(r'<td[^>]*>(.*?)</td>', r'| \1 ', html, flags=re.DOTALL)
    html = re.sub(r'<th[^>]*>(.*?)</th>', r'| **\1** ', html, flags=re.DOTALL)
    html = re.sub(r'<tr[^>]*>(.*?)</tr>', r'\1|\n', html, flags=re.DOTALL)

    # Remove remaining tags
    html = re.sub(r'<[^>]+>', ' ', html)

    # Decode entities
    html = html.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    html = html.replace('&quot;', '"').replace('&#39;', "'").replace('&nbsp;', ' ')
    html = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), html)

    # Clean whitespace
    html = re.sub(r'[ \t]+', ' ', html)
    html = re.sub(r'\n\s*\n\s*\n+', '\n\n', html)
    html = '\n'.join(line.rstrip() for line in html.split('\n'))
    return html.strip()


def scrape_all():
    os.makedirs(DOCS_DIR, exist_ok=True)
    results = {}
    total = sum(len(p) for p in SECTIONS.values())
    done = 0

    for section, pages in SECTIONS.items():
        results[section] = {}
        for path in pages:
            done += 1
            slug = path.rstrip("/").split("/")[-1]
            print(f"[{done}/{total}] {section}/{slug}...", end=" ", flush=True)
            html = fetch_page(path)
            if html:
                text = extract_text(html)
                results[section][slug] = text
                print(f"({len(text)} chars)")
            else:
                results[section][slug] = ""
                print("FAILED")
            time.sleep(0.3)

    return results


def generate_llm_txt(results):
    lines = [
        "# Astro Framework - LLM Reference",
        "",
        f"Version: Latest (v5.x)",
        f"Scraped: {datetime.now().strftime('%Y-%m-%d')}",
        "Source: https://docs.astro.build",
        "",
        "---",
        "",
        "## Table of Contents\n",
    ]

    for section in results:
        safe = section.lower().replace(" ", "-").replace("&", "and")
        lines.append(f"- [{section}](#{safe})")
        for slug in results[section]:
            name = slug.replace("-", " ").title()
            lines.append(f"  - [{name}](#{slug})")
    lines.append("\n---\n")

    for section, pages in results.items():
        lines.append(f"\n## {section}\n")
        for slug, content in pages.items():
            name = slug.replace("-", " ").title()
            lines.append(f"\n### {name}\n")
            if content:
                if len(content) > 5000:
                    content = content[:5000] + "\n\n[... truncated, see docs.astro.build]\n"
                lines.append(content)
            else:
                lines.append("[Content not available]")
            lines.append("")

    return "\n".join(lines)


def main():
    print("=== Astro Framework Doc Scraper ===\n")
    results = scrape_all()

    json_path = os.path.join(DOCS_DIR, "docs_raw.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved raw JSON: {json_path}")

    llm_txt = generate_llm_txt(results)
    llm_path = os.path.join(DOCS_DIR, "llm.txt")
    with open(llm_path, "w") as f:
        f.write(llm_txt)
    print(f"Generated llm.txt ({len(llm_txt)} chars)")

    for section, pages in results.items():
        safe = section.lower().replace(" ", "-").replace("&", "and")
        section_lines = [f"# Astro - {section}\n"]
        for slug, content in pages.items():
            name = slug.replace("-", " ").title()
            section_lines.append(f"\n## {name}\n")
            section_lines.append(content if content else "[Content not available]")
        with open(os.path.join(DOCS_DIR, f"{safe}.md"), "w") as f:
            f.write("\n".join(section_lines))
        print(f"Generated {safe}.md")

    print(f"\nDone! Files in {DOCS_DIR}")


if __name__ == "__main__":
    main()
