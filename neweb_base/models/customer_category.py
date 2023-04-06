# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class CustomerCategory(models.Model):
    _name = "neweb_base.customer_category"
    _description = "客戶分類基礎配置"
    _sql_constraints = [('name_uniq', 'unique(name)', 'Customer Category must be unique!!')]

    name = fields.Char(string='Customer Category', required=True, translate=True)
    disabled = fields.Boolean(string='Disabled')
    memo = fields.Text(string='Remark')
