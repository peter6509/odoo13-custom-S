# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime

class AcmeOutsuborderProdoutInherit(models.Model):
    _inherit = "alldo_acme_iot.outsuborder_prodout"
    # 委外加工給料

    date_supply = fields.Date(string="供料日期",required=True,default=datetime.today())
    date_due = fields.Date(string="應交日期",required=True)

class AcmeOutsuborderProdinInherit(models.Model):
    _inherit = "alldo_acme_iot.outsuborder_prodin"
    # 委外加工完工移轉

    date_delivery = fields.Date(string="實際交期",required=True,default=datetime.today())

