import pymongo
from flask import g
from flask.cli import with_appcontext


def get_mongo_database():
    if 'database' not in g:
        init_client()
    return g.database


def init_client():
    client = pymongo.MongoClient('localhost', 27017)
    sales_points_database = client['sales-points']

    sales_points_database.partners.create_index([("document", pymongo.ASCENDING)], unique=True)
    sales_points_database.partners.create_index([("address", pymongo.GEOSPHERE)])
    sales_points_database.partners.create_index([("coverageArea", pymongo.GEOSPHERE)])

    g.database = sales_points_database


@with_appcontext
def init_mongo_connection():
    init_client()
