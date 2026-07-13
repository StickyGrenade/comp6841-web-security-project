# Progress Log

## Milestone 1: Basic Flask Scaffold

Built the initial Flask scaffold for the vulnerable version of VulnerableNotes.
The app had one homepage route, a shared Jinja base template, a homepage
template, and simple CSS.

Manual testing:

- Confirmed the Flask app could start locally.
- Confirmed the homepage loaded in the browser.

Screenshots to capture:

- Homepage loading successfully.
- Terminal showing the local Flask server.

## Milestone 2: User Registration and Login

Added basic account functionality to the vulnerable version. The app now has a
local SQLite `users` table, registration, login, logout, session-based logged-in
state, flash messages, and navigation that changes based on whether a user is
logged in.

Manual testing:

- Initialize the database with `flask --app vulnerable_version/app.py init-db`.
- Register a local test account.
- Log in with the test account.
- Confirm the homepage shows the logged-in username.
- Log out and confirm the register/login links return.
- Try registering a duplicate username and confirm an error appears.

Screenshots to capture:

- Registration page.
- Successful registration message or redirect to login.
- Login page.
- Homepage showing logged-in username.
- Homepage after logout.

## Milestone 3: Notes Features

Added the core notes functionality for logged-in users. The vulnerable version
now has a local SQLite `notes` table, a page for creating and listing notes, an
individual note detail page at `/note/<id>`, and a basic search page for note
titles and body text.

Manual testing:

- Initialize the database with `flask --app vulnerable_version/app.py init-db`.
- Register and log in as a local test user.
- Create a note with a title and body.
- Confirm the note appears on the My notes page.
- Open the note detail page.
- Search for the note by title or body text.
- Log out and confirm notes pages require login.

Screenshots to capture:

- Empty My notes page.
- Note creation form.
- My notes page with at least one saved note.
- Individual note detail page.
- Search page with matching results.

## Milestone 4: SQL Injection Demonstration

Changed the vulnerable version's note search to intentionally use unsafe SQL
string construction. This creates a local-only SQL injection demonstration for
COMP6841. The vulnerable code is marked with a `VULNERABLE:` comment, and the
search page includes a warning that the behaviour is intentional.

Manual testing:

- Initialize the database with `flask --app vulnerable_version/app.py init-db`.
- Register and log in as a local test user.
- Create at least one normal note.
- Run a normal search and confirm it returns expected matching notes.
- Create or use a second local test user with a different note.
- Run a local SQL injection demonstration search and confirm the query logic can
  be changed in the vulnerable version.
- One local demonstration input for this app is `') OR 1=1 -- `.
- Keep all testing local to this app.

Screenshots to capture:

- Normal search input and expected result.
- SQL injection demonstration input.
- Unexpected or excessive results caused by the vulnerable query.
- Vulnerable `search()` route code showing the `VULNERABLE:` comment.
