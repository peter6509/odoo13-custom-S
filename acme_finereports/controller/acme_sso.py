# -*- coding: utf-8 -*-
# Author : Peter Wu

import json
from odoo import http
from odoo.http import request, Response

class NewPage(http.Controller):
	@http.route(['/acme-finereports/'],type="http",auth='public', website=True)
	def index(self,**post):
		return http.request.render('localhost:8075/webroot/decision/view/report?viewlet=')
