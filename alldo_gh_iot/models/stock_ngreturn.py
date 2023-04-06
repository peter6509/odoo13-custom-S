# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError

class stockngreturndata(models.Model):
    _name = "alldo_gh_iot.ngreturn_report"

    partner_id = fields.Many2one('res.partner',string="客戶")
    name = fields.Char(string="退料單號",default=lambda self: _('New'))
    report_date = fields.Date(string="製表日期")
    report_line = fields.One2many('alldo_gh_iot.ngreturn_report_line','rep_id',copy=False)
    report_memo = fields.Char(string="備註")


    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('alldo_gh_iot.return_ng') or _('New')
    #     res = super(stockngreturndata, self).create(vals)
    #     return res


class stockngreturnline(models.Model):
    _name = "alldo_gh_iot.ngreturn_report_line"

    rep_id = fields.Many2one('alldo_gh_iot.ngreturn_report',ondelete='cascade')
    item = fields.Integer(string="ITEM")
    prod_no = fields.Many2one('product.product',string="料號")
    m_ng_num = fields.Float(digits=(6,0),string="材料不良數量")
    p_ng_num = fields.Float(digits=(6,0),string="加工不良數量")
    m_loss_num = fields.Float(digits=(6,0),string="來料短少數量")
    prod_uom = fields.Char(string="單位",default='PCS')
    line_memo = fields.Char(string="說明")
    item1 = fields.Integer(string="ITEM1")
    prod_no1 = fields.Many2one('product.product',string="料號1")
    m_ng_num1 = fields.Float(digits=(6, 0), string="材料不良數量1")
    p_ng_num1 = fields.Float(digits=(6, 0), string="加工不良數量1")
    m_loss_num1 = fields.Float(digits=(6, 0), string="來料短少數量1")
    prod_uom1 = fields.Char(string="單位1", default='PCS')
    line_memo1 = fields.Char(string="說明1")
    item2 = fields.Integer(string="ITEM2")
    prod_no2 = fields.Many2one('product.product',string="料號2")
    m_ng_num2 = fields.Float(digits=(6, 0), string="材料不良數量2")
    p_ng_num2 = fields.Float(digits=(6, 0), string="加工不良數量2")
    m_loss_num2 = fields.Float(digits=(6, 0), string="來料短少數量2")
    prod_uom2 = fields.Char(string="單位2", default='PCS')
    line_memo2 = fields.Char(string="說明2")
    item3 = fields.Integer(string="ITEM3")
    prod_no3 = fields.Many2one('product.product',string="料號3")
    m_ng_num3 = fields.Float(digits=(6, 0), string="材料不良數量3")
    p_ng_num3 = fields.Float(digits=(6, 0), string="加工不良數量3")
    m_loss_num3 = fields.Float(digits=(6, 0), string="來料短少數量3")
    prod_uom3 = fields.Char(string="單位3", default='PCS')
    line_memo3 = fields.Char(string="說明3")
    item4 = fields.Integer(string="ITEM4")
    prod_no4 = fields.Many2one('product.product',string="料號4")
    m_ng_num4 = fields.Float(digits=(6, 0), string="材料不良數量4")
    p_ng_num4 = fields.Float(digits=(6, 0), string="加工不良數量4")
    m_loss_num4 = fields.Float(digits=(6, 0), string="來料短少數量4")
    prod_uom4 = fields.Char(string="單位4", default='PCS')
    line_memo4 = fields.Char(string="說明4")
    item5 = fields.Integer(string="ITEM5")
    prod_no5 = fields.Many2one('product.product',string="料號5")
    m_ng_num5 = fields.Float(digits=(6, 0), string="材料不良數量5")
    p_ng_num5 = fields.Float(digits=(6, 0), string="加工不良數量5")
    m_loss_num5 = fields.Float(digits=(6, 0), string="來料短少數量5")
    prod_uom5 = fields.Char(string="單位5", default='PCS')
    line_memo5 = fields.Char(string="說明5")


class ghreturnselect(models.Model):
    _name = "alldo_gh_iot.ngreturn_select"
    _description = "NG退回數據選單主檔"
    _rec_name = "report_date"

    report_date = fields.Date(string="印表日期",default=fields.Date.today())
    partner_id = fields.Many2one('res.partner',string="客戶")
    select_line = fields.One2many('alldo_gh_iot.ngreturn_selectitem','select_id')

    def run_gen_ngreturn(self):
        self.env.cr.execute("""delete from alldo_gh_iot_ngreturn_report""")
        self.env.cr.execute("""commit""")
        myrec = self.env['alldo_gh_iot.ngreturn_report']
        myname = self.env['ir.sequence'].next_by_code('alldo_gh_iot.return_ng')
        myrec.create({'partner_id': self.partner_id.id, 'report_date': self.report_date, 'name': myname})
        self.env.cr.execute("""select gennewngreturn('%s')""" % myname)
        self.env.cr.execute("""commit""")
        # if self.report_type == '1':  # 新單
        #     self.env.cr.execute("""select ckngreturn(%d)""" % self.partner_id.id)
        #     myres = self.env.cr.fetchone()[0]
        #     if myres:

        #         self.env.cr.execute("""select gennewngreturn(%d)""" % self.partner_id.id)
        #         self.env.cr.execute("""commit""")
        #     else:
        #         raise UserError("目前沒有新單可供列印！")
        # else:  # 舊單
        #     self.env.cr.execute("""select genoldngreturn('%s')""" % (self.report_no))
        #     self.env.cr.execute("""commit""")

        myrec = self.env['alldo_gh_iot.ngreturn_report'].search([])
        for rec in myrec:
            myid = rec.id

        myviewid = self.env.ref('alldo_gh_iot.ngreturn_report_action')
        return {'view_name': 'ngreturn_report_action',
                'name': (u'NG return Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_gh_iot.ngreturn_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                'view_mode': 'form',
                'view_type': 'form',
                }



class ghngreturnselectitem(models.Model):
    _name = "alldo_gh_iot.ngreturn_selectitem"
    _description = "NG退回數據選單明細"
    _order = "product_no,qc_date desc"

    select_id = fields.Many2one('alldo_gh_iot.ngreturn_select',ondelete='cascade')
    name = fields.Char(string="工單號碼")
    cus_name = fields.Many2one('res.partner',string="客戶")
    product_no = fields.Many2one('product.product',string="產品")
    qc_date = fields.Date(string="質檢日期")
    material_ng_num = fields.Float(string="材料不良",default=0)
    processing_ng_num = fields.Float(string="加工不良",default=0)
    loss_num = fields.Float(string="來料短少",default=0)
    line_memo = fields.Char(string="說明")
    report_no = fields.Char(string="NG退料單號")
    selectyn = fields.Boolean(string="選",default=False)
    qcid = fields.Integer(string="workorder qc id")

    def run_selectyn(self):
        for rec in self:
            if rec.selectyn==False:
                rec.update({'selectyn':True})
            else:
                rec.update({'selectyn':False})




