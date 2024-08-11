#!/usr/bin/python3
""" this module paform RESTfull action on places """
from models.city import City
from models.place import Place
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/cities/<city_id>/places', methods=['GET'])
def get_places(city_id):
    """ this method retrieves places base on city id given """
    city = storage.all(City).get("city." + city_id)
    if not city:
        abort(404)
    places = [places.to_dict() for place in city.places]
    return jsonify(places.to_dict())
