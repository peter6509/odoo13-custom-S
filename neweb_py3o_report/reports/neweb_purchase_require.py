# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class py3onewebpurchaserequire(models.Model):
    _inherit = "neweb.require_purchase"


    @api.depends('asset_expense_categ')
    def _get_asset_expense_categ(self):
        for rec in self:
            if rec.asset_expense_categ=='1':
                mycassetexpensecateg = '資產類'
            else:
                mycassetexpensecateg = '費用類'
            rec.cassetexpensecateg = mycassetexpensecateg
            return mycassetexpensecateg

    @api.depends('expense_type')
    def _get_expense_type(self):
        for rec in self:
            if rec.expense_type=='1':
                mycexpensetype = 'MA零件'
            else:
                mycexpensetype = '其他'
            rec.cexpensetype = mycexpensetype
            return mycexpensetype

    @api.depends('asset_type')
    def _get_asset_type(self):
        mycassettype=''
        for rec in self:
            if rec.asset_type=='1':
                mycassettype = '辦公器材'
            elif rec.asset_type=='2':
                mycassettype = '研發/測試設備'
            elif rec.asset_type=='3':
                mycassettype = 'MA備機'
            elif rec.asset_type=='4':
                mycassettype = '未來轉銷貨'
            elif rec.asset_type=='5':
                mycassettype = '其他'
            rec.cassettype = mycassettype
            return mycassettype

    @api.depends('catalog_attach_yn')
    def _get_cata_attach_yn(self):
        for rec in self:
            if rec.catalog_attach_yn=='1':
                myccataattachyn = '是'
            else:
                myccataattachyn = '否'
            rec.ccataattachyn = myccataattachyn
            return myccataattachyn



    cassetexpensecateg = fields.Char(string="申購類別py3o",compute=_get_asset_expense_categ)
    cexpensetype = fields.Char(string="費用類別py3o",compute=_get_expense_type)
    cassettype = fields.Char(string="資產類別py3o",compute=_get_asset_type)
    ccataattachyn = fields.Char(string="報價附件py3o",compute=_get_cata_attach_yn)






