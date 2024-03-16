#!/usr/bin/python3
"""Module implementing API endpoint for 
retrieving statistics on object 
types using count() method from storage."""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def app_views():
    """Define a function named 
        app_views that handles 
        requests to the '/status' 
        endpoint
        And Return a JSON response 
        with the status "OK"
    """
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """Retrieve counts of each object type using 
    the count() method from storage."""
    counts = {
        'users': storage.count('User'),
        'post': storage.count('Post'),
        'comments': storage.count('Comment')
    }
    return jsonify(counts)
