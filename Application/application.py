from flask import Flask, render_template, request

app = Flask(__name__)  #turn the current file to application

#gives the route of the application
#@ is a python decorator
#default is GET

@app.route("/", methods = ["GET", "POST"] )                         
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name","world"))
        #flask parses the url(?name=David) and return the name
        #2nd argument to get is the default argument

    
    #request.args.get to parse url when method="GET"
    #request.form.get to parse url when method="POST"
