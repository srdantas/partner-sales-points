import json

import cerberus
import werkzeug
from flask import request

import partners
from partners import requests_schemas


@partners.app.route('/partners', methods=['POST'])
def create_partner():
    body = json.loads(request.data)
    validator = cerberus.Validator(requests_schemas.partner_schema)
    if validator.validate(body):
        return body
    else:
        raise werkzeug.exceptions.BadRequest('Invalid payload')


@partners.app.route('/partners/<id>', methods=['GET'])
def get_partner(id=None):
    return f'{id}!'


@partners.app.route('/partners', methods=['GET'])
def search_partner_by_point():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return f'{lat}:{lon}'
