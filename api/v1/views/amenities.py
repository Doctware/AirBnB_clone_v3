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
