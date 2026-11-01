# mrboddu.co.uk website

Static website for Mr Krishna Boddu, built by Claude.

- `src/` page text (`pages_*.py`), settings (`site_config.py`), styles and the build script.
- `site/` the finished website, ready to publish (Netlify publishes this folder).
- `preview/` a PDF of every page and screenshots, for review.

Rebuild after editing: `python3 src/build.py`, then `node src/render.js` for a new preview.
`PREVIEW` in `src/site_config.py` is False for the live site; set it to True only for drafts (adds a banner and a noindex tag).
