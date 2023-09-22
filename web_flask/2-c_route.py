#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return `Hello HBNB!`"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return `HBNB`"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """Return `C` followed by <text>."""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
