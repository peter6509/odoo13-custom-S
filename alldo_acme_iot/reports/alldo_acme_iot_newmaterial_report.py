# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, api


class Reportnewmaterialbarcode(models.AbstractModel):
    _name = 'report.alldo_acme_iot.alldo_acme_iot_furance_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_acme_iot.furance_report'].search([])
        # print(docs)
        res_doc = []
        barcode_doc = []
        # for line in docs:
        temp = {
            'name': docs[0].name,
            'code': docs[0].code,
                }
        barcode_doc.append(temp)
        temp1 = {
            'barcode_line': barcode_doc,
        }
        res_doc.append(temp1)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_acme_iot.furance_report',
            'docs': res_doc,
            }
        return docargs


