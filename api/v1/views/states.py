#!/usr/bin/python3
""" thisss module handules all default RESTful API actions for State obj """
from models.state import State
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """ this mehods retrives list of all state obj """
    states = storage.all(State).values()
    return jsonify({"states": [state.to_dict() for state in states]})


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ retrives state obj base on provided id """
    states = storage.all(State)
    state = None
    for obj in states.values():
        if obj.id == state_id:
            state = obj
            break
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ this method delete obj base on provided id"""
    states = storage.all(State)
    state = None
    for obj in states.values():
        if obj.id == state_id:
            state = obj
            break
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
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


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ update the given obj from State """
    states = storage.all(State)
    state = None
    for obj in states.values():
        if obj.id == state_id:
            state = obj
            break
    if not state:
        abort(404)
    if not request.get_json():
        abort(404, discription="Not a JSON")
    data = request.get_json()
    ignore_keys = ['id', 'create_id', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
