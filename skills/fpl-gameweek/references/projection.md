# Projecting a gameweek

Run this whenever asked to optimize, build, or review a squad.

## Phase A — historical and state

Per candidate, over the last 3-6 gameweeks:

1. Underlying numbers: xG, xA, xGI, xGC, plus the ICT components. All native to the MCP player record.
2. Over/under-performance: goals minus xG, assists minus xA. Big positive variance is a regression risk. Big negative variance on a heavy-minutes player is a buy signal.
3. Minutes reliability: `minutes`, `starts`, share of available minutes, rotation pattern, suspension risk from `yellow_cards`, injury flags from `status` / `news` / `chance_of_playing_next_round`.

Then present-state context:

4. Fixture difficulty across the horizon, home/away split, opponent strength.
5. Blank and double gameweek flags.

**Early season (fewer than ~5 gameweeks played) the sample is thin.** Weight last season's baseline, preseason role and fixture context above current-season form, and say so in the confidence rationale. In GW1-2 every "form" number is a single match.

## Phase B — expected points and confidence

```
xP = base_appearance + attacking + defensive + bonus - risk_penalties
```

- `base_appearance` = P(60+ min) × 2 + P(1-59 min) × 1
- `attacking` = xG/90 × minutes_projection × goal_points(position) + xA/90 × minutes_projection × 3, adjusted for opponent and venue
- `defensive` (GK/DEF) = P(clean sheet | opponent, venue) × CS points, minus expected goals-conceded deductions; add save points for keepers
- `bonus` from BPS per 90 and share of team BPS
- `risk_penalties` for card rate, rotation risk, penalty-miss exposure

Calibration check: a starting XI plus a doubled captain should land near 50-55 for a normal squad. If a projection totals 70+, the scale is wrong, not the squad. (This happened once — a formula produced 79.7 for an average team.)

| Band | Range | Profile |
| --- | --- | --- |
| High | 80-100% | Nailed starter, elite underlying numbers, no rotation risk, on set pieces or penalties |
| Medium | 50-79% | Good fixtures and solid xP, some rotation risk or small sample |
| Low | <50% | High variance — injury return, punt, high ceiling and low floor |

## Before the plans: which problem actually costs points

A flagged player is only a problem if he has to start. Check the bench before spending a transfer on him.

In GW2 the squad carried two flags — Van de Ven at 50% and Gibbs-White at 75%. The first draft spent the free transfer on Van de Ven, which was wrong: Thomas sits on the bench at 4.0m, plays 90 minutes and had a home FDR 2 fixture, so benching Van de Ven cost about 0.1 xP. Gibbs-White had no cover and had to start away at Liverpool, so leaving him cost 2.6. Same transfer, twenty-six times the effect.

The test, in order:

1. Can the flagged player be benched with a legal XI? If yes, the fix is free — bench him.
2. Does a replacement already in the squad have a decent fixture this week? If yes, the transfer is not urgent.
3. Which unfixable slot has the largest xP hole? That is what the free transfer buys.
4. Only then ask whether a second move is worth -4.

Sell a benchable flagged player when his fixture run stays bad, when he is blocking a slot you need, or when his price is about to fall — not because the flag is visible.

## Judging a cheap defender

At 4.0-5.0m the job is not clean sheets, it is starting every week and hitting the defensive-contribution
threshold. Ten clearances, blocks, interceptions and tackles pays 2 points regardless of the scoreline, so a
defender in a bad team who defends constantly can out-earn a mid-price one in a good team who does not.

Judge on, in order: minutes and starts, defensive contribution per 90, then fixtures, then clean-sheet odds.
A 4.0m defender who plays 90 and clears 9 balls has a 3-4 point floor in a 3-0 defeat. That is doing its job.

The slot worth fixing is the one that does not play at all. Check `starts` and `minutes` from last season
before assuming a cheap player is a squad problem — one who returned 83 minutes and a single start across a
whole season is dead money and the reason Bench Boost is not worth playing; one who plays 90 every week is
the enabler funding the premium at the other end. Fix dead money with a free transfer, never with a hit:
a slot that is bench or fourth-choice cannot repay 4 points.

## Phase C — the three plans

| Plan | Risk | Shape |
| --- | --- | --- |
| A | Low | Banked free transfers only. No hit. The baseline everything else is measured against. |
| B | Medium | One transfer beyond free (-4). Buys a clear 5-gameweek xP upgrade in a strong fixture run, usually a well-owned asset. |
| C | High | Two or more beyond free (-8+). Buys ceiling: sub-10% differentials, a fixture-swing stack, or a structural fix that frees squad value. |

Requirements for each plan:

- A full legal 15. Check budget, formation and the 3-per-club limit **per plan**, not once.
- `projected_gross` (XI including doubled captain) and `projected_net` (gross minus hit). Net is what gets compared.
- `edge_vs_a_gw2` and `edge_vs_a_5gw` — the single-week and horizon edge over plan A.
- Its own risk list. A plan with no stated downside has not been thought through.
- A thesis in plain language: what you are buying and why it is worth the hit.

Also produce a differential alternative when rank-chasing is on the table: up to 3 high-ownership picks swapped for sub-10% options, stating the xP given up and the variance taken on.
