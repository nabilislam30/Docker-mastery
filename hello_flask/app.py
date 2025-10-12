import mysql.connector
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),  # ✅ Use 'db', not 'localhost'
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASS", "my-secret-pw"),
            database=os.getenv("DB_NAME", "mydatabase")
        )

        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        connection.close()

        return f"Connected to MySQL! 🎯 Version: {version[0]}"
    except Exception as e:
        return f"❌ Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)