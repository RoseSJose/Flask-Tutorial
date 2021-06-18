from flask import Flask

app = Flask(__name__)  #turn the current file to application
@app.route("/")        #gives the route of the application
                       #@ is a python decorator
def index():
    return "Hello, World!"
    
