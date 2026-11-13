
from db import get_db_connection
from werkzeug.security import generate_password_hash

db = get_db_connection()
cursor = db.cursor(dictionary=True)

cursor.execute("SELECT id, password FROM users")
users = cursor.fetchall()

for user in users:
    hashed_password = generate_password_hash(user["password"])

    cursor.execute(
        "UPDATE users SET password = %s WHERE id = %s",
        (hashed_password, user["id"])
    )

db.commit()

cursor.close()
db.close()

print("Password berhasil di-hash!")
