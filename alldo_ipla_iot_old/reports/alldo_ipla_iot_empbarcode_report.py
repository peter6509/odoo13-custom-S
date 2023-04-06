# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, api


class Reportempbarcode(models.AbstractModel):
    _name = 'report.alldo_ipla_iot.alldo_ipla_iot_empbarcode_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_ipla_iot.empinfo'].search([])
        # print(docs)
        res_doc = []
        barcode_doc = []
        for line1 in docs:
            for line in line1.barcode_line:
                if not line.emp_code1:
                    empcode1 = ' '
                    empname1 = ' '
                else:
                    empcode1 = line.emp_code1
                    empname1 = line.emp_name1
                if not line.emp_code2:
                    empcode2 = ' '
                    empname2 = ' '
                else:
                    empcode2 = line.emp_code2
                    empname2 = line.emp_name2
                if not line.emp_code3:
                    empcode3 = ' '
                    empname3 = ' '
                else:
                    empcode3 = line.emp_code3
                    empname3 = line.emp_name3
                if not line.emp_code4:
                    empcode4 = ' '
                    empname4 = ' '
                else:
                    empcode4 = line.emp_code4
                    empname4 = line.emp_name4
                if not line.emp_code5:
                    empcode5 = ' '
                    empname5 = ' '
                else:
                    empcode5 = line.emp_code5
                    empname5 = line.emp_name5
                if not line.emp_code6:
                    empcode6 = ' '
                    empname6 = ' '
                else:
                    empcode6 = line.emp_code6
                    empname6 = line.emp_name6
                if not line.emp_code7:
                    empcode7 = ' '
                    empname7 = ' '
                else:
                    empcode7 = line.emp_code7
                    empname7 = line.emp_name7
                if not line.emp_code8:
                    empcode8 = ' '
                    empname8 = ' '
                else:
                    empcode8 = line.emp_code8
                    empname8 = line.emp_name8
                if not line.emp_code9:
                    empcode9 = ' '
                    empname9 = ' '
                else:
                    empcode9 = line.emp_code9
                    empname9 = line.emp_name9
                if not line.emp_code10:
                    empcode10 = ' '
                    empname10 = ' '
                else:
                    empcode10 = line.emp_code10
                    empname10 = line.emp_name10

                temp = {
                    'emp_code1': empcode1,
                    'emp_name1': empname1,
                    'emp_code2': empcode2,
                    'emp_name2': empname2,
                    'emp_code3': empcode3,
                    'emp_name3': empname3,
                    'emp_code4': empcode4,
                    'emp_name4': empname4,
                    'emp_code5': empcode5,
                    'emp_name5': empname5,
                    'emp_code6': empcode6,
                    'emp_name6': empname6,
                    'emp_code7': empcode7,
                    'emp_name7': empname7,
                    'emp_code8': empcode8,
                    'emp_name8': empname8,
                    'emp_code9': empcode9,
                    'emp_name9': empname9,
                    'emp_code10': empcode10,
                    'emp_name10': empname10,

                }

                barcode_doc.append(temp)
            temp1 = {
                'empinfodate': line1.empinfo_date,
                'barcode_line': barcode_doc,
            }
            res_doc.append(temp1)
        docargs = {


            'doc_ids': docids,
            'doc_model': 'alldo_ipla_iot.empinfo',
            'docs': res_doc,
        }
        return docargs


