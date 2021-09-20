#!/usr/bin/python3
"""index.py to connect to API"""
import app_views from api.v1.views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.city import City


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def ret_status():
    """returns a JSON status of 200 response"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def some_stats():
    """ Retrieves the number of each objects by type """
    dict = {"amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)}
    return jsonify(dict)
