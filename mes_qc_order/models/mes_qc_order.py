# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)

from odoo import fields, models


class MesFqcOrder(models.Model):
    _name = 'mes.fqc.order'
    _rec_name = 'name'
    _order = 'name desc, id desc'
    _description = 'For Manufacture Flow Quality Control Order'

    name = fields.Char(string='FQC質檢單號', default='New', required=True, track_visibility='onchange', track_sequence=3,
                       copy=False)
    date = fields.Datetime(string=u'質檢日期', index=True, default=fields.Date.context_today)
    mo_number = fields.Char(string=u'生產單號')
    qc_prod_no = fields.Char(string=u'產品料號')
    qc_lot_number = fields.Char(string=u'質檢批號')
    qc_barcode_ids = fields.One2many('mes.fqc.barcodeline', 'fqc_id', string='Barcode Lines')
    qc_pic_ids = fields.One2many('mes.fqc.picline', 'fqc_id', string='Pic Lines')
    cam_pic_1 = fields.Char(string='產線拍照檔一')
    cam_pic_2 = fields.Char(string='產線拍照檔二')
    cam_pic_3 = fields.Char(string='產線拍照檔三')


class MesFqcBarCodeLine(models.Model):
    _name = 'mes.fqc.barcodeline'
    _description = "MES FQC BARCODE 項目表"

    _order = "sequence,id"

    fqc_id = fields.Many2one('mes.fqc.order', ondelete='cascade')
    sequence = fields.Integer(string="SEQ", default=10)
    barcode_seq = fields.Integer(string=u"品檢刷碼順序")
    barcode_name = fields.Char(string="BARCODE說明")
    barcode_context = fields.Char(string=u'條碼內容')


class MesFqcPicLine(models.Model):
    _name = 'mes.fqc.picline'
    _description = "MES QC PICTURE 項目表-For 流水號拍照"
    _order = "sequence,id"

    fqc_id = fields.Many2one('mes.fqc.order', ondelete='cascade')
    sequence = fields.Integer(string="SEQ", default=10)
    pic_seq = fields.Integer(string="品檢照相順序")
    pic_name = fields.Char(string="照相說明")
    pic_context = fields.Char(string='照像內容')
