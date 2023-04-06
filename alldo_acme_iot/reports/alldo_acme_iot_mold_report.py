# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class Reportmoldbarcode(models.AbstractModel):
    _name = 'report.alldo_acme_iot.alldo_acme_iot_mold_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_acme_iot.mold_report'].search([])
        res_doc = []
        moldcode_doc = []
        for line1 in docs:
            for line in line1.mold_line:
                if not line.mold_code1:
                    moldcode1 = ' '
                else:
                    moldcode1 = line.mold_code1
                if not line.mold_code2:
                    moldcode2 = ' '
                else:
                    moldcode2 = line.mold_code2
                if not line.mold_code3:
                    moldcode3 = ' '
                else:
                    moldcode3 = line.mold_code3
                if not line.mold_code4:
                    moldcode4 = ' '
                else:
                    moldcode4 = line.mold_code4
                if not line.mold_code5:
                    moldcode5 = ' '
                else:
                    moldcode5 = line.mold_code5
                if not line.mold_code6:
                    moldcode6 = ' '
                else:
                    moldcode6 = line.mold_code6
                if not line.mold_code7:
                    moldcode7 = ' '
                else:
                    moldcode7 = line.mold_code7
                if not line.mold_code8:
                    moldcode8 = ' '
                else:
                    moldcode8 = line.mold_code8
                if not line.mold_code9:
                    moldcode9 = ' '
                else:
                    moldcode9 = line.mold_code9
                if not line.mold_code10:
                    moldcode10 = ' '
                else:
                    moldcode10 = line.mold_code10
                if not line.mold_code11:
                    moldcode11 = ' '
                else:
                    moldcode11 = line.mold_code11
                if not line.mold_code12:
                    moldcode12 = ' '
                else:
                    moldcode12 = line.mold_code12
                if not line.mold_code13:
                    moldcode13 = ' '
                else:
                    moldcode13 = line.mold_code13
                if not line.mold_code14:
                    moldcode14 = ' '
                else:
                    moldcode14 = line.mold_code14
                if not line.mold_code15:
                    moldcode15 = ' '
                else:
                    moldcode15 = line.mold_code15
                if not line.mold_code16:
                    moldcode16 = ' '
                else:
                    moldcode16 = line.mold_code16
                if not line.mold_code17:
                    moldcode17 = ' '
                else:
                    moldcode17 = line.mold_code17
                if not line.mold_code18:
                    moldcode18 = ' '
                else:
                    moldcode18 = line.mold_code18
                if not line.mold_code19:
                    moldcode19 = ' '
                else:
                    moldcode19 = line.mold_code19
                if not line.mold_code20:
                    moldcode20 = ' '
                else:
                    moldcode20 = line.mold_code20

                temp = {
                    'mold_code1': moldcode1,
                    'mold_code2': moldcode2,
                    'mold_code3': moldcode3,
                    'mold_code4': moldcode4,
                    'mold_code5': moldcode5,
                    'mold_code6': moldcode6,
                    'mold_code7': moldcode7,
                    'mold_code8': moldcode8,
                    'mold_code9': moldcode9,
                    'mold_code10': moldcode10,
                    'mold_code11': moldcode11,
                    'mold_code12': moldcode12,
                    'mold_code13': moldcode13,
                    'mold_code14': moldcode14,
                    'mold_code15': moldcode15,
                    'mold_code16': moldcode16,
                    'mold_code17': moldcode17,
                    'mold_code18': moldcode18,
                    'mold_code19': moldcode19,
                    'mold_code20': moldcode20,
                }

                moldcode_doc.append(temp)
            temp1 = {
                'report_owner': line1.report_owner,
                'mold_line': moldcode_doc,
            }
            res_doc.append(temp1)
        docargs = {


            'doc_ids': docids,
            'doc_model': 'alldo_acme_iot.mold_report',
            'docs': res_doc,
        }
        return docargs


