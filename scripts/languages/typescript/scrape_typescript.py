#!/usr/bin/env python3
"""Scrape TypeScript docs and generate llm.txt."""

import json
import os
import re
import time
import urllib.request
from datetime import datetime

BASE_URL = "https://www.typescriptlang.org"
DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "docs", "languages", "typescript")

SECTIONS = {
    "Get Started": [
        "/docs/handbook/typescript-from-scratch.html",
        "/docs/handbook/typescript-in-5-minutes.html",
        "/docs/handbook/typescript-in-5-minutes-oop.html",
        "/docs/handbook/typescript-in-5-minutes-func.html",
        "/docs/handbook/typescript-tooling-in-5-minutes.html",
    ],
    "Handbook": [
        "/docs/handbook/intro.html",
        "/docs/handbook/2/basic-types.html",
        "/docs/handbook/2/everyday-types.html",
        "/docs/handbook/2/narrowing.html",
        "/docs/handbook/2/functions.html",
        "/docs/handbook/2/objects.html",
        "/docs/handbook/2/types-from-types.html",
        "/docs/handbook/2/generics.html",
        "/docs/handbook/2/keyof-types.html",
        "/docs/handbook/2/typeof-types.html",
        "/docs/handbook/2/indexed-access-types.html",
        "/docs/handbook/2/conditional-types.html",
        "/docs/handbook/2/mapped-types.html",
        "/docs/handbook/2/template-literal-types.html",
        "/docs/handbook/2/classes.html",
        "/docs/handbook/2/modules.html",
    ],
    "Reference": [
        "/docs/handbook/utility-types.html",
        "/docs/handbook/decorators.html",
        "/docs/handbook/declaration-merging.html",
        "/docs/handbook/enums.html",
        "/docs/handbook/iterators-and-generators.html",
        "/docs/handbook/jsx.html",
        "/docs/handbook/mixins.html",
        "/docs/handbook/namespaces.html",
        "/docs/handbook/namespaces-and-modules.html",
        "/docs/handbook/symbols.html",
        "/docs/handbook/triple-slash-directives.html",
        "/docs/handbook/type-compatibility.html",
        "/docs/handbook/type-inference.html",
        "/docs/handbook/variable-declarations.html",
    ],
    "Modules Reference": [
        "/docs/handbook/modules/introduction.html",
        "/docs/handbook/modules/theory.html",
        "/docs/handbook/modules/guides/choosing-compiler-options.html",
        "/docs/handbook/modules/reference.html",
        "/docs/handbook/modules/appendices/esm-cjs-interop.html",
    ],
    "Declaration Files": [
        "/docs/handbook/declaration-files/introduction.html",
        "/docs/handbook/declaration-files/by-example.html",
        "/docs/handbook/declaration-files/library-structures.html",
        "/docs/handbook/declaration-files/templates/module-d-ts.html",
        "/docs/handbook/declaration-files/templates/module-plugin-d-ts.html",
        "/docs/handbook/declaration-files/templates/module-class-d-ts.html",
        "/docs/handbook/declaration-files/templates/module-function-d-ts.html",
        "/docs/handbook/declaration-files/templates/global-d-ts.html",
        "/docs/handbook/declaration-files/templates/global-modifying-module-d-ts.html",
        "/docs/handbook/declaration-files/do-s-and-don-ts.html",
        "/docs/handbook/declaration-files/deep-dive.html",
        "/docs/handbook/declaration-files/publishing.html",
        "/docs/handbook/declaration-files/consumption.html",
    ],
    "JavaScript": [
        "/docs/handbook/intro-to-js-ts.html",
        "/docs/handbook/type-checking-javascript-files.html",
        "/docs/handbook/jsdoc-supported-types.html",
        "/docs/handbook/declaration-files/dts-from-js.html",
    ],
    "Project Configuration": [
        "/docs/handbook/tsconfig-json.html",
        "/docs/handbook/compiler-options-in-msbuild.html",
        "/docs/handbook/compiler-options.html",
        "/docs/handbook/project-references.html",
        "/docs/handbook/integrating-with-build-tools.html",
        "/docs/handbook/configuring-watch.html",
        "/docs/handbook/nightly-builds.html",
    ],
    "Tutorials": [
        "/docs/handbook/asp-net-core.html",
        "/docs/handbook/gulp.html",
        "/docs/handbook/dom-manipulation.html",
        "/docs/handbook/migrating-from-javascript.html",
        "/docs/handbook/babel-with-typescript.html",
    ],
    "What's New": [
        "/docs/handbook/release-notes/typescript-6-0.html",
        "/docs/handbook/release-notes/typescript-5-9.html",
        "/docs/handbook/release-notes/typescript-5-8.html",
        "/docs/handbook/release-notes/typescript-5-7.html",
        "/docs/handbook/release-notes/typescript-5-6.html",
        "/docs/handbook/release-notes/typescript-5-5.html",
        "/docs/handbook/release-notes/typescript-5-4.html",
        "/docs/handbook/release-notes/typescript-5-3.html",
        "/docs/handbook/release-notes/typescript-5-2.html",
        "/docs/handbook/release-notes/typescript-5-1.html",
        "/docs/handbook/release-notes/typescript-5-0.html",
    ],
}


def fetch_page(path):
    url = f"{BASE_URL}{path}"
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
        content_match = re.search(r'id="handbook-content"[^>]*>(.*?)</div>\s*</div>\s*</div>', html, re.DOTALL)
        if content_match:
            html = content_match.group(1)

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

    html = re.sub(r'<[^>]+>', ' ', html)
    html = html.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    html = html.replace('&quot;', '"').replace('&#39;', "'").replace('&nbsp;', ' ')
    html = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), html)

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
            slug = path.rstrip("/").split("/")[-1].replace(".html", "")
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
        "# TypeScript - LLM Reference",
        "",
        f"Version: Latest (TS 6.0)",
        f"Scraped: {datetime.now().strftime('%Y-%m-%d')}",
        "Source: https://www.typescriptlang.org/docs/handbook",
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
                    content = content[:5000] + "\n\n[... truncated, see typescriptlang.org/docs/handbook]\n"
                lines.append(content)
            else:
                lines.append("[Content not available]")
            lines.append("")

    return "\n".join(lines)


def main():
    print("=== TypeScript Doc Scraper ===\n")
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
        section_lines = [f"# TypeScript - {section}\n"]
        for slug, content in pages.items():
            name = slug.replace("-", " ").title()
            section_lines.append(f"\n## {name}\n")
            section_lines.append(content if content else "[Content not available]")
        with open(os.path.join(DOCS_DIR, f"{safe}.md"), "w") as f:
            f.write("\n".join(section_lines))
        print(f"Generated {safe}.md")

    # Cleanup raw JSON
    os.remove(json_path)
    print(f"\nDone! Files in {DOCS_DIR}")


if __name__ == "__main__":
    main()
