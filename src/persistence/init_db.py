from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = Path(__file__).with_name("schema.sql")
DB_PATH = PROJECT_ROOT / "data" / "adaptive_onboarding_tutor.db"

connection = sqlite3.connect(DB_PATH)

connection.execute("PRAGMA foreign_keys = ON;")

schema = SCHEMA_PATH.read_text(encoding="utf-8")

connection.executescript(schema)

connection.commit()
connection.close()

print(f"Database created at: {DB_PATH}")