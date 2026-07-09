# AI writing anti-patterns

Detection rubric derived from Wikipedia's "Signs of AI writing." When reviewing or writing text, flag and eliminate these.

## The vocabulary kill list

Words that signal AI authorship when they cluster together. One alone is forgivable. Three in a paragraph is a tell.

### The big offenders (all eras)

additionally, align with, boasts, bolstered, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (as verb), interplay, intricate/intricacies, key (as adjective), landscape (abstract), meticulous/meticulously, pivotal, robust, showcase, tapestry (abstract), testament, underscore (as verb), valuable, vibrant

### Promotional/travel-guide words

nestled, in the heart of, groundbreaking, renowned, featuring, diverse array, natural beauty, profound, rich (as vague praise), commitment to, exemplifies, boasts a

### Grok-specific overuse

causal, empirical, correlate

### The sneaky one in comments/discussion

"concrete" (as in "concrete evidence", "concrete examples")

## Structural tells

### The significance bloat

Adding statements about how X "represents broader trends" or "underscores the importance of" or "reflects the evolving landscape." These appear even for mundane topics. If a sentence exists only to assert importance without adding information, kill it.

**Phrases that signal it:**
- stands/serves as
- is a testament/reminder
- a vital/significant/crucial/pivotal/key role/moment
- underscores/highlights its importance/significance
- reflects broader
- symbolizing its ongoing/enduring/lasting
- contributing to the
- setting the stage for
- marking/shaping the
- represents/marks a shift
- key turning point
- evolving landscape
- focal point
- indelible mark
- deeply rooted

### Copulative avoidance

AI avoids "is" and "are" — replacing them with elaborate constructions. This is one of the strongest statistical tells (>10% drop in is/are usage in AI text).

| AI writes | Human writes |
|---|---|
| serves as the primary venue | is the primary venue |
| stands as a testament to | is |
| features a collection of | has |
| maintains a presence in | is in |
| boasts a rich history | has a long history |
| represents a departure from | is different from |
| refers to the practice of | is |
| ventured into politics as a candidate | was a candidate |

### Negative parallelisms

**"Not just X, but also Y"** — clearing up a misconception nobody had:
- "It's not just a restaurant, it's a community gathering space"
- "Not only did she excel academically, but she also..."

**"Not X, but Y"** — dramatic contrast that adds nothing:
- "It's not a trend, it's a movement"
- "no gimmicks, no shortcuts, just..."

**"X rather than Y"** (Grok-heavy):
- "prioritizing depth rather than breadth"

### Rule of three

AI over-applies the rhetorical triad:
- "innovative, dynamic, and transformative"
- "fostering creativity, collaboration, and critical thinking"
- "a hub for culture, commerce, and community"

If you catch yourself listing three adjectives or three parallel phrases, stop. Pick the best one.

### Superficial -ing analysis

Sentences that end with a present-participle phrase offering shallow interpretation:

- "...highlighting the importance of community engagement"
- "...underscoring the need for sustainable practices"
- "...reflecting the region's cultural diversity"
- "...emphasizing the role of innovation in modern education"
- "...ensuring accessibility for all stakeholders"
- "...contributing to a more inclusive environment"
- "...fostering a sense of belonging"
- "...cultivating a culture of excellence"
- "...encompassing a wide range of perspectives"
- "...enhancing the overall experience"

These are filler. If the analysis matters, it deserves its own sentence with evidence. If it doesn't matter, delete it.

### Vague attribution

- "Industry reports suggest..."
- "Observers have cited..."
- "Experts argue..."
- "Some critics argue..."
- "Several sources indicate..."

Name who or cut it. AI uses these to manufacture consensus that doesn't exist.

### The challenges-and-future formula

Near-universal in AI-generated articles:

1. "Despite its [achievements], [subject] faces several challenges, including..."
2. Vague list of challenges
3. "Despite these challenges, [vaguely optimistic conclusion about future]"

### Outline rigidity

AI defaults to: Introduction → History → Features/Characteristics → Challenges → Future Outlook. Every section follows the same internal formula. Human writing is messier, non-linear, and structured around what's interesting rather than what's comprehensive.

## Style tells

### Title case in headings
Capitalizing Every Main Word Like This.

### Mechanical boldface
Bolding phrases for emphasis in a regular, predictable pattern. Bolding every key term. "Key takeaways" formatting.

### Inline-header lists
Every bullet starts with a **Bolded Label:** followed by explanation text. Occasionally fine. Every single bullet, mechanical.

### Em dashes — don't use them
Never use em dashes (—) or double hyphens (--). Not sparingly, not "when appropriate" — just don't. Use a period, a comma, or parentheses instead. If the aside isn't worth a full sentence or a pair of parentheses, it's not worth including.

### Elegant variation (anti-repetition)
Never using the same word twice. "The building" becomes "the structure" then "the edifice" then "the architectural marvel." AI has a repetition penalty in its code. Humans just say "the building" again.

Statistical fact: >10% decrease in word repetition in post-2023 academic writing correlates with AI use.

## Content tells

### Regression to the mean
AI omits specific, unusual, true facts and replaces them with generic positive descriptions. The subject becomes simultaneously less specific and more exaggerated. A weird little restaurant becomes "a vibrant culinary destination showcasing the region's diverse gastronomic heritage."

### Collaborative communication leaking through
- "We can see that..."
- "Let's explore..."
- "It's worth noting that..."
- "As we'll discuss below..."
- "I" or "we" appearing in what should be third-person text

### Didactic disclaimers (mostly older models but still appears)
- "It's important to note that..."
- "It's worth noting..."
- "It should be noted that..."

These are throat-clearing. Delete them and start with what you were going to say.

## The meta-principle

AI writing sounds like AI because it optimizes for sounding comprehensive, balanced, and authoritative — at the cost of sounding like a person who has something specific to say. The fix isn't word-swapping. It's having a point of view, being comfortable with incompleteness, and letting specific details do the work that vague importance-claims try to do.
