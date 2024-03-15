#!/usr/bin/python3
"""Import the app_views blueprint 
    from the api.v1.views module"""
from api.v1.views import app_views
"""Import the jsonify function 
    from flask module
"""
from flask import jsonify
"""Define a route for the 
    app_views blueprint at the 
    endpoint '/status'
"""


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
