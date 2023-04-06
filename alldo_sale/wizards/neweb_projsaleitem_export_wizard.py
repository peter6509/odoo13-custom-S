# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import xlrd
import odoo.addons.decimal_precision as dp

class newebprojsaleitemexport(models.Model):
    _name = "neweb.projsaleitem_export"

    seqid = fields.Integer(string=u"項次")
    prodserial = fields.Char(string=u"項次")
    prodset = fields.Char(string=u"產品組別")
    prodbrand = fields.Char(string=u"品牌")
    prodmodeltype = fields.Char(string=u"機種-機型/料號")
    prodserial = fields.Char(string=u"序號")
    proddesc = fields.Char(string=u"規格說明")
    prodnum = fields.Float(digits=dp.get_precision('Product of Measure'), string=u"數量", default=1)
    prodprice = fields.Float(digits=dp.get_precision('Product Price'), string=u"成本")
    prodrevenue = fields.Float(digits=dp.get_precision('Product Price'), string=u"銷價")
    prodsubtot = fields.Float(digits=dp.get_precision('Product Price'), string=u"小計", store=False,
                               compute='_cal_subtot', track_visibility='always')
    supplier = fields.Char(size=20, string=u"報價廠商")
    costtype = fields.Char(string=u"成本類型")


