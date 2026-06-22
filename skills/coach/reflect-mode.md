# Reflect mode

Review the user's recent Slack messages and surface communication patterns worth adjusting.

## Flow

### Step 1: Ask what to review

Ask the user:
- Which channel or DM to review? (or "recent messages across channels")
- Any specific person or interaction they're curious about?
- How far back? (default: last 7 days)

### Step 2: Pull messages

Use Slack MCP tools to read the user's recent messages in the specified channel(s). Focus on:
- Messages to/about junior team members
- Messages in group channels where juniors are present
- Messages during high-pressure moments (incidents, deadlines, disagreements)

### Step 3: Score each message

For each message, silently assess against principles.md. Don't report every single message — aggregate into patterns.

### Step 4: Surface patterns (not individual gripes)

Present findings as patterns, not a list of failures:

**Format:**
```
Pattern: [name]
Frequency: [X of Y messages]
Example: "[quoted text]"
Impact: [how it likely lands]
Alternative: [what to try instead]
```

**Example patterns to look for:**
- Providing solutions before asking their read
- "I wonder why" questioning framing
- Responding to questions with corrections rather than building on their thinking
- Jumping to technical detail without acknowledging their concern
- Offering help in a way that implies they need it

### Step 5: Acknowledge strengths

Also surface positive patterns. "In your last 8 messages to X, you consistently used 'we' framing and offered without imposing. That's landing well."

### Step 6: One concrete suggestion

End with exactly one thing to try in the next interaction. Not three. Not a framework. One specific thing.

**Format:** "Next time you're about to respond to [person] in [channel], try [specific behavior] before [the thing you'd normally do]."

## What NOT to do

- Don't dump 20 flagged messages on the user — that's demoralizing, not coaching
- Don't review messages where the user was clearly joking or off-duty
- Don't compare the user to others ("X does this better")
- Don't flag messages that are fine just because they're short or direct
- Don't ignore context — a terse message during an incident is appropriate

## Privacy note

Only review messages the user explicitly asks to review. Never proactively scan channels without being asked.
