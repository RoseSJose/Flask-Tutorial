from flask import Flask, render_template, request

app = Flask(__name__)  #turn the current file to application
@app.route("/")        #gives the route of the application
                       #@ is a python decorator
def index():
    return render_template("index.html", name=request.args.get("name"))
        #flask parses the url and retrun the name
    
