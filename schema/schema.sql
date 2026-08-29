-- Welsh Learn DB — SQLite schema
-- Load JSON with: python -m src.welsh_db load

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS vocabulary (
    id          TEXT PRIMARY KEY,
    cy          TEXT NOT NULL,
    en          TEXT NOT NULL,
    pos         TEXT,
    gender      TEXT CHECK (gender IN ('m', 'f') OR gender IS NULL),
    plural      TEXT,
    topic       TEXT,
    level       TEXT,
    pron        TEXT
);

CREATE TABLE IF NOT EXISTS phrases (
    id          TEXT PRIMARY KEY,
    cy          TEXT NOT NULL,
    en          TEXT NOT NULL,
    pron        TEXT,
    topic       TEXT,
    level       TEXT,
    register    TEXT,
    region      TEXT,
    notes       TEXT
);

CREATE TABLE IF NOT EXISTS lessons (
    id          TEXT PRIMARY KEY,
    title       TEXT NOT NULL,
    level       TEXT,
    goals_json  TEXT,
    study_json  TEXT,
    practice_json TEXT
);

CREATE TABLE IF NOT EXISTS grammar_topics (
    id          TEXT PRIMARY KEY,
    title       TEXT NOT NULL,
    level       TEXT,
    summary     TEXT,
    body_json   TEXT
);

CREATE INDEX IF NOT EXISTS idx_vocab_topic ON vocabulary(topic);
CREATE INDEX IF NOT EXISTS idx_vocab_level ON vocabulary(level);
CREATE INDEX IF NOT EXISTS idx_vocab_cy ON vocabulary(cy);
CREATE INDEX IF NOT EXISTS idx_phrases_topic ON phrases(topic);
CREATE INDEX IF NOT EXISTS idx_phrases_level ON phrases(level);
