from flask import Flask
import mysql.connector
import os, time

app = Flask(__name__)

@app.route('/')
def home():
    retries = 10
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host=os.getenv("DB_HOST", "db"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASS", "my-secret-pw"),
                database=os.getenv("DB_NAME", "mydatabase")
            )
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            conn.close()
            return f"✅ Connected to MySQL! Version: {version[0]}"
        except Exception as e:
            retries -= 1
            print(f"❌ DB not ready yet ({e}), retrying in 5s...")
            time.sleep(5)
    return "❌ Could not connect to MySQL after retries."
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
