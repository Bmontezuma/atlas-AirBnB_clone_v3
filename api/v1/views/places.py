#!/usr/bin/python3
"""
Module for Place objects that handles RESTFul API actions.
"""

from flask import jsonify, abort, request
from models import storage
from models.place import Place
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'])
def places(city_id):
    """Handles HTTP requests for Place objects."""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)

    if request.method == 'GET':
        places = [place.to_dict() for place in city.places]
        return jsonify(places)

    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        if "user_id" not in data:
            abort(400, "Missing user_id")
        user_id = data["user_id"]
        if storage.get("User", user_id) is None:
            abort(404)
        if "name" not in data:
            abort(400, "Missing name")
        place = Place(**data)
        place.city_id = city_id
        place.save()
        return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'])
def place(place_id):
    """Handles HTTP requests for a specific Place object."""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(place.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        for key, value in data.items():
            if key not in ['id', 'user_id', 'city_id',
                           'created_at', 'updated_at']:
                setattr(place, key, value)
        place.save()
        return jsonify(place.to_dict())

    if request.method == 'DELETE':
        place.delete()
        storage.save()
        return jsonify({}), 200
