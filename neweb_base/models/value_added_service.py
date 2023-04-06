# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _


class ValueAddedService(models.Model):
    _name = 'neweb_base.value_added_service'
    _description = "Value-Added Service"

    name = fields.Char(string='Name', required=True, translate=True)
    content = fields.Text(string='Content')
    disabled = fields.Boolean(string='Disabled')
