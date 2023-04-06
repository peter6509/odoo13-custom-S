# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class wkorderselectitem(models.Model):
    _name = "alldo_acme_iot.wkorder_selectitem"

    report_owner = fields.Many2one('res.users',string="報表產出人")
    report_date = fields.Datetime(string="製作時間")
    report_line = fields.One2many('alldo_acme_iot.wkorder_selectitem_line','item_id',string="明細")

    def run_all_select(self):
        myrec = self.env['alldo_acme_iot.wkorder_selectitem'].search([])
        for rec in myrec.report_line:
            rec.update({'select_yn': True})

    def run_all_unselect(self):
        myrec = self.env['alldo_acme_iot.wkorder_selectitem'].search([])
        for rec in myrec.report_line:
            rec.update({'select_yn': False})

    def print_wkorder(self):
        mycount = self.env['alldo_acme_iot.wkorder_selectitem_line'].search_count([('item_id','=',self.id),('select_yn','=',True)])
        self.env.cr.execute("""select genselectitemreport()""")
        self.env.cr.execute("""commit""")
        if mycount == 0 :
            raise UserError("沒有選擇任何要列印的工單！")
        # self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        myrec = self.env['alldo_acme_iot.wkorder_printsheet'].search([])
        return self.env.ref('alldo_acme_iot.action_alldo_acme_iot_wkorder_report').report_action(myrec)

    def name_get(self):
        result = []
        for myrec in self:
            myname = "製表人:%s" % (myrec.report_owner.name)
            result.append((myrec.id, myname))
        return result


class wkorderselectitemline(models.Model):
    _name = "alldo_acme_iot.wkorder_selectitem_line"

    item_id = fields.Many2one('alldo_acme_iot.wkorder_selectitem',ondelete='cascade')
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



class wkorderprintsheet(models.Model):
    _name = "alldo_acme_iot.wkorder_printsheet"
    _description = "工單列印暫存檔"

    name = fields.Char(string="工單號",default=' ')
    product_no = fields.Char(string="料號",default=' ')
    product_blank = fields.Char(string="毛胚",default=' ')
    po_no = fields.Char(string="客戶訂單",default=' ')
    cus_name = fields.Many2one('res.partner',string="客戶名稱")
    order_num = fields.Integer(string="訂單數")
    blank_num = fields.Integer(string="毛胚數")
    eng_type = fields.Char(string="工程別",default=' ')
    cnc_prog = fields.Char(string="程式代號",default=' ')
    clamping_power = fields.Char(string="挾持壓力",default=' ')
    standard_num = fields.Integer(string="標準量")
    shipping_date = fields.Date(string="出貨日")
    blank_input_date = fields.Date(string="進貨日")
    ins1_name = fields.Char(string="檢1名稱",default=' ')
    ins1_size = fields.Char(string="檢1尺吋",default=' ')
    ins1_tolerance = fields.Char(string="檢1公差",default=' ')
    ins1_real_size = fields.Char(string="檢1實作尺寸",default=' ')
    ins1_testtype = fields.Char(string="檢1測試方式",default=' ')
    ins1_testmode = fields.Char(string="檢1測試工具",default=' ')

    ins2_name = fields.Char(string="檢2名稱",default=' ')
    ins2_size = fields.Char(string="檢2尺吋",default=' ')
    ins2_tolerance = fields.Char(string="檢2公差",default=' ')
    ins2_real_size = fields.Char(string="檢2實作尺寸",default=' ')
    ins2_testtype = fields.Char(string="檢2測試方式",default=' ')
    ins2_testmode = fields.Char(string="檢2測試工具",default=' ')
    ins3_name = fields.Char(string="檢3名稱",default=' ')
    ins3_size = fields.Char(string="檢3尺吋",default=' ')
    ins3_tolerance = fields.Char(string="檢3公差",default=' ')
    ins3_real_size = fields.Char(string="檢3實作尺寸",default=' ')
    ins3_testtype = fields.Char(string="檢3測試方式",default=' ')
    ins3_testmode = fields.Char(string="檢3測試工具",default=' ')
    ins4_name = fields.Char(string="檢4名稱",default=' ')
    ins4_size = fields.Char(string="檢4尺吋",default=' ')
    ins4_tolerance = fields.Char(string="檢4公差",default=' ')
    ins4_real_size = fields.Char(string="檢4實作尺寸",default=' ')
    ins4_testtype = fields.Char(string="檢4測試方式",default=' ')
    ins4_testmode = fields.Char(string="檢4測試工具",default=' ')
    ins5_name = fields.Char(string="檢5名稱",default=' ')
    ins5_size = fields.Char(string="檢5尺吋",default=' ')
    ins5_tolerance = fields.Char(string="檢5公差",default=' ')
    ins5_real_size = fields.Char(string="檢5實作尺寸",default=' ')
    ins5_testtype = fields.Char(string="檢5測試方式",default=' ')
    ins5_testmode = fields.Char(string="檢5測試工具",default=' ')
    workorder_memo = fields.Text(string="註記")
    product_blank1 = fields.Many2one('product.template', string="鑄件材質")
