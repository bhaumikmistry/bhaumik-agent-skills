#!/usr/bin/env python3
"""Generate index.html from the skills themselves.

The page is derived, never hand-edited, so it cannot drift from the repo. Add a
skill directory and this build fails until that skill has an entry in
site_content.py - which is the whole enforcement mechanism. Editing index.html
by hand is pointless; the next build overwrites it.

    python3 scripts/build_site.py

Design direction, recorded here because the page has no other design system:
a two-colour service manual - black ink and one spot red on off-white stock,
every skill an entry with its trigger, what it does and the rule it will not
bend. Two inks only. Rules, not cards. No shadows, no gradients.
"""
import re
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from site_content import SKILLS, EXAMPLES  # noqa: E402

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Bricolage+Grotesque:opsz,wght@12..96,300;12..96,400;12..96,600;12..96,800"
         "&family=Spline+Sans+Mono:wght@400;600&display=swap")


def read_skills():
    found = {}
    for d in sorted((ROOT / "skills").iterdir()):
        f = d / "SKILL.md"
        if not f.exists():
            continue
        fm = re.match(r"^---\n(.*?)\n---", f.read_text(), re.S)
        if not fm:
            raise SystemExit(f"{f} has no frontmatter")
        block = fm.group(1)
        desc = re.search(r"description:\s*(.+?)(?=\nmetadata:|\Z)", block, re.S).group(1)
        ver = re.search(r"version:\s*(\S+)", block)
        found[d.name] = {
            "dir": d.name,
            "description": " ".join(desc.split()),
            "version": ver.group(1) if ver else None,
            "refs": sorted(p.name for p in (d / "references").glob("*.md")),
        }
    missing = sorted(set(found) - set(SKILLS))
    if missing:
        raise SystemExit(
            f"no landing-page entry for: {', '.join(missing)}.\n"
            f"Add one to scripts/site_content.py, then re-run. The page is generated "
            f"from that file, so a skill without an entry would be invisible on it."
        )
    stale = sorted(set(SKILLS) - set(found))
    if stale:
        raise SystemExit(f"site_content.py documents skills that no longer exist: {', '.join(stale)}")
    return found


CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --stock:#f6f3f1; --ink:#191519; --ink-soft:#5d5459; --rule:#d6cfcb;
  --spot:#c1361b; --spot-wash:#f6e6e1; --band:#efe9e6;
  --mono:"Spline Sans Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  --sans:"Bricolage Grotesque","Trebuchet MS",Verdana,sans-serif;
  --measure:34rem;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --stock:#141013; --ink:#f2ebe8; --ink-soft:#a1918c; --rule:#33292c;
    --spot:#f0705a; --spot-wash:#2a1a18; --band:#1d1719;
  }
}
:root[data-theme="dark"]{
  --stock:#141013; --ink:#f2ebe8; --ink-soft:#a1918c; --rule:#33292c;
  --spot:#f0705a; --spot-wash:#2a1a18; --band:#1d1719;
}
body{margin:0;background:var(--stock);color:var(--ink);font-family:var(--sans);
  font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:64rem;margin:0 auto;padding:0 28px}
a{color:var(--spot);text-underline-offset:3px}
h1,h2,h3{margin:0;text-wrap:balance;font-weight:800;letter-spacing:-0.02em;line-height:1.05}
p{margin:0 0 1rem}
code,.mono{font-family:var(--mono);font-size:0.86em}

.masthead{border-bottom:2px solid var(--ink);padding:22px 0}
.masthead .wrap{display:flex;align-items:baseline;gap:16px;flex-wrap:wrap}
.wordmark{font-size:1.05rem;font-weight:800;letter-spacing:-0.01em}
.wordmark b{color:var(--spot)}
.masthead .meta{margin-left:auto;font-family:var(--mono);font-size:0.8rem;
  color:var(--ink-soft);letter-spacing:0.04em}

.hero{padding:76px 0 58px;border-bottom:1px solid var(--rule)}
.hero h1{font-size:clamp(2.6rem,7vw,5rem)}
.hero h1 em{font-style:normal;color:var(--spot)}
.hero .lede{max-width:var(--measure);margin-top:26px;font-size:1.13rem;color:var(--ink-soft)}
.cmd{margin-top:30px;display:inline-flex;align-items:center;gap:12px;
  border:1.5px solid var(--ink);padding:13px 17px;font-family:var(--mono);font-size:0.85rem}
.cmd span{color:var(--spot)}

section{padding:62px 0;border-bottom:1px solid var(--rule)}
.eyebrow{font-family:var(--mono);font-size:0.8rem;letter-spacing:0.04em;
  color:var(--spot);margin-bottom:14px}
section>.wrap>h2{font-size:clamp(1.7rem,3.4vw,2.4rem);max-width:26ch}
.intro{max-width:var(--measure);margin-top:18px;color:var(--ink-soft)}

.entry{display:grid;grid-template-columns:15rem 1fr;gap:34px;
  padding:30px 0;border-top:1px solid var(--rule)}
.entry:first-of-type{border-top:2px solid var(--ink)}
.entry .no{font-family:var(--mono);font-size:0.8rem;color:var(--spot)}
.entry h3{font-size:1.32rem;margin:7px 0 9px}
.entry .blurb{color:var(--ink-soft);font-size:0.95rem}
.entry .trig{margin-top:12px;font-family:var(--mono);font-size:0.82rem;
  color:var(--ink-soft);line-height:1.5}
.entry .trig b{color:var(--ink);font-weight:400;display:block;letter-spacing:0.1em;
  font-size:0.78rem;margin-bottom:3px}
.entry .body{max-width:var(--measure)}
.rule-note{margin-top:15px;padding:13px 16px;background:var(--spot-wash);
  border-left:2.5px solid var(--spot);font-size:0.92rem}
.rule-note b{display:block;font-family:var(--mono);font-size:0.78rem;
  letter-spacing:0.04em;color:var(--spot);margin-bottom:5px;font-weight:600}
.refs{margin-top:13px;font-family:var(--mono);font-size:0.8rem;color:var(--ink-soft)}

.ex{display:grid;grid-template-columns:repeat(2,1fr);gap:26px;margin-top:34px}
.ex article{border:1.5px solid var(--ink);display:flex;flex-direction:column;background:var(--band)}
.frame{position:relative;aspect-ratio:16/10;overflow:hidden;border-bottom:1.5px solid var(--ink);
  background:var(--stock)}
.frame iframe{position:absolute;top:0;left:0;width:1400px;height:875px;border:0;
  transform:scale(calc(1/2.1));transform-origin:top left;pointer-events:none}
.ex .txt{padding:19px 20px 21px}
.ex h3{font-size:1.12rem}
.ex .topic{font-family:var(--mono);font-size:0.8rem;letter-spacing:0.04em;
  color:var(--spot);margin-bottom:8px}
.ex .dir{margin:9px 0 0;font-size:0.94rem}
.ex .note{margin:10px 0 0;font-size:0.87rem;color:var(--ink-soft)}
.ex .foot{margin-top:15px;display:flex;justify-content:space-between;align-items:baseline;
  gap:12px;font-family:var(--mono);font-size:0.8rem;color:var(--ink-soft)}

.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:32px}
.cols h3{font-size:1rem;margin-bottom:9px}
.cols p{font-size:0.92rem;color:var(--ink-soft);margin:0}
.tree{margin-top:26px;font-family:var(--mono);font-size:0.82rem;line-height:1.85;
  color:var(--ink-soft);border:1px solid var(--rule);padding:19px 22px;overflow-x:auto}
.tree b{color:var(--spot);font-weight:400}

footer{padding:46px 0 70px;font-family:var(--mono);font-size:0.82rem;color:var(--ink-soft)}
footer a{color:var(--ink)}

@media (max-width:820px){
  .ex,.cols{grid-template-columns:1fr}
  .entry{grid-template-columns:1fr;gap:14px}
  .hero{padding:52px 0 42px}
  section{padding:46px 0}
  .frame iframe{transform:scale(calc(1/3.4))}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""


def entry(i, key, meta):
    c = SKILLS[key]
    refs = (f'<div class="refs">references/ {" · ".join(r.replace(".md", "") for r in meta["refs"])}</div>'
            if meta["refs"] else "")
    ver = f' · v{meta["version"]}' if meta["version"] else ""
    return f"""<article class="entry">
  <div>
    <div class="no">{i:02d}{escape(ver)}</div>
    <h3>{escape(key)}</h3>
    <div class="blurb">{escape(c["blurb"])}</div>
    <div class="trig"><b>FIRES ON</b>{escape(c["trigger"])}</div>
  </div>
  <div class="body">
    <p>{escape(c["body"])}</p>
    <div class="rule-note"><b>THE RULE IT WILL NOT BEND</b>{escape(c["rule"])}</div>
    {refs}
  </div>
</article>"""


def example(e):
    return f"""<article>
  <div class="frame"><iframe src="examples/{e['file']}" title="{escape(e['name'])}"
       loading="lazy" scrolling="no" tabindex="-1" aria-hidden="true"></iframe></div>
  <div class="txt">
    <div class="topic">{escape(e['topic'])}</div>
    <h3>{escape(e['name'])}</h3>
    <p class="dir">{escape(e['direction'])}</p>
    <p class="note">{escape(e['note'])}</p>
    <div class="foot"><span>Set in {escape(e['face'])}</span>
      <a href="examples/{e['file']}">Open the page &rarr;</a></div>
  </div>
</article>"""


def build():
    found = read_skills()
    order = ["ui-craft", "fpl-gameweek", "architecture-map", "coach",
             "interviewer", "not-ai", "arsenal-match-writeup"]
    order += [k for k in found if k not in order]
    entries = "\n".join(entry(i, k, found[k]) for i, k in enumerate(order, 1) if k in found)
    examples = "\n".join(example(e) for e in EXAMPLES)
    n = len(found)

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>bhaumik-agent-skills &mdash; {n} working methods, written down</title>
<meta name="description" content="A collection of agent skills for Claude Code: a working method per skill, each with the trigger that fires it and the rule it will not bend.">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="masthead"><div class="wrap">
  <div class="wordmark">bhaumik<b>/</b>agent-skills</div>
  <div class="meta">{n} SKILLS &middot; CLAUDE CODE &middot; MIT</div>
</div></header>

<div class="hero"><div class="wrap">
  <h1>Seven working methods,<br>written down so they <em>survive the session</em>.</h1>
  <p class="lede">A skill is not a prompt. It is a procedure with an order, a set of
  rules it refuses to break, and a record of what went wrong last time. These are the
  ones that earned their place by being used more than once.</p>
  <div class="cmd"><span>$</span> npx skills add bhaumikmistry/bhaumik-agent-skills</div>
</div></div>

<section><div class="wrap">
  <div class="eyebrow">WHAT THIS IS</div>
  <h2>An agent that forgets everything is only ever as good as its last instruction.</h2>
  <div class="intro">
    <p>Every one of these started as the same conversation happening for the third time.
    A skill is where that conversation stops being retyped: the order the steps go in,
    the check that is not optional, the mistake that was made once and is now written
    into the procedure so it is not made again.</p>
    <p>They install into Claude Code as a plugin and fire on what you actually say,
    rather than on a command you have to remember.</p>
  </div>
  <div class="cols">
    <div><h3>A fixed order</h3><p>Most of these refuse to start at the interesting
      step. The gameweek skill will not plan a transfer until last week is on the
      record, because planning first is just chasing scores.</p></div>
    <div><h3>A stated refusal</h3><p>Each one names the thing it will not do. That is
      usually the part carrying the value, and it is always the part learned the
      expensive way.</p></div>
    <div><h3>A record that outlives the chat</h3><p>Ledgers, retrospectives, design
      notes. If the reasoning only exists in a conversation, the next session
      re-derives it and gets a different answer.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">THE SKILLS</div>
  <h2>Seven of them, and what each one refuses to do.</h2>
  {entries}
</div></section>

<section><div class="wrap">
  <div class="eyebrow">BUILT WITH UI-CRAFT</div>
  <h2>Four landing pages, four briefs, no visual direction given.</h2>
  <div class="intro">
    <p>The <code>ui-craft</code> skill was tested by handing four agents four unrelated
    products and telling them nothing about how the pages should look. The risk was
    that all four would converge on the same warm-cream-and-serif default that
    generated interfaces reliably produce.</p>
    <p>They did not. Four directions, four typefaces, and every one of them traceable
    to something true about its subject. Each page below is rendered live from this
    repository &mdash; they are static files in <code>examples/</code>, not screenshots.</p>
  </div>
  <div class="ex">{examples}</div>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">HOW A SKILL IS PUT TOGETHER</div>
  <h2>One file that always loads, and references that load when they are needed.</h2>
  <div class="intro"><p><code>SKILL.md</code> carries the frontmatter the router reads
  and the procedure the agent follows. Anything long enough to be a distraction on
  every invocation &mdash; a schema, a catalogue, a scoring method &mdash; goes into
  <code>references/</code> and is read only when that step is reached.</p></div>
  <div class="tree">skills/<br>
  &nbsp;&nbsp;<b>ui-craft/</b><br>
  &nbsp;&nbsp;&nbsp;&nbsp;SKILL.md<br>
  &nbsp;&nbsp;&nbsp;&nbsp;references/<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shadcn.md &nbsp;impeccable.md &nbsp;new-component.md<br>
  <b>examples/</b> &nbsp;&larr; the four pages above<br>
  <b>scripts/</b> &nbsp;&nbsp;build_site.py &nbsp;site_content.py<br>
  index.html &nbsp;&larr; generated, never edited by hand</div>
</div></section>

<footer><div class="wrap">
  This page is generated by <code>scripts/build_site.py</code> from the skills themselves,
  so it cannot drift. Adding a skill without documenting it fails the build.<br>
  <a href="https://github.com/bhaumikmistry/bhaumik-agent-skills">github.com/bhaumikmistry/bhaumik-agent-skills</a>
  &nbsp;&middot;&nbsp; <a href="https://www.bhaumikmistry.com">bhaumikmistry.com</a>
</div></footer>
</body>
</html>
"""
    out = ROOT / "index.html"
    out.write_text(html)
    print(f"wrote index.html  ({len(html)//1024}KB, {n} skills, {len(EXAMPLES)} examples)")
    for k in order:
        if k in found:
            print(f"    {k}")


if __name__ == "__main__":
    build()
