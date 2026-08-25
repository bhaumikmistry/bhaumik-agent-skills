# Opposition analysis

`python3 scripts/league_study.py [gw]` pulls every league the manager is in, takes the top 2 in each, and writes `data/leagues/GW{N}.json` with their squads, captain, chip, and the players they owned that we did not — scored.

That is the evidence. The analysis is the reading of it, written by hand into `data/analysis/GW{N}.json`.

## Strip the chips before comparing anything

This is the technique that made GW1 legible. Rescore every rival squad the normal way — XI plus a normally doubled captain, no bench boost, no triple captain — and compare that number.

GW1 result: the raw gap to the world #1 was 50, not 67, and against the rival **median** it was 9, not 67. Half the "leaders" had picked a worse squad and won on a chip. One rival who beat us by 7 had a raw 42 against our 49.

Report both numbers. Total says who won; raw says who picked better.

## The survivorship caveat — always state it

The sample is league winners and runners-up. Squads selected on winning a single gameweek are differential-heavy **by construction** — every manager who took the same punts and lost is invisible. So:

- You may say: "gameweek winners looked differential-heavy."
- You may not say: "differentials win."
- Never recommend copying the winners' ownership profile on this evidence alone.

## What to compute

Per rival, and as a median across rivals:

- raw score, chip gain, chip used
- spend per position
- count of cheap (≤£5.0m) and premium (≥£6.5m) defenders
- average XI ownership, count of sub-10% starters
- exposure to specific clubs whose fixtures broke the gameweek open
- bench points, zero-minute starters
- captain and what it returned

Then find the recurring names across leaders that we do not own, and how many leaders held each.

## The player board — the part planning actually reads

`league_study.py` rolls every studied squad up into `player_board`: each player started by at least one leader, with price, points, ownership, how many leaders held them, and whether we own them. It ranks by **consensus × return** (`held_by × points`).

Read it as two different signals:

- **High held-count with a real return** = consensus. Several independent managers backed the player before the gameweek. Szoboszlai at 8 of 11 leaders is the strongest kind of evidence in this dataset, and it is worth more when it agrees with a fixture case you had already made yourself.
- **Low held-count with a huge return** = noise. Hinshelwood scored 16 and two managers owned him. Every manager who took the same punt and blanked is invisible. Do not promote this into a recommendation.

Also compute **what we owned that the leaders did not**. In GW1 our Guehi, Xhaka and Odegaard returned 30 points and between zero and two of eleven leaders held any of them. That is a real edge over the field, and the reflex after reading an opposition study is to trade edges away for consensus picks. Name the edges explicitly so the next planning step protects them.

Deduplicate by entry id before counting. A manager who tops two of your leagues appears twice in `studies` and will otherwise be counted twice — this produced "held by 13 of 11" before it was caught.

## Turning it into next-week actions

Every action needs a **why** that stands on its own, independent of the result being chased. Test each one:

- "Keep De Cuyper" — valid, because the fixture run and xGI case existed before the analysis; the GW1 evidence corroborates rather than causes it.
- "Buy De Cuyper because he scored 17" — invalid, that is buying a price that has already moved.
- "Take plan B, Szoboszlai" — valid, six of eighteen leaders held him and the fixture case was already made independently. Two unrelated sources agreeing is the strongest signal available.
- "Don't play Bench Boost yet" — valid, and it comes from our own squad, not theirs: our bench returned 3 while leaders' benches returned 11-41. A chip is only a weapon if the bench is worth boosting.

Write the analysis as `headline`, `summary`, `what_worked[]`, `what_didnt[]`, `caveats[]`, `gw{N+1}_actions[]`, each finding carrying its `evidence` string. Then copy the conclusions into the next gameweek's projection under `informed_by` so the reasoning travels with the deadline.

## Presentation rules

The written analysis is the section. The raw tables and squad cards go inside a `<details class="raw">` that stays **collapsed**. Nobody wants nine league tables before the point.

**A study belongs to one gameweek and never leaks into another.** The opposition section is scoped to whichever gameweek is selected: GW1 shows the GW1 study, GW2 shows "not ready" until GW2 has been played and studied. Mixing them makes it impossible to tell whether a recommendation came from evidence or from last week's evidence wearing this week's label — which is exactly the failure mode the whole ordering gate exists to prevent.

The actions key is per-gameweek too: the GW1 analysis carries `gw2_actions`, the GW2 analysis carries `gw3_actions`. The dashboard finds whichever key ends in `_actions` rather than hardcoding one.
