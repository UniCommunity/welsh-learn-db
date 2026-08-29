#!/usr/bin/env python3
"""Tiny CLI for the Welsh learning database."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.welsh_db import connect, load_all, mutate, search_phrases, search_vocab, topics


def main() -> int:
    parser = argparse.ArgumentParser(description="Query the Welsh Learn DB")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("load", help="Create/refresh SQLite from JSON")
    sub.add_parser("topics", help="List vocabulary and phrase topics")

    p_v = sub.add_parser("vocab", help="Search vocabulary")
    p_v.add_argument("query", nargs="?", default=None)
    p_v.add_argument("--topic")
    p_v.add_argument("--level")

    p_p = sub.add_parser("phrase", help="Search phrases")
    p_p.add_argument("query", nargs="?", default=None)
    p_p.add_argument("--topic")

    p_m = sub.add_parser("mutate", help="Apply an initial mutation")
    p_m.add_argument("word")
    p_m.add_argument("--kind", default="soft", choices=["soft", "nasal", "aspirate"])

    p_d = sub.add_parser("drill", help="Print a compact study card set")
    p_d.add_argument("--topic", default="greetings")

    args = parser.parse_args()
    conn = connect()

    if args.cmd == "load":
        counts = load_all(conn)
        print(json.dumps(counts, indent=2))
        return 0

    if args.cmd == "topics":
        for t in topics(conn):
            print(t)
        return 0

    if args.cmd == "vocab":
        rows = search_vocab(conn, args.query, args.topic, args.level)
        for r in rows:
            extra = f" ({r['gender']})" if r["gender"] else ""
            print(f"{r['cy']}{extra} — {r['en']}  [{r['topic'] or '-'} / {r['level'] or '-'}]")
        print(f"# {len(rows)} rows")
        return 0

    if args.cmd == "phrase":
        rows = search_phrases(conn, args.query, args.topic)
        for r in rows:
            print(f"{r['cy']}  →  {r['en']}  ({r['pron'] or ''})")
        print(f"# {len(rows)} rows")
        return 0

    if args.cmd == "mutate":
        print(mutate(args.word, args.kind))
        return 0

    if args.cmd == "drill":
        rows = search_phrases(conn, topic=args.topic)
        if not rows:
            rows = search_vocab(conn, topic=args.topic)
        for r in rows:
            print(f"{r['en']}")
            print(f"    {r['cy']}")
            if "pron" in r.keys() and r["pron"]:
                print(f"    [{r['pron']}]")
            print()
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
