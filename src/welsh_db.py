"""Load JSON learning data into SQLite and query it."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_DB = ROOT / "welsh_learn.sqlite"


def connect(db_path: Path | str = DEFAULT_DB) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    sql = (ROOT / "schema" / "schema.sql").read_text(encoding="utf-8")
    conn.executescript(sql)
    conn.commit()


def _load_json(name: str) -> Any:
    path = DATA / name
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_all(conn: sqlite3.Connection) -> dict[str, int]:
    init_schema(conn)
    counts: dict[str, int] = {}

    vocab = _load_json("vocabulary.json")["items"]
    conn.execute("DELETE FROM vocabulary")
    conn.executemany(
        """
        INSERT INTO vocabulary (id, cy, en, pos, gender, plural, topic, level, pron)
        VALUES (:id, :cy, :en, :pos, :gender, :plural, :topic, :level, :pron)
        """,
        [
            {
                "id": row["id"],
                "cy": row["cy"],
                "en": row["en"],
                "pos": row.get("pos"),
                "gender": row.get("gender"),
                "plural": row.get("plural"),
                "topic": row.get("topic"),
                "level": row.get("level"),
                "pron": row.get("pron"),
            }
            for row in vocab
        ],
    )
    counts["vocabulary"] = len(vocab)

    phrases = _load_json("phrases.json")["items"]
    conn.execute("DELETE FROM phrases")
    conn.executemany(
        """
        INSERT INTO phrases (id, cy, en, pron, topic, level, register, region, notes)
        VALUES (:id, :cy, :en, :pron, :topic, :level, :register, :region, :notes)
        """,
        [
            {
                "id": row["id"],
                "cy": row["cy"],
                "en": row["en"],
                "pron": row.get("pron"),
                "topic": row.get("topic"),
                "level": row.get("level"),
                "register": row.get("register"),
                "region": row.get("region"),
                "notes": row.get("notes"),
            }
            for row in phrases
        ],
    )
    counts["phrases"] = len(phrases)

    lessons = _load_json("lessons.json")["path"]
    conn.execute("DELETE FROM lessons")
    conn.executemany(
        """
        INSERT INTO lessons (id, title, level, goals_json, study_json, practice_json)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (
                row["id"],
                row["title"],
                row.get("level"),
                json.dumps(row.get("goals", []), ensure_ascii=False),
                json.dumps(row.get("study", []), ensure_ascii=False),
                json.dumps(row.get("practice", []), ensure_ascii=False),
            )
            for row in lessons
        ],
    )
    counts["lessons"] = len(lessons)

    grammar = _load_json("grammar.json")["topics"]
    conn.execute("DELETE FROM grammar_topics")
    conn.executemany(
        """
        INSERT INTO grammar_topics (id, title, level, summary, body_json)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (
                row["id"],
                row["title"],
                row.get("level"),
                row.get("summary"),
                json.dumps(row, ensure_ascii=False),
            )
            for row in grammar
        ],
    )
    counts["grammar_topics"] = len(grammar)

    conn.commit()
    return counts


def search_vocab(
    conn: sqlite3.Connection,
    q: str | None = None,
    topic: str | None = None,
    level: str | None = None,
) -> list[sqlite3.Row]:
    clauses: list[str] = []
    params: list[Any] = []
    if q:
        clauses.append("(cy LIKE ? OR en LIKE ?)")
        like = f"%{q}%"
        params.extend([like, like])
    if topic:
        clauses.append("topic = ?")
        params.append(topic)
    if level:
        clauses.append("level = ?")
        params.append(level)
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    return list(conn.execute(f"SELECT * FROM vocabulary {where} ORDER BY cy", params))


def search_phrases(
    conn: sqlite3.Connection,
    q: str | None = None,
    topic: str | None = None,
) -> list[sqlite3.Row]:
    clauses: list[str] = []
    params: list[Any] = []
    if q:
        clauses.append("(cy LIKE ? OR en LIKE ?)")
        like = f"%{q}%"
        params.extend([like, like])
    if topic:
        clauses.append("topic = ?")
        params.append(topic)
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    return list(conn.execute(f"SELECT * FROM phrases {where} ORDER BY id", params))


def topics(conn: sqlite3.Connection) -> Iterable[str]:
    rows = conn.execute(
        """
        SELECT topic FROM vocabulary WHERE topic IS NOT NULL
        UNION
        SELECT topic FROM phrases WHERE topic IS NOT NULL
        ORDER BY 1
        """
    )
    return [r[0] for r in rows]


SOFT = {"p": "b", "t": "d", "c": "g", "b": "f", "d": "dd", "g": "", "m": "f", "ll": "l", "rh": "r"}
NASAL = {"p": "mh", "t": "nh", "c": "ngh", "b": "m", "d": "n", "g": "ng"}
ASPIRATE = {"p": "ph", "t": "th", "c": "ch"}


def _apply_map(word: str, mapping: dict[str, str]) -> str:
    lower = word.lower()
    for src in sorted(mapping, key=len, reverse=True):
        if lower.startswith(src):
            dest = mapping[src]
            rest = word[len(src) :]
            if word[:1].isupper() and dest:
                dest = dest[0].upper() + dest[1:]
            elif word[:1].isupper() and not dest and rest:
                rest = rest[0].upper() + rest[1:]
            return dest + rest
    return word


def mutate(word: str, kind: str = "soft") -> str:
    kind = kind.lower()
    if kind in {"soft", "sm", "meddal"}:
        return _apply_map(word, SOFT)
    if kind in {"nasal", "nm", "trwynol"}:
        return _apply_map(word, NASAL)
    if kind in {"aspirate", "am", "llaes", "spirant"}:
        return _apply_map(word, ASPIRATE)
    raise ValueError(f"Unknown mutation kind: {kind}")


if __name__ == "__main__":
    import sys

    cmd = sys.argv[1] if len(sys.argv) > 1 else "load"
    conn = connect()
    if cmd == "load":
        print(load_all(conn))
    elif cmd == "topics":
        print("\n".join(topics(conn)))
    elif cmd == "mutate" and len(sys.argv) >= 3:
        kind = sys.argv[3] if len(sys.argv) > 3 else "soft"
        print(mutate(sys.argv[2], kind))
    else:
        print("Usage: python -m src.welsh_db [load|topics|mutate WORD [soft|nasal|aspirate]]")
