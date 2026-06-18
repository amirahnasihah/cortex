# Nuxt — Testing

## @nuxt/test-utils

Official testing utilities.

```bash
npx nuxi@latest module add test-utils
```

### Unit Testing (Vitest)

```ts
// vitest.config.ts
import { defineVitestConfig } from '@nuxt/test-utils/config'

export default defineVitestConfig({
  test: {
    environment: 'nuxt',
  },
})
```

```ts
// tests/unit/counter.test.ts
import { describe, it, expect } from 'vitest'
import { useCounter } from '~/composables/useCounter'

describe('useCounter', () => {
  it('should increment', () => {
    const { count, increment } = useCounter()
    increment()
    expect(count.value).toBe(1)
  })
})
```

### Component Testing

```ts
import { mountSuspended } from '@nuxt/test-utils/runtime'
import MyComponent from '~/components/MyComponent.vue'

describe('MyComponent', () => {
  it('renders', async () => {
    const component = await mountSuspended(MyComponent)
    expect(component.text()).toContain('Hello')
  })
})
```

### E2E Testing (Playwright)

```ts
// tests/e2e/example.test.ts
import { test, expect } from '@nuxt/test-utils/e2e'

test('homepage', async ({ page }) => {
  await page.goto('/')
  await expect(page.locator('h1')).toHaveText('Welcome')
})
```

### Setup

```ts
// tests/setup.ts
import { beforeAll, afterAll } from 'vitest'
import { setup, teardown } from '@nuxt/test-utils/e2e'

beforeAll(async () => {
  await setup({ rootDir: '.' })
})

afterAll(async () => {
  await teardown()
})
```

## Running Tests

```bash
npx nuxt test
# or
vitest
```

## Test Directory Structure

```
tests/
  unit/
    composables/
    components/
  e2e/
    pages/
```

## Config

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  testUtils: {
    testMatch: 'tests/**/*.test.ts',
  },
})
```
