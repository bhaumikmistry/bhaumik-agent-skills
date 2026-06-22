# Communication principles

Load this file before any coaching mode. These are the scoring rubric for all reviews, drafts, and coaching sessions.

## Origin

These principles emerged from specific feedback: in high-pressure situations (deadlines compressing, key people leaving, ambiguity), the communication style can land as shutting down junior engineers — even when intent is collaborative. The gap is between intent and delivery, not between good and bad character.

The incident: an MCP integration meeting where a junior engineer was brought in for expertise but without project context, a solution was pre-formed, discussion went circular under pressure, and the follow-up meeting was cancelled in favor of shipping solo. Impact: her input was bypassed.

Peer's read: "wrong venue, not wrong person." Both things are true — the structure was bad AND the way the impasse was handled was bad.

## The 5 commitments

### 1. Front-load context before asking for input

When bringing someone into a discussion where there's a knowledge gap, present the project context first. Never ask someone for advice on a domain where they lack the project-specific context to give useful input — that sets them up to say something uninformed and then get "corrected."

**Good:** "Here's what we've built, here's why we made these choices. Given that — what's your read?"
**Bad:** "What do you think about X?" (when they have no context on X)

**Real example:** The MCP meeting asked a junior engineer for input on tool integrations she had no project context for. Better structure: 30 min present context, then 30 min gather input.

### 2. Name the impasse instead of bypassing

When a discussion goes circular, call it out explicitly rather than cancelling and shipping solo. Even if you end up making the call, make it transparently.

**Good:** "I think we're going in circles. The disagreement is specifically about Y. I'm going to go with Z because of [reason] — I want to be upfront about that."
**Bad:** Cancel the follow-up meeting and submit the CR alone.

**Why it matters:** Bypassing says "your voice doesn't matter" even when the technical decision is correct. The cost of one transparent sentence is zero. The cost of silent bypass is trust.

### 3. Understand what they're optimizing for

Before pushing back on someone's position, surface their constraints. People argue for positions because of concerns you can't see.

**Good:** "What are you most worried about here?" / "What would break for you if we went with X?" / "Is there something in your sprint plan this would impact?"
**Bad:** Debating the position without understanding what drives it.

**Real example:** Concerns may have been about sprint plan impact, not just technical disagreement. Surfacing that changes the conversation from "your approach is wrong" to "let's solve both constraints."

### 4. Reduce the surface area of disagreement

Instead of debating broadly, isolate the specific point of difference.

**Good:** "I think we agree on A, B, and C. The thing we disagree on is D. Let's focus there."
**Bad:** Relitigating the entire approach when only one piece is contested.

### 5. Bring people along rather than teach/convince

Position yourself alongside, not above. Share the reasoning journey rather than asserting the conclusion.

**Good:** "Here's the journey I went through to land on X — does that track, or am I missing something?"
**Bad:** "Here's why X is the right approach." (positions you as the authority)

**The difference:** Teaching says "I know and you need to learn." Bringing along says "I went through this thinking and I want to check it with you." Same information, different power dynamic.

## Anti-patterns to flag

When reviewing a message, flag these:

| Pattern | Why it lands poorly | Real example |
|---------|-------------------|--------------|
| Providing the answer before asking their read | Signals "I already know, you're just confirming" | "May be its as simple as updating the Carnaval alarm" — gave the fix before she assessed |
| "I wonder why..." framing | Can read as "someone should have caught this" | "I wonder why this ticket is still being cut to FAR" — observing is fine, questioning implies blame |
| CC'ing people who don't need to act | Feels like performing collaboration for an audience | CC'ing someone on a routine routing question — ask: does he need to act, or am I signaling? |
| Offering a hypothesis before they've assessed | Robs them of ownership over the diagnosis | Let the person who owns the system diagnose it. Offer help, not answers. |
| "But the deadline" / "But X left" as justification | Reads as excusing rather than owning | These are real pressures — acknowledge privately, don't use as defense |
| Broad debate when only one point is contested | Exhausting and unproductive | Isolate the disagreement to one specific technical decision |
| Cancelling/bypassing after disagreement | Says "your voice doesn't matter" | Cancelled follow-up, shipped CR solo |
| "That's not who I am" | Defensive — denies impact | Say "that's not who I want to be" instead — acknowledges the gap |

## Positive patterns to reinforce

When these appear, call them out as strengths:

| Pattern | Why it works | Real example |
|---------|-------------|--------------|
| "We" language | Shared ownership, not blame | "This is something we could have missed in our transition" |
| Offering without imposing | Collaborative, not directive | "if you need to brainstorm, please reach out to me" |
| Asking before asserting | Surfaces hidden constraints | "what are you worried about?" |
| Confirming rather than assuming | Respect, not accusation | "you weren't paged for this, right?" |
| Letting the other person own the diagnosis | Builds their confidence and agency | Asking a peer to figure out where tickets are coming from, not telling them the answer |
| Factual framing over questioning framing | Observing vs. accusing | "Looks like this is still routing to FAR" vs. "I wonder why this is still routing to FAR" |
| Explicit offers with escape hatches | Respects autonomy | "Let me know if you want to brainstorm — no pressure" |

## Adjusting for audience

| Audience | Adjust |
|----------|--------|
| Junior engineer | Maximum care. Never imply they should have known. Frame questions as routing, not testing. Offer context before asking for input. |
| Peer | Direct. Can push back harder. Still apply principle 5. |
| Senior/skip-level | Concise. Lead with the point. Data over narrative. |
| Cross-team (no shared context) | Extra context upfront. Assume no shared assumptions. Principle 1 is critical. |
| Someone you've received feedback about | Extra care. Everything you do is being read through the lens of the feedback. Changed behavior over time > one perfect message. |

## The meta-rules

1. **Intent doesn't cancel impact.** "I didn't mean it that way" is information about the gap between intent and delivery. The skill exists to close that gap.

2. **One incident is not a reputation.** It's a signal, caught early. The goal is to make the next 5 interactions so clearly collaborative that this one becomes an outlier people forget.

3. **Changed behavior over time > one perfect apology.** No single message fixes a pattern. Consistency does.

4. **The feedback conversation itself is the test.** How you handle hearing "you shut down juniors" is the most visible demonstration of whether you actually do. Open with curiosity, listen without interrupting, reflect back, own the impact, share what you're changing, ask what else.

5. **Stress is an explanation, not an excuse.** Deadline pressure and losing team members are real. They explain the context. They don't justify the impact. Acknowledge them privately to maintain self-compassion — don't deploy them in conversations about impact on others.
