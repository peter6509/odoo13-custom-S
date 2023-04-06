# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp


class alldosaleinherit(models.Model):
    _inherit = "sale.order"
    _description = "銷售主檔"

    display_line = fields.One2many('alldo_sale.sitem_list', 'sitem_id', copy=True, string=u"明細資料")
    attach_line = fields.One2many('alldo_sale.attach_line','attach_id',copy=False,string=u"附件資料夾")
    sitem_untax = fields.Float(digits=(9,0), string=u"合計",
                               compute='_amount_untax', track_visibility='always')
    sitem_tax = fields.Float(digits=(5,0), string=u"營業稅",
                             compute='_amount_tax', track_visibility='always')
    sitem_amounttot = fields.Float(digits=(10,0), string=u"總價",
                                   compute='_amount_all', track_visibility='always')
    taxes_id = fields.Many2one('account.tax', string='Taxes',
                               domain=['|', ('active', '=', False), ('active', '=', True),
                                       ('type_tax_use', '=', 'sale')],
                               default=lambda self: self.env['account.tax'].search(
                                   [('type_tax_use', '=', 'sale')], limit=1))

    discount_amount = fields.Float(digits=(10, 0), string=u"優惠價(未税)")

    create_tag = fields.Boolean(strggg="創建新單記號",default=True)

    quotation_term = fields.Integer(string=u"有效天數", default=30)
    mobile_phone = fields.Char(string=u"行動電話")
    work_phone = fields.Char(string=u"工作電話")
    contact_id = fields.Many2one('res.partner', string=u"客戶聯絡人")
    quotation_memo = fields.Text(string=u"備註")
    is_discount = fields.Char(string="有優惠？",compute='_get_isdiscount')
    contact_id = fields.Many2one('res.partner',string="聯絡人")

    @api.onchange('partner_id')
    def onchange_partnerid(self):
        if self.partner_id:
            myrec = self.env['res.partner'].search([('parent_id', '=', self.partner_id.id)])
            ids = []
            for item in myrec:
                ids.append(item.id)
            res = {}
            res['domain'] = {'contact_id': [('id', 'in', ids)]}
            return res

    @api.depends('discount_amount','sitem_untax')
    def _get_isdiscount(self):
        for rec in self:
            if rec.discount_amount == rec.sitem_untax:
                rec.update({'is_discount':'N'})
            else:
                rec.update({'is_discount':'Y'})


    @api.model
    def create(self,vals):
        vals['create_tag']=False
        # if  not vals['contact_id']:
        #     raise UserError("未輸入聯絡人資訊")
        res = super(alldosaleinherit, self).create(vals)
        self.env.cr.execute("""update sale_order set create_tag=False where id=%d""" % res.id)
        self.env.cr.execute("""commit""")

        return res

    @api.depends('sitem_untax')
    def _get_amounttot(self):
        for order in self:
            if order.create_tag:
                order.update({'discount_amount': order.sitem_untax})

    @api.depends( 'display_line.sitem_num', 'display_line.sitem_price')
    def _amount_untax(self):
        for order in self:
            amount_untaxed = 0.0
            for line in order.display_line:
                amount_untaxed = amount_untaxed + (line.sitem_num * line.sitem_price)
            order.update({'sitem_untax' : amount_untaxed})
            # print(order.create_tag)
            if order.create_tag :
                order.update({'discount_amount': amount_untaxed})

    @api.depends('sitem_untax')
    def _amount_tax(self):
        for order in self:
            order.update({'sitem_tax' : (order.discount_amount * 0.05)})


    @api.depends('sitem_untax','sitem_tax')
    def _amount_all(self):

        """
        Compute the total amounts of the SO.
        """
        for order in self:
            order.update({'sitem_amounttot' : order.discount_amount + order.sitem_tax})

    @api.model
    def create(self, vals):
        rec = super(alldosaleinherit, self).create(vals)
        genprodid = self.env.ref('alldo_sale.alldo_sale_2')
        myrec = self.env['sale.order'].search([('id', '=', rec.id)])
        mysitemrec = self.env['alldo_sale.sitem_list'].search([('sitem_id', '=', rec.id)])

        if mysitemrec:
            mytaxesid = myrec.taxes_id
            # print mytaxesid
            myownerid = self.sudo().env.uid
            saleid = rec.id
            myprodid = genprodid.id
            self.env.cr.execute("select gensaleline(%s,%s,%s,%s);" % (myownerid, saleid, myprodid, mytaxesid.id))
            self.env.cr.execute("commit;")
            self.env.cr.execute("select setsaleitem(%d);" % rec.id)
            self.env.cr.execute("commit;")
        return rec


    def _write(self, vals):
        rec = super(alldosaleinherit, self)._write(vals)
        saleid = self.id
        # raise UserError("%s" % purid)
        genprodid = self.env.ref('alldo_sale.alldo_sale_2')
        myownerid = self.env.uid
        myprodid = genprodid.id
        myrec = self.env['sale.order'].search([('id', '=', saleid)])
        mytaxesid = myrec.taxes_id
        mysitemrec = self.env['alldo_sale.sitem_list'].search([('sitem_id', '=', saleid)])
        if mysitemrec:
            self.env.cr.execute("select gensaleline(%s,%s,%s,%s);" % (myownerid, saleid, myprodid, mytaxesid.id))
            self.env.cr.execute("commit;")
            self.env.cr.execute("select setsaleitem(%d);" % saleid)
            self.env.cr.execute("commit;")
            # self.env.cr.execute("select gensaletaxesid(%s);" % saleid)
        return rec



class alldosalesitemlist(models.Model):
    _name = "alldo_sale.sitem_list"
    _description = u'銷售明細檔'
    _order = "sitem_id,sequence,id"

    sitem_item = fields.Integer(string="項次")
    sitem_id = fields.Many2one('sale.order', required=True, ondelete='cascade')
    sitem_desc = fields.Text(string=u"規格說明")
    sitem_num = fields.Float(digits=(6,1), string=u"數量",default=1)
    sitem_unit = fields.Many2one('uom.uom',string="單位")
    sitem_price = fields.Float(digits=(8,0), string=u"優惠單價",default=0)
    sitem_subtotprice = fields.Float(digits=(9,0),string="小計",compute='_get_subtot',store=True)
    sitem_priceaddtax = fields.Float(digits=(9,0), string=u"含税優惠單價", compute='_get_addtax',store=True)
    sitem_cost = fields.Float(digits=(8,0), string=u"成本單價",default=0)
    sitem_costsubtot = fields.Float(digits=(9,0), string=u"成本＊數量", store=True,
                                    readonly=True, compute='_amount_all')
    sitem_profit = fields.Float(digits=(9,0), string=u"毛利", store=True, readonly=True,
                                compute='_amount_all')
    sitem_profitrate = fields.Float(digits=(5, 2), string=u"毛利率", store=True, readonly=True, compute='_amount_all')
    sale_no = fields.Char(related='sitem_id.name', string=u"銷售單號")
    sequence = fields.Integer(string="ITEM",default=10)


    @api.depends('sitem_num','sitem_price')
    def _get_subtot(self):
        for rec in self:
            rec.sitem_subtotprice = rec.sitem_num * rec.sitem_price

    @api.depends('sitem_price')
    def _get_addtax(self):
        for rec in self:
            rec.sitem_priceaddtax = rec.sitem_price * 1.05
            # rec.update({'sitem_priceaddtax': (rec.sitem_price * 1.05)})



    @api.depends('sitem_num', 'sitem_cost', 'sitem_price')
    def _amount_all(self):
        for sitem in self:
            amountcosttot = sitem.sitem_num * sitem.sitem_cost
            amountpricetot = sitem.sitem_num * sitem.sitem_price
            if amountpricetot == 0:
                amountprofitrate = 0
                sitem.update({'sitem_costsubtot': amountcosttot,
                              'sitem_profit': 0,
                              'sitem_profitrate': amountprofitrate})
            else:
                amountprofitrate = (amountpricetot - amountcosttot) / amountpricetot
                sitem.update({'sitem_costsubtot': amountcosttot,
                              'sitem_profit': amountpricetot - amountcosttot,
                              'sitem_profitrate': amountprofitrate})



class alldosaleattachline(models.Model):
    _name = "alldo_sale.attach_line"
    _description = u'銷售附件資料夾'
    _order = "attach_id,sequence,id"

    attach_item = fields.Integer(string="項次")
    sequence = fields.Integer(string="SEQ")
    attach_desc = fields.Text(string="文件描述")
    attach_id = fields.Many2one('sale.order', required=True, ondelete='cascade')
    attach_file = fields.Binary(string="文件",attachment=True)
    attach_filename = fields.Char(string="下載")