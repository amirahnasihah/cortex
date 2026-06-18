/**
 * Sanitize CMS rich editor HTML for safe frontend output.
 * Uses shared/utils/sanitize. Use when rendering microCMS rich text (e.g. body, description).
 */

import { sanitizeRichHtml } from '../../shared/utils/sanitize'

export function useSanitize() {
  return {
    sanitize: sanitizeRichHtml,
  }
}
