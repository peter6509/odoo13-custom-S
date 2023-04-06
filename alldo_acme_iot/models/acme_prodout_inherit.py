# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class AcmeProdOutLineInherit(models.Model):
    _inherit = "alldo_acme_iot.prodout_line"

    date_due = fields.Date(string="應交日期",required=True)


