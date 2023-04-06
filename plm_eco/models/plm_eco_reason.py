# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MrpEcoReason(models.Model):
    _name = 'mrp.eco.reason'
    _description = 'MrpEcOReason'
    _rec_name = 'name'

    name = fields.Char(string='原因名稱')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "設變原因已重覆"),
    ]
