# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class wkorderselectitem1(models.Model):
    _name = "alldo_gh_iot.wkorder_selectitem1"

    report_owner = fields.Many2one('res.users',string="報表產出人")
    report_date = fields.Datetime(string="製作時間")
    report_line = fields.One2many('alldo_gh_iot.wkorder_selectitem_line1','item_id',string="明細")

    def run_all_select(self):
        myrec = self.env['alldo_gh_iot.wkorder_selectitem1'].search([])
        for rec in myrec.report_line:
            rec.update({'select_yn': True})

    def run_all_unselect(self):
        myrec = self.env['alldo_gh_iot.wkorder_selectitem1'].search([])
        for rec in myrec.report_line:
            rec.update({'select_yn': False})

    def print_wkorder(self):
        mycount = self.env['alldo_gh_iot.wkorder_selectitem_line1'].search_count([('item_id','=',self.id),('select_yn','=',True)])
        self.env.cr.execute("""select genselectitemreport1()""")
        self.env.cr.execute("""commit""")
        if mycount == 0 :
            raise UserError("沒有選擇任何要列印的工單！")
        # self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        myrec = self.env['alldo_gh_iot.wkorder_printsheet1'].search([])
        return self.env.ref('alldo_gh_iot.action_alldo_gh_iot_wkorder_report1').report_action(myrec)

    def name_get(self):
        result = []
        for myrec in self:
            myname = "製表人:%s" % (myrec.report_owner.name)
            result.append((myrec.id, myname))
        return result


class wkorderselectitemline1(models.Model):
    _name = "alldo_gh_iot.wkorder_selectitem_line1"

    item_id = fields.Many2one('alldo_gh_iot.wkorder_selectitem1',ondelete='cascade')
    name = fields.Char(string="工單號碼")
    cus_name = fields.Many2one('res.partner', string="客戶")
    product_no = fields.Many2one('product.product',string="料號")
    eng_type = fields.Char(string="工程別")
    cnc_prog = fields.Char(string="程式代號")
    po_no = fields.Char(string="客戶訂單")
    order_num = fields.Integer(string="訂單數量")
    blank_num = fields.Integer(string="毛胚數量")
    shipping_date = fields.Date(string="出貨日")
    blank_input_date = fields.Date(string="進貨日")
    select_yn = fields.Boolean(string="勾選",defaulr=False)

    def selectyn(self):
        for rec in self:
            if rec.select_yn == False:
                rec.update({'select_yn': True})
            else:
                rec.update({'select_yn': False})



class wkorderprintsheet1(models.Model):
    _name = "alldo_gh_iot.wkorder_printsheet1"
    _description = "工單列印暫存檔"

    product_no = fields.Char(string="料號",default=' ')
    order_num = fields.Integer(string="訂單數")
    blank_num = fields.Integer(string="毛胚數")
    shipping_date = fields.Date(string="出貨日")
    blank_input_date = fields.Date(string="進貨日")
    wk_name1 = fields.Char(string="1工單號")
    wk_name2 = fields.Char(string="2工單號")
    wk_name3 = fields.Char(string="3工單號")
    wk_name4 = fields.Char(string="4工單號")
    wk_name5 = fields.Char(string="5工單號")
    wk_name6 = fields.Char(string="6工單號")
    wk_name7 = fields.Char(string="7工單號")
    wk_name8 = fields.Char(string="8工單號")
