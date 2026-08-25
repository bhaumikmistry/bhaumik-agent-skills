# Weekly strategy

Every projection carries a `strategy` block covering the next five to six gameweeks. It is written **before** the three plans, because a plan is only sensible inside a stance — "take a hit this week" means nothing until you know whether the fixtures are about to improve or get worse.

## Building it

1. Pull each squad club's fixtures for GW N through N+5 with difficulty per side.
2. Compute a **squad-weighted FDR per gameweek** — the mean difficulty across the current starting XI's clubs. That single number tells you which weeks to attack and which to survive.
3. Find the swings: the week where several assets face the same hard fixture, the week a new signing's run turns, the fixture that damages both sides of the squad at once (a Chelsea-Arsenal clash when you hold both).
4. Give every week a **stance** in plain words, plus what is planned, whether a chip is live, and what to watch.

## The stances that recur

| Stance | When | What it means |
| --- | --- | --- |
| Fix the flag | A doubt or a dead asset | Spend the free transfer on the problem, nothing else |
| Sell into the clash | Two owned clubs play each other | One of them has to go before the fixture, not after |
| Absorb it | Squad FDR spikes | Take no hits into a week nothing improves. Bank the transfer instead |
| Turn | FDR falls after a hard run | Spend banked transfers here — into the soft run, not out of the hard one |
| Attack the run | Sustained low FDR | Captaincy and chips become live |

## Chip timing

Chips get a plan, not a wish. For each one state the trigger and the fallback:

- **Wildcard** — hold until the squad needs three or more changes at once. Never spend it patching a single bad week.
- **Free Hit** — hold for a blank gameweek. Check `get_blank_gameweeks` each week.
- **Bench Boost** — gated by bench quality, not by the calendar. If the bench is 4.0m non-players the chip is worth about 3 points; the leaders' GW1 boosts returned 11 to 41. Name the upgrade path first, the week second.
- **Triple Captain** — a double gameweek if one exists, otherwise the best home fixture against the weakest side in the window, with a named fallback week.

## Rules

- Take hits **into** improving fixtures, never into the worst week in the window.
- The stance for a week can be "do nothing" — write it down anyway, so that banking a transfer is a decision on the record rather than an omission.
- Revise the block every week. Fixtures do not move but injuries, price rises and blank/double announcements do.
- Keep the horizon honest: an FDR of 3.36 against 2.91 is a real difference; 3.09 against 3.18 is not. Do not build a plan on noise.
