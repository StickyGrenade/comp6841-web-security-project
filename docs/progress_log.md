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
