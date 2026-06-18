#!/usr/bin/env python3
"""
Scrape Next.js documentation from nextjs.org/docs and nextjs.org/app/building-your-application.
Outputs individual markdown files into docs/frameworks/next/ and generates llm.txt.
"""

import re
import json
import time
import os
import sys
import urllib.request
import urllib.error
from html.parser import HTMLParser
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────

DOCS_DIR = Path(__file__).parents[3] / "docs" / "frameworks" / "next"
CACHE_DIR = Path(__file__).parents[3] / ".cache" / "next"
LLM_TXT = DOCS_DIR / "llm.txt"

BASE_URL = "https://nextjs.org"
DOCS_BASE = "https://nextjs.org/docs"

# Full doc structure from llms.txt
DOCS = [
    # Getting Started
    ("getting-started/installation", "Installation"),
    ("getting-started/project-structure", "Project Structure"),
    ("getting-started/folder-conventions", "Folder Conventions"),
    ("getting-started/file-conventions", "File Conventions"),
    ("getting-started/app-vs-pages-router", "App Router vs Pages Router"),
    ("getting-started/server-and-client-components", "Server and Client Components"),
    ("getting-started/typescript", "TypeScript"),
    ("getting-started/eslint", "ESLint"),
    ("getting-started/instrumentation", "Instrumentation"),
    ("getting-started/debugging", "Debugging"),
    ("getting-started/testing", "Testing"),
    ("getting-started/env-file", "Environment Variables"),
    ("getting-started/trailing-slashes", "Trailing Slashes"),
    ("getting-started/cache-revalidation", "Cache and Revalidation"),
    ("getting-started/partial-prerendering", "Partial Prerendering"),
    ("getting-started/draft-mode", "Draft Mode"),
    ("getting-started/csp", "Content Security Policy"),
    ("getting-started/analytics", "Analytics"),
    ("getting-started/third-party-libraries", "Third Party Libraries"),
    ("getting-started/localization", "Localizing Folder and Routing Names"),

    # App Router
    ("app/building-your-application/routing", "Routing Overview"),
    ("app/building-your-application/routing/defining-routes", "Defining Routes"),
    ("app/building-your-application/routing/dynamic-routes", "Dynamic Routes"),
    ("app/building-your-application/routing/colocation", "Route Colocation"),
    ("app/building-your-application/routing/parallel-routes", "Parallel Routes"),
    ("app/building-your-application/routing/intercepting-routes", "Intercepting Routes"),
    ("app/building-your-application/routing/handling-forms", "Forms and Error Handling"),
    ("app/building-your-application/routing/loading-ui-and-streaming", "Loading UI and Streaming"),
    ("app/building-your-application/routing/error-handling", "Error Handling"),
    ("app/building-your-application/routing/revalidating-static-data", "Revalidating Static Data"),
    ("app/building-your-application/routing/conditional-routes", "Conditional Routes"),
    ("app/building-your-application/routing/middleware", "Middleware"),
    ("app/building-your-application/routing/redirecting", "Redirecting"),
    ("app/building-your-application/routing/pagination", "Pagination"),
    ("app/building-your-application/routing/metadata", "Metadata and SEO"),

    ("app/building-your-application/data-fetching", "Data Fetching Overview"),
    ("app/building-your-application/data-fetching/server-and-client-components", "Server and Client Data Fetching"),
    ("app/building-your-application/data-fetching/caching-and-revalidating", "Caching and Revalidating"),
    ("app/building-your-application/data-fetching/fetching-data", "Fetching Data"),
    ("app/building-your-application/data-fetching/request-memoization", "Request Memoization"),
    ("app/building-your-application/data-fetching/patterns", "Data Fetching Patterns"),
    ("app/building-your-application/data-fetching/server-actions-and-mutations", "Server Actions and Mutations"),
    ("app/building-your-application/data-fetching/partial-prerendering", "Partial Prerendering"),
    ("app/building-your-application/data-fetching/incremental-static-regeneration", "Incremental Static Regeneration"),
    ("app/building-your-application/data-fetching/composition-patterns", "Data Fetching Composition Patterns"),

    ("app/building-your-application/rendering", "Rendering Overview"),
    ("app/building-your-application/rendering/server-components", "Server Components"),
    ("app/building-your-application/rendering/client-components", "Client Components"),
    ("app/building-your-application/rendering/composition-patterns", "Rendering Composition Patterns"),
    ("app/building-your-application/rendering/partial-prerendering", "Partial Prerendering"),
    ("app/building-your-application/rendering/incremental-static-regeneration", "Incremental Static Regeneration"),
    ("app/building-your-application/rendering/static-vs-dynamic-rendering", "Static vs Dynamic Rendering"),
    ("app/building-your-application/rendering/edge-and-nodejs-runtimes", "Edge and Node.js Runtimes"),

    ("app/building-your-application/caching", "Caching Overview"),
    ("app/building-your-application/caching/4-data-fetching-caches", "Data Fetching Caches"),
    ("app/building-your-application/caching/5-full-route-caches", "Full Route Caches"),
    ("app/building-your-application/caching/6-input-caches", "Input Caches"),
    ("app/building-your-application/caching/7-memoized-caches", "Memoized Caches"),
    ("app/building-your-application/caching/8-router-cache", "Router Cache"),
    ("app/building-your-application/caching/revalidating-caches", "Revalidating Caches"),
    ("app/building-your-application/caching/disabling-caches", "Disabling Caches"),

    ("app/building-your-application/configuring", "Configuring Overview"),
    ("app/building-your-application/configuring/babel", "Babel"),
    ("app/building-your-application/configuring/postcss", "PostCSS"),
    ("app/building-your-application/configuring/tailwind-css", "Tailwind CSS"),
    ("app/building-your-application/configuring/css-modules", "CSS Modules"),
    ("app/building-your-application/configuring/MDX", "MDX"),
    ("app/building-your-application/configuring/sass", "Sass"),
    ("app/building-your-application/configuring/env-vars", "Environment Variables"),
    ("app/building-your-application/configuring/src-directory", "src Directory"),
    ("app/building-your-application/configuring/absolute-imports", "Absolute Imports"),
    ("app/building-your-application/configuring/path-aliases", "Path Aliases"),
    ("app/building-your-application/configuring/custom-server", "Custom Server"),
    ("app/building-your-application/configuring/amp", "AMP Support"),
    ("app/building-your-application/configuring/parallel-routes", "Parallel Routes"),
    ("app/building-your-application/configuring/spa-mode", "Single Page Apps (SPA)"),

    ("app/building-your-application/optimizing", "Optimizing Overview"),
    ("app/building-your-application/optimizing/fonts", "Fonts"),
    ("app/building-your-application/optimizing/images", "Images"),
    ("app/building-your-application/optimizing/metadata", "Metadata"),
    ("app/building-your-application/optimizing/packages", "Package Bundling"),
    ("app/building-your-application/optimizing/instrumentation", "Instrumentation"),
    ("app/building-your-application/optimizing/memory-usage", "Memory Usage"),
    ("app/building-your-application/optimizing/third-party-libraries", "Third Party Libraries"),
    ("app/building-your-application/optimizing/analytics", "Analytics"),
    ("app/building-your-application/optimizing/static-exports", "Static Exports"),
    ("app/building-your-application/optimizing/outside-directory", "Serving from Alternate Path"),
    ("app/building-your-application/optimizing/caching", "Caching"),
    ("app/building-your-application/optimizing/testing", "Testing"),
    ("app/building-your-application/optimizing/partial-prerendering", "Partial Prerendering"),
    ("app/building-your-application/optimizing/build-cache", "Build Cache"),
    ("app/building-your-application/optimizing/after", "after() API"),
    ("app/building-your-application/optimizing/draft-mode", "Draft Mode"),
    ("app/building-your-application/optimizing/turbopack", "Turbopack"),
    ("app/building-your-application/optimizing/composition-patterns", "Composition Patterns"),

    ("app/building-your-application/deploying", "Deploying Overview"),
    ("app/building-your-application/deploying/finalizing", "Finalizing"),
    ("app/building-your-application/deploying/static-exports", "Static Exports"),
    ("app/building-your-application/deploying/iam-integrations", "IAM Integrations"),

    ("app/building-your-application/upgrading", "Upgrading Overview"),
    ("app/building-your-application/upgrading/version-15", "Upgrading to v15"),
    ("app/building-your-application/upgrading/version-14", "Upgrading to v14"),
    ("app/building-your-application/upgrading/app-router-migration", "Migrating from Pages to App Router"),
    ("app/building-your-application/upgrading/codemods", "Codemods"),

    # API Reference
    ("app/api-reference", "API Reference Overview"),

    ("app/api-reference/components", "Components Reference"),
    ("app/api-reference/components/image", "Image Component"),
    ("app/api-reference/components/link", "Link Component"),
    ("app/api-reference/components/script", "Script Component"),
    ("app/api-reference/components/font", "Font"),

    ("app/api-reference/directives", "Directives Reference"),
    ("app/api-reference/directives/use-client", "'use client' Directive"),
    ("app/api-reference/directives/use-server", "'use server' Directive"),
    ("app/api-reference/directives/use-form-status", "useFormStatus()"),
    ("app/api-reference/directives/use-optimistic", "useOptimistic()"),
    ("app/api-reference/directives/use-report-web-vitals", "useReportWebVitals()"),

    ("app/api-reference/file-conventions", "File Conventions Reference"),
    ("app/api-reference/file-conventions/layout", "layout.js"),
    ("app/api-reference/file-conventions/page", "page.js"),
    ("app/api-reference/file-conventions/loading", "loading.js"),
    ("app/api-reference/file-conventions/error", "error.js"),
    ("app/api-reference/file-conventions/not-found", "not-found.js"),
    ("app/api-reference/file-conventions/template", "template.js"),
    ("app/api-reference/file-conventions/not-found", "notFound()"),
    ("app/api-reference/file-conventions/error", "oncaught-error()"),
    ("app/api-reference/file-conventions/error", "onUncaughtError()"),
    ("app/api-reference/file-conventions/global-error", "global-error.js"),
    ("app/api-reference/file-conventions/metadata", "Metadata File Conventions"),
    ("app/api-reference/file-conventions/instrumentation", "instrumentation.js"),
    ("app/api-reference/file-conventions/middleware", "middleware.js"),
    ("app/api-reference/file-conventions/robots", "robots.js"),
    ("app/api-reference/file-conventions/sitemap", "sitemap.js"),
    ("app/api-reference/file-conventions/opengraph-image", "opengraph-image"),
    ("app/api-reference/file-conventions/open-graph-image", "open-graph-image"),
    ("app/api-reference/file-conventions/twitter-image", "twitter-image"),
    ("app/api-reference/file-conventions/icon", "icon"),
    ("app/api-reference/file-conventions/apple-icon", "apple-icon"),
    ("app/api-reference/file-conventions/favicon", "favicon"),

    ("app/api-reference/functions", "Functions Reference"),
    ("app/api-reference/functions/create-next-app", "createNextApp()"),
    ("app/api-reference/functions/next-request", "NextRequest"),
    ("app/api-reference/functions/next-response", "NextResponse"),
    ("app/api-reference/functions/cookies", "cookies()"),
    ("app/api-reference/functions/draft-mode", "draftMode()"),
    ("app/api-reference/functions/fetch", "fetch"),
    ("app/api-reference/functions/redirect", "redirect()"),
    ("app/api-reference/functions/revalidate-path", "revalidatePath()"),
    ("app/api-reference/functions/revalidate-tag", "revalidateTag()"),
    ("app/api-reference/functions/unstable-rethrow", "unstable_rethrow()"),
    ("app/api-reference/functions/send-from-response", "Send Response"),
    ("app/api-reference/functions/user-agent", "User Agent"),
    ("app/api-reference/functions/next-server", "next/server"),

    ("app/api-reference/config", "Config Reference"),
    ("app/api-reference/config/typescript", "next.config.js Options"),

    ("app/api-reference/next-cli", "CLI Reference"),
    ("app/api-reference/next-cli/create-next-app", "create-next-app CLI"),
    ("app/api-reference/next-cli/cli", "next CLI"),

    # Edge Runtime (old docs, may be legacy)
    ("edge", "Edge Runtime"),
    ("edge-api", "Edge API Routes"),
]


# ── Helpers ─────────────────────────────────────────────────────────────────

class TextExtractor(HTMLParser):
    """Extract text from HTML, trying to preserve structure."""

    SKIP_TAGS = {"script", "style", "nav", "footer", "noscript"}
    BLOCK_TAGS = {
        "h1", "h2", "h3", "h4", "h5", "h6", "p", "div", "pre", "code",
        "blockquote", "ul", "ol", "li", "table", "tr", "td", "th",
        "section", "article", "aside", "main",
    }

    def __init__(self):
        super().__init__()
        self.result = []
        self.current_text = ""
        self.skip_depth = 0
        self.tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
        if self.skip_depth > 0:
            return

        if tag in self.BLOCK_TAGS:
            t = self.current_text.strip()
            if t:
                self.result.append(t)
            self.current_text = ""

        if tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():
            level = int(tag[1])
            prefix = "#" * level
            t = self.current_text.strip()
            if t:
                self.result.append("")
                self.result.append(f"{prefix} {t}")
                self.current_text = ""

    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()

        if tag in self.SKIP_TAGS:
            self.skip_depth -= 1

        if self.skip_depth > 0:
            return

        if tag in self.BLOCK_TAGS:
            t = self.current_text.strip()
            if t:
                self.result.append(t)
            self.current_text = ""

    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        self.current_text += data

    def get_text(self):
        t = self.current_text.strip()
        if t:
            self.result.append(t)
        return "\n".join(self.result)


def get_slug(path):
    return path.split("/")[-1] or path.split("/")[-2]


def path_to_filename(path):
    """Convert URL path to a clean filename."""
    slug = get_slug(path)
    # Make safe for filesystem
    slug = re.sub(r'[^a-zA-Z0-9_-]', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug


def fetch_url(url, cache=True):
    """Fetch URL content with caching."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r'[^a-zA-Z0-9_./-]', '_', url.replace('/', '_'))
    cache_file = CACHE_DIR / safe_name

    if cache and cache_file.exists():
        return cache_file.read_text(encoding='utf-8')

    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; CortexBot/1.0)',
            'Accept': 'text/html,application/xhtml+xml,text/markdown,text/plain,*/*',
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode('utf-8')
            if cache:
                cache_file.write_text(content, encoding='utf-8')
            return content
    except Exception as e:
        print(f"  WARN: {e}", file=sys.stderr)
        return None


def html_to_markdown(html, url):
    """Convert HTML page to cleaned markdown-ish text."""
    extractor = TextExtractor()
    try:
        extractor.feed(html)
    except Exception:
        pass
    text = extractor.get_text()

    # Add source URL
    text = f"Source: {url}\n\n{text}"
    return text


def scrape_doc(path, output_dir):
    """Scrape a single doc page."""
    url = f"{BASE_URL}/{path}"
    slug = path_to_filename(path)

    # Try raw markdown first
    md_url = f"{url}.md"
    content = fetch_url(md_url, cache=False)
    if content and len(content) > 500 and not content.strip().startswith('<!DOCTYPE'):
        # Looks like real markdown
        print(f"  [MD] {slug} ({len(content)} chars)")
        return content

    # Try HTML
    content = fetch_url(url)
    if content is None:
        print(f"  [!!] {slug} (failed)")
        return None

    markdown = html_to_markdown(content, url)
    if len(markdown) < 50:
        print(f"  [!!] {slug} (too short: {len(markdown)} chars)")
        return None

    print(f"  [HTML] {slug} ({len(markdown)} chars)")
    return markdown


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    print("Scraping Next.js docs...\n")

    results = {}
    failed = []

    for path, title in DOCS:
        slug = get_slug(path)
        filename = path_to_filename(path) + ".md"
        filepath = DOCS_DIR / filename

        if filepath.exists() and filepath.stat().st_size > 500:
            print(f"  [SKIP] {filename}")
            continue

        content = scrape_doc(path, DOCS_DIR)
        if content:
            # Prepend title as H1 if not present
            if not content.startswith('#'):
                content = f"# {title}\n\n{content}"
            filepath.write_text(content, encoding='utf-8')
            results[path] = {"title": title, "filename": filename, "chars": len(content)}
        else:
            failed.append((path, title))

        time.sleep(0.3)  # Be polite

    # Generate llm.txt
    print("\nGenerating llm.txt...")
    lines = [
        "# Next.js Documentation",
        f"Scraped {len(results)} pages, {len(failed)} failed\n",
    ]

    sections = {}
    for path, title in DOCS:
        parts = path.split("/")
        section = parts[0] if parts[0] != "app" else (
            "Getting Started" if "getting-started" in parts else
            "App Router" if len(parts) > 1 and parts[1] == "build" else
            "App Router" if len(parts) > 1 and parts[1] == "build" else
            "App Router"
        )
        # Better section grouping
        if path.startswith("app/api-reference"):
            section = "API Reference"
        elif path.startswith("app/building-your-application"):
            subsection = parts[3] if len(parts) > 3 else ""
            section = f"Building: {subsection.replace('-', ' ').title()}" if subsection else "App Router"
        elif path.startswith("app/getting-started"):
            section = "Getting Started"
        elif path.startswith("edge"):
            section = "Edge Runtime"

        if section not in sections:
            sections[section] = []
        sections[section].append((path, title))

    for section, items in sections.items():
        lines.append(f"\n## {section}\n")
        for path, title in items:
            slug = path_to_filename(path)
            if path in results:
                lines.append(f"  {slug}.md - {title}")
            else:
                lines.append(f"  {slug}.md - {title} (FAILED)")

    llm_content = "\n".join(lines)
    LLM_TXT.write_text(llm_content, encoding='utf-8')

    print(f"\nDone! {len(results)} files, {len(failed)} failed")
    if failed:
        print("Failed:", [p for p, _ in failed[:10]])


if __name__ == "__main__":
    main()
