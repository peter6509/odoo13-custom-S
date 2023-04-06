# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotdbclearwizard(models.TransientModel):
    _name = "alldo_gh_iot.dbclear_wizard"

    passcode = fields.Char(string="PASS CODE",required=True)

    def run_db_clear(self):
        if self.passcode != '!99999ibm':
            raise UserError("PASSCODE ERROR")
        self.env.cr.execute("""delete from alldo_gh_iot_workorder""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_gh_iot_partner_prodin""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_gh_iot_partner_prodout""")
        self.env.cr.execute("""commit""")
        # self.env.cr.execute("""delete from alldo_gh_iot_emp_attendance""")
        # self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from stock_picking""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from stock_quant""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_gh_iot_equipment_iot_data""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_gh_iot_equipment_outofforder_status""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_gh_iot_excel_download""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from sale_order""")
        self.env.cr.execute("""commit""")
