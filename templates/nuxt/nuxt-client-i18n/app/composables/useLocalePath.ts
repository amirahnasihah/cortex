/**
 * Locale path — single entry point for locale-aware routes.
 * With @nuxtjs/i18n, the module's useLocalePath is auto-imported; this stub
 * ensures the structure is consistent. In projects with i18n, use the
 * composable provided by @nuxtjs/i18n (same name) for real locale paths.
 */
export function useLocalePath() {
  return (path: string) => path
}
