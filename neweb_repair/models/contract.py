# -*- encoding: utf-8 -*-
import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class Contract(models.Model):
	_name = 'neweb_contract.contract'
	_inherit = 'neweb_contract.contract'

	@api.depends('repair_ids')
	def _repair_count(self):
		self.repair_count = len(self.repair_ids)

	@api.depends()
	def _timesheet_count(self):
		self.env.cr.execute("""select gettimesheetcount(%d)""" % self.id)
		myres = self.env.cr.fetchone()[0]
		self.timesheet_count = myres


	repair_ids = fields.One2many('neweb_repair.repair', 'contract_id', string="Repairs")
	repair_count = fields.Integer(string="# Repair", compute=_repair_count)
	timesheet_count = fields.Integer(string="# TimeSheet HR",compute=_timesheet_count)

	def action_view_timesheet(self):
		# self.ensure_one()
		context = {'timesheet_origin': self.name}
		action = self.env.ref('neweb_emp_timesheet.action_timesheet_calendar_list')
		self.env.cr.execute("""select gentimesheetrec(%d)""" % self.id)
		myrec = self.env.cr.fetchall()
		ids = []
		for rec in myrec:
			ids.append((rec[0]))
		print("筆數：%s" % ids)

		return {
			'name': action.name,
			'help': action.help,
			'type': action.type,
			# 'view_type': action.view_type,
			'view_mode': action.view_mode,
			'target': action.target,
			'res_model': action.res_model,
			'domain': [('id', 'in', ids)],
			'context': context,
		}


	def action_view_repair(self):
		self.ensure_one()
		action = self.env.ref('neweb_repair.action_contract_repair_list')
		context = {'contract_id': self.id, 'customer_id': self.customer_name.id}

		return {
			'name': action.name,
			'help': action.help,
			'type': action.type,
			# 'view_type': action.view_type,
			'view_mode': action.view_mode,
			'target': action.target,
			'res_model': action.res_model,
			'domain': [('contract_id', '=', self.id)],
			'context': context,
		}