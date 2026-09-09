---
name: ui-craft
description: Build and refine user interfaces that do not look agent-generated. Reaches for shadcn/ui before writing anything by hand, adapts what it takes to the project's own design system rather than pasting defaults, runs Impeccable's deterministic detector to catch AI-slop patterns, and publishes genuinely reusable components to a shadcn registry so they can be installed by name. Use for any UI work - a new page, screen or component, a redesign, "make this look better", a design review, or setting up a component library.
metadata:
  version: 1.0.0
---

# UI craft

Most agent-built interfaces fail the same way. They are not broken, they are
generic: Inter on a white card, a grey subtitle, three status chips, a shadow
on everything, and no evidence anyone decided anything. This skill exists to
make the decisions explicit and to reuse work rather than regenerate it.

Three tools do most of the lifting, and each covers what the others miss:

| Tool | What it is for | Where it comes from |
|---|---|---|
| **shadcn/ui** | The component you should not be writing. 70+ accessible primitives you own outright once added. | `ui.shadcn.com/docs/components` |
| **Impeccable** | A deterministic detector, 61 rules, that catches the defaults an agent reaches for without thinking. | `impeccable.style` / `github.com/pbakaus/impeccable` |
| **Your own registry** | Anything you built twice. Published so it is installed by name next time, not re-derived. | `ui.shadcn.com/docs/registry` |

## The order is fixed

Skipping step 0 is what produces a page that ignores the design system it was
dropped into.

```
0. GROUND     read what already exists   -> DESIGN.md / PRODUCT.md, the token
                                            file, the real component inventory.
                                            Never invent a palette a project
                                            already has.
1. REUSE      shadcn first               -> npx shadcn@latest add <name>
                                            If a primitive exists, take it.
                                            Writing your own Dialog is a bug.
2. ADAPT      make it belong             -> retheme to the project's tokens.
                                            A raw shadcn paste is recognisable
                                            on sight; that is the slop.
3. BUILD      only when nothing fits     -> to the bar in references/new-component.md
4. CHECK      run the detector           -> npx impeccable detect <path>
                                            Deterministic, no API key, no LLM.
5. PUBLISH    if it will be used again   -> registry item, GitHub, then offer it
                                            to the shadcn registry directory
```

**Gate before step 3:** search the shadcn catalogue and the project's existing
components first, and say what you searched. "There is no shadcn component for
this" is a claim that has to be checked, not assumed - the catalogue includes
things people routinely rebuild by hand, like Command, Combobox, Resizable,
Sidebar and Chart.

## Rules that must not be broken

- **Read the design system before writing a line.** If `DESIGN.md` exists, it
  wins. If it does not, derive tokens from what the project already ships and
  say so. Never introduce a second palette or a second type scale.
- **Never paste a shadcn component unedited into a themed project.** It arrives
  in shadcn's defaults. Retheme it to the project's tokens in the same commit,
  or it reads as borrowed.
- **No pure black, no pure grey.** Tint neutrals toward the accent. This is an
  Impeccable rule and it is the single fastest way a palette stops looking
  generated.
- **Not everything is a card.** Cards inside cards is a detector rule and a
  reliable sign nobody decided on a hierarchy.
- **Avoid the default typefaces.** Inter, Arial and the system stack are what
  an agent reaches for when it has not chosen. Pick a face for a reason and be
  able to state the reason.
- **No bounce or elastic easing.** It dates the work instantly.
- **Run the detector before claiming the UI is done.** It is deterministic, it
  takes seconds, and it does not need an API key. "It looks fine" is not a
  check.
- **Show the component in place before declaring it finished.** Build it, render
  it, look at it. A component that has only ever existed in a diff has not been
  reviewed.

## References

| File | Read it when |
|---|---|
| `references/shadcn.md` | Choosing or installing a component, or setting shadcn up in a project that has none |
| `references/impeccable.md` | Installing the detector, wiring the edit hook, or interpreting what it flags |
| `references/new-component.md` | Nothing in the catalogue fits and you are about to write one, and when publishing it |

## What "stand out" actually means

Not louder. Decided. A page reads as designed when a stranger can name the
choice behind it: this face because the subject is editorial, this accent
because it comes from the product's own material, this density because the
data is scanned rather than read. The detector removes the tells; it cannot
supply the point of view. That part is a judgement, it should be stated in one
sentence before any code is written, and `DESIGN.md` is where it gets recorded
so the next session does not re-litigate it.
