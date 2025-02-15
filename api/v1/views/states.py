#!/usr/bin/python3
"""Flask application for state class/entity"""
from app.v1.views import app_veiws
from models import storage
from models.state import State
from flask import jsonify, abort, request


@app_veiws.route("/states", methods=["GET"], strict_slashes=False)
def retrieves_all():
    """Return the list of all state objects"""
    states = storage.all(State).values()
    states_list = []
    for state in states:
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_veiws.route('/states/<state_id>', methods=["GET"], strict_slashes=False)
def get_state(state_id):
    """Return object by its id"""
    state = storage.all(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_veiws.route('/states/<state_id>', methods=["DELETE"],
                 strict_slashes=False)
def delete_state(state_id):
    """Delete an object by its id"""
    state = storage.all(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_veiws.route('/states', methods=["POST"], strict_slashes=False)
def create_state():
    """Create a new object"""
    state_data = request.get_json()
    if not state_data:
        abort(400, "Not a JSON")
    elif "name" not in state_data:
        abort(400, "Missing name")
    new_state = State(**state_data)
    new_state.save()
    return jsonify(new_state.to_dict())


@app_veiws.route('/states/<state_id>', methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """Updates an object"""
    state_data = request.get_json()
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    elif not state_data:
        abort(400, "Not a JSON")

    for key, value in state_data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
