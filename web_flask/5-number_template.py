#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask, abort, render_template


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


@app.route('/python/', strict_slashes=False)
def pythonIsCool():
    """Return `Python is cool`."""
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def pythonText(text):
    """Return `Python ` followed by the value of text."""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def isNumber(n):
    """Check if <n> is a number"""
    if not n.isdigit():
        return abort(404)
    return f"{int(n)} is a number"


@app.route('/number_template/<n>', strict_slashes=False)
def numberTemplate(n):
    """Render a template if n is a number"""
    if not n.isdigit():
        return abort(404)
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.')
