# FoodGauge — landing page

Static landing page for **FoodGauge**, a food label and barcode scanner (iOS live, Android in closed testing).

Live: https://teach-bot-sys.github.io/foodgauge-site/

| File | |
|---|---|
| `index.html` | English (canonical, `x-default`) |
| `tr.html` `ru.html` `ar.html` | Turkish, Russian, Arabic — each fully pre-rendered |
| `app.css` | Compiled styles (the pages need no JavaScript) |
| `llms.txt` | Structured plain-text brief for AI/LLM crawlers |
| `robots.txt` | Explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot and others |
| `sitemap.xml` | All four language URLs with `hreflang` alternates |
| `og.png` | 1200×630 social preview |

Every page ships its full content in the HTML source — no client-side rendering is
required to read it — plus `SoftwareApplication`, `FAQPage` and `WebSite` JSON-LD,
canonical and `hreflang` tags. Arabic renders right-to-left with the layout mirrored.

The pages are plain HTML (FAQ uses native `<details>`), so there is no client-side rendering step.
The November 2026 copy was regenerated with `_src/build_pages.py` (run `python3 _src/build_pages.py .`); the older React + Vite source no longer matches
the live text, so do not rebuild from it without carrying these changes over.

Not medical advice. Label-based general information only.
