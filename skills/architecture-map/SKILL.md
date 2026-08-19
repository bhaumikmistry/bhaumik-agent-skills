---
name: architecture-map
description: Turn anything — a repository, an idea, a rough thought, a design doc, or a set of design docs — into an interactive isometric "city" map of a system's architecture: one self-contained HTML page with a zoomable/pannable iso diagram, a click-to-inspect side panel, and light + dark themes built in. Works in two stages — first synthesize a knowledge doc (the authored understanding), then render it to the interactive page from a bundled engine. Use when someone wants to see, explain, pitch, or onboard people to how a system fits together, or asks for an architecture diagram, system map, codebase overview, or "show me how this works". Adapts to any input; re-run to refresh.
metadata:
  version: 2.0.0
---

# Architecture map

Turn a system into a place you can walk around: an isometric city where every
building is a subsystem sized by its weight, every line is a real (or intended)
call path, and every moving dot is a payload the system ships. The result is a
**single self-contained HTML file** — one page, no build, no network — with a
zoomable diagram on the left and a click-to-inspect panel on the right, in both
light and dark themes.

## What makes this skill different

It maps **anything**, not just code:

| Input | Stage 1 becomes… |
|---|---|
| A **repository** | A knowledge doc *measured* from the code — real files, counts, call paths |
| An **idea or a thought** ("I want to build X") | A knowledge doc *synthesized* from the idea — a proposed architecture |
| **One design doc** | A knowledge doc *extracted* from the doc — the system it describes |
| **A set of design docs** | A knowledge doc *reconciled* across the docs — one coherent system |

The work is always two stages, in order. Do not skip stage 1.

## The one rule

**Prose, groups and flows are authored. For a repository, counts and geometry
are measured; for an idea or a doc, everything is authored — say so.**

No scanner can say what a subsystem is *for*, and no reader wants a map that
lies about what exists. Read the input and write about it. That is the work.

---

## Stage 1 — Synthesize the knowledge doc

Produce `architecture.knowledge.md`: the authored understanding of the system.
This is the thinking step, and it is where quality is won or lost.

Read **`references/knowledge-doc.md`** for the full method and a template. In
short, capture:

- **Title & one-paragraph intro** — what the system is and why it exists.
- **Groups (4–7)** — the neighborhoods, named the way people talk: "Entry &
  control", "The run pipeline", "Outside world". Not "utils" and "lib".
- **Nodes (8–25)** — one per subsystem. For each: `name`, `role` (a short noun
  phrase), `owns` (1–2 plain-language sentences), `tech` (example
  implementation), and `weight` 1–6 (how much of the system lives here → its
  building height).
- **Edges** — real or intended call/data paths only. If you can't name the path,
  don't draw it. Mark each `run` (part of the primary flow) or `dep` (a
  supporting dependency), with a one-word `verb` ("enqueue", "fetch creds").
- **Flows / lifecycle** — the ordered steps of the system's main verb, e.g. how
  one request travels end to end. These become the overview panel.

How you fill it depends on the input:
- **Repo:** explore the code first (framework, entry points, modules, data
  stores). Ground every node and edge in files you actually read.
- **Idea / thought:** reason from first principles to a sensible architecture;
  state assumptions in the intro.
- **Design doc(s):** read them fully; extract components and flows; where docs
  conflict or omit, note it in the intro rather than inventing silently.

Show the knowledge doc's shape to the user (or write the file) before rendering,
so the authored half is reviewable.

---

## Stage 2 — Render the interactive page

Copy the bundled engine and fill in one data block. **Do not hand-roll a new
renderer** — the bundled one already solves the hard parts (zoom math, click
selection, painter's ordering, theming).

1. Copy `assets/architecture-map.html` to the output location the user wants
   (e.g. `architecture-map.html` in their project, or wherever they ask).
2. In the copied file, edit **only** the `DATA` object (clearly marked
   `EDIT THIS BLOCK ONLY`). Translate the knowledge doc into:
   `title`, `subtitle`, `groups {label, hue}`, `nodes {group, name, role, tech,
   owns[], h}`, `edges [[from,to,type,verb]]`, and `overview {intro[], steps[]}`.
   Node grid positions are **optional** — the engine auto-lays-out each group as
   its own row, so you usually only set `h` (weight) and, occasionally, `w`/`d`
   for a wide service. Leave everything below `ENGINE — do not edit` untouched.
3. Read **`references/rendering.md`** for the DATA schema, the projection, and
   the gotchas that must stay solved (they are already correct in the engine —
   the reference exists so you don't reintroduce the bugs if you touch it).

### The deliverable is fixed — these are non-negotiable

The bundled engine already delivers all of these; verify they survive any edit:

- **One page.** A single self-contained HTML file. No external CSS/JS/fonts/
  images, no CDN, no network. Fills the frame; responsive from ~320px up.
- **Zoom & pan.** Wheel zooms toward the cursor; drag pans; on-screen
  **+ / − / RESET** controls. (Zoom uses `getScreenCTM()`, not element width.)
- **Side panel.** Clicking a building selects it and fills the right panel with
  its role, tech, what it owns, and its Sends-to / Receives-from connections;
  those connections are click-through. A back button returns to the overview.
- **Light + dark, by default.** Themes via `prefers-color-scheme`; both must be
  legible. Colors are authored in OKLCH.

---

## Verify, then be honest

1. Open the file in a browser and **look at it**: no overlapping buildings, no
   edge cutting through a facade, every building clickable, the panel updates,
   zoom/pan/reset work, both themes legible (toggle OS dark mode).
2. Then tell the user plainly what is authored vs measured:
   > The interaction and geometry are correct. **The content is a first draft** —
   > for an idea or a design doc, *every* node, edge and flow is authored (I read
   > the input and wrote it), not measured. Edit the `DATA` block; nothing else
   > needs to change.

Do not leave mediocre writing behind a polished-looking map without saying so.

## Updating an existing map

If an `architecture-map.html` already exists, this is an update: re-open its
`DATA` block, add/adjust nodes and edges from the new understanding, and leave
authored prose you didn't need to change exactly as it is. Report what you added
and what you left alone.

## What not to do

- Do not skip Stage 1. A map with no knowledge doc behind it is decoration.
- Do not draw an edge you cannot name.
- Do not rewrite the engine. Fill the `DATA` block.
- Do not hand-write grid coordinates for every node — trust auto-layout, override
  only when a specific placement matters.
- Do not add a build step, a framework, or a network request. One file, opens anywhere.

## Files

- `assets/architecture-map.html` — the engine **and** a complete worked example
  (an RPA browser-automation platform). Open it to see the target; copy it to start.
- `references/knowledge-doc.md` — Stage 1: how to synthesize the knowledge doc, with a template.
- `references/rendering.md` — Stage 2: DATA schema, the isometric projection, and the solved gotchas.
