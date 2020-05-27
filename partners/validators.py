import cerberus
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


def validate_partner_body(body):
    validator = cerberus.Validator(partner_schema)
    if validator.validate(body):
        return body
    else:
        raise werkzeug.exceptions.BadRequest('Invalid payload')
