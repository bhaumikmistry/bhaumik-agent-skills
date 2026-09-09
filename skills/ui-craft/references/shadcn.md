# shadcn/ui

Docs: https://ui.shadcn.com/docs/components

## The model, and why it matters here

shadcn is not an npm dependency. The CLI **copies source into the project** and
from that moment you own it: you can edit it, retheme it, delete half of it.
There is no upgrade that will overwrite your changes and no version to keep in
step with.

Two consequences worth holding onto:

- Taking a component is not a dependency decision, so the bar for reaching for
  one is low. Writing a Dialog, a Combobox or a focus trap by hand when the
  catalogue has one is wasted work with worse accessibility.
- Because you own it, **the paste is the start, not the end**. A component left
  in shadcn's default styling inside a themed project is exactly the tell this
  skill exists to remove.

## Setting it up where it does not exist

```bash
npx shadcn@latest init          # writes components.json, sets up the alias + tokens
npx shadcn@latest add button    # then take components one at a time
```

`init` asks where components live and which token names to use. Answer with the
project's existing conventions, not the defaults, or every later `add` lands in
the wrong place.

**Tailwind v4:** shadcn supports it, but v4 moves theme config into CSS via
`@theme`. If the project is on a v4 alpha, check that `init` produced tokens the
project's CSS actually reads rather than a `tailwind.config.js` nothing loads.

## The catalogue, by what you are actually trying to do

Check here before concluding nothing fits. The right-hand column is the mistake
people make when they do not check.

| Need | Component | Commonly rebuilt by hand as |
|---|---|---|
| Overlay, focus trapped | `dialog`, `alert-dialog`, `sheet`, `drawer` | a div with `position: fixed` and no escape handling |
| Pick from a long list | `combobox`, `command` | an input with a filtered `<ul>` and no keyboard nav |
| Pick from a short list | `select`, `radio-group` | a native select that ignores the design system |
| Tabular data | `table`, `data-table` | a hand-rolled grid, then sorting bolted on |
| App chrome | `sidebar`, `navigation-menu`, `menubar`, `breadcrumb` | nested lists and manual aria |
| Transient feedback | `toast`, `sonner` | a fixed-position div and a `setTimeout` |
| Loading | `skeleton`, `spinner`, `progress` | a spinning border and a shrug |
| Disclosure | `accordion`, `collapsible`, `popover`, `hover-card` | `useState` and a conditional render |
| Dates | `calendar`, `date-picker` | an `<input type="date">` that looks foreign |
| Charts | `chart` | a raw Recharts config with default colours |
| Panels | `resizable`, `scroll-area`, `separator` | overflow hacks |
| Form plumbing | `form`, `input`, `textarea`, `checkbox`, `switch`, `toggle`, `label` | uncontrolled inputs and no error surface |
| Structure | `card`, `badge`, `avatar`, `tooltip`, `pagination`, `carousel` | usually fine to take as-is, then retheme |

`registry directory` on the docs site also lists community registries. Check it
before writing something niche; someone has often already published it.

## Adapting what you take

Do this in the same commit as the `add`, or it ships generic.

1. **Repoint the colours at the project's tokens.** shadcn arrives referencing
   its own `--primary`, `--muted`, `--border`. If the project names them
   something else, rename rather than introducing a parallel set.
2. **Reset the radius and shadow to the project's scale.** These two carry more
   house style than colour does, and shadcn's defaults are recognisable.
3. **Delete the variants you will not use.** A `button.tsx` shipping six
   variants when the product uses two is dead surface that later work will
   copy.
4. **Check the dark theme.** shadcn ships both; a project with only one of them
   will otherwise get a component that is invisible in the mode nobody tested.

## Provenance

Note in the component file where it came from and what was changed:

```tsx
/* From shadcn/ui `dialog`. Retheme: our --surface/--ink tokens, radius
   dropped to 4px, the default fade+zoom replaced with a plain fade. */
```

One line. It tells the next person that editing this is expected, and stops it
being "upgraded" back to defaults.
