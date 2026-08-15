# FoodGauge — landing page

Static, pre-rendered landing page for **FoodGauge**, an AI food label scanner for Android and iOS.

Live: https://teach-bot-sys.github.io/foodgauge-site/

| File | |
|---|---|
| `index.html` | English (canonical, `x-default`) |
| `tr.html` `ru.html` `ar.html` | Turkish, Russian, Arabic — each fully pre-rendered |
| `app.css` `app.js` | Compiled styles and script |
| `llms.txt` | Structured plain-text brief for AI/LLM crawlers |
| `robots.txt` | Explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot and others |
| `sitemap.xml` | All four language URLs with `hreflang` alternates |
| `og.png` | 1200×630 social preview |

Every page ships its full content in the HTML source — no client-side rendering is
required to read it — plus `SoftwareApplication`, `FAQPage` and `WebSite` JSON-LD,
canonical and `hreflang` tags. Arabic renders right-to-left with the layout mirrored.

Built from a React + Vite + Tailwind source project, server-rendered to static HTML:

```bash
npx vite build
npx vite build --ssr src/entry-server.tsx --outDir dist-ssr
node prerender.mjs
```

Not medical advice. Label-based general information only.
