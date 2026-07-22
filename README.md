# VulnerableNotes

VulnerableNotes is a small local Flask web application for my UNSW COMP6841
Security Engineering project. I am building a simple notes app, introducing
selected vulnerabilities on purpose, demonstrating them safely on my own
machine, and then fixing them in a separate secure version.

This project is for local educational use only. All testing was done against my
own local application.

## Current Status

Completed so far:

- Milestone 1: basic Flask scaffold
- Milestone 2: registration, login, logout, and sessions
- Milestone 3: create, list, view, and search notes
- Milestone 4: SQL injection demonstration in note search

Still to do:

- Stored XSS demonstration
- Broken access control / IDOR demonstration
- Weak password handling demonstration
- Fixed secure version
- Final report and presentation polish

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the vulnerable version database:

```bash
flask --app vulnerable_version/app.py init-db
```

Run the vulnerable version locally:

```bash
python3 vulnerable_version/app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## What I Tested

I tested the local app by registering fake accounts, logging in and out,
creating notes, viewing note details, and searching notes. For SQL injection, I
used two local test users and compared a normal search with a crafted local
search input on `/search`. Details are in `docs/progress_log.md` and
`docs/vulnerability_writeups/sql_injection.md`.

## Documentation

- `docs/progress_log.md`: development progress and reflections
- `docs/vulnerability_writeups/`: vulnerability explanations
- `docs/screenshots/`: evidence screenshots
