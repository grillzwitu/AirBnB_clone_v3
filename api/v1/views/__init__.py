#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint

# creates a variable app_views which is
# an instance of Blueprint (url prefix must be /api/v1)
app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

import * from api.v1.views.index
import * from api.v1.views.states
import * from api.v1.views.cities
from api.v1.views.amenities import *
