# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.bom.line'

    product_version = fields.Integer(string='版本號', related='product_id.version', store=True, readonly=True)
