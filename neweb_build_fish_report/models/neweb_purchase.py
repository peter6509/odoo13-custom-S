# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request
import pytz

class newebpurchasereport(models.Model):
    _inherit = "purchase.order"

    @api.depends('name')
    def _get_ename(self):
        myename=' '
        for rec in self:
            myename = rec.name[2:]
            rec.ename = myename
            return myename

    @api.depends('partner_contact')
    def _get_contact(self):
        mycontact=' '
        for rec in self:
            if not rec.partner_contact.name:
                mycontact=' '
            else:
                mycontact = rec.partner_contact.name
            rec.ccontact = mycontact
            return mycontact

    @api.depends('partner_id')
    def _get_phone(self):
        myphone= ' '
        for rec in self:
            if not rec.partner_id.phone:
                myphone= ' '
            else:
                myphone = rec.partner_id.phone
            rec.cphone = myphone
            return myphone

    @api.depends('partner_id')
    def _get_fax(self):
        myfax = ' '
        for rec in self:
            if not rec.partner_id.fax:
                myfax = ' '
            else:
                myfax = rec.partner_id.fax
            rec.cfax = myfax
            return myfax

    ename = fields.Char(string="P/O",compute=_get_ename)
    ccontact = fields.Char(string="contact",compute=_get_contact)
    cphone = fields.Char(string="phone",compute=_get_phone)
    cfax = fields.Char(string="FAX",compute=_get_fax)

    def action_purchase_taiwan_print(self):
        self.ensure_one()
        # obj_precision = self.env['decimal.precision']
        # prec = obj_precision.precision_get('Neweb Price')
        # lang = self._context.get('lang')
        # record_lang = self.env['res.lang'].search([('code', '=', lang)], limit=1)
        # strftime_format = "%s %s" % (record_lang.date_format, record_lang.time_format)
        # user_tz = pytz.timezone(self.env.get('tz') or self.env.user.tz or 'UTC')
        # #
        # values = {
        #           "symbol": self.currency_id.symbol,
        #           }
        # return values
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_purchase_taiwan_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

    def action_purchase_english_print(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_purchase_english_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }
