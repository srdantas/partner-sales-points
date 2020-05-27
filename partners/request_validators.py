import json

import cerberus
import werkzeug
from flask import request

geo_json_schema = {'type': {'type': 'string', 'required': True}, 'coordinates': {'type': 'list', 'required': True}}

partner_schema = {
    'id': {'type': 'string', 'required': True},
    'tradingName': {'type': 'string', 'required': True},
    'ownerName': {'type': 'string', 'required': True},
    'document': {'type': 'string', 'required': True},
    'coverageArea': {'type': 'dict', 'required': True, 'schema': geo_json_schema},
    'address': {'type': 'dict', 'required': True, 'schema': geo_json_schema}
}


def validate_partner_body():
    body = json.loads(request.data)
    validator = cerberus.Validator(partner_schema)
    if validator.validate(body):
        return body
    else:
        raise werkzeug.exceptions.BadRequest('Invalid payload')


def validate_search_query_string():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not lat or not lon:
        raise werkzeug.exceptions.BadRequest('Invalid request, we need lat and lon params')
    else:
        try:
            return float(lat), float(lon)
        except Exception:
            raise werkzeug.exceptions.BadRequest('Invalid request, we need lat and lon params are float values')
