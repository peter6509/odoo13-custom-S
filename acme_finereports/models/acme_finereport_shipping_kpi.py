# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class AcmeFineReportShippingKPI(models.Model):
    _name = "alldo_acme_iot.finereport_shipping_kpi"
    _description = "產品出貨達成率KPI"
    _order = "seq"

    product_no = fields.Many2one('product.product',string="產品")
    so_no = fields.Char(string="銷售單號")
    seq = fields.Integer(string="SEQ")
    partner_id = fields.Many2one('res.partner',string="客戶")

    @api.model
    def init(self):
        self._cr.execute("""drop view if exists finereport_last10_shipping_kpi_view cascade""")
        self._cr.execute("""CREATE VIEW finereport_last10_shipping_kpi_view as (
                         select A.product_no,A.so_no,A.seq,C.default_code,B.commitment_date,B.shipping_date,B.partner_id,D.name as cusname,
                         B.dif_value,B.holiday_num,B.shipping_kpi
                          from alldo_acme_iot_finereport_shipping_kpi A 
                         left join alldo_acme_iot_shipping_kpi_report B on A.so_no = B.so_no and A.product_no = B.product_no
                         left join product_product C on A.product_no = C.id
                         left join res_partner D on B.partner_id = D.id order by A.seq
                          )""")
