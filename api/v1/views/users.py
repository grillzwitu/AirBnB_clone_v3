#!/usr/bin/python3
"""
    View for User objects
"""

from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def retrieve_user():
    """
        Retrieve User objects
    """
    users = storage.all("User").values()

    a_list = []
    for user in users:
        a_list.append(user.to_dict())
    return jsonify(a_list)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def retrieve_user(user_id):
    """
        Retrieve User object
    """
    user = storage.get(User, user_id)

    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """
        Delete User object
    """
    user = storage.get(User, user_id)

    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({})


@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
def add_user():
    """
        Create User object
    """
    if request.is_json:
        req = request.get_json()
        if 'email' not in req:
            return make_response(jsonify({'error': 'Missing email'}), 400)
        if 'password' not in req:
            return make_response(jsonify({'error': 'Missing password'}), 400)
        user = User(**req)
        user.save()
        return make_response(jsonify(user.to_dict()), 201)
    else:
        return make_response(jsonify({'error': 'Not a JSON'}) 400)


@app_views.route('/user/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def update_user(user_id):
    """
        Update User object
    """
    user = storage.get(User, user_id)

    if user is None:
        abort(404)
    if request.is_json:
        req = request.get_json().items()
        for key, val in req:
            if key not in ['id', 'created_at', 'updated_at', 'email']:
                setattr(user, key, val)
        user.save()
        return jsonify(user.to_dict())
    else:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
