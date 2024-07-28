#!/usr/bin/python3
"""
A script that starts a Flask web application
"""


from flask import Flask, render_template
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


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>")
def pythonPage(text='is cool'):
    """
    print pythonPage
    """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>")
def numberPage(n):
    """
    print number page
    """
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """print number template page"""
    return render_template('5-number.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
