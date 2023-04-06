# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError

class stockpickinginherit(models.Model):
    _inherit = "stock.picking"

    mo_group_id = fields.Integer(string="工單群組ID")
    report_date = fields.Date(string="製表日期")
    report_no = fields.Char(string="JH出貨單號",copy=False)
    report_memo = fields.Text(string="JH MEMO",copy=False)
    shipping_update_wkorder = fields.Boolean(default=False)

    def write(self, vals):
        res = super(stockpickinginherit, self).write(vals)
        for rec in self:
            # self.env.cr.execute("""select gennewshippingno(%d)""" % rec.id)
            # self.env.cr.execute("""commit""")
            if rec.state=='done':
                self.env.cr.execute("""select updateshippingwkorder(%d)""" % rec.id)
                self.env.cr.execute("""commit""")
        return res

    def run_newshipping_report(self):
        # self.env.cr.execute("""delete from alldo_gh_iot_stockpicking_report""")
        # self.env.cr.execute("""commit""")
        self.env.cr.execute("""update stock_picking set report_no=null where id=%d""" % self.id)
        self.env.cr.execute("""commit""")

        # self.env.cr.execute("""select gennewshippingno(%d)""" % self.id)
        # myreportno = self.env.cr.fetchone()[0]
        #
        # self.env.cr.execute("""select genoldshipping('%s')""" % myreportno)
        # self.env.cr.execute("""commit""")
        # myrec = self.env['alldo_gh_iot.stockpicking_report'].search([])
        # myid = myrec[0].id
        # myviewid = self.env.ref('alldo_gh_iot.gh_iot_shipping_report_action')
        # return {'view_name': 'gh_iot_shipping_report_action',
        #         'name': (u'employee info  item Data'),
        #         'views': [[False, 'form']],
        #         'res_model': 'alldo_gh_iot.stockpicking_report',
        #         'context': self._context,
        #         'type': 'ir.actions.act_window',
        #         'res_id': myid,
        #         'target': 'current',
        #         'view_id': myviewid.id,
        #         'view_mode': 'form',
        #         'view_type': 'form'
        #         }

    def run_shipping_report(self):
        self.env.cr.execute("""delete from alldo_ipla_iot_stockpicking_report""")
        self.env.cr.execute("""commit""")
        if not self.report_no:
            self.env.cr.execute("""select gennewshippingno(%d)""" % self.id)
            myreportno = self.env.cr.fetchone()[0]
        else:
            myreportno = self.report_no

        # print('%s' % myreportno)
        # 舊單
        self.env.cr.execute("""select genoldshipping('%s')""" % myreportno)
        self.env.cr.execute("""commit""")
        myrec = self.env['alldo_ipla_iot.stockpicking_report'].search([])
        myid = myrec[0].id
        myviewid = self.env.ref('alldo_ipla_iot.gh_iot_shipping_report_action')
        return {'view_name': 'ipla_iot_shipping_report_action',
                'name': (u'employee info  item Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_ipla_iot.stockpicking_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                'view_mode': 'form',
                'view_type': 'form'
                }







class stockpickingreportdata(models.Model):
    _name = "alldo_ipla_iot.stockpicking_report"

    partner_id = fields.Many2one('res.partner',string="客戶")
    name = fields.Char(string="出貨單號",default=lambda self: _('New'))
    report_date = fields.Date(string="出貨日期")
    picking_id = fields.Many2one('stock.picking',string="PICKING ID")
    report_line = fields.One2many('alldo_ipla_iot.stockpicking_report_line','rep_id',copy=False)
    tot_untax_amount = fields.Float(digits=(9,0),string="出貨總價",compute="_get_totuntaxamount")
    tot_tax_amount = fields.Float(digits=(7,0),string="稅金",compute="_get_tottaxamount")
    tot_amount = fields.Float(digits=(10,0),string="合計總和",compute="_get_totamount")
    report_memo = fields.Char(string="備註")

    @api.depends('report_line')
    def _get_totuntaxamount(self):
        myuntaxamount=0
        for rec in self.report_line:
            myuntaxamount = myuntaxamount + (rec.prod_num * rec.prod_price) + (rec.prod_num1 * rec.prod_price1) + (rec.prod_num2 * rec.prod_price2) + (rec.prod_num3 * rec.prod_price3) + (rec.prod_num4 * rec.prod_price4) + (rec.prod_num5 * rec.prod_price5)
        self.tot_untax_amount = myuntaxamount
        return myuntaxamount

    @api.depends('report_line')
    def _get_tottaxamount(self):
        myuntaxamount = 0
        for rec in self.report_line:
            myuntaxamount = myuntaxamount + (rec.prod_num * rec.prod_price) + (rec.prod_num1 * rec.prod_price1) + (
                        rec.prod_num2 * rec.prod_price2) + (rec.prod_num3 * rec.prod_price3) + (
                                        rec.prod_num4 * rec.prod_price4) + (rec.prod_num5 * rec.prod_price5)
        mytaxamount = round((myuntaxamount * .05),0) ;
        self.tot_tax_amount = mytaxamount
        return myuntaxamount

    @api.depends('tot_untax_amount','tot_tax_amount')
    def _get_totamount(self):
        for rec in self:
            rec.tot_amount = rec.tot_untax_amount + rec.tot_tax_amount


    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('alldo_gh_iot.shipping') or _('New')
    #     res = super(stockpickingreportdata, self).create(vals)
    #     return res


class stockpickingreportline(models.Model):
    _name = "alldo_ipla_iot.stockpicking_report_line"

    rep_id = fields.Many2one('alldo_ipla_iot.stockpicking_report',ondelete='cascade')
    item = fields.Integer(string="ITEM")
    prod_no = fields.Many2one('product.product',string="料號")
    prod_num = fields.Float(digits=(6,0),string="數量")
    prod_uom = fields.Char(string="單位",default='PCS')
    prod_price = fields.Float(digits=(8,0),string="單價")
    sum_price = fields.Float(digits=(9,0),string="金額合計")
    line_memo = fields.Char(string="說明")
    item1 = fields.Integer(string="ITEM1")
    prod_no1 = fields.Many2one('product.product',string="料號1")
    prod_num1 = fields.Float(digits=(6, 0), string="數量1")
    prod_uom1 = fields.Char(string="單位1", default='PCS')
    prod_price1 = fields.Float(digits=(8, 0), string="單價1")
    sum_price1 = fields.Float(digits=(9, 0), string="金額合計1")
    line_memo1 = fields.Char(string="說明1")
    item2 = fields.Integer(string="ITEM2")
    prod_no2 = fields.Many2one('product.product',string="料號2")
    prod_num2 = fields.Float(digits=(6, 0), string="數量2")
    prod_uom2 = fields.Char(string="單位2", default='PCS')
    prod_price2 = fields.Float(digits=(8, 0), string="單價2")
    sum_price2 = fields.Float(digits=(9, 0), string="金額合計2")
    line_memo2 = fields.Char(string="說明2")
    item3 = fields.Integer(string="ITEM3")
    prod_no3 = fields.Many2one('product.product',string="料號3")
    prod_num3 = fields.Float(digits=(6, 0), string="數量3")
    prod_uom3 = fields.Char(string="單位3", default='PCS')
    prod_price3 = fields.Float(digits=(8, 0), string="單價3")
    sum_price3 = fields.Float(digits=(9, 0), string="金額合計3")
    line_memo3 = fields.Char(string="說明3")
    item4 = fields.Integer(string="ITEM4")
    prod_no4 = fields.Many2one('product.product',string="料號4")
    prod_num4 = fields.Float(digits=(6, 0), string="數量4")
    prod_uom4 = fields.Char(string="單位4", default='PCS')
    prod_price4 = fields.Float(digits=(8, 0), string="單價4")
    sum_price4 = fields.Float(digits=(9, 0), string="金額合計4")
    line_memo4 = fields.Char(string="說明4")
    item5 = fields.Integer(string="ITEM5")
    prod_no5 = fields.Many2one('product.product',string="料號5")
    prod_num5 = fields.Float(digits=(6, 0), string="數量5")
    prod_uom5 = fields.Char(string="單位5", default='PCS')
    prod_price5 = fields.Float(digits=(8, 0), string="單價5")
    sum_price5 = fields.Float(digits=(9, 0), string="金額合計5")
    line_memo5 = fields.Char(string="說明5")