from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "postgres")

@app.route("/")
def home():
    return "Backend Running"

@app.route("/data")
def data():
    conn = psycopg2.connect(
        host=DB_HOST,
        database="appdb",
        user="admin",
        password="admin"
    )
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({"time": str(result[0])})

app.run(host="0.0.0.0", port=5000)