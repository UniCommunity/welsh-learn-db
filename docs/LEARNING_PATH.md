# Suggested path

Follow `data/lessons.json` in order. A sustainable pace is one lesson every few days plus daily 10-minute review.

## Weekly rhythm

| Day | Minutes | Task |
| --- | --- | --- |
| Daily | 10 | Drill yesterday's phrases (`python src/cli.py drill --topic greetings`) |
| 3× week | 20 | New lesson + mutation practice |
| 1× week | 30 | Listen to easy Welsh (news headlines, learners' radio) and log 5 unknown words |

## Using the database

```bash
python src/cli.py load
python src/cli.py vocab --topic family
python src/cli.py phrase thank
python src/cli.py mutate Cymru --kind soft
python src/cli.py drill --topic courtesy
```

## What “done” looks like at Entry

- Greet, thank, apologise, and say your name and origin
- Affirm, ask, and negate simple `dw i'n` sentences
- Recognise soft mutation in the wild even if you still hesitate to produce it
- Count to 20 and name the days

Then add nasal/aspirate recognition and a wider verb-noun set.
