"""Editorial copy for the landing page, one entry per skill.

Deliberately separate from SKILL.md. A skill's own description is written to be
read by a router deciding whether to fire; this is written to be read by a
person deciding whether they care. They are not the same job and one should not
be made to do the other.

build_site.py fails when a skill directory has no entry here, which is what
stops the page silently going stale.
"""

SKILLS = {
    "ui-craft": dict(
        blurb="Build interfaces that do not read as agent-generated.",
        trigger="a new page, a redesign, “make this look better”",
        body="Reaches for shadcn/ui before writing anything by hand, retheming what it takes "
             "to the project's own tokens rather than pasting defaults. Runs Impeccable's "
             "deterministic detector over the result, then publishes anything built twice to "
             "a registry so it installs by name next time.",
        rule="Rendering the page is the check. The detector is a linter and will pass a page "
             "with visibly broken controls, because it never opens one.",
    ),
    "fpl-gameweek": dict(
        blurb="Run a Fantasy Premier League season as a ledger rather than a hunch.",
        trigger="transfers, captaincy, chips, “predict next team”",
        body="Pulls live data, projects three ranked plans at no hit, minus four and minus "
             "eight, then scores every one of them against the real result once the gameweek "
             "settles, including the plans that were never played. Studies what the league "
             "leaders did differently with their chips stripped out.",
        rule="Planning is the last step, not the first. Without last week's opposition read "
             "on the record it refuses to plan, because the alternative is chasing scores.",
    ),
    "architecture-map": dict(
        blurb="Turn a system into a place you can walk around.",
        trigger="“how does this fit together”, onboarding, a system diagram",
        body="Takes a repository, a design doc or a rough idea and renders an isometric city: "
             "buildings sized by weight, lines that are real call paths, moving dots that are "
             "payloads. One self-contained page, zoomable, click-to-inspect.",
        rule="Synthesise the understanding first and render it second. A diagram drawn "
             "straight from a file listing shows the folders, not the system.",
    ),
    "coach": dict(
        blurb="Communication coaching, in four modes.",
        trigger="“help me write”, “how does this sound”, “coach me”",
        body="Drafts messages, reviews them against a set of stated commitments, reads back "
             "over past conversations for patterns, and prepares for the conversation nobody "
             "wants to have.",
        rule="Front-load the context before asking for input, and name the impasse rather "
             "than routing around it.",
    ),
    "interviewer": dict(
        blurb="Keep an async interview series moving.",
        trigger="“draft outreach”, “next question”, “follow up with”",
        body="Drafts the approach, shapes questions that earn a real answer instead of a "
             "press release, chases politely, and holds the pipeline so nobody is left on "
             "read for three weeks.",
        rule="One question at a time. A list of six arrives as homework and gets answered "
             "like homework.",
    ),
    "not-ai": dict(
        blurb="Strip the tells out of writing.",
        trigger="“de-AI this”, “sounds generated”, “too robotic”",
        body="Works from a catalogue of the patterns that give machine prose away: elaborate "
             "verbs where a plain one would do, the rule of three, negative parallelism, "
             "hedge-then-assert, and the closing sentence about significance that says "
             "nothing.",
        rule="Specific beats smooth. One odd true detail is worth more than a paragraph that "
             "reads well and asserts nothing.",
    ),
    "arsenal-match-writeup": dict(
        blurb="Write up a match without inventing any of it.",
        trigger="“we just played”, “match report”, “update the tracker”",
        body="Produces a verified post for the site and updates the fixture tracker in the "
             "same pass, so the write-up and the record cannot disagree with each other.",
        rule="Every scoreline, scorer and minute is checked against a source before it is "
             "written. Recalled football is confidently wrong football.",
    ),
}

EXAMPLES = [
    dict(file="pitchside.html", name="Pitchside", topic="Grassroots football",
         direction="A public notice pinned to a clubhouse door.",
         face="Public Sans",
         note="The brief's real problem was not weather, it was that nobody knows who "
              "decided what. So the hero is a dated, signed call-off notice and the "
              "accountability log is a section rather than a footnote."),
    dict(file="nightfall.html", name="Nightfall", topic="Moth recording",
         direction="A night-lit field ledger, machine in cold actinic blue, recorder in lamp-amber.",
         face="Newsreader",
         note="Certainty is drawn as a fill texture, not a percentage: solid means separable, "
              "hatched means two moths that cannot be told apart without dissection. It "
              "survives greyscale and colour blindness, which a number does not."),
    dict(file="lending-shed.html", name="The Lending Shed", topic="Tool library",
         direction="A workshop shadow board, where every tool has an outline it goes back into.",
         face="Archivo",
         note="A tool library's problem is return, not acquisition, so deposits and late fees "
              "are stated up front with a note naming who each rule protects, and every "
              "liability is capped at the deposit."),
    dict(file="couchette.html", name="Couchette", topic="European night trains",
         direction="A printed continental timetable read at night.",
         face="Bodoni Moda",
         note="Bookability is a column in the table rather than an error bolted on, and each "
              "unbookable route names the operator responsible, so it reads as a fact about "
              "the railway instead of a failure of the site."),
]
