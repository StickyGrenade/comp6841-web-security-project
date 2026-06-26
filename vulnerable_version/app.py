import os
import sqlite3
from functools import wraps

from flask import (
    abort,
    Flask,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")
app.config["DATABASE"] = os.path.join(app.root_path, "vulnerablenotes.sqlite3")


def get_db():
    """Open one SQLite connection for the current request."""
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row

    return g.db


@app.teardown_appcontext
def close_db(error=None):
    """Close the database connection when the request finishes."""
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Create database tables from the schema file."""
    db = get_db()

    with app.open_resource("schema.sql") as schema_file:
        db.executescript(schema_file.read().decode("utf-8"))


@app.cli.command("init-db")
def init_db_command():
    """Reset the local development database."""
    init_db()
    print("Initialized the vulnerable version database.")


def login_required(view):
    """Redirect visitors to the login page if they are not signed in."""
    @wraps(view)
    def wrapped_view(**kwargs):
        if session.get("user_id") is None:
            flash("Please log in to access that page.")
            return redirect(url_for("login"))

        return view(**kwargs)

    return wrapped_view


@app.route("/")
def index():
    """Show the public home page for the vulnerable app scaffold."""
    return render_template("index.html")


@app.route("/register", methods=("GET", "POST"))
def register():
    """Register a new local test account."""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db = get_db()
                # VULNERABLE: Passwords are stored in plaintext for the later
                # COMP6841 weak password handling demonstration.
                db.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, password),
                )
                db.commit()
            except sqlite3.IntegrityError:
                error = f"The username '{username}' is already taken."
            else:
                flash("Registration successful. Please log in.")
                return redirect(url_for("login"))

        flash(error)

    return render_template("register.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    """Log in with a local test account."""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        error = None
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,),
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        # VULNERABLE: Plaintext password comparison is intentionally kept for
        # the later COMP6841 weak password handling demonstration.
        elif user["password"] != password:
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            flash(f"Welcome back, {user['username']}!")
            return redirect(url_for("index"))

        flash(error)

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log out the current user."""
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("index"))


@app.route("/notes", methods=("GET", "POST"))
@login_required
def notes():
    """Create a note and list notes owned by the current user."""
    db = get_db()

    if request.method == "POST":
        title = request.form["title"].strip()
        body = request.form["body"].strip()
        error = None

        if not title:
            error = "Note title is required."
        elif not body:
            error = "Note body is required."

        if error is None:
            db.execute(
                """
                INSERT INTO notes (user_id, title, body)
                VALUES (?, ?, ?)
                """,
                (session["user_id"], title, body),
            )
            db.commit()
            flash("Note created.")
            return redirect(url_for("notes"))

        flash(error)

    user_notes = db.execute(
        """
        SELECT id, title, body, created_at
        FROM notes
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (session["user_id"],),
    ).fetchall()

    return render_template("notes.html", notes=user_notes)


@app.route("/note/<int:note_id>")
@login_required
def note_detail(note_id):
    """Show one note owned by the current user."""
    note = get_db().execute(
        """
        SELECT id, title, body, created_at
        FROM notes
        WHERE id = ? AND user_id = ?
        """,
        (note_id, session["user_id"]),
    ).fetchone()

    if note is None:
        abort(404)

    return render_template("note_detail.html", note=note)


@app.route("/search")
@login_required
def search():
    """Search notes owned by the current user."""
    query = request.args.get("q", "").strip()
    results = []

    if query:
        like_query = f"%{query}%"
        results = get_db().execute(
            """
            SELECT id, title, body, created_at
            FROM notes
            WHERE user_id = ? AND (title LIKE ? OR body LIKE ?)
            ORDER BY created_at DESC
            """,
            (session["user_id"], like_query, like_query),
        ).fetchall()

    return render_template("search.html", query=query, results=results)


if __name__ == "__main__":
    app.run(debug=True)
