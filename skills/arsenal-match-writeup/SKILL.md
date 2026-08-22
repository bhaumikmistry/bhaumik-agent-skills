---
name: arsenal-match-writeup
description: Write a verified Arsenal match post for bhaumikmistry.com and update the gooner tracker. Fires on "new Arsenal match", "write up the game", "match report", "Arsenal blog", "update the tracker", "we just played".
---

# arsenal-match-writeup

Turns a played fixture into a post on the site and a row on the tracker, with every fact checked first. Format lives in [post-format.md](post-format.md).

The rule that matters: **nothing goes in the post because it sounds right.** Every minute, scorer and quote is read off a source before it is written. An earlier pass over this blog found 28 posts where every Arteta quote was invented, goals were credited to the wrong player, and five posts pointed at image URLs that had never existed. That is the failure mode this skill exists to prevent.

## 1. Find the fixture

`public/projects/gooner-tracker/fixtures.json` holds `upcoming`, `past` and `trophies`. The match is usually the first entry in `upcoming`. Take its date, opponent, competition and venue from there rather than from memory.

## 2. Verify before writing

Work in this order. Stop when you have the goal timeline and at least one real quote.

1. **Search** for the result: `Arsenal <opponent> <date> match report`. Search summaries are written by a small model and routinely garble the venue and the assist. Use them to find the ESPN game id, then read the report.
2. **Fetch the ESPN report**: `https://www.espn.com/soccer/report/_/gameId/<id>`. This is the reliable one. Ask it for the goal timeline, how each goal was scored, who came on, and any manager quotes.
3. **Search separately for quotes.** ESPN reports usually carry none.

| Source | Fetchable | Good for |
|---|---|---|
| espn.com report | yes | the goal timeline, assists, substitutions |
| premierleague.com news | yes | goals, table position, both managers quoted |
| en.wikipedia.org | yes | season pages, finals, shootout order |
| statmuse.com | yes | a season's result list |
| skysports.com | yes | quotes, context |
| nbcsports.com | yes | quotes |
| arsenal.com | **403** | nothing, do not try |
| arseblog.com and arseblog.news | **403** | nothing, do not try |
| bbc.com | **blocked** | nothing |
| fbref, worldfootball, 11v11 | **403** | nothing |

Two traps worth knowing. StatMuse gives a clean list of a whole season but its home and away column is wrong often enough to matter, so confirm the venue from the report. And a competition can move: the 2026 Community Shield was in Cardiff, not Wembley.

**If a quote cannot be sourced, there is no quote.** Replace the blockquote with a verified sentence. Never write "Arteta said" over words nobody said.

## 3. Write the post

Follow [post-format.md](post-format.md). Filename is `subject_DD_MM_YY.mdx` in `app/blog/posts/`.

## 4. Update the tracker

Move the fixture from `upcoming` into `past`:

```json
{
  "id": "past-<next number>",
  "opponent": "Coventry City",
  "isHome": true,
  "date": "2026-08-21",
  "time": "20:00",
  "venue": "Emirates Stadium",
  "competition": "PL",
  "score": "3-0",
  "watched": true,
  "blogLink": "/blog/coventry_opener_21_08_26"
}
```

- **Score is always Arsenal first**, whatever the venue. A 2-1 away defeat is `"1-2"`.
- A shootout uses the existing convention: `"1-1 (3-4 pens)"`.
- Keep `past` sorted newest first. Competitions in use: `PL`, `UCL`, `FA Cup`, `EFL Cup`, `Community Shield`.
- A new opponent needs a crest in the `logoMap` in `app/projects/gooner-tracker/page.tsx`. Check the file exists first: `https://raw.githubusercontent.com/bhaumikmistry/football-logos/refs/heads/master/teams/<slug>.png`, where the slug is the club name lowercased with `_` in place of spaces. If it is missing, the fork has a `scripts/build_index.py` that rebuilds the flat list from upstream.
- Seasons are derived from dates, July to June, so nothing needs to be told which season a match belongs to.

If silverware was won, add to `trophies` with `season`, `competition`, `date`, `detail`, `image`, and `credit` plus `creditUrl` when the photo needs attribution.

## 5. Check the prose

Both of these, in this order:

1. The **not-ai** skill for the judgement call.
2. `npx @slop-detector/slop-detector --file <post>` for the mechanical sweep. Under about 25 is fine.

Hits inside a verbatim quote are left alone. A manager saying three things in a row is not slop, it is a transcript.

## 6. See it work

```bash
pnpm build
pnpm dev        # port 3003
```

Check the post itself, `/blog`, `/sports`, and `/projects/gooner-tracker?season=<yyyy-yy>` with the season in the query string.

## House rules

- No em dashes anywhere, in posts or commit messages.
- No Claude attribution line in commits or pull request bodies.
- Fixture dates are plain `YYYY-MM-DD`, which `new Date()` reads as UTC. Build dates from their parts or every date on the page renders a day early west of Greenwich.
- Only use image URLs you have seen resolve. Arsenal's CDN paths carry a signing token, and a path without one is a broken image. No images is better than invented ones, and a credits line with no images above it is worse than either.
