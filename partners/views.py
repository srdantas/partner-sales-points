import werkzeug

import partners
import partners.partner
from partners import requests


@partners.app.route('/partners', methods=['POST'])
def create_partner():
    body = partners.requests.partner_body()
    partners.partner.create_partner(body)
    return '', 201


@partners.app.route('/partners/<partner_id>', methods=['GET'])
def get_partner(partner_id=None):
    return partners.partner.get_partner(partner_id), 200


@partners.app.route('/partners', methods=['GET'])
def search_partner_by_point():
    lat, lon = partners.requests.search_query_string()
    results = partners.partner.search_partner(lat, lon)
    return {'results': results, 'size': len(results)}, 200


@partners.app.errorhandler(werkzeug.exceptions.HTTPException)
def handle_http_exception(e):
    return {'message': e.description}, e.code


@partners.app.errorhandler(Exception)
def handle_exception(e):
    return {'message': str(e)}, 500
