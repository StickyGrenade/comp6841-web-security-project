# VulnerableNotes

VulnerableNotes is a small local Flask web application for a UNSW COMP6841
Security Engineering project. The project will be built incrementally: first as
a simple notes app, then as an intentionally vulnerable version, and finally as
a fixed secure version with before/after documentation.

This project is for local educational use only. All testing should be performed
only against this application running on your own computer.

## Current Status

Implemented so far:

- Milestone 1: basic Flask scaffold.
- Milestone 2: user registration, login, logout, sessions, and a local SQLite
  `users` table.

Not implemented yet:

- Notes features.
- SQL injection demonstration.
- Stored XSS demonstration.
- Broken access control / IDOR demonstration.
- Fixed secure version.

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

## Current Manual Tests

- Open the homepage.
- Register a local test account.
- Log in with that account.
- Confirm the navigation changes to show the logged-in username.
- Log out and confirm the navigation returns to register/login links.
- Try registering the same username twice and confirm the app shows an error.