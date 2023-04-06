# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class ReportSaleOrderp(models.AbstractModel):
    _name = 'report.centtech_report.sale_order_report_customp'



    @api.multi
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        myid = self.env.context.get('active_id')
        docs = self.env['sale.order'].browse(docids)

        docargs = {
            'doc_ids': docids,
            'doc_model': self.model,
            'docs': docs,
        }
        return self.env['report'].sudo().render('centtech_report.sale_order_report_customp', values=docargs)


