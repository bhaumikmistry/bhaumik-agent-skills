# Stage 1 — The knowledge doc

The knowledge doc is the authored understanding of the system. It is the input
to rendering, and the part only a human-or-agent-that-read-the-material can
write. Get this right and the picture follows.

Write it to `architecture.knowledge.md`. Keep it tight — it is a working
artifact, not a report.

## The shape

```markdown
# <System name>

<One paragraph: what this system is, who it serves, why it exists. If the input
was an idea or a design doc, state your assumptions and anything the source left
unspecified — here, not silently in the diagram.>

## Groups (districts)
- **<Group label>** — <one line on what this neighborhood is for>
- ... (4–7 total)

## Nodes (subsystems)
| id | group | name | role | weight | tech | owns |
|----|-------|------|------|--------|------|------|
| orch | pipe | Orchestrator | Workflow engine | 5 | Step Functions | Expands a job into ordered steps; retries; resumes. |
| ... |

## Edges (paths)
| from | to | type | verb |
|------|----|------|------|
| orch | queue | run | enqueue |
| runner | secrets | dep | fetch creds |
| ... |

## Primary flow (lifecycle)
1. **<Step>** — <what happens>
2. ...
```

## Field guidance

- **Groups** — the mental model, not the folder layout. Name them the way the
  team (or the doc) talks. 4–7 keeps the city readable.
- **role** — a short noun phrase used as the panel subtitle: "the session gate",
  "system of record", "work buffer".
- **weight (1–6)** — how much of the system lives here. It becomes building
  height on a rough log scale: the busiest/most-central subsystem is a tower;
  a thin adapter is one storey. Don't make everything a 5.
- **owns** — one or two plain sentences. The interesting decision, not a
  dependency list. This is the writing that makes the map worth reading.
- **tech** — an example implementation ("Playwright", "SQS / Kafka",
  "DynamoDB"). For an idea, pick reasonable defaults and say they're examples.
- **edges** — a path you can name. `run` = part of the primary flow (drawn
  solid, animated as the main payload); `dep` = a supporting dependency (dashed).
  The `verb` is one or two words on the wire: "query", "persist", "on error".

## Filling it by input type

- **Repository** — explore before you write. Identify the framework and entry
  points, the top-level modules, the data stores and external calls. Every node
  should map to real code; every edge to a real call. Weight tracks real size
  (lines / files / responsibility), not vibes.
- **An idea or a thought** — design a sensible architecture for it. Prefer
  well-worn building blocks. Put your assumptions in the intro so the reader
  knows this is a proposal, not an existing system.
- **One design doc** — extract the components and flows it describes. If the doc
  implies a component without naming it, add it and note that you inferred it.
- **A set of design docs** — reconcile them into one system. When they overlap,
  merge; when they conflict, pick one and record the conflict in the intro.
  Don't emit two nodes for the same thing under different doc vocabularies.

## Scale

Past ~25 buildings the map stops being readable. Fold the smallest siblings into
a parent node, or map one subsystem/package at a time. If the system is genuinely
larger, produce several maps rather than one crowded one.
