from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/login", methods=["GET","POST"])
def login():
    # Remember that user logged in
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")
    
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")
