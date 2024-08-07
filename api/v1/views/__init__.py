#!/usr/bin/python3
""" creating blue print for easy routing """
from flask import Blueprint
from api.v1.views.index import *
from api.vi.views.state import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
