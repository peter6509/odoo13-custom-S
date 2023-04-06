# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotdbclearwizard(models.TransientModel):
    _name = "alldo_ipla_iot.dbclear_wizard"

    passcode = fields.Char(string="PASS CODE",required=True)

    def run_db_clear(self):
        if self.passcode != '!99999ibm':
            raise UserError("PASSCODE ERROR")
        self.env.cr.execute("""delete from alldo_ipla_iot_workorder""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_outsuborder""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_po_wkorder""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_partner_prodin""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_partner_prodout""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from stock_picking""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_emp_attendance""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_equipment_iot_data""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_equipment_outofforder_status""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_excel_download""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_furnace_stock_move""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_electronic_scale""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from alldo_ipla_iot_emp_attendance_list""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from mrp_production""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from sale_order""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from purchase_order""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from stock_quant""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from stock_production_lot""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""update stock_quant set reserved_quantity=0 ;""")
        self.env.cr.execute("""commit""")