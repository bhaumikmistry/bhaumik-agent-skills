# bhaumik-agent-skills

Private agent skills for Claude Code.

## Usage

```bash
claude --plugin-dir /path/to/bhaumik-agent-skills
```

## Skills

### coach

Communication coaching skill. Four modes:

| Mode | Trigger | What it does |
|------|---------|--------------|
| **Draft** | "help me write", "draft a message to" | Draft messages with communication principles applied |
| **Review** | "how does this sound", paste a message | Review a draft against principles, flag anti-patterns, offer rewrites |
| **Reflect** | "review my slack", "what patterns do you see" | Review Slack history for communication patterns |
| **Coach** | "coach me for a meeting", "how should I approach" | Prepare for difficult conversations |

Based on 5 communication commitments:
1. Front-load context before asking for input
2. Name the impasse instead of bypassing
3. Understand what they're optimizing for
4. Reduce the surface area of disagreement
5. Bring people along rather than teach/convince

### interviewer

Async interview series skill (Zero Token, All Human). Handles outreach, question crafting, follow-ups, and pipeline management.

| Mode | Trigger | What it does |
|------|---------|--------------|
| **Outreach** | "draft outreach", "new target", "reach out to" | Cold outreach with story-driven hooks by platform |
| **Questions** | "prepare questions", "Q1", "next question" | Craft questions using the arc (origin→craft→tension→human→closing) |
| **Follow-up** | "follow up with", "nudge", "they haven't replied" | Thread revival, short-answer pushback, platform escalation |
| **Tone** | (loaded automatically) | Friendly, curious, story-telling voice guide |

Key principles:
- Never sound AI-written — be a person
- One question at a time, build on exact words from their answer
- Tell a discovery story as the hook (how you found them)
- Reference something specific they made/wrote/built
- Create tension or contrast they have to resolve

## Structure

```
.claude-plugin/plugin.json
.codex-plugin/plugin.json
skills/
├── coach/
│   ├── SKILL.md            ← dispatcher
│   ├── principles.md       ← the 5 commitments + anti-patterns + positive patterns
│   ├── draft-mode.md       ← drafting flow
│   ├── review-mode.md      ← message review flow
│   ├── reflect-mode.md     ← Slack history review flow
│   └── coach-mode.md       ← meeting/conversation prep flow
└── interviewer/
    ├── SKILL.md            ← dispatcher
    ├── tone.md             ← voice & personality guide
    ├── question-craft.md   ← question anatomy, arc, techniques
    ├── outreach.md         ← cold outreach by platform
    ├── follow-up.md        ← nudge strategies & thread revival
    └── data/
        └── target-list.md  ← pipeline reference & series info
```

## Adding new skills

Create a new directory under `skills/` with a `SKILL.md` frontmatter file:

```yaml
---
name: <skill-name>
description: <when this skill fires — under 500 chars>
---
```
