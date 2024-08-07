#!/usr/bin/python3
""" thisss module handules all default RESTful API actions for State obj """
from models.state import State
from flask import jsonify, request, abort
from api.v1.views import app_views


@app_views.route('/states/<state_id>', methods=['GET'])
def get_states():
    """ this mehods retrives list of all state obj """
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """ retrives state obj """
    state = storge.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ this method delete provided stae oobj"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'])
def create_state():
    """ this method create new state """
    if not request.json:
        abort(400, discription="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, discription="Missing name")
    new_state = State(**data)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """ update the given obj from State """
    state == storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.json():
        abort(404, discription="Not a JSON")
    data = request.get_json()
    ignore_keys = ['id', 'create_id', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
