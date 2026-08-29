"""Example queries against a loaded welsh_learn.sqlite."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.welsh_db import connect, load_all, mutate, search_vocab, search_phrases


def main() -> None:
    conn = connect()
    print("Loading…", load_all(conn))

    print("\nFamily nouns:")
    for row in search_vocab(conn, topic="family"):
        print(f"  {row['cy']:12} {row['en']}")

    print("\nPhrases matching 'thank':")
    for row in search_phrases(conn, q="thank"):
        print(f"  {row['cy']} = {row['en']}")

    print("\nMutation demo:")
    for word in ("Cymru", "tad", "cath", "pen", "gardd"):
        print(f"  {word:8} SM={mutate(word,'soft'):8} NM={mutate(word,'nasal'):10} AM={mutate(word,'aspirate')}")


if __name__ == "__main__":
    main()
