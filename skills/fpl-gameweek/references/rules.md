# FPL rules the projections must respect

## Squad and budget

- £100.0m starting budget
- 15 players: 2 GK, 5 DEF, 5 MID, 3 FWD
- Maximum 3 players from any single club

## Lineup and captaincy

- Starting XI needs at least 1 GK, 3 DEF, 2 MID, 1 FWD
- Captain scores 2x; vice-captain gets 2x only if the captain plays 0 minutes
- Autosubs replace 0-minute starters with bench players in bench order, but only where the XI stays legal

## Transfers

- 1 free transfer per gameweek, banking to a maximum of 5
- Each transfer beyond the banked free transfers costs -4
- Selling price: keep 50% of any rise, rounded down to £0.1m. Drops hit 1:1

## Chips

Two full sets per season. The first-half set expires after GW19. From `bootstrap-static` this season: wildcard GW2-19 and GW20-38; free hit GW2-19 and GW20-38; bench boost GW1-19 and GW20-38; triple captain GW1-19 and GW20-38.

- **Wildcard** — unlimited free transfers, permanent
- **Free Hit** — unlimited free transfers for one gameweek, reverts after, banked FTs preserved
- **Bench Boost** — bench scores for one gameweek
- **Triple Captain** — captain scores 3x

Doubles are the priority window for BB and TC — check `get_double_gameweeks` before committing. But bench quality gates BB regardless: a bench of 4.0m non-players makes the chip worth ~3 points. Opening weekend is the exception, because nobody rotates in GW1.

## Scoring notes for this season

`defensive_contribution` is a live stat — defenders and midfielders earn from clearances, blocks, interceptions, tackles and recoveries. Factor it into the defensive component of xP, particularly for cheap defenders who play 90 minutes in bad teams.
