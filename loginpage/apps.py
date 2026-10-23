
import os
from datetime import timedelta
from functools import wraps

import psycopg 
from psycopg.rows import dict_row
from psycopg.errors import UniqueViolation

from flask import (
    Flask, render_template, request, redirect,
    url_for, session, flash
)
from werkzeug.security import (
    generate_password_hash, check_password_hash
)

app = Flask(__name__)

# Read secrets from environment variables.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")

if not app.config["SECRET_KEY"] or not DATABASE_URL:
    raise RuntimeError(
        "Set both SECRET_KEY and DATABASE_URL environment variables."
    )

app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = (
    os.environ.get("COOKIE_SECURE", "false").lower() == "true"
)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=14)


def get_db_connection():
    return psycopg.connect(
        DATABASE_URL,
        row_factory=dict_row,
        connect_timeout=5
    )


def init_db():
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                email VARCHAR(255) NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            )
        """)


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped_view


@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Enter your email address and password.")
            return render_template("register.html")

        if len(password) < 12:
            flash("Your password must contain at least 12 characters.")
            return render_template("register.html")

        password_hash = generate_password_hash(password)

        try:
            with get_db_connection() as conn:
                user = conn.execute(
                    """
                    INSERT INTO users (email, password_hash)
                    VALUES (%s, %s)
                    RETURNING id, email
                    """,
                    (email, password_hash)
                ).fetchone()

        except UniqueViolation:
            flash("Unable to register with those details.")
            return render_template("register.html")

        session.clear()
        session["user_id"] = user["id"]
        session["email"] = user["email"]

        return redirect(url_for("dashboard"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        remember = request.form.get("rememberme") == "on"

        with get_db_connection() as conn:
            user = conn.execute(
                """
                SELECT id, email, password_hash
                FROM users
                WHERE email = %s
                """,
                (email,)
            ).fetchone()

        if user and check_password_hash(
            user["password_hash"], password
        ):
            session.clear()
            session["user_id"] = user["id"]
            session["email"] = user["email"]
            session.permanent = remember

            return redirect(url_for("dashboard"))

        flash("Invalid email address or password.")

    return render_template("login.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template(
        "dashboard.html",
        email=session.get("email")
    )


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
