#!/usr/bin/python3
"""
A python module that starts Flask web application
run using `./0-hello_route.py`
This module can be imported and used in other applications
"""

from flask import Flask

app = Flask("__name__")


@app.route("/")
@app.route("/hbnb", strict_slashes=False)
def display():
    """
    This function displays the HBNB on the screen
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
