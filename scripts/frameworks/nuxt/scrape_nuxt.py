#!/usr/bin/env python3
"""Scrape Nuxt framework docs and generate llm.txt + per-section markdown files."""

import json
import os
import re
import time
import urllib.request
from datetime import datetime

BASE_URL = "https://nuxt.com/docs/4.x"
RAW_URL = "https://nuxt.com/raw/docs/4.x"
MODULES_URL = "https://nuxt.com/modules"
DOCS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    "docs", "frameworks", "nuxt",
)

SECTIONS = {
    "Getting Started": [
        "getting-started/introduction",
        "getting-started/installation",
        "getting-started/configuration",
        "getting-started/views",
        "getting-started/assets",
        "getting-started/styling",
        "getting-started/routing",
        "getting-started/seo-meta",
        "getting-started/transitions",
        "getting-started/data-fetching",
        "getting-started/state-management",
        "getting-started/error-handling",
        "getting-started/server",
        "getting-started/layers",
        "getting-started/prerendering",
        "getting-started/deployment",
        "getting-started/testing",
        "getting-started/upgrade",
    ],
    "Directory Structure": [
        "directory-structure",
        "directory-structure/nuxt-config",
        "directory-structure/app",
        "directory-structure/app/pages",
        "directory-structure/app/components",
        "directory-structure/app/composables",
        "directory-structure/app/layouts",
        "directory-structure/app/middleware",
        "directory-structure/app/plugins",
        "directory-structure/app/utils",
        "directory-structure/app/assets",
        "directory-structure/app/app-config",
        "directory-structure/app/error",
        "directory-structure/server",
        "directory-structure/content",
        "directory-structure/layers",
        "directory-structure/modules",
        "directory-structure/public",
        "directory-structure/shared",
    ],
    "Guide - Concepts": [
        "guide/concepts/rendering",
        "guide/concepts/vuejs-development",
        "guide/concepts/nuxt-lifecycle",
        "guide/concepts/auto-imports",
        "guide/concepts/server-engine",
        "guide/concepts/modules",
        "guide/concepts/esm",
        "guide/concepts/typescript",
        "guide/concepts/code-style",
    ],
    "Guide - Best Practices": [
        "guide/best-practices/hydration",
        "guide/best-practices/performance",
        "guide/best-practices/plugins",
    ],
    "Guide - Going Further": [
        "guide/going-further/runtime-config",
        "guide/going-further/hooks",
        "guide/going-further/kit",
        "guide/going-further/nuxt-app",
        "guide/going-further/layers",
        "guide/going-further/experimental-features",
        "guide/going-further/features",
        "guide/going-further/internals",
        "guide/going-further/debugging",
        "guide/going-further/events",
    ],
    "Guide - Recipes": [
        "guide/recipes/custom-routing",
        "guide/recipes/vite-plugin",
        "guide/recipes/custom-usefetch",
        "guide/recipes/sessions-and-authentication",
    ],
    "Guide - Modules": [
        "guide/modules/getting-started",
        "guide/modules/module-anatomy",
        "guide/modules/recipes-basics",
        "guide/modules/recipes-advanced",
        "guide/modules/module-dependencies",
        "guide/modules/testing",
        "guide/modules/best-practices",
        "guide/modules/ecosystem",
    ],
    "Guide - AI": [
        "guide/ai/mcp",
        "guide/ai/llms-txt",
    ],
    "API - Components": [
        "api/components/client-only",
        "api/components/nuxt-page",
        "api/components/nuxt-layout",
        "api/components/nuxt-link",
        "api/components/nuxt-loading-indicator",
        "api/components/nuxt-error-boundary",
        "api/components/nuxt-img",
        "api/components/nuxt-picture",
        "api/components/nuxt-welcome",
        "api/components/nuxt-island",
        "api/components/nuxt-route-announcer",
        "api/components/nuxt-time",
        "api/components/nuxt-announcer",
        "api/components/nuxt-client-fallback",
        "api/components/dev-only",
        "api/components/teleports",
    ],
    "API - Composables": [
        "api/composables/use-async-data",
        "api/composables/use-fetch",
        "api/composables/use-lazy-async-data",
        "api/composables/use-lazy-fetch",
        "api/composables/use-cookie",
        "api/composables/use-state",
        "api/composables/use-head",
        "api/composables/use-seo-meta",
        "api/composables/use-server-seo-meta",
        "api/composables/use-route",
        "api/composables/use-router",
        "api/composables/use-runtime-config",
        "api/composables/use-app-config",
        "api/composables/use-nuxt-app",
        "api/composables/use-error",
        "api/composables/use-request-headers",
        "api/composables/use-request-url",
        "api/composables/use-request-event",
        "api/composables/use-request-fetch",
        "api/composables/use-request-header",
        "api/composables/use-response-header",
        "api/composables/use-hydration",
        "api/composables/use-loading-indicator",
        "api/composables/use-announcer",
        "api/composables/use-route-announcer",
        "api/composables/use-nuxt-data",
        "api/composables/use-preview-mode",
        "api/composables/use-head-safe",
        "api/composables/use-runtime-hook",
        "api/composables/on-prehydrate",
        "api/composables/create-use-async-data",
        "api/composables/create-use-fetch",
    ],
    "API - Utils": [
        "api/utils/define-page-meta",
        "api/utils/navigate-to",
        "api/utils/abort-navigation",
        "api/utils/add-route-middleware",
        "api/utils/define-nuxt-route-middleware",
        "api/utils/define-route-rules",
        "api/utils/set-response-status",
        "api/utils/set-page-layout",
        "api/utils/show-error",
        "api/utils/clear-error",
        "api/utils/create-error",
        "api/utils/call-once",
        "api/utils/refresh-nuxt-data",
        "api/utils/clear-nuxt-data",
        "api/utils/clear-nuxt-state",
        "api/utils/refresh-cookie",
        "api/utils/reload-nuxt-app",
        "api/utils/on-nuxt-ready",
        "api/utils/on-before-route-leave",
        "api/utils/on-before-route-update",
        "api/utils/prefetch-components",
        "api/utils/preload-components",
        "api/utils/preload-route-components",
        "api/utils/prerender-routes",
        "api/utils/define-nuxt-component",
        "api/utils/define-nuxt-plugin",
        "api/utils/update-app-config",
        "api/utils/dollarfetch",
        "api/utils/define-lazy-hydration-component",
    ],
    "API - Commands": [
        "api/commands/dev",
        "api/commands/build",
        "api/commands/generate",
        "api/commands/preview",
        "api/commands/module",
        "api/commands/add",
        "api/commands/init",
        "api/commands/analyze",
        "api/commands/info",
        "api/commands/prepare",
        "api/commands/cleanup",
        "api/commands/typecheck",
        "api/commands/upgrade",
        "api/commands/build-module",
        "api/commands/devtools",
        "api/commands/test",
    ],
    "API - Kit": [
        "api/kit/modules",
        "api/kit/runtime-config",
        "api/kit/templates",
        "api/kit/nitro",
        "api/kit/resolving",
        "api/kit/logging",
        "api/kit/builder",
        "api/kit/layers",
        "api/kit/programmatic",
        "api/kit/compatibility",
        "api/kit/autoimports",
        "api/kit/components",
        "api/kit/context",
        "api/kit/pages",
        "api/kit/layout",
        "api/kit/head",
        "api/kit/plugins",
        "api/kit/examples",
    ],
    "API - Advanced": [
        "api/advanced/hooks",
        "api/advanced/import-meta",
        "api/nuxt-config",
    ],
    "Examples": [
        "examples/hello-world",
        "examples/features/auto-imports",
        "examples/features/data-fetching",
        "examples/features/state-management",
        "examples/features/meta-tags",
        "examples/features/layouts",
        "examples/routing/pages",
        "examples/routing/middleware",
        "examples/routing/universal-router",
        "examples/advanced/config-extends",
        "examples/advanced/error-handling",
        "examples/advanced/testing",
        "examples/advanced/use-cookie",
        "examples/advanced/jsx",
        "examples/advanced/locale",
        "examples/advanced/teleport",
    ],
}


def fetch_page(path):
    """Fetch a page from the Nuxt docs."""
    # Try raw markdown first, fall back to HTML
    url = f"{RAW_URL}/{path}.md"
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (compatible; LLMScraper/1.0)",
            "Accept": "text/markdown, text/plain, */*",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode("utf-8", errors="replace")
            if content and len(content) > 50:
                return content
    except Exception:
        pass

    # Fall back to HTML page
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
    """Extract readable text from HTML."""
    if not html:
        return ""
    # If it looks like markdown already, clean it up
    if html.startswith("#") or html.startswith("---"):
        return html.strip()

    # Remove nav, footer, sidebar, scripts, styles
    html = re.sub(
        r'<(script|style|nav|footer|aside|header)[^>]*>.*?</\1>',
        "", html, flags=re.DOTALL | re.IGNORECASE,
    )
    html = re.sub(r'<!--.*?-->', "", html, flags=re.DOTALL)

    # Keep main content area
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if main_match:
        html = main_match.group(1)

    # Convert elements to markdown-ish
    html = re.sub(r'<h1[^>]*>(.*?)</h1>', r"\n# \1\n", html, flags=re.DOTALL)
    html = re.sub(r'<h2[^>]*>(.*?)</h2>', r"\n## \1\n", html, flags=re.DOTALL)
    html = re.sub(r'<h3[^>]*>(.*?)</h3>', r"\n### \1\n", html, flags=re.DOTALL)
    html = re.sub(r'<h4[^>]*>(.*?)</h4>', r"\n#### \1\n", html, flags=re.DOTALL)
    html = re.sub(r'<li[^>]*>(.*?)</li>', r"- \1\n", html, flags=re.DOTALL)
    html = re.sub(r'<p[^>]*>(.*?)</p>', r"\1\n", html, flags=re.DOTALL)
    html = re.sub(r'<code[^>]*>(.*?)</code>', r"`\1`", html, flags=re.DOTALL)
    html = re.sub(r'<pre[^>]*>(.*?)</pre>', r"\n```\n\1\n```\n", html, flags=re.DOTALL)
    html = re.sub(r'<td[^>]*>(.*?)</td>', r"| \1 ", html, flags=re.DOTALL)
    html = re.sub(r'<th[^>]*>(.*?)</th>', r"| **\1** ", html, flags=re.DOTALL)
    html = re.sub(r'<tr[^>]*>(.*?)</tr>', r"\1|\n", html, flags=re.DOTALL)
    html = re.sub(r'<br\s*/?>', "\n", html, flags=re.DOTALL)

    # Remove remaining tags
    html = re.sub(r'<[^>]+>', " ", html)

    # Decode entities
    html = html.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    html = html.replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")
    html = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), html)

    # Clean whitespace
    html = re.sub(r'[ \t]+', " ", html)
    html = re.sub(r'\n\s*\n\s*\n+', "\n\n", html)
    html = "\n".join(line.rstrip() for line in html.split("\n"))
    return html.strip()


def scrape_all():
    """Scrape all sections."""
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
            content = fetch_page(path)
            if content:
                text = extract_text(content)
                results[section][slug] = text
                print(f"({len(text)} chars)")
            else:
                results[section][slug] = ""
                print("FAILED")
            time.sleep(0.3)

    return results


def generate_llm_txt(results):
    """Generate llm.txt index file."""
    lines = [
        "# Nuxt Framework - LLM Reference",
        "",
        "Version: Nuxt 4.x",
        f"Scraped: {datetime.now().strftime('%Y-%m-%d')}",
        "Source: https://nuxt.com",
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
                    content = content[:5000] + "\n\n[... truncated, see nuxt.com/docs]\n"
                lines.append(content)
            else:
                lines.append("[Content not available]")
            lines.append("")

    return "\n".join(lines)


def main():
    print("=== Nuxt Framework Doc Scraper ===\n")
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

    # Generate per-section markdown files
    for section, pages in results.items():
        safe = section.lower().replace(" ", "-").replace("&", "and")
        section_lines = [f"# Nuxt - {section}\n"]
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
