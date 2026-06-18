/**
 * Shared Schema.org types (used by layout and useSeo).
 */
export interface Organization {
  '@type': 'Organization'
  name: string
  url: string
}

export interface WebSite {
  '@type': 'WebSite'
  name: string
  url: string
  publisher: { '@id': string }
}
