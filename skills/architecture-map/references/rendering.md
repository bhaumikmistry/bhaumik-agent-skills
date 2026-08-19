# Stage 2 — Rendering reference

You render by copying `assets/architecture-map.html` and editing its `DATA`
block. The engine below that block is already correct. This reference documents
the DATA schema, the projection, and the gotchas the engine already solves —
read it so you don't reintroduce a solved bug if you ever touch the engine.

## The DATA schema

```js
var DATA = {
  title: "…",                 // header title + document title
  subtitle: "…",              // small kicker above the title (optional)
  groups: {
    key: { label: "Human name", hue: 235 }   // hue 0–360 optional (auto-assigned)
  },
  nodes: {
    id: {
      group: "key",           // required — which district
      name: "Label",          // required — shown on the building + panel
      role: "short phrase",   // panel subtitle
      tech: "Example impl",   // panel chip
      owns: ["sentence", …],  // panel body — plain language
      h: 4,                   // weight 1–6 → building height (default 3)
      w: 2, d: 2,             // footprint in cells (default 2×2; widen a bar service to w:3)
      gx: 0, gy: 0            // explicit grid position — OPTIONAL, omit to auto-layout
    }
  },
  edges: [ ["from","to","run|dep","verb"], … ],
  overview: { intro: ["para", …], steps: [ {title,text}, … ] }   // optional
};
```

Auto-layout places each group as its own row (district), front-to-back in
`groups` insertion order, nodes left-to-right in `nodes` insertion order. So:
**order groups back→front and nodes along their flow, set `h`, and you're done.**
Only set `gx`/`gy` when a specific placement matters.

## The projection (2:1 dimetric isometric)

```
toScreen(gx, gy, z) = { x: (gx - gy) * TW, y: (gx + gy) * TH - z * ZH }
```

with `TW=34, TH=17, ZH=16`. One grid step along `gx` moves half a tile right and
half-down; `gy` mirrors it left; `z` lifts straight up. Buildings extrude from a
footprint up to height `h`, drawn as a lit top face plus two shaded walls.

**Paint order** (already implemented): floor grid → district plates → edges →
buildings **back-to-front by `depthKey = gx + w + gy + d`** → flow dots → labels.
Painting buildings after edges is what makes a payload appear to enter a module.

## The gotchas the engine already solves — keep them solved

1. **Never call `setPointerCapture` on the SVG.** It retargets the subsequent
   `click` to the SVG, so building clicks stop selecting. The engine instead
   records the pressed node on `pointerdown` and, on `pointerup`, selects it only
   if the pointer didn't drag (>5px = a pan, not a click).
2. **Zoom must use `getScreenCTM().inverse()`**, not `(clientX/width)*viewBox`.
   The SVG letterboxes its viewBox (`preserveAspectRatio`), so width-based math
   drifts. Convert the cursor through the screen matrix, clamp the new width,
   then apply the *same* effective scale to the offset — no jump at the limits.
3. **Only buildings are interactive.** `#scene > :not(.node){ pointer-events:none }`
   so grid lines, plates, edges, labels, and moving dots can't swallow a click,
   while empty space still starts a pan.
4. **Dot visibility is toggled via `display`, not CSS opacity.** The payload
   dots animate `opacity` with SMIL; a CSS opacity rule would fight it. To dim
   non-selected dots, set `style.display='none'` in JS.
5. **Themes are `prefers-color-scheme` + OKLCH custom properties.** Every color
   is a `--var` with a light and a dark value; SVG fills reference the vars so
   both themes recolor for free. Keep both legible.
6. **Respect `prefers-reduced-motion`** — the payload animation hides under it.

## Sanity checklist before you ship

- Buildings don't overlap; no edge slices through a facade.
- Every building selects and fills the panel; connection links are click-through.
- Wheel zoom tracks the cursor; drag pans; RESET recenters and clears selection.
- Toggle OS dark mode — both themes read cleanly.
- The file has no `http://`/`https://` asset references and opens offline.
