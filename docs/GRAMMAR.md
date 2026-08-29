# Welsh grammar field guide

Spoken (colloquial) Welsh first. Literary Welsh keeps extra endings and particles; learn those when you start reading news or older prose.

Machine-readable notes: [`data/grammar.json`](../data/grammar.json), [`data/mutations.json`](../data/mutations.json), [`data/numbers.json`](../data/numbers.json).  
Practice the maps with `python src/cli.py mutate Cymru --kind soft`.

## 1. Word order: VSO (and Aux–S–aspect–VN)

Unmarked clauses put the **verb first**.

- Inflected verb: *Gwelodd Mair gath* — “Mair saw a cat.” The object often takes **soft mutation**.
- Everyday present uses **bod + subject + aspect + verb-noun**:
  *Mae Siân yn darllen y llyfr* — “Siân is reading / reads the book.”

Workhorse pattern:

**auxiliary → subject → aspect particle → verb-noun → object**

Fronting (focus) puts the important phrase first, then a relative-like clause.

## 2. Mutations (treigladau)

Dictionaries list the **radical**. If a lookup fails, undo a mutation (*dad* → *tad*).

| Radical | Soft (meddal) | Nasal (trwynol) | Aspirate (llaes) |
| --- | --- | --- | --- |
| p | b | mh | ph |
| t | d | nh | th |
| c | g | ngh | ch |
| b | f | m | — |
| d | dd | n | — |
| g | *(drops)* | ng | — |
| m | f | — | — |
| ll | l | — | — |
| rh | r | — | — |

**Soft** (every day): after *i, o, am, dy, ei* (“his”); feminine singular after *y/yr/'r*; adjective after a feminine noun; after *dau/dwy*; object after many inflected verbs.

**Nasal:** after *fy* and locative *yn* — *fy nhad*, *yng Nghaerdydd*.

**Aspirate:** only *p t c*. After *a* (“and”), *â/gyda*, *ei* (“her”), masculine *tri*.

Possessives:

- *fy* + nasal — my
- *dy* + soft — your (informal)
- *ei* + soft — his
- *ei* + aspirate (+ *h-* on vowels) — her
- *ein / eu* + *h-* on vowels — our / their
- *eich* — your (formal/plural), no mutation

## 3. Articles

No indefinite article. *ci* = “a dog / dog.” *un* means “one,” not English *a*.

Definite article:

1. *'r* after a vowel — *i'r dre*
2. *yr* before a vowel or *h* — *yr ysgol*
3. otherwise *y* — *y llyfr*

Feminine singular nouns soft-mutate after it: *y gath*, *yr ardd* (*gardd*).

## 4. Nouns: gender and number

Masculine or feminine. Learn gender with the word. Months are masculine. Gender shows in mutation and in *dau/dwy, tri/tair, pedwar/pedair*.

Nouns mark **number, not case**. Plurals vary (*-au, -iau, -on, vowel change, irregulars*). Some nouns are collective (*adar*) with a unit form (*aderyn*).

Possession is often “X of the Y”: *llyfr y ferch*.

## 5. Adjectives

Most follow the noun: *ci mawr*. After a feminine noun they often soft-mutate: *cath fawr*.

Preposed set (usually + soft mutation): *hen, hoff, prif, unig* — *hen dŷ*.

Predicative adjectives: *yn* + soft mutation — *Mae Gwyn yn ddiflas*.

## 6. Pronouns and *ti* vs *chi*

| | Informal sg | Formal / plural |
| --- | --- | --- |
| you | *ti* | *chi* |

Spoken subject pronouns after *bod*: *i, ti, e/o* (South *e*, North *o*), *hi, ni, chi, nhw*.

Yes/no often **echoes the verb**:

- *Wyt ti'n hoffi coffi?* — *Ydw* / *Nac ydw*

## 7. Verbs: verb-noun + *bod*

Dictionary form = **verb-noun** (*dysgu, mynd, bwyta*). Tense and person sit on an auxiliary.

### Periphrastic tenses

| Particle | Sense | Example |
| --- | --- | --- |
| *yn / 'n* | present | *Dw i'n mynd* |
| *wedi* | perfect | *Dw i wedi mynd* |
| *newydd* + SM | just | *Mae hi newydd fynd* |
| *am* + SM | about to | *Dw i am fynd* |

Colloquial present of *bod* (statement):

| | Affirmative | Negative |
| --- | --- | --- |
| I | *dw i* | *dw i ddim* |
| you sg | *wyt ti* | *dwyt ti ddim* |
| he / she | *mae e/o*, *mae hi* | *dydy e/o ddim*, *dydy hi ddim* |
| we | *dyn ni* | *dyn ni ddim* |
| you pl/form | *dych chi* | *dych chi ddim* |
| they | *maen nhw* | *dyn nhw ddim* |

Also meet *roedd* (was), *bydd* (will be / habitual), *byddai* (would).

### Inflected tenses

Spoken Welsh still conjugates **past, future, conditional** on the main verb. After the subject, the object often soft-mutates.

High-frequency irregulars: **mynd, dod, gwneud, cael**.

Spoken passive is often *cael* + verb-noun.

## 8. Inflected prepositions

Not *i e* for “to him”: *iddo fe*, *arni hi*, *amdana i*, *ohono fo*, *gen i*.

Stems: *ar → arn-*, *am → amdan-*, *o → ohon-*, *rhwng → rhyng-*.

Typical mutation after the bare preposition:

- soft: *i, o, am, ar, at, …*
- nasal: locative *yn*
- aspirate: *â, gyda*
- none: *mewn, rhwng, ger, cyn*

*yn* is three words in practice: aspect (*yn mynd*), predicate linker (*yn hapus*), and “in” (*yn y dre*).

## 9. Numbers

Decimal first: *un, dau/dwy, tri/tair, pedwar/pedair, pump … deg*.

- *dau/dwy* + soft mutation
- *tri* (masc.) + aspirate
- some shorten before a noun (*pum, chwe*)

Vigesimal forms still appear in time and set phrases.

## 10. One stacked example

*Alla i gael paned o goffi, os gwelwch yn dda?*

- *Alla i* — inflected *gallu*
- *gael* — soft mutation of *cael*
- *o goffi* — *o* + soft mutation
- *os gwelwch yn dda* — polite “please”

## Learn in this order

1. Present of *bod* + *yn* + verb-noun + *ddim*
2. Soft mutation survival kit
3. Article + feminine gender effect
4. *ti / chi* and verb-echo yes/no
5. *wedi* perfect
6. Nasal/aspirate recognition
7. Inflected past of common verbs
8. Inflected prepositions (*i, ar, am, o, gan*)

See [`LEARNING_PATH.md`](LEARNING_PATH.md) and [`data/lessons.json`](../data/lessons.json).
