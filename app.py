from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
    count = r.incr("count")
    return f"Hello Cloud Engineer! Visit count: {count}"

app.run(host="0.0.0.0", port=5000)
