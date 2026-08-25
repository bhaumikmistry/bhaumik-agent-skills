---
name: fpl-gameweek
description: Run the full Fantasy Premier League gameweek cycle - pull live data through the fpl MCP server, project three ranked plans (no hit / -4 / -8), score every plan against the real result including the ones not played, study what league leaders did differently with chips stripped out, and rebuild and republish the dashboard. Use for any FPL request: transfers, captaincy, chips, "predict next team", "who should I bring in", post-gameweek reviews, league or rival analysis, or updating the dashboard.
---

# FPL Gameweek Cycle

The repo is a working FPL desk: a ledger under `data/`, generator scripts under `scripts/`, and a published dashboard. Everything below exists so that each gameweek leaves behind a record that the next one can learn from.

## The order is fixed

Planning gameweek N is the **last** step, not the first. Everything from gameweek N-1 has to be on the record before a single transfer is proposed, because the opposition read is an input to the plan rather than a report about it.

```
1. SCORE       GW N-1 settles      -> score every plan, autosubs applied
                                      data/actuals/GW{N-1}.json  (plan_results)
2. STUDY       pull the leagues    -> squads, chips, captains, player board
                                      data/leagues/GW{N-1}.json  (generated)
3. READ        write the analysis  -> what worked, what did not, who delivered,
                                      caveats, actions for the next deadline
                                      data/analysis/GW{N-1}.json (by hand)
4. STRATEGY    look 5-6 weeks out  -> per-week stance, fixture swings, chip timing
                                      strategy block in the next projection
5. PLAN        only now            -> three plans for GW N, each citing the read
                                      data/projections/GW{N}.json (informed_by)
6. PUBLISH     rebuild, verify, republish
```

**Gate before step 5:** if `data/analysis/GW{N-1}.json` does not exist, do steps 1-4 first. Planning without it produces recommendations that cannot explain why they are not just chasing last week's scores.

Then `python3 scripts/build_dashboard.py` and republish the artifact. Never edit `dashboard.html` — it is generated.

## Rules that must never be broken

- **Pull live data every time.** Squad, prices, injuries and ownership move daily. Never answer from memory or from earlier in the conversation.
- **Verify legality explicitly** for every squad you present: 2 GK / 5 DEF / 5 MID / 3 FWD, max 3 per club, within budget, XI has ≥1 GK ≥3 DEF ≥2 MID ≥1 FWD. Show the arithmetic.
- **A hit must clear its cost over the planning horizon, not one week.** Show the math both ways — a plan that loses this week and wins over five gameweeks is legitimate, but say so plainly.
- **Never present a point estimate without a confidence band.**
- **Recommend one plan, present all three.** The manager picks.
- **This agent recommends; it never executes.** No transfer, captaincy change or chip is ever made on the FPL site.
- **Separate what the data supports from judgement.** Label speculation as speculation.

## Working directory

The skill expects an FPL desk repo — a `data/` ledger, `scripts/` generators, and a published dashboard. If those are missing, create them on first use: `data/{projections,actuals,leagues,analysis,retro}/` plus the scripts in the table below. `references/ledger.md` carries every file shape.

The manager's team ID comes from the authenticated MCP credentials, so squad tools work without arguments. Record team name, manager, season and entry gameweek in the project's own `CLAUDE.md` rather than here.

## Data access

The `fpl` MCP server is installed globally (`uv tool install fpl-mcp`) and registered at user scope. Auth is a PingOne OIDC refresh token in `~/.fpl-mcp/`. If authenticated calls fail the token expired — re-run in a **real terminal**, it needs a TTY and cannot run through Claude's Bash tool:

```
~/.local/bin/fpl-mcp-config setup
```

Tool map, available metrics, and the known gaps (set-piece order, per-90 rates, team xG ranks) are in `references/data-sources.md`. Read it before reaching for raw HTTP.

## Scripts

| Script | Does |
| --- | --- |
| `scripts/build_dashboard.py` | Merges the whole ledger into `dashboard.html`. Run after every ledger change. |
| `scripts/league_study.py [gw]` | Pulls every league, studies the top 2 in each, writes `data/leagues/GW{N}.json`. |
| `scripts/score_gw{N}.py` | Scores plans against real results with autosubs, writing per-player results back into every plan. |
| `scripts/make_gw{N}_plans.py` | Derives plan squads by swapping players out of a base squad rather than hand-writing 45 rows. |

Write the scripts once and copy them forward per gameweek. They handle fetching, arithmetic, constraint checks and rendering — never selection.

## Judgement, not scripts

A scoring formula was tried for squad selection and produced nonsense: it never bought the £15.5m player who was the highest scorer in the game, because price penalised him in the z-score, and it captained whoever cost most. **Pick players by reading their records; use scripts for fetching, arithmetic, constraint checks and rendering.** Every hand-picked player carries a `reason` field stating why, from last season's numbers and the fixture, so the reasoning is auditable afterwards.

## Working the four phases

1. **Project** — three plans, expected points with confidence, per-plan risk list. → `references/projection.md`
2. **Score** — every plan, autosubs applied, hits deducted, results written back into each plan. → `references/scoring.md`
2b. **Strategy** — the six-week roadmap the plans have to sit inside. → `references/strategy.md`
3. **Study** — leaders' squads with chips stripped out, plus the survivorship caveat that governs how far you may read into it. → `references/opposition.md`
4. **Publish** — rebuild, verify in a browser, republish to the same artifact URL. → `references/dashboard.md`

| Reference | Read it when |
| --- | --- |
| `references/rules.md` | Building any squad — the constraints and chip windows |
| `references/data-sources.md` | Before reaching for raw HTTP; tool map, available metrics, known gaps |
| `references/projection.md` | Projecting a gameweek and writing the three plans |
| `references/scoring.md` | After a gameweek settles |
| `references/opposition.md` | Studying leagues and rivals, and reading the player board |
| `references/strategy.md` | Setting the per-week stance and chip timing before planning |
| `references/ledger.md` | Writing any file under `data/` |
| `references/dashboard.md` | Touching the template, the design, or publishing |

## Output format

Structure any analysis or team build in this order:

1. **Squad matrix** — Player · Pos · Club · £ · Fixture · FDR · Conf% · xP
2. **Transfer and strategy summary** — FTs available and used, hits and their justification, chip status, bank, resulting team value
3. **Risk and confidence assessment** — what drives each score, the downside scenario, what would change the call
4. **Retrospective ledger** — previous projections against actual outcomes, once history exists

## Season context to keep current

- Chips: two sets. First-half set expires **GW19** (wildcard and free hit open GW2-19; bench boost and triple captain GW1-19).
- Free transfers bank to a maximum of **5**. Extra transfers cost **-4** each.
- Selling price: you keep 50% of a rise, rounded down to £0.1m; drops hit 1:1.
- `defensive_contribution` is a scoring stat this season — factor it into defender and midfielder projections.
