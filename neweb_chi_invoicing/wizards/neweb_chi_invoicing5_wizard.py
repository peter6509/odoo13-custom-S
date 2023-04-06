# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import timedelta,datetime
from odoo.exceptions import UserError
import xlsxwriter



class newebchiinvoicing5wizard(models.TransientModel):
    _name = "neweb_chi_invoicing.chiinvoicing5_wizard"
    _description = "專案/產品主檔整批匯出精靈"


    invoicing_start_date = fields.Date(string="匯出啟始日期")
    invoicing_end_date = fields.Date(string="匯出截止日期")
    project_ids = fields.Many2many('neweb.project','chi_project_rel','chi_id','proj_id',string="專案編號")
    export_user = fields.Many2one('res.users',string="匯出人員",default=lambda self:self.env.uid)


    def getunchiexportproj(self):
        if not self.project_ids:
            if not self.invoicing_start_date or not self.invoicing_end_date:
                raise UserError("啟始日期/截止日期不完整！")
            self.env.cr.execute("""select gen_chi_export_proj('%s','%s',%d)""" % (self.invoicing_start_date,self.invoicing_end_date,self.export_user.id))
        else:
            self.env.cr.execute("""select gen_chi_export_proj_ids(%d,%d)""" % (self.id,self.export_user.id))
        myid = self.env['neweb_chi_invoicing.un_export_proj'].search([])
        if not myid:
            raise UserError("沒有需匯出的專案項目,請確認")
        ########  刪除整批匯出暫存檔  #############
        self.env.cr.execute("""select prerunpackageexport()""")
        self.env.cr.execute("""commit""")
        return {'view_name': 'newebchiunexportprojselect',
                'name': ('專案購貨明細資料'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_chi_invoicing.un_export_proj',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'res_id': myid.id,
                'flags': {'action_buttons': False,'initial_mode':'edit'},
                'view_mode': 'form',
                'view_type': 'form'
                }

