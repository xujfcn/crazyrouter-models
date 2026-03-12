# crazyrouter-models

Static SEO landing pages for `crazyrouter.com/models/*`.

## Generate pages

Run:

```bash
python scripts/generate_pages.py
```

The generator fetches live pricing from `https://crazyrouter.com/api/pricing` and rebuilds:

- `index.html` for `/models/`
- `sitemap.xml` for index-priority pages
- individual model pages under each model folder

## Index strategy

Current index-priority pages:

- `gpt-4o`
- `gpt-5`
- `claude-sonnet-4-6`

Current review/noindex pages:

- `gpt-5-mini`
- `claude-opus-4-6`
- `gemini-2-5-pro`
- `gemini-2-5-flash`
- `deepseek-v3`
- `deepseek-r1`
- `o3`
- `o4-mini`

## What each page includes

- live price comparison versus direct provider pricing
- canonical URL and robots control
- Product + FAQ JSON-LD
- review metadata (`last reviewed`, `review cadence`, `owner`)
- code examples and related model links
- model-specific positioning, best-fit use cases, and disqualification guidance
