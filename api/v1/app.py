#!/usr/bin/python3
"""Import the Flask class from the flask module"""
from flask import Flask
"""Import the os module for operating 
    system functionality"""
import os
"""Import the storage object from the models module"""
from models import storage
"""Import the app_views blueprint 
    from the api.v1.views module"""
from api.v1.views import app_views

"""Create a Flask application instance 
    with the name of the current module"""
app = Flask(__name__)
"""Register a function to be called 
    when the application context is destroyed"""


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Define the teardown_appcontext 
        function with an exception parameter
        and Call the close method of the 
        storage object to clean up resources 
        when the application context is destroyed
    """
    storage.close()


if __name__ == '__main__':
    """Get the value of the HBNB_API_HOST 
        environment variable, defaulting 
        to '0.0.0.0' if not set"""
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    """Get the value of the HBNB_API_PORT 
        environment variable, defaulting 
        to 5000 if not set"""
    port = int(os.getenv('HBNB_API_PORT', 5000))
    """Run the app with the specified host and port
        and enable threading
    """
    app.run(host=host, port=port, threaded=True)
