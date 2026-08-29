# Welsh NLP field guide

Welsh is low-resource in raw web tokens, but unusually well organised: public tools from Bangor’s Uned Technolegau Iaith (techiaith), Cardiff / CorCenCC, Welsh Government grants, and Microsoft.

This note is the repo’s map from **learner data in this project** to **production and research NLP**. Machine-readable links live in [`data/nlp_resources.json`](../data/nlp_resources.json).

## Why generic multilingual models stumble

1. **Initial mutation** — *tad / dad / nhad / thad* are one lemma. BPE and English-centric spellcheckers miss this. This repo’s `src.welsh_db.mutate()` and `data/mutations.json` implement the maps; they do not decide *when* a mutation applies.
2. **Verb-noun + bod** — tense sits on the auxiliary (`Dw i'n mynd`). See [`GRAMMAR.md`](GRAMMAR.md).
3. **Article clitic** — *y / yr / 'r*.
4. **Register and dialect** — *Shwmae* vs *S'mae*; tagged in `data/phrases.json`.
5. **Code-switching** — everyday Welsh mixes English. CorCenCC includes that mix; many MT sets do not.

Rule-based proofing (Cysill) still beats naive neural taggers on mutations.

## Stack by layer

| Layer | Tool / resource | Role |
| --- | --- | --- |
| Proofing | Cysill / Cysgliad | Spelling, grammar, mutation rules |
| Surface NLP | [CyTag](https://github.com/CorCenCC/CyTag) | Segment, sentence, tokenise, POS |
| Corpus | [CorCenCC](https://www.corcencc.org) | ~11M words, POS + semantic tags |
| Parallel text | OPUS + Iriaith EN–CY segments | MT / LLM post-training |
| ASR data | Common Voice CY, Bangor bank, Cymen | Speech training |
| STT | Trawsgrifiwr; Whisper-cy fine-tunes; Teams bilingual | Transcription |
| TTS | Piper voices; Trosleisio | Speech synthesis |
| Voice UI | Macsen | Welsh assistant |
| LLMs | Iriaith Welsh Llama 3; BritLLM; community finetunes | Generation |
| Eval | [techiaith/llm-evals-cy](https://github.com/techiaith/llm-evals-cy) | Grammar, lexicon, registers, MT |
| Learner CEFR | CardiffNLP CEFR-Cymraeg | Proficiency classification |

End-user catalogue: Welsh Government technology pages / Helo Blod.

## Task honesty

| Task | Status | Watch-out |
| --- | --- | --- |
| Spell / mutation check | Production (Cysill) | Best correctness tool |
| Tokenise + POS | Good in-domain (CyTag) | Drops on messy social text |
| Dependency parse | Research-ready (UD / HPLT) | Not a polished API |
| EN↔CY news/legal MT | Usable with post-edit | Weak on slang and mutations |
| Read-speech ASR | Strong and improving | Accents + noise |
| Conversational ASR | Getting there | Code-switch failures |
| TTS | Usable Piper | Less natural than EN flagships |
| Chat LLMs in Welsh | Possible | Fluency ≠ grammaticality |

Generic chat models often emit **fluent but wrongly mutated** Welsh. Run `welsh-grammar` in `llm-evals-cy` before trusting output.

## Hubs

- https://huggingface.co/techiaith
- https://github.com/techiaith
- https://github.com/CorCenCC
- https://techiaith.cymru
- https://techiaith.bangor.ac.uk
- https://www.gov.wales/welsh-language-technology-and-artificial-intelligence-ai-updates

## Experiments that use *this* repo

1. **Lemma search** — undo soft/nasal/aspirate with `mutate()` (or an inverse table) before SQLite `LIKE`.
2. **Grammar lint** — pipe generated sentences through Cysill or a rule layer built from `data/grammar.json`.
3. **CEFR filter** — attach Cardiff CEFR-Cymraeg scores to `level` on vocab/phrases.
4. **ASR loop** — transcribe with Trawsgrifiwr / Whisper-cy and compare to `data/phrases.json`.
5. **Eval harness** — treat `docs/GRAMMAR.md` headings as labels for model-output checks.

Related docs: [`GRAMMAR.md`](GRAMMAR.md), [`LEARNING_PATH.md`](LEARNING_PATH.md), [`RESOURCES.md`](RESOURCES.md).
