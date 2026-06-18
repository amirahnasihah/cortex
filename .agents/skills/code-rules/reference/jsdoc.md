# JSDoc blocks

Put a JSDoc block at the **very top** of every component, page, util, and hook.

## Template

```ts
/**
 * [Module]: [Name]
 *
 * @file [path/to/this/file]
 * @description [One sentence: what this file is].
 * @module [Module]
 */
```

## Examples

Vue SFC:

```vue
<script setup lang="ts">
/**
 * Components: PrimaryButton
 *
 * @file @/components/ui/primary-button.vue
 * @description Primary button for CTAs.
 * @module Components
 */
</script>
```

Hook / composable:

```ts
/**
 * Hooks: useCustomFetch
 *
 * @file @/composables/use-custom-fetch.ts
 * @description Reusable fetch hook with custom settings.
 * @returns success bool, message string
 * @module Hooks
 */
const useCustomFetch = (): { success: boolean; message: string } => {
  // …
}
```
