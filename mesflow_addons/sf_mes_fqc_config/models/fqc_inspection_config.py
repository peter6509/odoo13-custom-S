# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError


class FqcProductCheckItem(models.Model):
    _name = 'fqc.product.check.item'
    _rec_name = 'name'
    _description = 'MES 檢驗項目名稱'

    name = fields.Char(string='檢驗項目名稱')


class FqcProductCheckDoc(models.Model):
    _name = 'fqc.product.check.doc'
    _rec_name = 'name'
    _description = 'MES 檢驗規格說明'

    name = fields.Char(string='檢驗規格說明')


class FqcSetupCheckList(models.Model):
    _name = "fqc.setup.check.list"
    _description = "FQC 質檢檢驗項目規格說明"
    _order = "sequence, id"

    qc_id = fields.Many2one('qc.setup', ondelete='cascade')
    sequence = fields.Integer(string="SEQ", default=10)
    check_item = fields.Many2one('fqc.product.check.item', string="檢驗項目名稱",)
    check_item_doc = fields.Many2one('fqc.product.check.doc', string="檢驗規格說明",)


class mixmesqcconfig(models.Model):
    _inherit = "qc.setup"

    check_list_ids = fields.One2many('fqc.setup.check.list', 'qc_id', string='檢驗項目規格說明')


class MesFqcOrder(models.Model):
    _inherit = "mes.fqc.order"

    check_list_ids = fields.One2many('mes.fqc.check.list', 'fqc_id', string='檢驗項目規格說明')


class MesFqcCheckList(models.Model):
    _name = "mes.fqc.check.list"
    _description = "FQC 質檢檢驗項目規格說明"
    _order = "sequence, id"

    fqc_id = fields.Many2one('mes.fqc.order', ondelete='cascade')
    sequence = fields.Integer(string="SEQ", default=10)
    check_item = fields.Many2one('fqc.product.check.item', string="檢驗項目名稱", )
    check_item_doc = fields.Many2one('fqc.product.check.doc', string="檢驗規格說明", )
