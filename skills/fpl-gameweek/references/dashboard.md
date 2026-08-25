# The dashboard

`dashboard.html` is generated. Edit `scripts/template.html` for anything visual or behavioural, `data/` for content, then:

```
python3 scripts/build_dashboard.py
```

The build injects the merged ledger into the template at the `/*__DATA__*/ null` marker and writes `dashboard.html`. Republish with the Artifact tool using the **same file path** to keep the URL. Record that URL in the project's `CLAUDE.md` so later sessions update the same artifact instead of creating a new one.

## Verify before publishing

The page is self-contained but it is real code and it does break. Serve it and look at it:

```
(python3 -m http.server 8931 &) ; sleep 1
# navigate a browser tab to http://localhost:8931/dashboard.html
pkill -f "http.server 8931"
```

`file://` URLs are blocked by the browser tooling, hence the local server. Check the console for exceptions, click through every gameweek chip and every plan card, and confirm the pitch actually changes.

## Layout

```
masthead (crest, team, next deadline)
stat strip (points, rank, value, free transfers, chips)
gameweek rail - one chip per logged GW, click to switch
gameweek panel
  informed_by (collapsed)  - what the last opposition read changed
  six-week stance (collapsed) - one table row per gameweek: FDR, stance, the week,
                            plan, chip, watch. Summary line carries hardest week,
                            softest week and the chip window so it reads closed.
  plan cards A / B / C - click to switch the whole panel
  pitch (formation lines + bench) | side column (armband, moves, chips, risks)
  squad matrix table
  plan ledger - projected vs actual net for every plan
charts - projected against actual per plan; overall rank
opposition (scoped to the selected gameweek)
  studied:   headline, summary, what worked / what did not, who delivered,
             caveats, next-deadline actions, <details> raw league data (collapsed)
  unstudied: "not ready" state naming the four steps that produce it
```

## Design tokens

Matchday teamsheet, not a SaaS dashboard. Archivo for display and UI, Newsreader for body, Roboto Mono for numbers.

| Token | Light | Dark |
| --- | --- | --- |
| `--ground` | `#f1f3ee` | `#0f1210` |
| `--surface` | `#fbfcf9` | `#171b16` |
| `--ink` | `#12150f` | `#e8ebe2` |
| `--pitch` / `--good` | `#2e8b57` | `#3d9e6b` |
| `--proj` | `#8b5cc7` | `#9b75d6` |
| `--rust` | `#c0603a` | `#cf7a50` |

Violet is projected, green is actual, rust is cost or risk. That pairing passed the dataviz validator's six checks in both modes — do not swap in a green/amber pair, it fails CVD separation.

Themes are defined three ways because the viewer has three states: bare `:root` for light, `@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`, and `:root[data-theme="dark"]`. Never define a colour only inside a media or `[data-theme]` block.

## Rules the template must keep

- **Source stays pure ASCII.** Every `·` `£` `→` `—` `−` `Δ` is written as a `\uXXXX` escape, and `build_dashboard.py` dumps JSON with `ensure_ascii=True`. Without this, charset guessing renders `Â·` and `â€"` all over the page. After any edit: `sum(1 for c in s if ord(c) > 127)` must be 0.
- **Scope the SVG sizing rule.** `svg { width: 100% }` unscoped blew the crest up to half the page. It is `.chart svg`.
- **Every gameweek-specific section reads the selected gameweek, never a season-level fallback.** The opposition study, the analysis, the player board and the strategy all come from `gw.leagues` / `gw.analysis` / `gw.projection.strategy`. `buildLeagues(gw)` is called from `render()` so it re-renders on every switch. A gameweek with no study shows the "not ready" state with the pipeline steps — it must never borrow another week's data, because a projected gameweek showing last week's opposition read is worse than showing nothing.
- **The panel follows the selected plan.** Squad source is `plan.squad` first, falling back to actuals only when a gameweek has no plans. Mode is "actual" when the squad rows carry `points`, not when the gameweek has an actuals file.
- **Context collapses, decisions do not.** The stance and the carried-over opposition read sit above the plan cards inside `<details>` closed by default, with a summary line dense enough to be useful unopened. The plans, the pitch and the ledger are always visible. Six equal cards in an auto-fit grid orphaned the sixth on its own row and read as clutter — a table with one row per gameweek is the right shape for six ordered weeks.
- **`el(tag, cls, text)` — the first argument is the tag.** Passing a class name in that slot silently creates an unknown element that renders unstyled but looks almost right. When something appears unstyled, check whether the class has CSS at all before assuming the markup is wrong: a class with no rule and a bad tag look identical on screen.
- **Wide content scrolls inside its own container.** Tables live in `.tablewrap` with `overflow-x: auto`; the body never scrolls sideways.

## Editing traps

- When splicing the template with Python string indexes, remember the CSS and the JS both contain a `/* ---------- charts ---------- */` marker. Slicing to the first match duplicated the entire document once. Search for the unique surrounding text, and afterwards assert `s.count("<script>") == 1`.
- Card width is 118px; player names use `word-break: keep-all` so "DONNARUMMA" does not split mid-word.
