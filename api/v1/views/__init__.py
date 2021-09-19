#!/usr/bin/python3
"""
    Import of the views of the api
"""

from flask import Blueprint

from api.v1.views.amenities import *

app_views = Blueprint("app", __name__, url_prefix="/api/v1")
