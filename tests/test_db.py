from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.welsh_db import connect, load_all, mutate, search_vocab


def test_mutations():
    assert mutate("Cymru", "soft") == "Gymru"
    assert mutate("tad", "soft") == "dad"
    assert mutate("cath", "soft") == "gath"
    assert mutate("gardd", "soft") == "ardd"
    assert mutate("tad", "nasal") == "nhad"
    assert mutate("tad", "aspirate") == "thad"
    assert mutate("afal", "soft") == "afal"


def test_load_and_search(tmp_path):
    db = tmp_path / "test.sqlite"
    conn = connect(db)
    counts = load_all(conn)
    assert counts["vocabulary"] >= 20
    assert counts["phrases"] >= 20
    rows = search_vocab(conn, q="Wales")
    assert any(r["cy"] == "Cymru" for r in rows)
