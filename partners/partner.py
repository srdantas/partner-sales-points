import database


def create_partner(partner):
    database.insert(partner)


def get_partner(partner_id):
    return database.get_by_id(partner_id)


def search_partner(lat, lon):
    return database.search_coverage(lat, lon)
