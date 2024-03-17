#!/usr/bin/python3
"""
Amenities view module.

This module defines routes for managing Amenity objects in the API.
"""

from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage, Amenity


@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    """Retrieves the list of all Amenity objects"""
    amenities = [amenity.to_dict() for amenity in storage.all(Amenity).values()]
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """Retrieves a specific Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        return jsonify(amenity.to_dict())
    else:
        abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Deletes a specific Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    """Creates a new Amenity object"""
    if not request.json:
        abort(400, "Not a JSON")
    if 'name' not in request.json:
        abort(400, "Missing name")
    amenity = Amenity(**request.json)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """Updates a specific Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    for key, value in request.json.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict())
"""Flask application for Amenity class"""
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import jsonify, abort, request


@app_views.route('/amenities', methods=["GET"], strict_slashes=False)
def retrieves_all_amenities():
    """Return the list of all Amenity object"""
    amenities = storage.all(Amenity).values()
    amenities_list = []
    for amenity in amenities:
        amenities_list.append(amenity.to_dict())
    return jsonify(amenities_list)


@app_views.route('/amenities/<amenity_id>',
                 methods=["GET"], strict_slashes=False)
def get_amenities(amenity_id):
    """Return an object by id"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=["DELETE"],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """Delete an object by id"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify[{}], 200


@app_views.route('/amenities', methods=["POST"], strict_slashes=False)
def create_amenity():
    """Create a new object"""
    amenity_data = request.get_json()
    if not amenity_data:
        abort(400, "Not a JSON")
    elif "name" not in amenity_data:
        abort(400, "Missing name")
    new_amenity = Amenity(**amenity_data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                 methods=["PUT"], strict_slashes=False)
def update_amenity(amenity_id):
    """Update an amenity"""
    amenity_data = request.get_json()
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    elif not amenity_data:
        abort(400, "Not a JSON")

    for key, value in amenity_data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
    origin/storage_get_count
