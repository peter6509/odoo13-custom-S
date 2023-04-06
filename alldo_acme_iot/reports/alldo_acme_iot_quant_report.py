# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class Reportquantbarcode(models.AbstractModel):
    _name = 'report.alldo_acme_iot.alldo_acme_iot_quant_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_acme_iot.quant_report'].search([])
        res_doc = []
        quantcode_doc = []
        for line1 in docs:
            for line in line1.quant_line:
                if not line.lot_code1:
                    lotcode1 = ' '
                else:
                    lotcode1 = line.lot_code1
                if not line.lot_code2:
                    lotcode2 = ' '
                else:
                    lotcode2 = line.lot_code2
                if not line.lot_code3:
                    lotcode3 = ' '
                else:
                    lotcode3 = line.lot_code3
                if not line.lot_code4:
                    lotcode4 = ' '
                else:
                    lotcode4 = line.lot_code4
                if not line.lot_code5:
                    lotcode5 = ' '
                else:
                    lotcode5 = line.lot_code5
                if not line.lot_code6:
                    lotcode6 = ' '
                else:
                    lotcode6 = line.lot_code6
                if not line.lot_code7:
                    lotcode7 = ' '
                else:
                    lotcode7 = line.lot_code7
                if not line.lot_code8:
                    lotcode8 = ' '
                else:
                    lotcode8 = line.lot_code8
                if not line.lot_code9:
                    lotcode9 = ' '
                else:
                    lotcode9 = line.lot_code9
                if not line.lot_code10:
                    lotcode10 = ' '
                else:
                    lotcode10 = line.lot_code10
                if not line.lot_code11:
                    lotcode11 = ' '
                else:
                    lotcode11 = line.lot_code11
                if not line.lot_code12:
                    lotcode12 = ' '
                else:
                    lotcode12 = line.lot_code12
                if not line.lot_code13:
                    lotcode13 = ' '
                else:
                    lotcode13 = line.lot_code13
                if not line.lot_code14:
                    lotcode14 = ' '
                else:
                    lotcode14 = line.lot_code14
                if not line.lot_code15:
                    lotcode15 = ' '
                else:
                    lotcode15 = line.lot_code15
                if not line.lot_code16:
                    lotcode16 = ' '
                else:
                    lotcode16 = line.lot_code16
                if not line.lot_code17:
                    lotcode17 = ' '
                else:
                    lotcode17 = line.lot_code17
                if not line.lot_code18:
                    lotcode18 = ' '
                else:
                    lotcode18 = line.lot_code18
                if not line.lot_code19:
                    lotcode19 = ' '
                else:
                    lotcode19 = line.lot_code19
                if not line.lot_code20:
                    lotcode20 = ' '
                else:
                    lotcode20 = line.lot_code20

                temp = {
                    'lot_code1': lotcode1,
                    'lot_code2': lotcode2,
                    'lot_code3': lotcode3,
                    'lot_code4': lotcode4,
                    'lot_code5': lotcode5,
                    'lot_code6': lotcode6,
                    'lot_code7': lotcode7,
                    'lot_code8': lotcode8,
                    'lot_code9': lotcode9,
                    'lot_code10': lotcode10,
                    'lot_code11': lotcode11,
                    'lot_code12': lotcode12,
                    'lot_code13': lotcode13,
                    'lot_code14': lotcode14,
                    'lot_code15': lotcode15,
                    'lot_code16': lotcode16,
                    'lot_code17': lotcode17,
                    'lot_code18': lotcode18,
                    'lot_code19': lotcode19,
                    'lot_code20': lotcode20,
                }

                quantcode_doc.append(temp)
            temp1 = {
                'report_owner': line1.report_owner,
                'quant_line': quantcode_doc,
            }
            res_doc.append(temp1)
        docargs = {


            'doc_ids': docids,
            'doc_model': 'alldo_acme_iot.quant_report',
            'docs': res_doc,
        }
        return docargs


