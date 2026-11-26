import sqlite3

DB_PATH = "notes.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT NOT NULL)"
    )
    return conn

def add_note(text):
    with get_connection() as conn:
        conn.execute("INSERT INTO notes (text) VALUES (?)", (text,))

def list_notes():
    with get_connection() as conn:
        return conn.execute("SELECT id, text FROM notes ORDER BY id").fetchall()

if __name__ == "__main__":
    add_note("Set up the Ubuntu VM")
    add_note("Installed Python and SQLite")
    for note_id, text in list_notes():
        print(f"{note_id}: {text}")
