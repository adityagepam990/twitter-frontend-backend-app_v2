# Styling

- SCSS Modules only. No Tailwind, no inline `style={{}}`, no CSS-in-JS.
- `src/styles/_tokens.scss` is the only file allowed to contain a colour, font family, font size, spacing value, radius, or breakpoint value. Every other stylesheet consumes tokens by reference.
- Every media query goes through the `respond-to()` mixin defined in `_mixins.scss`. A raw `@media` outside `_mixins.scss` is a violation.
- Keep `_tokens.scss` compact and comfortably under 5,000 tokens so it survives a context compaction with content intact.
- Component styles live in a co-located `.module.scss` file per component, never a shared global stylesheet beyond `globals.scss`.
- Never hardcode a hex value, pixel size, or breakpoint in a component stylesheet — reference a token instead.
