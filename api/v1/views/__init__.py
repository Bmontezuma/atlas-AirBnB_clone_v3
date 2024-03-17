#!/usr/bin/python3
"""import Blueprint function from flask module"""
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint(url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.amenities import *
from api.v1.views.cities import  # Add this line to import cities.py
from api.v1.views.users import *
from api.v1.views.places_reviews import *
from api.v1.views.places import *
