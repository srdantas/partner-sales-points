from partners import db


def create_partner(partner):
    database = db.get_mongo_database()
    return database.partners.insert_one(partner)
