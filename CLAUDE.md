# bhaumik-agent-skills

A plugin of agent skills for Claude Code, and a generated landing page that
documents them at https://bhaumikmistry.github.io/bhaumik-agent-skills/

## The one rule that matters

**`index.html` is generated. Never edit it by hand.**

```bash
python3 scripts/build_site.py
```

It reads every `skills/*/SKILL.md` frontmatter and renders the page from that
plus the editorial copy in `scripts/site_content.py`. Anything typed directly
into `index.html` is gone at the next build.

## Adding a skill

The build enforces most of this, so the short version is: add the skill, run the
build, and do what it tells you.

1. `skills/<name>/SKILL.md` with frontmatter carrying `name` (matching the
   directory), a `description` written for the router, and optionally
   `metadata.version`. Long material goes in `skills/<name>/references/*.md`.
2. **Add an entry to `scripts/site_content.py`** keyed by the directory name,
   with four fields:
   - `blurb` — one line, what it is, written for a person rather than a router
   - `trigger` — what someone says that fires it
   - `body` — two or three sentences on what it actually does
   - `rule` — **the thing it refuses to do.** This is the important field. Every
     skill here exists because a mistake was made twice; the rule is that mistake
     written down. A skill with no stated refusal is usually a skill that has not
     been used in anger yet.
3. `python3 scripts/build_site.py`. It **fails** if a skill directory has no
   entry, and fails if `site_content.py` names a skill that no longer exists. It
   also picks up the ordering list in `build_site.py` — new skills land at the
   end unless added to `order`.
4. Bump the version in `.claude-plugin/marketplace.json` and `.codex-plugin/plugin.json`,
   and add a section to `README.md`.
5. Run the detector on the rebuilt page and open it:
   ```bash
   NODE_OPTIONS= npx -y impeccable@latest detect index.html
   python3 -m http.server 8933   # then actually look at it, including at 375px
   ```

## Changing a skill's description

`SKILL.md` frontmatter feeds the page directly, so a description edit needs a
rebuild. The two files say different things on purpose: `description` is written
to be read by a router deciding whether to fire, `site_content.py` is written to
be read by a person deciding whether they care. Do not collapse one into the
other.

## The examples

`examples/` holds four landing pages built by four agents with the `ui-craft`
skill, and the page frames them live rather than screenshotting them. They are
evidence, not decoration: they exist to show that four agents given no visual
direction produced four different designs.

If you replace one, keep it a single self-contained file whose `<head>` holds
only charset, viewport, title, one font link and one `<style>` block, and update
its entry in `EXAMPLES`.

## The landing page's own design

Recorded here because the page has no `DESIGN.md` and the direction is otherwise
only in the generator's docstring:

> A two-colour service manual — black ink and one spot red on off-white stock,
> every skill an entry with its trigger, what it does and the rule it will not bend.

Two inks and the stock, nothing else. Rules rather than cards, no shadows, no
gradients. Bricolage Grotesque for everything human, Spline Sans Mono for
anything a machine reads or types. Neutrals are tinted toward the spot rather
than being grey.

It was built with the `ui-craft` skill in this repo, which means it is bound by
its rules: the detector runs, but **opening the page is the check**, and the
detector has never once caught a broken control because it does not render
anything.
