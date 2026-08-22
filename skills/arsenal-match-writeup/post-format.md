# Post format

What every match post on bhaumikmistry.com looks like, taken from the 60-odd already there.

## File

`app/blog/posts/<subject>_<DD>_<MM>_<YY>.mdx`

The subject is the story, not the fixture: `coventry_opener_21_08_26`, `champions_palace_24_05_26`, `etihad_heartbreak_19_04_26`. Posts from 2025 use the American order in their names, posts from 2026 use day first. Follow the 2026 pattern.

## Frontmatter

```yaml
---
title: "Title Defence Begins: Three Past Coventry on Opening Night"
publishedAt: "2026-08-21"
summary: "Havertz, Saka and Ødegaard see off the newly promoted Sky Blues 3-0, with Christos Tzolis involved in two on his debut."
tags: [arsenal, premier-league, christos-tzolis, kai-havertz]
---
```

- `publishedAt` is the match date.
- Tags are lowercase and hyphenated: `[arsenal, premier-league, champions-league, kai-havertz]`. Some older posts use `["Premier League", "Arsenal"]` in title case, which splits the tag filter on `/blog` into two chips for the same thing. Do not add more of those.
- Tags decide what appears on `/sports`, which selects on club and competition tags.

## Body

- No `# H1`. The title comes from the frontmatter. Sections are `###`.
- Two to four sections, named for what happened, not "First Half" and "Second Half". "The New Boy", "The Garnacho Scare", "Five Kicks".
- **Bold** on first mention of a player who did something. Not on every name in the post.
- Blockquote for the manager, one or two, and only ever real words.
- Close with `**Man of the Match: <name>** <flag emoji>` and a line or two saying why.
- Write as a supporter. "We" and "us", not "Arsenal" and "the Gunners" every sentence.
- Minutes and scorers belong in the prose, not in a table. The tracker holds the data.

## Images

Only URLs that have been seen to resolve. Real Arsenal CDN links look like:

```
https://www.arsenal.com/sites/default/files/styles/large/public/images/GettyImages-2233029167_yjd52c2n.jpg?auto=webp&itok=xVM0yowk
```

The `itok` token is the tell. A tidy-looking path such as `.../images/kai_havertz_celebration.jpg?auto=webp` is invented and will 404. `arsenal.com` refuses automated fetches, so the URLs have to come from the person writing, and a post with no images is fine. If there are no images, there is no credits line either.

## A worked example

`app/blog/posts/coventry_opener_21_08_26.mdx` is the reference: verified timeline, two real Arteta quotes, man of the match going to the debutant who set up two rather than to a scorer, and a closing line pointing at the next fixture.
