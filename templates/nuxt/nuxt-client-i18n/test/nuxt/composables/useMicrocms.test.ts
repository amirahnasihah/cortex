import { describe, it, expect, vi } from 'vitest'
import { mockNuxtImport } from '@nuxt/test-utils/runtime'

const $fetchMock = vi.fn()
mockNuxtImport('$fetch', () => $fetchMock)

describe('useMicrocms', () => {
  it('get() returns data from $fetch with correct URL and API key header', async () => {
    const mockData = { id: '1', title: 'Test' }
    $fetchMock.mockResolvedValue(mockData)

    const { get } = useMicrocms()
    const result = await get<{ id: string; title: string }>('news')

    expect($fetchMock).toHaveBeenCalledWith(
      expect.stringContaining('https://example.microcms.io/api/v1/news'),
      expect.objectContaining({
        headers: expect.objectContaining({ 'X-MICROCMS-API-KEY': expect.any(String) }),
      }),
    )
    expect(result).toEqual(mockData)
  })

  it('get() appends query params when options.query is provided', async () => {
    $fetchMock.mockResolvedValue({})

    const { get } = useMicrocms()
    await get('news', { query: { limit: '10', offset: '0' } })

    expect($fetchMock).toHaveBeenCalledWith(
      expect.stringMatching(/\?.*limit=10.*offset=0/),
      expect.any(Object),
    )
  })
})
