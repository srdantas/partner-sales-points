import json

import werkzeug
from flask import request

import partners
import partners.partner
from partners import requests_validators


@partners.app.route('/partners', methods=['POST'])
def create_partner():
    data = json.loads(request.data)
    body = requests_validators.validate_partner_body(data)
    if partners.partner.create_partner(body).inserted_id:
        return {}, 201
    else:
        raise werkzeug.exceptions.InternalServerError('Error for save partner')


@partners.app.route('/partners/<id>', methods=['GET'])
def get_partner(id=None):
    return f'{id}!'


@partners.app.route('/partners', methods=['GET'])
def search_partner_by_point():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return f'{lat}:{lon}'


@partners.app.errorhandler(werkzeug.exceptions.HTTPException)
def handle_exception(e):
    return {'message': e.description}, e.code
