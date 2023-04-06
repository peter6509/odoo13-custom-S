# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, api


class Reportbarcode5(models.AbstractModel):
    _name = 'report.alldo_ipla_iot.alldo_ipla_iot_barcode5_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_ipla_iot.furance_report'].search([])
        # print(docs)
        res_doc = []
        barcode_doc = []
        for line in docs:
            temp = {
                'name': line.name,
                'code': line.code,
                    }
            barcode_doc.append(temp)
        temp1 = {
            'barcode_line': barcode_doc,
        }
        res_doc.append(temp1)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_ipla_iot.furance_report',
            'docs': res_doc,
            }
        return docargs


