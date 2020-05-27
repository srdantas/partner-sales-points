def partner_to_document(partner):
    partner['_id'] = partner['id']
    del partner['id']
    return partner


def partner_from_document(partner):
    partner['id'] = partner['_id']
    del partner['_id']
    return partner
