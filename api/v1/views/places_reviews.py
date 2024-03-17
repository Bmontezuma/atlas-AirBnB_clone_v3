#!/usr/bin/python3
"""
Module for Review objects that handles RESTful API actions.
"""

from flask import jsonify, abort, request
from models import storage
from models.review import Review
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'])
def get_post_reviews(place_id):
    """Handles GET and POST requests for Review objects."""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)

    if request.method == 'GET':
        reviews = [review.to_dict() for review in place.reviews]
        return jsonify(reviews)

    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        if "user_id" not in data:
            abort(400, "Missing user_id")
        if "text" not in data:
            abort(400, "Missing text")
        user_id = data["user_id"]
        user = storage.get("User", user_id)
        if user is None:
            abort(404)
        data['place_id'] = place_id
        review = Review(**data)
        review.save()
        return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'])
def get_put_delete_review(review_id):
    """Handles GET, PUT, and DELETE requests for a Review object."""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(review.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")
        for key, value in data.items():
            if key not in ['id', 'user_id', 'place_id',
                           'created_at', 'updated_at']:
                setattr(review, key, value)
        review.save()
        return jsonify(review.to_dict()), 200

    if request.method == 'DELETE':
        review.delete()
        storage.save()
        return jsonify({}), 200
