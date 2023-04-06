# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, api


class Reportequipstatusbarcode(models.AbstractModel):
    _name = 'report.alldo_ipla_iot.alldo_ipla_iot_equipstatusbarcode_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_ipla_iot.equipstatusinfo'].search([])
        # print(docs)
        res_doc = []
        barcode_doc = []
        for line1 in docs:
            for line in line1.barcode_line:
                if not line.status_code1:
                    statuscode1 = ' '
                    statusname1 = ' '
                else:
                    statuscode1 = line.status_code1
                    statusname1 = line.status_name1
                if not line.status_code2:
                    statuscode2 = ' '
                    statusname2 = ' '
                else:
                    statuscode2 = line.status_code2
                    statusname2 = line.status_name2
                if not line.status_code3:
                    statuscode3 = ' '
                    statusname3 = ' '
                else:
                    statuscode3 = line.status_code3
                    statusname3 = line.status_name3
                if not line.status_code4:
                    statuscode4 = ' '
                    statusname4 = ' '
                else:
                    statuscode4 = line.status_code4
                    statusname4 = line.status_name4
                if not line.status_code5:
                    statuscode5 = ' '
                    statusname5 = ' '
                else:
                    statuscode5 = line.status_code5
                    statusname5 = line.status_name5
                if not line.status_code6:
                    statuscode6 = ' '
                    statusname6 = ' '
                else:
                    statuscode6 = line.status_code6
                    statusname6 = line.status_name6
                if not line.status_code7:
                    statuscode7 = ' '
                    statusname7 = ' '
                else:
                    statuscode7 = line.status_code7
                    statusname7 = line.status_name7
                if not line.status_code8:
                    statuscode8 = ' '
                    statusname8 = ' '
                else:
                    statuscode8 = line.status_code8
                    statusname8 = line.status_name8
                if not line.status_code9:
                    statuscode9 = ' '
                    statusname9 = ' '
                else:
                    statuscode9 = line.status_code9
                    statusname9 = line.status_name9
                if not line.status_code10:
                    statuscode10 = ' '
                    statusname10 = ' '
                else:
                    statuscode10 = line.status_code10
                    statusname10 = line.status_name10

                temp = {
                    'status_code1': statuscode1,
                    'status_name1': statusname1,
                    'status_code2': statuscode2,
                    'status_name2': statusname2,
                    'status_code3': statuscode3,
                    'status_name3': statusname3,
                    'status_code4': statuscode4,
                    'status_name4': statusname4,
                    'status_code5': statuscode5,
                    'status_name5': statusname5,
                    'status_code6': statuscode6,
                    'status_name6': statusname6,
                    'status_code7': statuscode7,
                    'status_name7': statusname7,
                    'status_code8': statuscode8,
                    'status_name8': statusname8,
                    'status_code9': statuscode9,
                    'status_name9': statusname9,
                    'status_code10': statuscode10,
                    'status_name10': statusname10,

                }
                barcode_doc.append(temp)
            temp1 = {
                'print_num': line1.print_num,
                'barcode_line': barcode_doc,
            }
            res_doc.append(temp1)
        docargs = {


            'doc_ids': docids,
            'doc_model': 'alldo_ipla_iot.equipstatusinfo',
            'docs': res_doc,
        }
        return docargs


