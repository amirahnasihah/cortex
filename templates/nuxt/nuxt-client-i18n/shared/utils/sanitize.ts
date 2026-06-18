/**
 * Sanitize HTML from CMS rich editor for safe frontend output.
 * Removes script tags and event handler attributes (on*) to prevent XSS.
 * For stricter sanitization (allowlist of tags/attrs), use isomorphic-dompurify or similar in the project.
 */

const SCRIPT_REGEX = /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi
const ON_ATTR_REGEX = /\s+on\w+\s*=\s*["'][^"']*["']/gi

export function sanitizeRichHtml(html: string): string {
  if (typeof html !== 'string') return ''
  return html
    .replace(SCRIPT_REGEX, '')
    .replace(ON_ATTR_REGEX, '')
    .trim()
}
