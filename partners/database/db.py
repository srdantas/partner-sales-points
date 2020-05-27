import pymongo
from flask import g

from partners.database import mapper


def init_client():
    client = pymongo.MongoClient('localhost', 27017)
    sales_points_database = client['sales-points']

    sales_points_database.partners.create_index([("document", pymongo.ASCENDING)], unique=True)
    sales_points_database.partners.create_index([("address", pymongo.GEOSPHERE)])
    sales_points_database.partners.create_index([("coverageArea", pymongo.GEOSPHERE)])

    g.database = sales_points_database


def get_mongo_database():
    if 'database' not in g:
        init_client()
    return g.database


def get_partners_collections():
    return get_mongo_database().partners


def insert_partner(partner):
    partner_document = mapper.partner_to_document(partner)
    return get_partners_collections().insert_one(partner_document)


def get_partner(partner_id):
    partner = get_partners_collections().find_one({'_id': partner_id})
    if partner:
        return mapper.partner_from_document(partner)
    else:
        return None


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
    results = get_partners_collections().aggregate(pipeline)
    return list(map(mapper.partner_from_document, results))
