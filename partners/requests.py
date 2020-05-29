import json

import cerberus
import flask
import werkzeug

geo_json_schema = {'type': {'type': 'string', 'required': True}, 'coordinates': {'type': 'list', 'required': True}}

partner_schema = {
    'id': {'type': 'string', 'required': True},
    'tradingName': {'type': 'string', 'required': True},
    'ownerName': {'type': 'string', 'required': True},
    'document': {'type': 'string', 'required': True},
    'coverageArea': {'type': 'dict', 'required': True, 'schema': geo_json_schema},
    'address': {'type': 'dict', 'required': True, 'schema': geo_json_schema}
}


def partner_body():
    body = json.loads(flask.request.data)
    validator = cerberus.Validator(partner_schema)
    if validator.validate(body):
        return body
    else:
        raise werkzeug.exceptions.BadRequest('Invalid payload')


def search_query_string():
    lat = flask.request.args.get('lat')
    lon = flask.request.args.get('lon')
    if not lat or not lon:
        raise werkzeug.exceptions.BadRequest('Invalid request, we need lat and lon params')
    else:
        try:
            return float(lat), float(lon)
        except Exception:
            raise werkzeug.exceptions.BadRequest('Invalid request, we need lat and lon params are float values')
