#!/usr/bin/env python3
"""Scrape Tailwind CSS docs and generate llm.txt for LLM consumption."""

import json
import os
import re
import time
import urllib.request
from datetime import datetime

BASE_URL = "https://tailwindcss.com"
DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "docs", "tailwind")

# All doc pages organized by section
SECTIONS = {
    "Getting Started": [
        "installation",
        "editor-setup",
        "compatibility",
        "upgrade-guide",
    ],
    "Core Concepts": [
        "styling-with-utility-classes",
        "hover-focus-and-other-states",
        "responsive-design",
        "dark-mode",
        "theme",
        "colors",
        "adding-custom-styles",
        "detecting-classes-in-source-files",
        "functions-and-directives",
    ],
    "Base Styles": [
        "preflight",
    ],
    "Layout": [
        "aspect-ratio", "columns", "break-after", "break-before", "break-inside",
        "box-decoration-break", "box-sizing", "display", "float", "clear",
        "isolation", "object-fit", "object-position", "overflow", "overscroll-behavior",
        "position", "top-right-bottom-left", "visibility", "z-index",
    ],
    "Flexbox & Grid": [
        "flex-basis", "flex-direction", "flex-wrap", "flex", "flex-grow", "flex-shrink",
        "order", "grid-template-columns", "grid-column", "grid-template-rows", "grid-row",
        "grid-auto-flow", "grid-auto-columns", "grid-auto-rows", "gap",
        "justify-content", "justify-items", "justify-self", "align-content",
        "align-items", "align-self", "place-content", "place-items", "place-self",
    ],
    "Spacing": [
        "padding", "margin",
    ],
    "Sizing": [
        "width", "min-width", "max-width", "height", "min-height", "max-height",
        "inline-size", "min-inline-size", "max-inline-size",
        "block-size", "min-block-size", "max-block-size",
    ],
    "Typography": [
        "font-family", "font-size", "font-smoothing", "font-style", "font-weight",
        "font-stretch", "font-variant-numeric", "font-feature-settings",
        "letter-spacing", "line-clamp", "line-height", "list-style-image",
        "list-style-position", "list-style-type", "text-align", "color",
        "text-decoration-line", "text-decoration-color", "text-decoration-style",
        "text-decoration-thickness", "text-underline-offset", "text-transform",
        "text-overflow", "text-wrap", "text-indent", "tab-size", "vertical-align",
        "white-space", "word-break", "overflow-wrap", "hyphens", "content",
    ],
    "Backgrounds": [
        "background-attachment", "background-clip", "background-color",
        "background-image", "background-origin", "background-position",
        "background-repeat", "background-size",
    ],
    "Borders": [
        "border-radius", "border-width", "border-color", "border-style",
        "outline-width", "outline-color", "outline-style", "outline-offset",
    ],
    "Effects": [
        "box-shadow", "text-shadow", "opacity", "mix-blend-mode",
        "background-blend-mode", "mask-clip", "mask-composite", "mask-image",
        "mask-mode", "mask-origin", "mask-position", "mask-repeat", "mask-size", "mask-type",
    ],
    "Filters": [
        "filter", "filter-blur", "filter-brightness", "filter-contrast",
        "filter-drop-shadow", "filter-grayscale", "filter-hue-rotate",
        "filter-invert", "filter-saturate", "filter-sepia",
        "backdrop-filter", "backdrop-filter-blur", "backdrop-filter-brightness",
        "backdrop-filter-contrast", "backdrop-filter-grayscale",
        "backdrop-filter-hue-rotate", "backdrop-filter-invert",
        "backdrop-filter-opacity", "backdrop-filter-saturate", "backdrop-filter-sepia",
    ],
    "Tables": [
        "border-collapse", "border-spacing", "table-layout", "caption-side",
    ],
    "Transitions & Animation": [
        "transition-property", "transition-behavior", "transition-duration",
        "transition-timing-function", "transition-delay", "animation",
    ],
    "Transforms": [
        "backface-visibility", "perspective", "perspective-origin", "rotate",
        "scale", "skew", "transform", "transform-origin", "transform-style",
        "translate", "zoom",
    ],
    "Interactivity": [
        "accent-color", "appearance", "caret-color", "color-scheme", "cursor",
        "field-sizing", "pointer-events", "resize", "scroll-behavior",
        "scrollbar-color", "scrollbar-width", "scrollbar-gutter", "scroll-margin",
        "scroll-padding", "scroll-snap-align", "scroll-snap-stop", "scroll-snap-type",
        "touch-action", "user-select", "will-change",
    ],
    "SVG": [
        "fill", "stroke", "stroke-width",
    ],
    "Accessibility": [
        "forced-color-adjust",
    ],
}


def fetch_page(slug):
    url = f"{BASE_URL}/docs/{slug}"
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (compatible; LLMScraper/1.0)",
            "Accept": "text/html",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ERROR fetching {slug}: {e}")
        return None


def extract_text_from_html(html):
    """Extract meaningful text content from HTML, keeping structure."""
    if not html:
        return ""

    # Remove script, style, nav, footer, header tags
    html = re.sub(r'<(script|style|nav|footer|header|aside)[^>]*>.*?</\1>', '', html, flags=re.DOTALL | re.IGNORECASE)

    # Remove HTML comments
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    # Convert common elements
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


def extract_main_content(html):
    """Try to extract just the main doc content, not sidebar/footer."""
    # Try to find the main content area
    patterns = [
        r'<article[^>]*>(.*?)</article>',
        r'<main[^>]*>(.*?)</main>',
        r'class="[^"]*prose[^"]*"[^>]*>(.*?)</div>',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL)
        if m:
            return m.group(1)
    return html


def scrape_all():
    os.makedirs(DOCS_DIR, exist_ok=True)
    results = {}
    total = sum(len(pages) for pages in SECTIONS.values())
    done = 0

    for section, pages in SECTIONS.items():
        results[section] = {}
        for slug in pages:
            done += 1
            print(f"[{done}/{total}] {section}/{slug}...", end=" ", flush=True)
            html = fetch_page(slug)
            if html:
                content = extract_main_content(html)
                text = extract_text_from_html(content)
                results[section][slug] = text
                print(f"({len(text)} chars)")
            else:
                results[section][slug] = ""
                print("FAILED")
            time.sleep(0.3)  # Be polite

    return results


def generate_llm_txt(results):
    """Generate a structured llm.txt file."""
    lines = [
        "# Tailwind CSS v4.3 - LLM Reference",
        "",
        f"Scraped: {datetime.now().strftime('%Y-%m-%d')}",
        "Source: https://tailwindcss.com/docs",
        "",
        "---",
        "",
    ]

    # Table of contents
    lines.append("## Table of Contents\n")
    for section in results:
        safe = section.lower().replace(" ", "-").replace("&", "")
        lines.append(f"- [{section}](#{safe})")
        for slug in results[section]:
            name = slug.replace("-", " ").title()
            lines.append(f"  - [{name}](#{slug})")
    lines.append("\n---\n")

    # Content
    for section, pages in results.items():
        lines.append(f"\n## {section}\n")
        for slug, content in pages.items():
            name = slug.replace("-", " ").title()
            lines.append(f"\n### {name}\n")
            if content:
                # Truncate very long content to keep llm.txt manageable
                if len(content) > 4000:
                    content = content[:4000] + "\n\n[... truncated, see full page at tailwindcss.com/docs/" + slug + "]\n"
                lines.append(content)
            else:
                lines.append("[Content not available]")
            lines.append("")

    return "\n".join(lines)


def main():
    print("=== Tailwind CSS Doc Scraper ===\n")
    results = scrape_all()

    # Save raw JSON
    json_path = os.path.join(DOCS_DIR, "docs_raw.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved raw JSON: {json_path}")

    # Generate llm.txt
    llm_txt = generate_llm_txt(results)
    llm_path = os.path.join(DOCS_DIR, "llm.txt")
    with open(llm_path, "w") as f:
        f.write(llm_txt)
    print(f"Generated llm.txt ({len(llm_txt)} chars)")

    # Generate section files
    for section, pages in results.items():
        safe = section.lower().replace(" ", "-").replace("&", "and")
        section_lines = [f"# Tailwind CSS - {section}\n"]
        for slug, content in pages.items():
            name = slug.replace("-", " ").title()
            section_lines.append(f"\n## {name}\n")
            if content:
                section_lines.append(content)
            else:
                section_lines.append("[Content not available]")
        with open(os.path.join(DOCS_DIR, f"{safe}.md"), "w") as f:
            f.write("\n".join(section_lines))
        print(f"Generated {safe}.md")

    print(f"\nDone! Files in {DOCS_DIR}")


if __name__ == "__main__":
    main()
