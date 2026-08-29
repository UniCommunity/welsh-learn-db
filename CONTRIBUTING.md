# Contributing

## Data rules

- Edit JSON in `data/`, not the generated SQLite file.
- Keep IDs stable. New items get the next free `v###` / `p###`.
- Gloss in short, natural English. Do not paste copyrighted course text.
- Mark gender on nouns whenever you know it.
- Tag `region` only when a form is strongly North or South.
- Pronunciation hints stay approximate; prefer consistency over faux-IPA.

## Code

- Python 3.10+
- `pytest` for tests
- No required third-party runtime deps

```bash
python src/cli.py load
python -m pytest -q
```

## Suggested additions

- Audio URLs or local filename fields
- IPA column
- Anki / CSV export
- More intermediate vocabulary
- Verb-noun argument patterns
- Place-name mutation table
