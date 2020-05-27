import partners.database


def create_partner(partner):
    return partners.database.insert(partner)


def find_partner(partner_id):
    return partners.database.get(partner_id)


def search_partner(lat, lon):
    return partners.database.search_coverage(lat, lon)
