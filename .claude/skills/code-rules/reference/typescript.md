# TypeScript — patterns & examples

Detail for the rules in `SKILL.md`. The theme throughout: **one source of truth
per type, and types that can't express invalid states.**

## Parse, don't validate

Runtime boundaries (API, `JSON.parse`, form input, `catch`) are genuinely
`unknown`. Don't cast — parse into a typed shape once, at the edge.

```ts
import { z } from "zod"

const UserSchema = z.object({ id: z.string(), name: z.string() })
type User = z.infer<typeof UserSchema>          // type derived from the schema

const user = UserSchema.parse(await res.json()) // unknown → User (validated)
// past this line `user` is typed; no more `unknown` inside the app
```

No validator lib? Hand-write a type guard:

```ts
const isUser = (x: unknown): x is User =>
  typeof x === "object" && x !== null &&
  "id" in x && typeof (x as Record<string, unknown>).id === "string"
```

`as` is allowed **only** as a genuine escape hatch (e.g. inside a guard you've
already checked) — never to skip validation at a boundary.

## Make illegal states unrepresentable

```ts
// ❌ allows {loading:true, error:"x", data:…} — nonsense combos compile
type State = { loading: boolean; data?: Data; error?: string }

// ✅ only the three real states exist
type State =
  | { status: "loading" }
  | { status: "ok"; data: Data }
  | { status: "error"; error: string }
```

Narrowing on `status` then gives `data` / `error` safely, no optional chaining.

## Derive, don't duplicate

```ts
const ROUTES = { home: "/", about: "/about" } as const
type Route = (typeof ROUTES)[keyof typeof ROUTES]   // "/" | "/about"

type FetchUserReturn = ReturnType<typeof fetchUser>
```

If a type and a value describe the same thing, derive the type from the value.

## `satisfies` over `as`

```ts
const config = { port: 3000 } as Config         // ❌ widens/lies, kills inference
const config = { port: 3000 } satisfies Config   // ✅ checks; keeps literal types
```

## Enums → `as const` unions

```ts
// ❌ enum Role { Admin, User }   — extra runtime, awkward interop
const ROLE = { admin: "admin", user: "user" } as const
type Role = (typeof ROLE)[keyof typeof ROLE]      // "admin" | "user"
```

## Errors are `unknown`

```ts
try {
  // …
} catch (e: unknown) {
  if (e instanceof ApiError) handleApi(e)
  else throw e            // don't swallow what you can't handle
}
```

## No floating promises

```ts
doAsync()                                           // ❌ unhandled rejection, no ordering
await doAsync()                                     // ✅
void doAsync()                                      // ✅ explicit fire-and-forget
const [a, b] = await Promise.all([getA(), getB()])  // independent → run in parallel
```
