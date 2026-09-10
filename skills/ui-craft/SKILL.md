---
name: ui-craft
description: Build and refine user interfaces that do not look agent-generated. Reaches for shadcn/ui before writing anything by hand, adapts what it takes to the project's own design system rather than pasting defaults, runs Impeccable's deterministic detector to catch AI-slop patterns, and publishes genuinely reusable components to a shadcn registry so they can be installed by name. Use for any UI work - a new page, screen or component, a redesign, "make this look better", a design review, or setting up a component library.
metadata:
  version: 1.1.0
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

### When there is no React project

shadcn ships `.tsx` and assumes React, Tailwind and a build step. If the
deliverable is a single HTML file, an email, a slide, a canvas, a Framer or
Webflow page, or anything else the CLI cannot install into, then **steps 1, 2
and 5 do not apply and you skip straight to 3**. Do not spend a paragraph
justifying that you are writing a tab strip by hand; the format excluded the
catalogue, not your judgement.

Two things still carry over, and they are the ones that matter:

- The **catalogue is a checklist of what a component has to do**, even when you
  cannot install it. Read shadcn's tabs before hand-rolling tabs and you inherit
  the roving tabindex, the `aria-selected`, and the arrow-key behaviour you were
  about to forget.
- **Interactivity without a framework is where the bugs are.** CSS-only state
  via `:checked` and sibling combinators is fragile: the `~` and `+` combinators
  only reach *siblings*, so an input nested inside the thing it is meant to
  style will silently never match. Two of the four pages this skill was tested
  on shipped exactly that bug and only rendering caught it.

### When there is no project at all

Step 0 says read `DESIGN.md`. For a one-off page there is no repo and no
`DESIGN.md`, and that is the common case, not an edge case. Then step 0 becomes:
**decide the direction in one sentence, name the token set you are inventing,
and write both at the top of the file as a comment.** That comment is the
design system for a page that has no other record of one.

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
- **Both themes, unless you commit to one on purpose.** Light and dark, checked,
  not assumed. But a page whose subject *is* a single light condition - a moth
  trap at 2am, a cinema, a darkroom - may commit to one palette. Then say so in
  the direction sentence and paint every colour explicitly, so it holds on any
  host background. What is not allowed is shipping one theme by accident.
- **Avoid the default typefaces.** Inter, Arial and the system stack are what
  an agent reaches for when it has not chosen. Pick a face for a reason and be
  able to state the reason.
- **No bounce or elastic easing.** It dates the work instantly.
- **Render it and look at it. This is the check.** Build it, serve it, open it,
  resize it to 375px. A page that has only ever existed in a diff has not been
  reviewed. When this skill was tested, the detector passed a page clean that
  had radio buttons rendering as raw native dots and a price line wrapping onto
  a second row. Only opening it found either.
- **Run the detector too, but know what it is.** It is a linter: deterministic,
  fast, no API key, and blind to everything it cannot parse. Deterministic is
  not the same as correct. A clean run means "no known string patterns matched",
  not "this is good". See `references/impeccable.md` for what it cannot see.
- **Never edit code to satisfy the detector when you know it is wrong.** If a
  finding is a parser limitation, say so, leave the better CSS in place, and
  record why. Rewriting good code to launder a false positive is the same
  failure as writing to a metric.

## References

| File | Read it when |
|---|---|
| `references/shadcn.md` | Choosing or installing a component, or setting shadcn up in a project that has none |
| `references/impeccable.md` | Installing the detector, wiring the edit hook, or interpreting what it flags |
| `references/new-component.md` | Nothing in the catalogue fits and you are about to write one, and when publishing it |

## Two things the rules do not cover

**Content is the design.** On every page this skill was tested against, the
thing that made it work was what it said, not how it was set: naming who each
rule protects, publishing last year's real damage figures, admitting which
routes still need a phone call. A page with nothing to say cannot be rescued by
typography, and no detector will ever tell you that.

**Encode meaning in more than colour.** If a distinction matters - confident vs
uncertain, bookable vs not, in vs out - carry it in texture, weight, shape or a
word as well as hue. It survives greyscale, colour blindness and a bad phone
screen in sunlight. The best single decision made across the test pages was
rendering statistical uncertainty as a hatched fill rather than a number.

## What "stand out" actually means

Not louder. Decided. A page reads as designed when a stranger can name the
choice behind it: this face because the subject is editorial, this accent
because it comes from the product's own material, this density because the
data is scanned rather than read. The detector removes the tells; it cannot
supply the point of view. That part is a judgement, it should be stated in one
sentence before any code is written, and `DESIGN.md` is where it gets recorded
so the next session does not re-litigate it.
