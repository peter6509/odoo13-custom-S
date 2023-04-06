# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _


class SLA(models.Model):
	_name = 'neweb_base.sla'
	_description = "SLA"
	_sql_constraints = [('name_uniq', 'unique(name)', 'SLA Name must be unique!!')]

	name = fields.Char(string='SLA Name')
	response_time = fields.Float(digits=(5,1),string=u'Response Time', required=True)
	onsite_time = fields.Float(digits=(5,1),string='On Site Time', required=True)
	maintenance_time = fields.Float(digits=(5,1),string='Maintenance Time', required=True)
	disabled = fields.Boolean(string='Disabled',default=False)
	active = fields.Boolean(string="ACTIVE",default=True)
	# memo = fields.Text(string='Remark')

