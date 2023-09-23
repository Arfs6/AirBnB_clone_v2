#!/usr/bin/python3
"""List all states in storage."""

from flask import Flask, render_template

from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closeStorageSession(*args):
    """Make sure we're using the most up-to-date data"""
    storage.close()


def sortKey(value):
    """Return the key to use for sorting State objects"""
    return value.name


@app.route('/states')
def listStates():
    """Return a list of states"""
    from models.state import State
    states = storage.all(State).values()
    # Order the State objects
    states = list(states)
    states.sort(key=sortKey)
    return render_template('9-states.html', obj=states)


@app.route('/states/<id>')
def displayState(id):
    """Display a State object."""
    from models.state import State
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            state.cities.sort(key=sortKey)
            return render_template('9-states.html', obj=state)
    return render_template('9-states.html', obj=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
