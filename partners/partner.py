import partners.database


def create_partner(partner):
    partners.database.insert(partner)


def get_partner(partner_id):
    return partners.database.get_by_id(partner_id)


def search_partner(lat, lon):
    return partners.database.search_coverage(lat, lon)
