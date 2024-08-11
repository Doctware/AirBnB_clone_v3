#!/usr/bin/python3
""" this module parfomes RESTfull action on USERS """
from flask import request, abort, jsonify
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'])
def get_users():
    """ this methods get all users obj """
    users = storage.all(User)
    return jsonify([users.to_dict() for user in users.values()])


@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """ this method is use to get user obj base on given id """
    user = storage.all(User).get("user." + user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """ this method delete user obj base on given id """
    user = storage.all(User).get("user." + user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({})


@app_views.route('/users', methods=['POST'])
def create_user():
    """ this methos is use to create user object """
    if not request.is_json():
        abort(400, discription="Not a JSON")
    data = request.get_json()
    if 'name' not in data.items():
        abort(400, discription="Missing name")
    if 'email' not in data.items():
        abort(400, discription="Missing email")
    if 'password' not in data.items():
        abort(400, discription="Missing password")
    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """ update user object base in given id """
    user = storage.all(User).get("user." + user_id)
    if not user:
        abort(404)
    if not request.json():
        abort(400, discription="Not a JSON")
    data = request.get_json()
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
