from flask import request

from partners import app


@app.route('/partners', methods=['POST'])
def create_partner():
    return 'Hello World!'


@app.route('/partners/<id>', methods=['GET'])
def get_partner(id=None):
    return f'{id}!'


@app.route('/partners', methods=['GET'])
def search_partner_by_point():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return f'{lat}:{lon}'

