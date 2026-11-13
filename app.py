
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    keyword = request.args.get("q", "")

    page = request.args.get("page", 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    db = None
    cursor = None
    mahasiswa = []

    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        query = """
            SELECT /*+ MAX_EXECUTION_TIME(3000) */
            *
            FROM mahasiswa
            WHERE nama LIKE %s
            LIMIT %s OFFSET %s
        """

        cursor.execute(query, (f"%{keyword}%", per_page, offset))
        mahasiswa = cursor.fetchall()

    except Exception as e:
        print("Terjadi error:", e)
        return "Pencarian gagal. Silakan coba lagi.", 500

    finally:
        if cursor is not None:
            cursor.close()

        if db is not None:
            db.close()

    return render_template(
        "search.html",
        keyword=keyword,
        mahasiswa=mahasiswa,
        page=page
    )


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        db = None
        cursor = None

        try:
            db = get_db_connection()
            cursor = db.cursor(dictionary=True)

            query = """
                SELECT *
                FROM users
                WHERE username = %s
            """

            cursor.execute(query, (username,))
            user = cursor.fetchone()

        except Exception as e:
            print("Login error:", e)
            return "Terjadi kesalahan pada server.", 500

        finally:
            if cursor is not None:
                cursor.close()

            if db is not None:
                db.close()

        if user and check_password_hash(user["password"], password):
            return "Login berhasil!"

        return "Username atau password salah!"

    return render_template("login.html")


@app.route("/api/mahasiswa", methods=["GET"])
def api_mahasiswa():

    db = None
    cursor = None

    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        query = """
            SELECT id, nim, nama, prodi, fakultas
            FROM mahasiswa
        """

        cursor.execute(query)
        data = cursor.fetchall()

        return jsonify({
            "status": "success",
            "total": len(data),
            "data": data
        })

    except Exception as e:
        print("API error:", e)

        return jsonify({
            "status": "error",
            "message": "Gagal mengambil data mahasiswa"
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if db is not None:
            db.close()



if __name__ == "__main__":
    app.run(debug=True)
