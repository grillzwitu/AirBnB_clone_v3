#!/usr/bin/python3
"""
    View for Place objects
"""

from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models import storage
from models.places import Place


@app_views.route('/places', methods=['GET'], strict_slashes=False)
def retrieve_places():
    """
        Retrieve Place objects
    """
    places = storage.all("Place").values()

    a_list = []
    for places in places:
        a_list.append(places.to_dict())
    return jsonify(a_list)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def retrieve_places(place_id):
    """
        Retrieve Place object
    """
    place = storage.get(Place, place_id)

    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_places(place_id):
    """
        Delete Place object
    """
    place = storage.get(Place, place_id)

    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return jsonify({})


@app_views.route('/places', methods=['POST'],
                 strict_slashes=False)
def add_places():
    """
        Create Place object
    """
    if request.is_json:
        req = request.get_json()
        if 'email' not in req:
            return make_response(jsonify({'error': 'Missing email'}), 400)
        if 'password' not in req:
            return make_response(jsonify({'error': 'Missing password'}), 400)
        place = Place(**req)
        place.save()
        return make_response(jsonify(place.to_dict()), 201)
    else:
        return make_response(jsonify({'error': 'Not a JSON'}) 400)


@app_views.route('/places/<place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_places(place_id):
    """
        Update Place object
    """
    place = storage.get(Place, place_id)

    if place is None:
        abort(404)
    if request.is_json:
        req = request.get_json().items()
        for key, val in req:
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(place, key, val)
        place.save()
    else:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
