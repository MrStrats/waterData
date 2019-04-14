import os
from flask import Flask, request
from flask_restful import Resource, Api
import pymongo
import flask_rest_service
import flask_restful

"""
from flask.ext import restful
from flask.ext.pymongo import PyMongo

from flask import make_response
from bson.json_util import dumps
"""
MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/rest"

app = Flask(__name__)

app.config['MONGO_URI'] = MONGO_URL
mongo = pymongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import flask_rest_service.resources