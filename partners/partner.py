from partners import db
from partners import mapper


def create_partner(partner):
    database = db.get_mongo_database()
    partner_document = mapper.partner_to_document(partner)
    return database.partners.insert_one(partner_document)


def find_partner(partner_id):
    database = db.get_mongo_database()
    partner = database.partners.find_one({'_id': partner_id})
    if partner:
        return mapper.partner_from_document(partner)
    else:
        return None


def search_partner(lat, lon):
    database = db.get_mongo_database()
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
    results = database.partners.aggregate(pipeline)
    return list(map(mapper.partner_from_document, results))
