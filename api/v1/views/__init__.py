#!/usr/bin/python3
"""Script that creates the Blueprint Flask Class and import modules"""
from flask import Blueprint
from api.v1.views.index import *  # Added line to import index.py
from api.v1.views.states import *  # Added line to import states.py
from api.v1.views.amenities import *  # Added line to import amenities.py
from api.v1.views.cities import *  # Added line to import cities.py
from api.v1.views.users import *  # Added line to import users.py
from api.v1.views.places_reviews import *  # Line to import places_reviews.py
from api.v1.views.places import *  # Added line to import places.py

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
