# Building a new component, and publishing it

Reached only when the shadcn catalogue and the project's own components have
both been checked and neither fits. Say what you checked before you start.

## The bar

A component that is going to be published has to clear all of this. A component
that is genuinely one-off does not - but be honest about which one you are
writing, because "I'll generalise it later" almost never happens.

- **One job.** If the name needs "and" in it, it is two components.
- **Controlled and uncontrolled both work.** Accept `value` + `onChange`, fall
  back to internal state when neither is passed.
- **Keyboard reachable.** Tab order, Enter and Space where they are expected,
  Escape to dismiss anything that overlays. If it traps focus, it releases it.
- **Announced.** A real role, a label, and state changes that reach a screen
  reader. `aria-*` guessed at is worse than none.
- **Themed through tokens, never literals.** No hex in the component. This is
  what makes it portable to the next project.
- **Both themes.** Light and dark, checked, not assumed.
- **Motion respects `prefers-reduced-motion`.** And no bounce.
- **Empty, loading and error states exist.** `/impeccable harden` is the prompt
  for this if you would rather be asked than remember.
- **The detector passes.** `npx impeccable detect <file>` before it is offered
  to anyone.

## Publishing it

Three audiences, in order. Do not skip to the third.

### 1. The project's own registry

Even a registry only you consume is worth it - it turns "copy that file from the
other repo" into a command.

`registry.json` at the repo root:

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "bhaumik",
  "homepage": "https://www.bhaumikmistry.com",
  "items": [
    {
      "name": "stat-strip",
      "type": "registry:ui",
      "title": "Stat strip",
      "description": "A row of labelled figures with an optional note under each.",
      "files": [{ "path": "components/ui/stat-strip.tsx", "type": "registry:ui" }],
      "registryDependencies": ["separator"],
      "dependencies": ["clsx@^2.1.0"]
    }
  ]
}
```

`name`, `type`, `title`, `description` and `files` are all required, and each
file needs `path` and `type`. Declare `registryDependencies` for other registry
items and `dependencies` for npm packages, or installs break on someone else's
machine.

Build and serve:

```bash
npx shadcn@latest build          # flattens to JSON under /r
```

Then it installs by URL:

```bash
npx shadcn@latest add https://www.bhaumikmistry.com/r/stat-strip.json
```

Or, once a consumer registers the namespace:

```bash
npx shadcn@latest registry add @bhaumik=https://www.bhaumikmistry.com/r/{name}.json
npx shadcn@latest add @bhaumik/stat-strip
```

Conventions worth following: keep items under `registry/[STYLE]/[NAME]`, and use
`@/registry` paths in imports so a consumer's alias resolves.

### 2. GitHub

The registry JSON is the install path; the repo is where the component is read,
argued with and improved. It needs:

- The component, its story or a demo route, and its tests
- A README section showing the rendered result, the props, and the one decision
  the component makes that a reader would otherwise ask about
- The `registry.json` entry in the same commit as the component, so the two
  never disagree

### 3. The shadcn registry directory

Once it is installable and documented, it can be listed among the community
registries on the shadcn docs site. Only offer something that has survived real
use in at least two places - a component published from a single call site is
usually still shaped like that call site.

## When not to publish

Most components. Publishing is a maintenance commitment: an install path that
must keep working, a dependency list that must stay honest, and someone else's
build that breaks when it does not. Build it in the project, use it twice, and
publish it on the second use when the shape has stopped moving.
