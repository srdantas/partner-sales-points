import pymongo.errors

import database.connection
import database.mapper


def insert_partner(partner):
    partner_document = database.mapper.partner_to_document(partner)
    try:
        database.connection.get_collection().insert_one(partner_document)
    except pymongo.errors.DuplicateKeyError:
        raise ValueError('Id or document already exists in database')


def get_partner_by_id(partner_id):
    partner = database.connection.get_collection().find_one({'_id': partner_id})
    return database.mapper.partner_from_document(partner) if partner else None


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
    results = database.connection.get_collection().aggregate(pipeline)
    return list(map(database.mapper.partner_from_document, results))
