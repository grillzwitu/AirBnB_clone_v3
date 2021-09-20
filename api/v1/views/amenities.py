#!/usr/bin/python3
"""
    View for Amenity objects
"""

from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def retrieve_amenities():
    """
        Retrieve Amenity objects
    """
    amenities = storage.all("Amenity").values()

    a_list = []
    for amenity in amenities:
        a_list.append(amenity.to_dict())
    return jsonify(a_list)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def retrieve_amenity(amenity_id):
    """
        Retrieve Amenity object
    """
    amenity = storage.get(Amenity, amenity_id)

    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """
        Delete Amenity object
    """
    amenity = storage.get(Amenity, amenity_id)

    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def add_amenity():
    """
        Create Amenity object
    """
    if request.is_json:
        req = request.get_json()
        if 'name' in req:
            amenity = Amenity(**req)
            amenity.save()
            return make_response(jsonify(amenity.to_dict()), 201)
        else:
            return make_response(jsonify({'error': 'Missing name'}), 400)
    else:
        return make_response(jsonify({'error': 'Not a JSON'}) 400)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """
        Update Amenity object
    """
    amenity = storage.get(Amenity, amenity_id)

    if amenity is None:
        abort(404)
    if request.is_json:
        req = request.get_json().items()
        for key, val in req:
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(amenity, key, val)
        amenity.save()
    else:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
