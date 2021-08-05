from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Did I mention how much I'm hating Flask?</p>"