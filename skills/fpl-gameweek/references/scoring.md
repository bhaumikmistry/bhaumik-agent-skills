# Scoring a gameweek

After the gameweek settles, score **every plan**, not just the one played. Each plan's squad is a known 15, so its real return is computable. That is the entire point of the three-plan structure: the counterfactuals get scored, so over a season the record shows whether hits were worth taking.

## Method

1. Fetch per-player results from `event/{gw}/live/` — `minutes` and `total_points` per element id.
2. Apply autosubs: any starter on 0 minutes is replaced by the first bench player with minutes, **only if** the resulting XI stays legal (exactly 1 GK, ≥3 DEF, ≥2 MID, ≥1 FWD). Bench order matters.
3. Captain doubles. If the captain played 0 minutes the vice-captain's score doubles instead.
4. `net = gross - hits`.
5. Write the results **back into each plan's own squad** — `minutes`, `points`, `autosub_in`, `autosub_out`, `counted` — and into `data/actuals/GW{N}.json` as `plan_results`.

Step 5 is not optional. Without it the dashboard shows plan A's players no matter which plan is selected, because the panel falls back to the actuals file.

## Traps that have already bitten

- **`web_name` is ambiguous.** "Wilson" matched a Brentford forward instead of Harry Wilson at Leeds and silently cost a plan 2 points. Always resolve on **name + club**, and assert the resolved squad still has shape 2/5/5/3 — a mis-resolved player usually breaks the shape, so the assert catches it.
- **Autosubs are not in the live total.** FPL's live `points` excludes pending autosubs until the gameweek finishes. Record both and say which is which.
- **`event.finished` can read false** while player minutes are already populated. Trust the player data, note the flag.
- **An unplayed fixture penalises squads unevenly.** If a plan holds two players from a match that has not kicked off and another holds one, the comparison is not yet fair. Say so rather than presenting it as final.

## The retrospective

Each one covers:

1. Projected against actual, per player and squad total.
2. Plan A vs B vs C on actual net, and whether the hit paid. Keep a running tally — one week proves nothing, ten weeks show whether the risk appetite is set right.
3. Counterfactual transfer paths: `Δ = actual_points_gained − points_hit_cost − alternative_path_points`.
4. Model feedback: if actuals keep landing below the confidence lower bound for a category (mid-table attackers away from home, say), record the bias and adjust that category's weighting. Log every change in `data/retro/model-adjustments.md` with the gameweek and reason.
