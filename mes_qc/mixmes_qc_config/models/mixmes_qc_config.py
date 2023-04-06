# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError


class mixmesqcconfig(models.Model):
    _name = "mixmes_qc_config.qc_setup"
    _description = "MES QC基礎設定檔"
    _rec_name = "prod_no"

    prod_no = fields.Char(string="產品料號", required=True)
    prod_desc = fields.Char(string="產品說明")
    barcode_num = fields.Integer(string="BARCODE項數", compute='_get_barcodenum')
    pic_num = fields.Integer(string="PICTURE項數", compute='_get_picnum')
    barcode_ids = fields.One2many('mixmes_qc_config.barcode_line', 'qc_id', string="BARCODE line")
    pic_ids = fields.One2many('mixmes_qc_config.pic_line', 'qc_id', string="PICTURE Line")

    def name_get(self):
        res = []
        for rec in self:
            myname = "[%s]%s" % (rec.prod_no, rec.prod_desc)
            res += [(rec.id, myname)]
        return res

    @api.depends('barcode_ids')
    def _get_barcodenum(self):
        nitem = 0
        for rec in self.barcode_ids:
            nitem = nitem + 1
        self.barcode_num = nitem

    @api.depends('pic_ids')
    def _get_picnum(self):
        nitem = 0
        for rec in self.pic_ids:
            nitem = nitem + 1
        self.pic_num = nitem

    @api.model
    def create(self, vals):

        res = super(mixmesqcconfig, self).create(vals)
        self.env.cr.execute("""select setqcconfigitem(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def _write(self, vals):

        res = super(mixmesqcconfig, self)._write(vals)
        for rec in self:
            self.env.cr.execute("""select setqcconfigitem(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return


class mixmesqcconfigbarcodeline(models.Model):
    _name = "mixmes_qc_config.barcode_line"
    _description = "MES QC BARCODE配置表"
    _order = "sequence,id"

    qc_id = fields.Many2one('mixmes_qc_config.qc_setup', ondelete='cascade')
    sequence = fields.Integer(string="SEQ", default=10)
    barcode_seq = fields.Integer(string="品檢刷碼順序")
    barcode_name = fields.Char(string="BARCODE說明")

    @api.model
    def create(self, vals):
        if 'barcode_name' in vals and vals['barcode_name']:
            myres = self.env['mixmes_qc_config.barcode_line'].search_count([('barcode_name','=',vals['barcode_name'])])
            if myres > 1:
                raise UserError("BARCODE說明已重複！")
        res = super(mixmesqcconfigbarcodeline, self).create(vals)
        return res




class mixmesqcconfigpicline(models.Model):
    _name = "mixmes_qc_config.pic_line"
    _description = "MES QC PICTURE配置表"
    _order = "sequence,id"

    qc_id = fields.Many2one('mixmes_qc_config.qc_setup', ondelete='cascade')
    sequence = fields.Integer(string="SEQ", default=10)
    pic_seq = fields.Integer(string="品檢照相順序")
    pic_name = fields.Char(string="照相說明")

    @api.model
    def create(self, vals):
        if 'pic_name' in vals and vals['pic_name']:
            myres = self.env['mixmes_qc_config.pic_line'].search_count([('pic_name','=',vals['pic_name'])])
            if myres > 1:
                raise UserError("照片說明已重複！")
        res = super(mixmesqcconfigpicline, self).create(vals)
        return res


