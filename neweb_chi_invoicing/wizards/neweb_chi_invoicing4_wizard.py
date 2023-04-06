# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError


class newebchiinvoicing4wizard(models.Model):
    _name = "neweb_chi_invoicing.chiinvoicing4_wizard"
    _description = "進項憑證單筆匯出精靈"

    purchase_no = fields.Many2one('purchase.order',string="採購編號")
    export_user = fields.Many2one('res.users', string="匯出人員", default=lambda self: self.env.uid)

    def run_invoicing4_export(self):
        self.env.cr.execute("""select gen_unexport_purinv1(%d,%d)""" % (self.export_user.id,self.purchase_no.id))
        myid = self.env['neweb_chi_invoicing.un_export_purinv'].search([])
        if not myid:
            raise UserError("沒有需匯出的進項項目,請確認")
        self.env.cr.execute("""select prerunpackageexport()""")
        self.env.cr.execute("""commit""")
        return {'view_name': 'newebchiunexportpurinvselect',
                'name': ('進項購貨明細資料'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_chi_invoicing.un_export_purinv',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'res_id': myid.id,
                'flags': {'action_buttons': False, 'initial_mode': 'edit'},
                'view_mode': 'form',
                'view_type': 'form'
                }