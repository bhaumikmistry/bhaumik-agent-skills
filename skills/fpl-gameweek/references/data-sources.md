# Data sources

## MCP tools

| Need | Tool |
| --- | --- |
| Current squad, bank, value, captain | `get_my_team`, `get_my_current_team` |
| Season position and deadlines | `get_gameweek_status` |
| Filter and rank the player pool | `analyze_players` |
| One player in depth, incl. gameweek history | `get_player_information` |
| Head-to-head comparison | `compare_players` |
| Name lookup | `search_fpl_players` |
| Fixture runs by player, team or position | `analyze_fixtures`, `analyze_player_fixtures` |
| Blanks and doubles | `get_blank_gameweeks`, `get_double_gameweeks` |
| Price risers and fallers | `get_price_changes` |
| Captaincy shortlist with breakdown | `suggest_captain` |
| Live scores mid-gameweek | `get_gameweek_live_scores`, `get_dream_team` |
| Mini-league context | `get_league_standings`, `get_league_analytics` |
| Our transfer history | `get_manager_transfer_history` (needs an explicit team_id) |

## What every player record carries

`form`, `points`, `points_per_game`, `minutes`, `starts`, `goals`, `assists`, `clean_sheets`, `goals_conceded`, `saves`, `bonus`, `bps`, `influence`, `creativity`, `threat`, `ict_index`, `expected_goals`, `expected_assists`, `expected_goal_involvements`, `expected_goals_conceded`, `selected_by_percent`, `transfers_in_event`, `transfers_out_event`, `cost_change_event`, `cost_change_start`, `status`, `news`, `chance_of_playing_next_round`.

xG / xA / xGI / xGC are **native** — do not go looking for Understat or FBref. They are season cumulative totals; for per-gameweek splits use `get_player_information` with `include_history=True`.

## Gaps and how to fill them

- **Set-piece and penalty order** is not exposed by the MCP surface:
  ```
  curl -s https://fantasy.premierleague.com/api/bootstrap-static/ | python3 -c "import sys,json;d=json.load(sys.stdin);print([(e['web_name'],e.get('penalties_order'),e.get('corners_and_indirect_freekicks_order'),e.get('direct_freekicks_order')) for e in d['elements'] if e.get('penalties_order')][:40])"
  ```
- **Per-90 rates** — derive: `stat / (minutes / 90)`.
- **Team attack/defence strength** — `strength_attack_*` and `strength_defence_*` are zeroed in bootstrap this season. Use `strength_overall_home` / `_away` (1-5) and fixture difficulty instead.
- **Last season's record per player** — `element-summary/{id}/` → `history_past`. Carries points, minutes, goals, assists, clean sheets, bonus, starts and xGI for prior seasons. This is the only honest basis for a GW1 build.
- **Opponent-adjusted projections** are not provided. FDR from `analyze_fixtures` is the adjustment input.

## Raw endpoints worth knowing

```
bootstrap-static/            players, teams, events, chips, game settings
fixtures/                    every fixture with per-side difficulty
event/{gw}/live/             per-player minutes and points for a gameweek
entry/{id}/                  a manager, including every league they are in
entry/{id}/event/{gw}/picks/ a manager's squad, multipliers, active chip
leagues-classic/{id}/standings/   league table
element-summary/{id}/        one player: history, history_past, fixtures
```

Prefer the MCP tools. Fall back to raw HTTP only for what they genuinely do not expose.
