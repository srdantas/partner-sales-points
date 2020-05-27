import werkzeug

import partners
import partners.partner
from partners import request_validators


@partners.app.route('/partners', methods=['POST'])
def create_partner():
    body = request_validators.validate_partner_body()
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
    lat, lon = request_validators.validate_search_query_string()
    results = partners.partner.search_partner(lat, lon)
    return {'results': results, 'size': len(results)}, 200


@partners.app.errorhandler(werkzeug.exceptions.HTTPException)
def handle_exception(e):
    return {'message': e.description}, e.code


@partners.app.errorhandler(Exception)
def handle_exception(e):
    return {'message': str(e)}, 500
