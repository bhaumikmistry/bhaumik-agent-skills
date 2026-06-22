---
name: interviewer
description: Async interview series helper — draft outreach, craft questions, follow up with interviewees, and manage the interview pipeline. Fires on "interview", "draft outreach", "new target", "follow up with", "Q1", "next question", "prepare questions for".
---

# interviewer

Helps run the Zero Token, All Human async interview series. Drafts outreach, crafts questions, follows up, and tracks the pipeline — all with the friendly, curious, storytelling tone that gets people to respond.

## When this skill fires

- The user wants to draft outreach to a new interview target
- The user wants to craft questions for an interviewee
- The user needs to follow up with someone who hasn't replied
- The user wants to build on an interviewee's answer with a follow-up question
- The user adds a new person to the target list
- The user says "interview", "new target", "draft outreach", "prepare questions", "follow up"

## Dispatch

| Intent | Read next |
|--------|-----------|
| Draft cold outreach to a new person | [outreach.md](outreach.md) |
| Craft interview questions (first or follow-up) | [question-craft.md](question-craft.md) |
| Follow up with someone who hasn't replied | [follow-up.md](follow-up.md) |
| Understand the voice and tone to use | [tone.md](tone.md) |

## Before doing anything

1. Load [tone.md](tone.md) — every message uses this as the voice guide.
2. Check the interviewee's file in `~/mac-workspace/assist/people/interviews/` for context.
3. Read [question-craft.md](question-craft.md) if writing any question.

## About the series

**Zero Token, All Human** (bhaumikmistry.com/zero-token-all-human)
- Async email conversations with people who have interesting, non-linear paths
- No AI-generated filler, no calls — just real back-and-forth over email
- Inspired by Brian Lovin's Staff Design and Will Larson's StaffEng
- Published example: Antje Barth (https://www.bhaumikmistry.com/zero-token-all-human/antje-barth)

## Key rules

- NEVER sound like AI wrote it
- ONE question at a time (unless interviewee asks for full list)
- Always build on the previous answer — pick up their exact words
- Keep emails short — no walls of text
- Always check existing interview file before drafting anything
- Reference data in [data/target-list.md](data/target-list.md) for pipeline status
