/**
 * Standard microCMS layer — only ONE composable for all microCMS access.
 * No direct fetch in components. No duplicate API logic.
 */

export function useMicrocms() {
  const config = useRuntimeConfig()
  const apiKey = config.public.microcmsApiKey as string
  const baseUrl = 'https://example.microcms.io/api/v1'

  async function get<T>(endpoint: string, options?: { query?: Record<string, string> }): Promise<T> {
    const query = new URLSearchParams(options?.query).toString()
    const url = `${baseUrl}${endpoint}${query ? `?${query}` : ''}`
    const res = await $fetch<T>(url, {
      headers: {
        'X-MICROCMS-API-KEY': apiKey,
      },
    })
    return res
  }

  return { get }
}
