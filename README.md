# Welsh Learn DB

Open, structured **dataset + starter toolkit** for learning Cymraeg (Welsh).

JSON is the source of truth. A small Python loader builds a local SQLite database you can query from a CLI, scripts, or your own app.

**Repository:** https://github.com/UniCommunity/welsh-learn-db

This is a template you can fork. It is not an official Dysgu Cymraeg course.

## Grammar guide (integrated)

Full spoken-Welsh field guide: **[docs/GRAMMAR.md](docs/GRAMMAR.md)**

| Topic | Where it lives |
| --- | --- |
| VSO + *bod* + verb-noun | [docs/GRAMMAR.md](docs/GRAMMAR.md#1-word-order-vso-and-auxsaspectvn) · `data/grammar.json` |
| Mutations | [docs/GRAMMAR.md](docs/GRAMMAR.md#2-mutations-treigladau) · `data/mutations.json` · `src/welsh_db.py mutate()` |
| Articles, gender, adjectives | [docs/GRAMMAR.md](docs/GRAMMAR.md#3-articles) |
| Tenses and irregulars | [docs/GRAMMAR.md](docs/GRAMMAR.md#7-verbs-verb-noun--bod) |
| Inflected prepositions | [docs/GRAMMAR.md](docs/GRAMMAR.md#8-inflected-prepositions) |
| Suggested study order | [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md) · `data/lessons.json` |

## NLP guide (integrated)

Welsh language technology map: **[docs/NLP.md](docs/NLP.md)** · catalogue **[`data/nlp_resources.json`](data/nlp_resources.json)**

| Topic | Where it lives |
| --- | --- |
| Why mutations break generic models | [docs/NLP.md](docs/NLP.md#why-generic-multilingual-models-stumble) · `data/mutations.json` |
| Tools, corpora, ASR, MT, LLMs | [docs/NLP.md](docs/NLP.md#stack-by-layer) |
| Task honesty | [docs/NLP.md](docs/NLP.md#task-honesty) |
| Experiments on this repo | [docs/NLP.md](docs/NLP.md#experiments-that-use-this-repo) |

## What is in the box

| Path | Contents |
| --- | --- |
| `data/vocabulary.json` | Starter lemmas (family, time, food, verbs, colours, culture) |
| `data/phrases.json` | High-frequency phrases with register and region tags |
| `data/mutations.json` | Soft / nasal / aspirate maps, triggers, examples |
| `data/alphabet.json` | Yr wyddor, including digraph letters |
| `data/numbers.json` | Decimal 0–100 samples + vigesimal notes |
| `data/grammar.json` | Entry-level notes (bod, VSO, article, gender, yes/no) |
| `data/lessons.json` | 8-lesson path from sounds to mutation recognition |
| `data/nlp_resources.json` | Hubs, tools, datasets, models, experiment hooks |
| `schema/schema.sql` | SQLite tables |
| `src/welsh_db.py` | Load + search + `mutate()` |
| `src/cli.py` | Command-line interface |
| `docs/` | Pronunciation, grammar, NLP, schema, resources |

## Quick start

```bash
git clone https://github.com/UniCommunity/welsh-learn-db.git
cd welsh-learn-db

python3 src/cli.py load
python3 src/cli.py vocab --topic family
python3 src/cli.py phrase --topic greetings
python3 src/cli.py mutate Cymru --kind soft
python3 src/cli.py drill --topic courtesy
python3 examples/query_examples.py
```

Optional tests:

```bash
pip install -r requirements.txt
python -m pytest -q
```

## Example

```text
$ python3 src/cli.py mutate tad --kind nasal
nhad

$ python3 src/cli.py vocab Wales
Cymru (f) — Wales  [places / entry]
```

Soft mutation of *Cymru* is *Gymru* (`Croeso i Gymru`). The helper in `src/welsh_db.py` implements the common initial maps; it does not decide *when* a mutation applies — that is grammar.

## Design notes

- **Levels:** `entry` ≈ Mynediad / A1, `foundation` ≈ Sylfaen / A2.
- **Register:** `informal` (`ti`) vs `formal` (`chi`) vs `neutral`.
- **Region:** `north`, `south`, or `all`. Spoken Welsh is not one accent.
- **No audio in v0.1.** Pair items with Learn Welsh, S4C, or your tutor.
- Data is original learner material compiled for this template, not a scrape of a copyrighted course.

## Repo as a GitHub template

On GitHub: **Settings → General → Template repository** so others can use **Use this template**.

Suggested topics: `welsh`, `cymraeg`, `language-learning`, `dataset`, `sqlite`, `nlp`.

## Roadmap

- [ ] CSV / Anki export
- [ ] IPA field
- [ ] Audio filename or URL column
- [ ] Intermediate vocabulary pack
- [ ] Optional FastAPI read-only server
- [ ] Inverse-mutation lemma search in the CLI
- [ ] Hook Cysill / llm-evals-cy against generated Welsh

## Licence

MIT — see `LICENSE`. Welsh is a living language; treat speakers and place names with care, and prefer official courses for classroom use.

**Pob lwc — good luck.**
