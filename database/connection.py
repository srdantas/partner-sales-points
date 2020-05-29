import flask
import pymongo


def __init_client():
    client = pymongo.MongoClient('localhost', 27017)
    sales_points_database = client['sales-points']
    partners_collection = sales_points_database.partners

    partners_collection.create_index([("document", pymongo.ASCENDING)], unique=True)
    partners_collection.create_index([("address", pymongo.GEOSPHERE)])
    partners_collection.create_index([("coverageArea", pymongo.GEOSPHERE)])

    flask.g.collection = partners_collection


def get_collection():
    if 'collection' not in flask.g:
        __init_client()
    return flask.g.collection
