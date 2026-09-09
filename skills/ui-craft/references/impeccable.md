# Impeccable

Site: https://impeccable.style  ·  Source: https://github.com/pbakaus/impeccable

Design guidance built for coding agents. It began as Anthropic's frontend-design
skill and grew into one skill, 23 commands and **61 deterministic detector
rules**. The detector is the part that matters most here: it runs without an API
key and without a model, so it is a real check rather than a second opinion from
the same kind of system that wrote the code.

## Installing

```bash
npx impeccable install          # detects the harness, installs native hooks
npx impeccable update           # later
```

For Claude Code specifically:

```
/plugin marketplace add pbakaus/impeccable
```

Then once per project, in the agent chat:

```
/impeccable init
```

`init` records **durable product context** in `PRODUCT.md`: audience, purpose,
operating context, constraints, voice. This is deliberately separate from visual
direction, so later commands do not confuse what the product *is* with how it
currently *looks*.

## The two files, and why they are separate

| File | Holds | Written by |
|---|---|---|
| `PRODUCT.md` | Audience, purpose, constraints, voice, evidence. Changes rarely. | `/impeccable init` |
| `DESIGN.md` | The visual system actually in the code: tokens, type scale, spacing, motion. | `/impeccable document` |

`/impeccable document` generates `DESIGN.md` **from the existing code**, which
makes it the fastest honest answer to "what is this project's design system"
when nobody wrote one down. Run it before redesigning anything you did not build.

## The detector

```bash
npx impeccable detect <dir|file.html|url>     # human-readable
npx impeccable detect <path> --json            # machine-readable
```

No API key, no network model call, same answer every run. That is why it belongs
in the release path and not in a review conversation.

Installed hooks run it automatically on direct edits to UI files. On Cursor the
hook can block a bad write before it lands; on Claude Code and GitHub Copilot the
findings surface after the edit.

## The rules worth knowing before you write anything

These are the AI-slop defaults the detector was built around. Knowing them
up front is cheaper than being told afterwards.

- **Overused fonts.** Arial, Inter, the system stack. Not forbidden, but if one
  is used it should be a decision with a reason, not the fallback.
- **Grey text on coloured backgrounds.** Fails contrast and looks unfinished.
- **Pure black and pure grey.** Always tint neutrals toward the accent. This one
  change does more for "not generated" than any other single edit.
- **Cards around everything, and cards inside cards.** A sign no hierarchy was
  chosen. Nesting is the stronger tell.
- **Bounce and elastic easing.** Dates the work immediately. Prefer plain
  ease-out and short durations.

## Commands, by when you would reach for one

23 exist; these are the ones that carry the weight.

| Stage | Command | Does |
|---|---|---|
| Once per project | `init` | Records `PRODUCT.md` |
| Before coding | `shape` | UX/UI planning |
| Building | `craft` | Full design-then-build with visual iteration |
| Targeted fixes | `typeset`, `layout`, `colorize`, `animate` | One dimension at a time |
| Review | `critique` | UX review: hierarchy, clarity |
| Review | `audit` | Technical: accessibility, performance, responsiveness |
| Edge cases | `harden` | Error states, empty states, failure paths |
| Iterate live | `live` | Variant iteration against the running app |
| Ship | `polish` | Final pass |
| Record | `document` | Writes `DESIGN.md` |

`critique` and `audit` are not the same check and neither replaces the detector.
`critique` is judgement about hierarchy, `audit` is accessibility and
performance, `detect` is the deterministic rule set. A serious pass runs the
detector always, and adds `critique` when the layout is new.

## How this fits the rest of the skill

The detector removes the tells. It cannot supply a point of view, and it will
happily pass a page that is competent and forgettable. Decide the direction
first, in one sentence, then let the detector stop you shipping the defaults
underneath it.
