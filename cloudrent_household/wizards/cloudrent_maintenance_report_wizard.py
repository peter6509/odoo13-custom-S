# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class cloudrentmainreportwizard(models.TransientModel):
    _name = "cloudrent.maintenance_report_wizard"

    main_start_date = fields.Date(string="啟始時間",required=True)
    main_end_date = fields.Date(string="截止時間",required=True)

    def cloudrent_maintenance_print(self):
        data = dict()
        data["startdate"] = self.main_start_date
        data["enddate"] = self.main_end_date

        return self.env.ref('cloudrent_household.action_cloudrent_maintenance_report').report_action(self, data=data)


