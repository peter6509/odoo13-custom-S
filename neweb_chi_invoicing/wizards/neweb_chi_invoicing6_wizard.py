# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import timedelta,datetime
from odoo.exceptions import UserError
import xlsxwriter



class newebchiinvoicing6wizard(models.TransientModel):
    _name = "neweb_chi_invoicing.chiinvoicing6_wizard"
    _description = "(維護)專案/產品主檔整批匯出精靈"


    con_start_date = fields.Date(string="啟始時間",required=True)
    con_end_date = fields.Date(string="截止時間",required=True)
    export_user = fields.Many2one('res.users',string="匯出人員",default=lambda self:self.env.uid)


    def getunchiexportmainproj(self):
        self.env.cr.execute("""select gen_chi_export_mainproj('%s','%s',%d)""" % (self.con_start_date,self.con_end_date, self.export_user.id))
        self.env.cr.execute("""commit""")
        myid = self.env['neweb_chi_invoicing.un_export_main_proj'].search([])
        if not myid:
            raise UserError("沒有需匯出的專案項目,請確認")
        ########  刪除整批匯出暫存檔  #############
        self.env.cr.execute("""select prerunpackageexport()""")
        self.env.cr.execute("""commit""")
        return {'view_name': 'newebchiunexportmainprojselect',
                'name': ('專案購貨明細資料'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_chi_invoicing.un_export_main_proj',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'res_id': myid.id,
                'flags': {'action_buttons': False,'initial_mode':'edit'},
                'view_mode': 'form',
                'view_type': 'form'
                }

