#!/usr/bin/python3
""" this module paform actions om amenities obj """
from flask import request, jsonify, abort
from models.amenity import Amenity
from api.v1.views import app_views
from models import storage


@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    """ this method retrieves all amenities object """
    amenities = storage.all(Amenity)
    return jsonify([amenity.to_dict()for amenity in amenities.values()])


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """ this method retrieves amenities obj base on amenity id provided """
    amenities = storage.all(Amenity).get("amenity." + amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def del_amenity(amenity_id):
    """ this method delete Amenity obj base on given id """
    amenities = storage.all(Amenity).get("amenity." + amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', metthods=['POST'])
def create_amenity():
    """ this method create obj on Amenity """
    if not request.is_json:
        abort(400, discriptoin="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, discription="Missing name")
    new_amenity = Amenity(**data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict())
