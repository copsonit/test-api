# Simple flask without blueprints.
# Use with:
# FLASK_APP=hello.py
# flask run
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
        return "<p>Hello!!</p>"
