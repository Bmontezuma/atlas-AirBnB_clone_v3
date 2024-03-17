#!/usr/bin/python3
"""Module for City API views"""

from flask import jsonify, abort, request
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """Retrieves the list of all City objects of a State"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object"""
    city = storage.get(City, city_id)
    if city is None:

"""Flask application for City class"""
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State
from flask import jsonify, abort, request


@app_views.route('/states/<state_id>/cities',
                 methods=["GET"], strict_slashes=False)
def retrieve_all_cities(state_id):
    """Return the list of all City objects"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    cities = state.cities
    cities_list = []
    for city in cities:
        cities_list.append(city.to_dict())
    return jsonify(cities_list)


@app_views.route('/cities/<city_id>', methods=["GET"], strict_slashes=False)
def get_city(city_id):
    """Return object by id"""
    city = storage.get(City, city_id)
    if not city:
     origin/storage_get_count
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """Creates a City"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    data = request.get_json()
    data['state_id'] = state_id
    city = City(**data)
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    city.save()

@app_views.route('/cities/<city_id>', methods=["DELETE"], strict_slashes=False)
def delete_city(city_id):
    """Delete object by id"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify[{}], 200


@app_views.route('/states/<state_id>/cities',
                 methods=["POST"], strict_slashes=False)
def create_city(state_id):
    """Create an object"""

    city_data = request.get_json()
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    elif not city_data:
        abort(404, "Not a JSON")
    elif "name" not in city_data:
        abort(404, "Missing name")

    city_data["state_id"] = state_id
    new_city = City(**city_data)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/citie/<city_id>', methods=["PUT"], strict_slashes=False)
def update_city(city_id):
    """Update object by id"""
    city_data = request.get_json()
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    elif not city_data:
        abort(400, "Not a JSON")

    for key, value in city_data.items():
        if key not in ["id", "state_id", "created_at", "updated_at"]:
            setattr(city, key, value)
    storage.save()
     origin/storage_get_count
    return jsonify(city.to_dict()), 200
