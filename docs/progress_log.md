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

## Milestone 5: Stored XSS Demonstration

For the second vulnerability demonstration, I changed the note detail template
so the note body is rendered with Jinja's `| safe` filter instead of normal
escaping. I marked the unsafe rendering with a `VULNERABLE:` comment and added a
warning on the note detail page so the intentional behaviour is obvious.

I tested this locally by creating a normal note and confirming the body still
displayed correctly. I then created a note with a harmless local script payload
in the body. When I opened that note's detail page, the browser showed an alert
dialog. On the notes list page, the same payload stayed escaped and did not run.
That made it clear the stored content became dangerous only when the detail page
bypassed escaping.

Screenshots from this stage belong in
`docs/screenshots/milestone_05_stored_xss/`.

## Milestone 6: Broken Access Control / IDOR Demonstration

For the third vulnerability demonstration, I changed the note detail route so it
checks that a visitor is logged in, but does not check note ownership. The route
looks up a note by ID only. I marked the missing ownership check with a
`VULNERABLE:` comment and added a warning on the note detail page.

I tested this locally with two fake users, Alice and Bob, each with their own
note. While logged in as Bob, I changed the note ID in the URL to Alice's note.
The vulnerable app displayed Alice's private note. Logged-out visitors were
still redirected to login, which made the lesson clear: authentication without
authorization is not enough.

Screenshots from this stage belong in
`docs/screenshots/milestone_06_idor/`.

## Milestone 7: Weak Password Handling Demonstration

For the fourth vulnerability demonstration, I formally showed the plaintext
password storage that had been present since registration was added. The
register and login routes already stored and compared passwords as plain text,
with `VULNERABLE:` comments. I also added a warning on the register page so the
intentional behaviour is obvious.

I registered a local test account with a fake password, then inspected the
SQLite database and confirmed the password was stored in readable plaintext. I
logged in with the same fake password to confirm the vulnerable comparison still
worked. That made the risk clear: if the database file is leaked, every password
can be read directly.

Screenshots from this stage belong in
`docs/screenshots/milestone_07_passwords/`.

## Milestone 8: Fixed Secure Version

After completing the vulnerable version demonstrations, I built a separate fixed
secure version in `fixed_version/` called SecureNotes. It mirrors the same app
features but patches each demonstrated issue.

The fixed version uses parameterized SQL for search, normal Jinja escaping for
note bodies, ownership checks on note detail pages, and Werkzeug password hashing
for registration and login. It runs on port 5001 so I can compare it with the
vulnerable version on port 5000.

I retested each exploit against the fixed app. The SQL injection input was
treated as ordinary search text and returned no unexpected results. The stored
XSS payload displayed as escaped text on the note detail page. Bob received a
404 when trying to open Alice's note by ID. Passwords in the fixed database were
stored as hashes, not readable plaintext.

Screenshots from this stage belong in
`docs/screenshots/milestone_08_fixed_version/`.

## Reflection So Far

Building the app in small milestones helped me understand each piece before
moving on. The biggest early challenge was learning how Flask routes, templates,
sessions, and SQLite fit together. Once notes were working, it became clearer
why security issues belong in ordinary application code, not only in separate
"security tools".

Building the fixed version made the before-and-after comparison clearer. Each
fix was small and targeted, which helped me explain what changed and why.

The next planned step is final report and presentation preparation.
