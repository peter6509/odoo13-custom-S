# _*_ coding: utf-8 _*_

from odoo import models, api


class ReportPurchaseOrder1(models.AbstractModel):
    _name = 'report.centtech_report.purchase_order_report_custom1'



    @api.multi
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        myid = self.env.context.get('active_id')
        docs = self.env['purchase.order'].browse(docids)

        docargs = {
            'doc_ids': docids,
            'doc_model': self.model,
            'docs': docs,
        }
        return self.env['report'].sudo().render('centtech_report.purchase_order_report_custom1', values=docargs)


