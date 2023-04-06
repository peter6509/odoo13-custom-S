# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
# import odoo.addons.decimal_precision as dp
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class newebchipurchase(models.Model):
    _name = "neweb_chi_invoicing.purchase_select"
    _description = "進銷存進項分批選單主檔"

    @api.depends()
    def _get_owner(self):
        self.select_owner=self.env.user
        return self.env.user

    select_owner = fields.Many2one('res.users',string="選單人",store=True,compute=_get_owner)
    purchase_line = fields.One2many('neweb_chi_invoicing.purchase_select_line','purchase_id')

    def select_alltrue(self):

        for rec in self.purchase_line:
            rec.update({'chi_select':1})


    def select_allfalse(self):
        for rec in self.purchase_line:
            rec.update({'chi_select':0})


    def return_purinv(self):
        # return {'type': 'ir.actions.client', 'tag': 'history_back'}

        myid = self.env.context.get('invoiceopen_id')
        myviewid = self.env.ref('neweb_purinv.neweb_purinv_invoice_view_form')
        return {
            'view_name': 'newebinvoicingexportwizard',
            'name': ('進銷存 purchase 分批選單'),
            'views': [(myviewid.id, 'form'),],
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_purinv.invoice',
            # 'view_id': myviewid.id,
            'res_id': myid,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'main',
            'tag':'reload',}


class newebchipurchaseline(models.Model):
    _name = "neweb_chi_invoicing.purchase_select_line"
    _description = "進銷存進項分批選單明細檔"

    purchase_id = fields.Many2one('neweb_chi_invoicing.purchase_select',ondelete='cascade')
    pitem_machine_type = fields.Char(string="機種")
    pitem_model_type = fields.Char(string="機種-機型/料號")
    pitem_spec = fields.Char(string="規格說明")
    pitem_num = fields.Float(digits=(10,0), string="數量", required=True)
    pitem_price = fields.Float(digits=(13,2), string="單價", required=True)
    pitem_id = fields.Integer(string="PITEM ID")
    chi_select = fields.Boolean(string="進銷存勾選", default=False)
    purchase_no = fields.Char(string="單號", default='')

    def selectyn(self):
        for rec in self:
            if rec.chi_select==False:
                rec.chi_select = True
                self.env.cr.execute("""update neweb_pitem_list set chi_select=True where id=%d""" % rec.pitem_id)
                self.env.cr.execute("""commit""")
            else:
                rec.chi_select = False
                self.env.cr.execute("""update neweb_pitem_list set chi_select=False where id=%d""" % rec.pitem_id)
                self.env.cr.execute("""commit""")
