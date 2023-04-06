# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import timedelta,datetime
from odoo.exceptions import UserError
import xlsxwriter



class newebchiinvoicing7wizard(models.TransientModel):
    _name = "neweb_chi_invoicing.chiinvoicing7_wizard"
    _description = "(維護案)銷貨憑證整批匯出精靈"

    export_user = fields.Many2one('res.users',string="匯出人員",default=lambda self:self.env.uid)


    def getunchiexportsaleinv(self):

        self.env.cr.execute("""select gen_unexport_mainsaleinv(%d)""" % (self.export_user.id))
        myid = self.env['neweb_chi_invoicing.un_export_invoiceopen'].search([])
        if not myid:
            raise UserError("沒有需匯出的銷項項目,請確認")
        self.env.cr.execute("""select prerunpackageexport()""")
        self.env.cr.execute("""commit""")
        return {'view_name': 'newebchiunexportprojselect',
                'name': ('專案購貨明細資料'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_chi_invoicing.un_export_invoiceopen',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'res_id': myid.id,
                'flags': {'action_buttons': False,'initial_mode':'edit'},
                'view_mode': 'form',
                'view_type': 'form'
                }

