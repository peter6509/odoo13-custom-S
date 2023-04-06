# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _


class NewebBaseResPartner(models.Model):
	# _name = 'res.partner'
	_inherit = 'res.partner'

	comp_create_date = fields.Date(string="Company Create Date")
	paidup_capital = fields.Float(digits=(13,0),string="Paid-up Capital")
	payment = fields.Selection([('telegraphic transfer', 'Telegraphic Transfer'), ('check', 'Check'), ('cash', 'Cash')])
	payment_days = fields.Integer(string="Payment Days")
	checkout_date = fields.Integer(string="Checkout Date")
	pay_date = fields.Integer(string="Pay Date")

	related_user_id = fields.Many2one('res.users', string="Related User")
	customer_category_id = fields.Many2one('neweb_base.customer_category', ondelete='cascade', string="Customer Category")




