#!/usr/bin/python3
"""
app
"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv

from api.v1.views import app_views
from models import storage


app = Flask(__name__)

# CORS setup
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    teardown function
    """
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """Returns a JSON-formated status code for errors"""
    data = {
        "error": "Not found"
    }

    resp = jsonify(data)
    resp.status_code = 404

    return (resp)


if __name__ == "__main__":
    app.run(
        host=getenv("HBNB_API_HOST", "0.0.0.0"),
        port=getenv("HBNB_API_PORT", 5000))
    API_HOST = getenv("HBNB_API_HOST", "0.0.0.0")
    API_PORT = getenv("HBNB_API_PORT", 5000)
    app.run(host=API_HOST, port=API_PORT, threaded=True)
    origin/storage_get_count
