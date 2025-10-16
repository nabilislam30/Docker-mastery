from flask import Flask, render_template
import redis, os, random

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0
)

quotes = [
    "Innovation starts with curiosity.",
    "Keep it simple, make it reliable.",
    "Every refresh is a new beginning.",
    "Docker today, architect tomorrow.",
    "Build. Break. Learn. Repeat."
]

@app.route("/")
def index():
    try:
        count = r.get("count")
        if count is None:
            count = 0
        count = int(count) + 1
        r.set("count", count)
        quote = random.choice(quotes)
        return render_template("index.html", count=count, quote=quote)
    except redis.exceptions.ConnectionError:
        return "<h2>Redis connection failed 💥</h2>", 500

@app.route("/health")
def health():
    try:
        r.ping()
        return {"status": "UP"}, 200
    except redis.exceptions.ConnectionError:
        return {"status": "DOWN"}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)