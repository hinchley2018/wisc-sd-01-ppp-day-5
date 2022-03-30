from flask import Flask

#create an app instance
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"
