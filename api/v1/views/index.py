#!/usr/bin/python3
""" the module index"""
from api.v1.views import app_view 
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def get_status():
    """ this method get the response status """
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=['GET'])
def stats():
    """this end point retrieves each number of oobject by type """
    stats = {
            storage.count(Amenity),
            storage.count(City),
            storage.count(Place),
            storrage.counnt(Review),
            storage.count(State),
            storage.count(User)
    }
    return jsonify(stats)
