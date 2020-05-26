import werkzeug

import partners


@partners.app.errorhandler(werkzeug.exceptions.HTTPException)
def handle_exception(e):
    return {'message': e.description}, e.code
