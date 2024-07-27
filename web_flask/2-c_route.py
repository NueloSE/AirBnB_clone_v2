#!/usr/bin/python3
"""
A script that starts a Flask web application
"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def rootPage():
    """
    Prints root page
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnbPage():
    """
    prints hbnbpage
    """
    return "HBNB"


@app.route("/c/<text>")
def nextPage(text):
    """
    print a custom page from url
    """
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
