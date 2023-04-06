# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)

import json
import logging
import odoo
import werkzeug
import requests
from odoo.addons.web.controllers.main import db_monodb, ensure_db, set_cookie_and_redirect, login_and_redirect
import odoo.addons.web.controllers.main as main
from odoo import http, registry
from odoo.http import request

_logger = logging.getLogger(__name__)


class LineNotifyRoute(http.Controller):
    @http.route('/lineaccount', type='http', methods=['GET'], auth="none", csrf=False)
    def line_access_token(self, **kw):
        request.params['login_success'] = False
        if not request.uid:
            request.uid = odoo.SUPERUSER_ID

        code = request.params['code']
        state = request.params['state']
        line_configure = request.env['line.notify.configure'].search([('active', '=', True), ('test_mode', '=', False)])
        employee_id = request.env['hr.employee'].search([('state_code', '=', state)])

        token_url = 'https://notify-bot.line.me/oauth/token?'
        URL = token_url + 'grant_type=authorization_code' + '&redirect_uri=' + line_configure.redirect_url + '&client_id=' + line_configure.client_id + '&client_secret=' + line_configure.client_secret + '&code=' + code
        token_check = requests.post(URL)
        if token_check.status_code == 200:
            token_code = json.loads(token_check.text)['access_token']
            print(token_code)
            employee_id.write({'line_access_token': token_code})
        return werkzeug.utils.redirect('/web/login')
