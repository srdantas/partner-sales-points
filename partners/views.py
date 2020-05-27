import json

import werkzeug
from flask import request

import partners
import partners.partner
from partners import validators


@partners.app.route('/partners', methods=['POST'])
def create_partner():
    data = json.loads(request.data)
    body = validators.validate_partner_body(data)
    if partners.partner.create_partner(body).inserted_id:
        return '', 201
    else:
        raise werkzeug.exceptions.InternalServerError('Error for save partner')


@partners.app.route('/partners/<partner_id>', methods=['GET'])
def get_partner(partner_id=None):
    partner = partners.partner.find_partner(partner_id)
    if partner:
        return partner, 200
    else:
        raise werkzeug.exceptions.NotFound(f'partner {partner_id} not found')


@partners.app.route('/partners', methods=['GET'])
def search_partner_by_point():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    results = partners.partner.search_partner(float(lat), float(lon))
    return {'results': results, 'size': len(results)}, 200


@partners.app.errorhandler(werkzeug.exceptions.HTTPException)
def handle_exception(e):
    return {'message': e.description}, e.code


@partners.app.errorhandler(Exception)
def handle_exception(e):
    print(e)
    return {'message': 'Sorry, you can retry in a feel minutes'}, 500
