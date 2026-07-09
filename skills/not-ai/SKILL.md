---
name: not-ai
description: Strip AI-sounding language from writing. Fires on "make this not sound like AI", "de-AI this", "make this human", "rewrite naturally", "sounds too robotic", "AI voice", "sounds generated", "clean up the AI", "less AI".
---

# not-ai

Rewrites text to eliminate the patterns that make writing sound machine-generated. Uses the anti-pattern catalog in [anti-patterns.md](anti-patterns.md) as the detection rubric.

## When this skill fires

- The user pastes text and says it sounds like AI
- The user asks you to write something and wants it to sound human
- The user says "de-AI this", "too robotic", "sounds generated"
- You're drafting anything where sounding human matters (outreach, blog posts, messages)

## How to use

1. Load [anti-patterns.md](anti-patterns.md) — that's your checklist.
2. Scan the text for violations. Flag them silently (don't lecture the user about each one).
3. Rewrite with these replacement principles:

| Instead of... | Do this |
|---|---|
| Elaborate verbs ("serves as", "stands as", "showcases") | Simple copulatives ("is", "has", "was") |
| AI vocabulary (delve, tapestry, landscape, pivotal, robust) | Plain words or cut entirely |
| Negative parallelisms ("not just X, but also Y") | Say the thing directly |
| Rule of three ("innovative, dynamic, and transformative") | Pick one word. Maybe zero. |
| Superficial -ing analysis ("highlighting the importance of...") | Delete it. If the point matters, make it a real sentence. |
| Elegant variation (never repeating a word) | Repeat the word. Humans do. |
| Hedge-then-assert ("While X is debated, it remains significant") | Take a position or cut the sentence |
| Promotional puffery ("vibrant", "groundbreaking", "renowned") | Specific facts or nothing |
| Vague attribution ("experts argue", "observers note") | Name who, or cut it |
| Em dashes (—) or double hyphens (--) | Period, comma, or parentheses. Never em dashes. |

4. After rewriting, read it aloud in your head. Does it sound like a person talking? Or a brochure? If brochure, cut more.

## The hierarchy

When in doubt, prioritize:

1. **Specificity over generality** — a weird true detail beats a smooth generic claim
2. **Short over long** — if you can cut it without losing meaning, cut it
3. **Simple verbs over fancy ones** — "is" is fine. "represents" is usually not.
4. **Repetition over variation** — repeating a word is better than forcing a synonym
5. **Silence over filler** — not every sentence needs a concluding thought about significance

## What NOT to do

- Don't just swap AI words for synonyms (that's still the same structure)
- Don't add self-aware jokes about being AI (cringe, and still obvious)
- Don't overcorrect into choppy fragments (humans write full sentences too)
- Don't strip all personality — the goal is human voice, not no voice
