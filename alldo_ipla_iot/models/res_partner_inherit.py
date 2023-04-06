# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class alldorespartnerinherit(models.Model):
    _inherit = "res.partner"

    outsourcing_out_line = fields.One2many('alldo_acme_iot.partner_prodout','partner_id',string="委外供應商加工給料記錄")
    outsourcing_in_line = fields.One2many('alldo_acme_iot.partner_prodin','partner_id',string="委外供應商加工回廠記錄")
    partner_code = fields.Char(string="客戶編號")
    fax = fields.Char(string="傳真")
    blank_stock_supplier = fields.Many2one('stock.location',string="委外加工倉")

    def name_get(self):
        result = []
        for record in self:
            result.append(
                (record.id, '[%s]%s' % (record.partner_code, record.name)))
        return result

    @api.model
    def create(self,vals):

        res = super(alldorespartnerinherit, self).create(vals)
        self.env.cr.execute("""select gensuploc(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res



class partneroutprodin(models.Model):
    _name = "alldo_acme_iot.partner_prodin"
    _description = "委外入庫記錄明細"

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    prodin_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="產品")
    in_good_num = fields.Float(digits=(10, 2), string="良品數量", default=0.00)
    in_ng_num = fields.Float(digits=(10, 2), string="NG數量", default=0.00)
    process_num = fields.Float(digits=(10, 2), string="目前已加工數", default=0.00)
    in_stock_num = fields.Float(digits=(10,2),string="已入庫數量", default=0.00)
    in_loc = fields.Char(string="說明")
    in_owner = fields.Many2one('res.users', string="建檔人員")

class partneroutprodout(models.Model):
    _name = "alldo_acme_iot.partner_prodout"
    _description = "委外加工給料記錄明細"

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    prodout_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="產品")
    out_good_num = fields.Float(digits=(10, 2), string="給料數量", default=0.00)
    out_ng_num = fields.Float(digits=(10, 2), string="給料NG數量", default=0.00)
    out_loc = fields.Char(string="說明")
    out_owner = fields.Many2one('res.users', string="建檔人員")
    out_return_date = fields.Date(string="交期")
    out_memo = fields.Text(string="備註")
    report_date = fields.Date(string="製表日期")
    report_no = fields.Char(string="託工單號")