from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """Show the public home page for the vulnerable app scaffold."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
