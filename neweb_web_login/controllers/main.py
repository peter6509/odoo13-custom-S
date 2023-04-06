# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import odoo
from odoo import http
from odoo.http import request
import werkzeug.utils
import werkzeug.wrappers
from odoo.addons.web.controllers.main import ensure_db, abort_and_redirect

def ensure_db(redirect='/web/database/selector'):
    # This helper should be used in web client auth="none" routes
    # if those routes needs a db to work with.
    # If the heuristics does not find any database, then the users will be
    # redirected to db selector or any url specified by `redirect` argument.
    # If the db is taken out of a query parameter, it will be checked against
    # `http.db_filter()` in order to ensure it's legit and thus avoid db
    # forgering that could lead to xss attacks.

    db = request.params.get('db')

    # Ensure db is legit
    if db and db not in http.db_filter([db]):
        db = None

    if db and not request.session.db:
        # User asked a specific database on a new session.
        # That mean the nodb router has been used to find the route
        # Depending on installed module in the database, the rendering of the page
        # may depend on data injected by the database route dispatcher.
        # Thus, we redirect the user to the same page but with the session cookie set.
        # This will force using the database route dispatcher...
        r = request.httprequest
        url_redirect = r.base_url
        if r.query_string:
            # Can't use werkzeug.wrappers.BaseRequest.url with encoded hashes:
            # https://github.com/amigrave/werkzeug/commit/b4a62433f2f7678c234cdcac6247a869f90a7eb7
            url_redirect += '?' + r.query_string
        response = werkzeug.utils.redirect(url_redirect, 302)
        request.session.db = db
        abort_and_redirect(url_redirect)

    # if db not provided, use the session one
    if not db and request.session.db and http.db_filter([request.session.db]):
        db = request.session.db

    # if no database provided and no database in session, use monodb
    if not db:
        db = http.db_monodb(request.httprequest)

    # if no db can be found til here, send to the database selector
    # the database selector will redirect to database manager if needed
    if not db:
        if len(http.db_list()) > 1:
            db =http.db_list()[0]
        else:
            werkzeug.exceptions.abort(werkzeug.utils.redirect(redirect, 303))

    # always switch the session to the computed db
    if request.session.db and db != request.session.db:
        request.session.logout()
        abort_and_redirect(request.httprequest.url)

    request.session.db = db

