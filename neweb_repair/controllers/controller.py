#-*- coding: utf-8 -*-

from odoo import http
import xmlrpclib
import logging
from datetime import datetime, timedelta
import time
import base64

_logger = logging.getLogger(__name__)


class NewebRepair(http.Controller):

	# {"params": {"sessid":"NTcxODQ5NmY6MTpuZXdlYg==", "pwd":"fddfdsfdsf!@$", "timeline":"2012-01-01", "repair_num":"", "serial_num":[]}}
	@http.route('/neweb_repair/repair/list', auth='public', type='json', methods=['POST'])
	def list(self, **post):
		if not post.get('sessid') or not post.get('pwd') or not post.get('timeline'):
			return {'error': 'Missing Required Parameters'}

		sessid, pwd, timeline = post.get('sessid'), post.get('pwd'), post.get('timeline')
		expdt, _uid, db = base64.b64decode(sessid).split(':')
		uid = int(_uid)
		now = datetime.now()
		now_x = int(time.mktime(now.timetuple()))
		if now_x > int(expdt, 16):
			return {'error': 'Session Expired'}

		url = http.request.env['ir.config_parameter'].get_param('web.base.url')

		remote_vals = {'timeline': timeline}
		if post.get('repair_num'):
			remote_vals['repair_num'] = post.get('repair_num')

		sn = post.get('serial_num')
		if sn and isinstance(sn, list) and len(sn)>0:
			remote_vals['serial_num'] = post.get('serial_num')

		objs = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
		repairs = objs.execute_kw(db, uid, pwd, 'neweb_repair.repair', 'get_repair_list', [remote_vals])

		_logger.info('repairs: %s' % repairs)

		return {'repairs': repairs}
