#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def rootPage():
	return "Hello HBNB!"


@app.route("/hbnb")
def hbnbPage():
	return "HBNB"

@app.route("/c/<text>")
def nextPage(text):
	return f"C {escape(text)}"


if __name__ == "__main__":
	app.run(host="0.0.0.0")
