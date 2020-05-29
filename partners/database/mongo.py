import flask
import pymongo
import pymongo.errors

import partners.database.mapper


def init_client():
    client = pymongo.MongoClient('localhost', 27017)
    sales_points_database = client['sales-points']
    partners_collection = sales_points_database.partners

    partners_collection.create_index([("document", pymongo.ASCENDING)], unique=True)
    partners_collection.create_index([("address", pymongo.GEOSPHERE)])
    partners_collection.create_index([("coverageArea", pymongo.GEOSPHERE)])

    flask.g.collection = partners_collection


def get_collection():
    if 'collection' not in flask.g:
        init_client()
    return flask.g.collection


def insert_partner(partner):
    partner_document = partners.database.mapper.partner_to_document(partner)
    try:
        get_collection().insert_one(partner_document)
    except pymongo.errors.DuplicateKeyError:
        raise ValueError('Id or document already exists in database')


def get_partner_by_id(partner_id):
    partner = get_collection().find_one({'_id': partner_id})
    return partners.database.mapper.partner_from_document(partner) if partner else None


def search_partner_coverage(lat, lon):
    pipeline = [
        {
            '$geoNear': {
                'near': {'type': 'Point', 'coordinates': [lat, lon]},
                'key': 'address',
                'distanceField': 'dist.calculated',
                'query': {
                    'coverageArea': {'$geoIntersects': {'$geometry': {'type': 'Point', 'coordinates': [lat, lon]}}}}
            }
        },
        {'$sort': {'dist.calculated': 1}}
    ]
    results = get_collection().aggregate(pipeline)
    return list(map(partners.database.mapper.partner_from_document, results))
