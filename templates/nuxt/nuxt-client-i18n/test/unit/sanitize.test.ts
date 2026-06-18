import { describe, it, expect } from 'vitest'
import { sanitizeRichHtml } from '../../shared/utils/sanitize'

describe('sanitizeRichHtml', () => {
  it('returns empty string for non-string input', () => {
    expect(sanitizeRichHtml(null as unknown as string)).toBe('')
    expect(sanitizeRichHtml(undefined as unknown as string)).toBe('')
  })

  it('strips script tags from CMS rich text', () => {
    const html = '<p>Hello</p><script>alert("xss")</script><p>World</p>'
    expect(sanitizeRichHtml(html)).toBe('<p>Hello</p><p>World</p>')
  })

  it('strips event handler attributes (on*)', () => {
    const html = '<p onclick="alert(1)">Click</p><a onmouseover="evil()">Link</a>'
    expect(sanitizeRichHtml(html)).not.toContain('onclick')
    expect(sanitizeRichHtml(html)).not.toContain('onmouseover')
  })

  it('preserves safe rich editor output (paragraphs, links, lists)', () => {
    const html = '<p>Text with <strong>bold</strong> and <a href="/">link</a>.</p><ul><li>Item</li></ul>'
    expect(sanitizeRichHtml(html)).toBe(html)
  })

  it('handles empty string', () => {
    expect(sanitizeRichHtml('')).toBe('')
  })
})
