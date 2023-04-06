# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class eramainreportwizard(models.TransientModel):
    _name = "era.maintenance_report_wizard"

    main_start_date = fields.Date(string="啟始時間",required=True)
    main_end_date = fields.Date(string="截止時間",required=True)

    def era_maintenance_print(self):
        data = dict()
        data["startdate"] = self.main_start_date
        data["enddate"] = self.main_end_date

        return self.env.ref('era_household.action_era_maintenance_report').report_action(self, data=data)


