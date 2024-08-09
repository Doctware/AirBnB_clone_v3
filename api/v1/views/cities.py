#!/usr/bin/python3
""" this module paformes action on cities OBJ """
from flask import jsonify, abort, request
from models.city import City
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """ this method retrieves all citites obj base on the given state.id """
    state = storage.all(State).get("state." + state_id)
    if not state:
        abort(404)
    cities = [Cities.to_dict() for city in state.cities]
    jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """ this method retrieves a city base on given id """
    cities = storage.all(City)
    city = None
    for obj in cities.values():
        if obj.id == city_id:
            city = obj
            break
    if not city:
        abort(404)
    return jsonify(city)


@app_views.route('/citties/<city_id>',  methods=['GET'])
def deelete_city(city_id):
    """ this method deletes city obj base on the given id """
    cities = storage.all(City)
    city = None
    for obj in citites.values():
        if obj.id == city_id:
            city = obj
            break
    if not city:
        abort(404)
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """ this method create city obj base on given state_id """
    state = storage.all(State).get("state." + state_id)
    if not state:
        abort(404)
    if not request.json():
        abort(404, discription="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(404, discription="Missing name")
    data['state_id'] = state_id
    new_city = City(**data)
    storage.new(new_city)
    storage.save()
    jsonify(new_city.to_dict()),201

