#!/usr/bin/python3
"""This module performs actions on Amenity objects"""
from flask import request, jsonify, abort
from models.amenity import Amenity
from api.v1.views import app_views
from models import storage


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """Retrieves all Amenity objects"""
    amenities = storage.all(Amenity)
    return jsonify([amenity.to_dict() for amenity in amenities.values()])


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves an Amenity object based on the provided amenity_id"""
    amenity = storage.all(Amenity).get("Amenity." + amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_amenity(amenity_id):
    """Deletes an Amenity object based on the provided amenity_id"""
    amenity = storage.all(Amenity).get("Amenity." + amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """Creates a new Amenity object"""
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    new_amenity = Amenity(**data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_ameity(amenity_id):
    """ this method Updates Amenity obj base on given id """
    amenity = storage.all(Amenity).get("Amenity." + amenity_id)
    if not amenity:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_josn()
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(amenity, key, vakuei)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
