from flask import Flask, render_template, request

app = Flask(__name__)  #turn the current file to application
@app.route("/")        #gives the route of the application
                       #@ is a python decorator
def index():
    return render_template("index.html")
        #flask parses the url(?name=David) and return the name
        #2nd argument to get is the default argument

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name","world"))
