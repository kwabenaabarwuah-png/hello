# Notes App

A small notes app with three interfaces, all sharing one SQLite database:

- `app.py`: database functions (`add_note`, `list_notes`)
- `cli.py`: terminal menu for adding and listing notes
- `web.py`: Flask web page for adding and listing notes in the browser

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
```

## Run

```bash
python cli.py   # terminal menu
python web.py   # web page at http://localhost:5000
```

The notes are stored in `notes.db`, which is created automatically and ignored by Git.
