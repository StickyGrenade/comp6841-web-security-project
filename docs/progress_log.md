# Progress Log

This log records how I built VulnerableNotes for COMP6841. All testing was done
only against my own local Flask app.

## Milestone 1: Basic Flask Scaffold

I started with the smallest working Flask app. I created a home route, a shared
Jinja base template, a homepage template, and simple CSS. At this stage the app
only showed the VulnerableNotes homepage.

I set up a virtual environment, installed Flask, ran the app locally, and
confirmed the homepage loaded at `http://127.0.0.1:5000/`. This gave me a clean
base before adding accounts, notes, or security demonstrations.

Screenshots from this stage are in `docs/screenshots/milestone_01_scaffold/`.

## Milestone 2: User Registration and Login

Next I added user accounts. I created a SQLite `users` table, an `init-db`
command, registration, login, logout, and Flask sessions. The navigation changes
depending on whether someone is logged in.

I tested this by registering a local account, logging in, checking that the
homepage showed the signed-in username, logging out, and trying to register the
same username twice. Duplicate registration showed a clear error. I also kept
passwords in plaintext in the vulnerable version on purpose, with a
`VULNERABLE:` comment, so I could demonstrate weak password handling later.

Screenshots from this stage are in `docs/screenshots/milestone_02_auth/`.

## Milestone 3: Notes Features

I then built the normal notes features. I added a `notes` table, a page for
creating and listing notes, a note detail page at `/note/<id>`, and a search
page. Logged-out users are redirected to login when they try to open notes
pages.

I tested creating notes, viewing them in the list, opening one note by ID, and
searching by title or body text. At this point search still used parameterized
SQL and note content was rendered with normal Jinja escaping. I wanted the
normal app behaviour working before I introduced intentional vulnerabilities.

Screenshots from this stage are in `docs/screenshots/milestone_03_notes/`.

## Milestone 4: SQL Injection Demonstration

For the first vulnerability demonstration, I changed the note search route so it
builds SQL with string interpolation instead of placeholders. I marked the
unsafe code with a `VULNERABLE:` comment and added a warning on the search page
so the intentional behaviour is obvious.

I tested this locally with two fake users, Alice and Bob, each with their own
note. A normal search as Bob only returned Bob's matching note. When I entered
`') OR 1=1 -- ` into search, the query logic changed and the results included
notes that a normal search should not return. That made the impact easy to see.

Screenshots from this stage belong in
`docs/screenshots/milestone_04_sql_injection/`.

## Reflection So Far

Building the app in small milestones helped me understand each piece before
moving on. The biggest early challenge was learning how Flask routes, templates,
sessions, and SQLite fit together. Once notes were working, it became clearer
why security issues belong in ordinary application code, not only in separate
"security tools".

The next planned steps are stored XSS, broken access control / IDOR, weak
password handling, a fixed secure version, and final report preparation.
