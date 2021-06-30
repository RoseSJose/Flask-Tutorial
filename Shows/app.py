from flask import Flask, render_template, request, jsonify
import crawler
import psycopg2

app = Flask(__name__)
dbconn = psycopg2.connect(dbname="show")

@app.route("/")
def index():
    crawler.create_table()
    crawler.insert()
    return render_template("index.html")

@app.route("/search")
def search():
    cursor = dbconn.cursor()
    cursor.execute("SELECT title FROM shows WHERE title LIKE %s", ("%" + request.args.get("q") + "%",))
    shows = cursor.fetchall()
    return render_template("search.html", shows=shows)