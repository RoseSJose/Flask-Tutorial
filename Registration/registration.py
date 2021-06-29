import os
from flask import Flask, render_template, request, redirect
import psycopg2
from flask_mail import Mail, Message

app = Flask(__name__)

'''app.config["MAIL_DEFAULT_SENDER"]=os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"]=os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"]=587 # for gmail
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USERNAME"]=os.getenv("MAIL_USERNAME")

mail = Mail(app)'''

SPORTS=[
    'Football',
    'Basketball',
    'Volleyball',
    'Cricket',
    'Tennis'
]

dbconn = psycopg2.connect(dbname = 'registration')
cursor = dbconn.cursor()
f = open('sqlcode.sql')
sqlcode = f.read()
cursor.execute(sqlcode)
cursor.close()
dbconn.commit()

@app.route("/")
def index():
    return render_template("index.html", sports = SPORTS)
    
@app.route("/register", methods=["POST"])
def register():
    dbconn = psycopg2.connect(dbname = 'registration')
    cursor = dbconn.cursor()
    name = request.form.get("email")
    if not name:
        return render_template("error.html", msg = "Missing Name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", msg = "Missing Sport")
    if sport not in SPORTS:
        return render_template("error.html", msg = "Invalid Sport")
        
    cursor.execute("INSERT INTO registrants(name , sport) VALUES (%s, %s)",(name, sport));
    cursor.close()
    dbconn.commit()
    #message = Message("You are registed", recipients=[name])
    #mail.send(message)
    return redirect("/registrants")
    
@app.route("/registrants")
def registrants():
    dbconn = psycopg2.connect(dbname = 'registration')
    cursor = dbconn.cursor()
    cursor.execute("SELECT name, sport FROM registrants")
    REGISTRANTS = cursor.fetchall()     
    cursor.close()
    dbconn.commit()
    return render_template("registrants.html", registrants=REGISTRANTS)
    
    
    
