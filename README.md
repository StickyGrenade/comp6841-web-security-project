# VulnerableNotes

VulnerableNotes is a small local Flask web application for my UNSW COMP6841
Security Engineering project. I built a simple notes app, introduced selected
vulnerabilities on purpose, demonstrated them safely on my own machine, and
fixed them in a separate secure version called SecureNotes.

This project is for local educational use only. All testing was done against my
own local application.

## Current Status

Completed:

- Milestone 1: basic Flask scaffold
- Milestone 2: registration, login, logout, and sessions
- Milestone 3: create, list, view, and search notes
- Milestone 4: SQL injection demonstration in note search
- Milestone 5: stored XSS demonstration in note detail rendering
- Milestone 6: broken access control / IDOR demonstration
- Milestone 7: weak password handling demonstration
- Milestone 8: fixed secure version with all four issues patched

Still to do:

- Final report and presentation polish (Milestone 9)

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

## Vulnerable Version

Initialize the vulnerable version database:

```bash
flask --app vulnerable_version/app.py init-db
```

Run the vulnerable version locally:

```bash
python3 vulnerable_version/app.py
```

Open:

```text
http://127.0.0.1:5000/
```

## Fixed Secure Version

Initialize the fixed version database:

```bash
flask --app fixed_version/app.py init-db
```

Run the fixed secure version locally:

```bash
python3 fixed_version/app.py
```

Open:

```text
http://127.0.0.1:5001/
```

Both versions can run at the same time on different ports for before-and-after
comparison.

## What I Tested

I tested the local apps by registering fake accounts, logging in and out,
creating notes, viewing note details, and searching notes. I demonstrated SQL
injection, stored XSS, IDOR, and plaintext password storage in the vulnerable
version, then verified each issue was blocked or fixed in the secure version.
Details are in `docs/progress_log.md` and `docs/vulnerability_writeups/`.

## Documentation

- `docs/progress_log.md`: development progress and reflections
- `docs/vulnerability_writeups/`: vulnerability explanations and fixes
- `docs/screenshots/`: evidence screenshots
