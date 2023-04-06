# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request

class newebbfcustomdata(models.Model):
    _inherit = "neweb.project"

    @api.depends('proj_sale')
    def _get_projsalename(self):
        for rec in self:
            if rec.proj_sale :
                myprojsalename = rec.proj_sale.name
            else:
                myprojsalename = ' '
            rec.projsalename = myprojsalename
            return myprojsalename

    @api.depends('cus_name')
    def _get_projcusname(self):
        for rec in self:
            if rec.cus_name:
                myprojcusname = rec.cus_name.name
            else:
                myprojcusname = ' '
            rec.projcusname = myprojcusname
            return myprojcusname

    @api.depends('main_cus_name')
    def _get_maincusname(self):
        for rec in self:
            if rec.main_cus_name:
                mymaincusname = rec.main_cus_name.name
            else:
                mymaincusname = ' '
            rec.maincusname = mymaincusname
            return mymaincusname

    @api.depends('cus_name')
    def _get_creditrulelist(self):
        for rec in self:
            if rec.cus_name.credit_rulelist:
                mycreditrulelist = rec.cus_name.credit_rulelist
            else:
                mycreditrulelist = ' '
            rec.creditrulelist = mycreditrulelist
            return mycreditrulelist

    @api.depends('acc_receivable')
    def _get_accrec1(self):
        for rec in self:
            if rec.acc_receivable == '2':
                myaccrec1 = True
            else:
                myaccrec1 = False
            rec.is_accrec1 = myaccrec1
            return myaccrec1

    @api.depends('acc_receivable')
    def _get_accrec2(self):
        for rec in self:
            if rec.acc_receivable=='3':
                myaccrec2=True
            else:
                myaccrec2=False
            rec.is_accrec2=myaccrec2
            return myaccrec2

    @api.depends('acc_receivable')
    def _get_accrec3(self):
        for rec in self:
            if rec.acc_receivable == '4':
                myaccrec3 = True
            else:
                myaccrec3 = False
            rec.is_accrec3 = myaccrec3
            return myaccrec3

    @api.depends('self_receive_type','acc_receivable')
    def _get_accrec4(self):
        for rec in self:
            if rec.self_receive_type == '1' and rec.acc_receivable not in ('2','3','4'):
                myaccrec4 = True
            else:
                myaccrec4 = False
            rec.is_accrec4 = myaccrec4
            return myaccrec4

    @api.depends('self_rece_stamp')
    def _get_stamp1(self):
        for rec in self:
            if rec.self_rece_stamp=='1':
                mystamp1 = True
            else:
                mystamp1 = False
            rec.is_stamp1 = mystamp1
            return mystamp1

    @api.depends('self_rece_stamp')
    def _get_stamp2(self):
        for rec in self:
            if rec.self_rece_stamp == '2':
                mystamp2 = True
            else:
                mystamp2 = False
            rec.is_stamp2 = mystamp2
            return mystamp2

    @api.depends('self_rece_stamp')
    def _get_stamp3(self):
        for rec in self:
            if rec.self_rece_stamp == '3':
                mystamp3 = True
            else:
                mystamp3 = False
            rec.is_stamp3 = mystamp3
            return mystamp3

    @api.depends('self_rece_stamp')
    def _get_stamp4(self):
        for rec in self:
            if rec.self_rece_stamp == '4':
                mystamp4 = True
            else:
                mystamp4 = False
            rec.is_stamp4 = mystamp4
            return mystamp4



    projsalename = fields.Char(string="專案業務",compute=_get_projsalename)
    projcusname = fields.Char(string="客戶名稱",compute=_get_projcusname)
    maincusname = fields.Char(string="維護客戶名稱",compute=_get_maincusname)
    creditrulelist = fields.Char(string="信用條件",compute=_get_creditrulelist)
    is_accrec1 = fields.Boolean(string="IS郵寄",compute=_get_accrec1)
    is_accrec2 = fields.Boolean(string="IS電匯", compute=_get_accrec2)
    is_accrec3 = fields.Boolean(string="IS親領",compute=_get_accrec3)
    is_accrec4 = fields.Boolean(string="IS現金",compute=_get_accrec4)
    is_stamp1 = fields.Boolean(string="IS無",compute=_get_stamp1)
    is_stamp2 = fields.Boolean(string="IS收款章", compute=_get_stamp2)
    is_stamp3 = fields.Boolean(string="IS發票章", compute=_get_stamp3)
    is_stamp4 = fields.Boolean(string="IS大小章", compute=_get_stamp4)

    def action_print_custom_data(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_custom_data_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }


class newebbfprojcontact(models.Model):
    _inherit = "neweb.projcontact"


    @api.depends('contact_type')
    def _get_contacttypename(self):
        for rec in self:
            if rec.contact_type:
                mycontacttypename = rec.contact_type.name
            else:
                mycontacttypename = ' '
            rec.contacttypename = mycontacttypename
            return mycontacttypename

    @api.depends('contact_name')
    def _get_contactname(self):
        for rec in self:
            if rec.contact_name:
               mycontactnname = rec.contact_name.name
            else:
               mycontactnname = ' '
            rec.contactname = mycontactnname
            return mycontactnname

    contacttypename = fields.Char(string="人員別",compute=_get_contacttypename)
    contactname = fields.Char(string="姓名",compute=_get_contactname)
