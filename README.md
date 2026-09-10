# bhaumik-agent-skills

Private agent skills for Claude Code.

**[bhaumikmistry.github.io/bhaumik-agent-skills](https://bhaumikmistry.github.io/bhaumik-agent-skills/)**
— the skills, what each one refuses to do, and four example pages rendered live.

## Usage

```bash
claude --plugin-dir /path/to/bhaumik-agent-skills
```

## Examples

Four landing pages built by four agents with the `ui-craft` skill. No visual
direction was given to any of them — the test was whether they would converge on
the same generated-looking default. They did not.

| Page | Brief | Direction it committed to | Set in |
|---|---|---|---|
| [Pitchside](examples/pitchside.html) | Grassroots football call-offs | A public notice pinned to a clubhouse door | Public Sans |
| [Nightfall](examples/nightfall.html) | Moth recording for naturalists | A night-lit field ledger, machine in actinic blue | Newsreader |
| [The Lending Shed](examples/lending-shed.html) | A tool library | A workshop shadow board | Archivo |
| [Couchette](examples/couchette.html) | European night trains | A printed continental timetable | Bodoni Moda |

Nightfall's best decision is worth calling out: it draws statistical uncertainty
as a **hatched fill** rather than a percentage, so "these two moths cannot be
separated without dissection" survives greyscale and colour blindness.

## The landing page is generated

`index.html` is built from the skills themselves by `scripts/build_site.py` and
must never be edited by hand. Adding a skill without documenting it **fails the
build**. See [CLAUDE.md](CLAUDE.md).

## Skills

### coach

Communication coaching skill. Four modes:

| Mode | Trigger | What it does |
|------|---------|--------------|
| **Draft** | "help me write", "draft a message to" | Draft messages with communication principles applied |
| **Review** | "how does this sound", paste a message | Review a draft against principles, flag anti-patterns, offer rewrites |
| **Reflect** | "review my slack", "what patterns do you see" | Review Slack history for communication patterns |
| **Coach** | "coach me for a meeting", "how should I approach" | Prepare for difficult conversations |

Based on 5 communication commitments:
1. Front-load context before asking for input
2. Name the impasse instead of bypassing
3. Understand what they're optimizing for
4. Reduce the surface area of disagreement
5. Bring people along rather than teach/convince

### interviewer

Async interview series skill (Zero Token, All Human). Handles outreach, question crafting, follow-ups, and pipeline management.

| Mode | Trigger | What it does |
|------|---------|--------------|
| **Outreach** | "draft outreach", "new target", "reach out to" | Cold outreach with story-driven hooks by platform |
| **Questions** | "prepare questions", "Q1", "next question" | Craft questions using the arc (origin→craft→tension→human→closing) |
| **Follow-up** | "follow up with", "nudge", "they haven't replied" | Thread revival, short-answer pushback, platform escalation |
| **Tone** | (loaded automatically) | Friendly, curious, story-telling voice guide |

Key principles:
- Never sound AI-written — be a person
- One question at a time, build on exact words from their answer
- Tell a discovery story as the hook (how you found them)
- Reference something specific they made/wrote/built
- Create tension or contrast they have to resolve

### architecture-map

Turn **anything** — a repo, an idea, a rough thought, or one/many design docs —
into an interactive isometric "city" map of a system's architecture. One
self-contained HTML page: a zoomable/pannable iso diagram on the left, a
click-to-inspect side panel on the right, light + dark themes built in.

| Stage | What it does |
|-------|--------------|
| **1 · Knowledge doc** | Synthesize the authored understanding — groups (districts), subsystems (nodes) with role/weight/tech, edges, and the primary flow. Measured for a repo; authored for an idea or design doc. |
| **2 · Interactive page** | Copy the bundled engine (`assets/architecture-map.html`) and fill one `DATA` block. Auto-layout, zoom/pan, click→panel, and theming are already solved. |

Fires on: "architecture diagram", "system map", "codebase overview", "show me
how this works", "visualize this design". Open `assets/architecture-map.html`
to see a complete worked example (an RPA browser-automation platform).

### fpl-gameweek

Fantasy Premier League gameweek cycle. Runs the whole loop in a fixed order, because the opposition read is an input to the plan rather than a report about it.

| Step | Trigger | What it does |
|------|---------|--------------|
| **Score** | gameweek settles | Scores every plan against the real result — including the ones not played — with autosubs applied |
| **Study** | after scoring | Pulls every league, studies the top finishers, builds a player board of who delivered |
| **Read** | after the study | Writes what worked, what did not, and what it changes, with the survivorship caveat stated |
| **Strategy** | before planning | Squad-weighted fixture difficulty five to six weeks out, a stance per week, chip timing |
| **Plan** | last | Three ranked plans — no hit, -4, -8 — each citing the read |
| **Publish** | after any change | Rebuilds and republishes the dashboard artifact |

Techniques that make it work:

- **Strip the chips before comparing.** Rescore every rival normally — no bench boost, no triple captain. A 67-point gap became 22 once the chips came out, and half the "leaders" had picked a worse squad.
- **Bench before transfer.** A flagged player is only a problem if he has to start. Benching one cost 0.1 expected points; the other, with no cover, cost 2.6. Same transfer, twenty-six times the effect.
- **Judgement, not optimizers.** A scoring formula was tried and never bought the highest-scoring player in the game, because price penalised him in the z-score. Scripts fetch, check constraints and render; people pick.
- **Score the counterfactuals.** Every plan is scored after the fact, so over a season the record shows whether the hits were worth taking.

Needs the `fpl` MCP server (`uv tool install fpl-mcp`) with an authenticated FPL account.

### ui-craft

Build interfaces that do not read as agent-generated. Three tools, each covering
what the others miss.

| Step | What happens |
|------|--------------|
| **Ground** | Read `DESIGN.md` / `PRODUCT.md` and the real token file before writing anything |
| **Reuse** | `npx shadcn@latest add <name>` — writing your own Dialog or Combobox is a bug |
| **Adapt** | Retheme to the project's tokens in the same commit; a raw shadcn paste is the tell |
| **Build** | Only when the catalogue genuinely has nothing, and to a stated bar |
| **Check** | `npx impeccable detect` — 61 deterministic rules, no API key, no model |
| **Publish** | Registry item → GitHub → the shadcn community directory, in that order |

The slop rules worth knowing before you start: no pure black or grey (tint
neutrals), no grey text on coloured backgrounds, not everything is a card and
never a card inside a card, avoid Inter/Arial/system defaults unless chosen for
a reason, no bounce or elastic easing.

- shadcn/ui: https://ui.shadcn.com/docs/components
- Impeccable: https://impeccable.style · https://github.com/pbakaus/impeccable
- Registries: https://ui.shadcn.com/docs/registry

### not-ai

Rewrites text to strip the patterns that make writing sound machine-generated. Uses an anti-pattern catalog derived from Wikipedia's "Signs of AI writing" as the rubric.

### arsenal-match-writeup

Turns a played Arsenal fixture into a post on bhaumikmistry.com and a row on the gooner tracker. Checks the goal timeline against the ESPN report and the quotes against the post-match coverage before writing a word, updates `fixtures.json`, then runs the prose through not-ai and the slop detector.

Written after a pass over that blog found 28 posts whose Arteta quotes were every one of them invented.

## Structure

```
.claude-plugin/plugin.json
.codex-plugin/plugin.json
skills/
├── coach/
│   ├── SKILL.md            ← dispatcher
│   ├── principles.md       ← the 5 commitments + anti-patterns + positive patterns
│   ├── draft-mode.md       ← drafting flow
│   ├── review-mode.md      ← message review flow
│   ├── reflect-mode.md     ← Slack history review flow
│   └── coach-mode.md       ← meeting/conversation prep flow
├── interviewer/
│   ├── SKILL.md            ← dispatcher
│   ├── tone.md             ← voice & personality guide
│   ├── question-craft.md   ← question anatomy, arc, techniques
│   ├── outreach.md         ← cold outreach by platform
│   ├── follow-up.md        ← nudge strategies & thread revival
│   └── data/
│       └── target-list.md  ← pipeline reference & series info
├── not-ai/
│   ├── SKILL.md            ← rewrite rules
│   └── anti-patterns.md    ← detection rubric
├── arsenal-match-writeup/
│   ├── SKILL.md            ← verify, write, update the tracker
│   └── post-format.md      ← what a match post looks like
└── architecture-map/
    ├── SKILL.md            ← two-stage flow (knowledge doc → interactive page)
    ├── references/
    │   ├── knowledge-doc.md  ← Stage 1: synthesize the understanding
    │   └── rendering.md      ← Stage 2: DATA schema, projection, solved gotchas
    └── assets/
        └── architecture-map.html  ← engine + worked example (copy & swap DATA)
```

## Adding new skills

Create a new directory under `skills/` with a `SKILL.md` frontmatter file:

```yaml
---
name: <skill-name>
description: <when this skill fires — under 500 chars>
---
```
