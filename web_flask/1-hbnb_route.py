#!/usr/bin/python3
"""
A script that helps to start a Flask web application
"""


from flask import Flask

app = Flask(__name__)


@app.route("/")
def root_display():
    return "Hello HBNB!"


@app.route("/hbnb")
def display():
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
