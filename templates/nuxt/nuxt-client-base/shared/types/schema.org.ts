/**
 * Schema.org types
 * Minimal type definitions for structured data
 * Extend as needed per project
 */

export interface SchemaOrganization {
  '@type': 'Organization'
  '@id'?: string
  name: string
  url: string
  logo?: {
    '@type': 'ImageObject'
    url: string
  }
  sameAs?: string[]
}

export interface SchemaWebSite {
  '@type': 'WebSite'
  '@id'?: string
  url: string
  name: string
  publisher: {
    '@id': string
  }
}

export interface SchemaArticle {
  '@context': 'https://schema.org'
  '@type': 'Article' | 'NewsArticle' | 'BlogPosting'
  headline: string
  description?: string
  image?: string
  datePublished: string
  dateModified?: string
  author: SchemaOrganization | SchemaPerson
  publisher: SchemaOrganization
}

export interface SchemaPerson {
  '@type': 'Person'
  name: string
  url?: string
}

export interface SchemaBreadcrumbList {
  '@context': 'https://schema.org'
  '@type': 'BreadcrumbList'
  itemListElement: SchemaListItem[]
}

export interface SchemaListItem {
  '@type': 'ListItem'
  position: number
  name?: string
  item?: string | Record<string, unknown>
}
