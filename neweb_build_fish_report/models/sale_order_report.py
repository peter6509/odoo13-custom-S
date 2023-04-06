# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError
from odoo.http import request
import pytz

class saleorderbfreport(models.Model):
    _inherit = "sale.order"

    def custom_report(self):
        obj_precision = self.env['decimal.precision']
        prec=obj_precision.precision_get('Neweb Price')
        lang=self._context.get('lang')
        record_lang=self.env['res.lang'].search([('code','=',lang)],limit=1)
        strftime_format="%s %s" % (record_lang.date_format,record_lang.time_format)
        user_tz = pytz.timezone(self.env.get('tz') or self.env.user.tz or 'UTC')
        date_order = "- -"
        validity_date = "- -"
        if self.date_order:
            date_order_dt = pytz.UTC.localize(self.date_order).astimezone(user_tz)
            date_order = date_order_dt.strftime(strftime_format)
        if self.validity_date:
            validity_date_dt = pytz.UTC.localize(self.validity_date).astimezone(user_tz)
            validity_date = validity_date_dt.strftime(strftime_format)
        lines=[]
        for item in self.display_line:
            lines.append(
                {"sitem_item" : item.sitem_item,
                 "sitem_modeltype" : item.sitem_modeltype,
                 "sitem_desc" : item.sitem_desc,
                 "sitem_num" : int(item.sitem_num),
                 "sitem_price" : format(item.sitem_price,'.%sf' % prec),
                 'sitem_subtot': format(item.sitem_num * item.sitem_price,'.%sf' % prec),
                 "newebmaindate": item.newebmaindate
                 })
        if not self.payment_term_new:
            paymenttermname = ' '
        else:
            paymenttermname = self.payment_term_new.name

        if self.open_account_day=='1':
            myopenaccday = '30天'
        elif self.open_account_day=='2':
            myopenaccday = '45天'
        elif self.open_account_day=='3':
            myopenaccday = '60天'
        elif self.open_account_day=='4':
            myopenaccday = '90天'
        elif self.open_account_day=='5':
            myopenaccday = '120天'


        # 新版欄位 open_account_day2
        # if not self.open_account_day2:
        #     myopenaccday = self.open_account_day1.name
        # else:
        #     myopenaccday = self.open_account_day2.name

        if not self.warranty_service_rule_new:
            warrantyservicename=' '
        else:
            warrantyservicename=self.warranty_service_rule_new.name
        if not self.quotation_include:
            quotationinclude=' '
        else:
            quotationinclude = self.quotation_include.name
        deliveryterm= ' '
        if self.delivery_term=='1':
            deliveryterm = '30天'
        elif self.delivery_term=='2':
            deliveryterm = '45天'
        elif self.delivery_term=='3':
            deliveryterm = '60天'
        if not self.main_service_rule_new:
            mainservicerulename = ' '
        else:
            mainservicerulename = self.main_service_rule_new.name
        if not self.routine_maintenance_new:
            routinemaintenancename = ' '
        else:
            routinemaintenancename = self.routine_maintenance_new.name
        if not self.call_service_response1:
            callserviceresponse1 = ' '
        else:
            callserviceresponse1 = self.call_service_response1.name
        if not self.maintenance_start:
            maintenancestart = ' '
        else:
            maintenancestart = self.maintenance_start
        if not self.maintenance_end:
            maintenanceend = ' '
        else:
            maintenanceend = self.maintenance_end
        values = {"display_line": lines,
                 "partnername" : self.partner_id.name if self.partner_id.name else ' ',
                 "contactname" : self.contact_id.name if self.contact_id.name else ' ',
                 "contactphone": self.contact_id.phone if self.contact_id.phone else ' ',
                 "contactemail": self.contact_id.email if self.contact_id.email else ' ',
                 "contactstreet": self.contact_id.street if self.contact_id.street else' ',
                 "saleorderno": self.name if self.name else ' ',
                 "dateorder": self.date_order1 if self.date_order1 else ' ',
                 "workphone": self.work_phone if self.work_phone else ' ',
                 "mobilephone" : self.mobile_phone if self.mobile_phone else ' ',
                 "partnercontactname" : self.user_id.partner_id.name if self.user_id.partner_id.name else ' ',
                 "sitemuntax" : format(self.sitem_untax,'.%sf' % prec),
                 "sitemtax": format(self.sitem_tax,'.%sf' % prec),
                 "sitemamounttot": format(self.sitem_amounttot,'.%sf' % prec),
                 "discountamount":format(self.discount_amount,'.%sf' % prec),
                 "symbol": self.pricelist_id.currency_id.symbol,
                 "openaccday": self.open_account_day2.name if self.open_account_day2 else ' ',
                 "warrantyservicename": warrantyservicename,
                 "quotationinclude": quotationinclude,
                 "deliveryterm" : deliveryterm,
                 "quotationterm" : self.quotation_term if self.quotation_term else ' ',
                 "paymenttermname" : paymenttermname,
                 "mainservicerulename": mainservicerulename,
                 "routinemaintenancename" : routinemaintenancename,
                 "callserviceresponse1" : callserviceresponse1,
                 "maintenancestart": maintenancestart,
                 "maintenanceend": maintenanceend,
                 "quotationmemo": self.quotation_memo,
                 }
        return values

    def action_print_gov_sale(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_gov_sale_order/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

    def action_print_sale(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_sale_order/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

    def action_print_sale_main(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_sale_main/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }


class newebsitemline(models.Model):
    _inherit = "neweb.sitem_list"

    @api.depends('sitem_num', 'sitem_price')
    def _get_subtot(self):
        mysitemsubtot = 0
        for rec in self:
            mysitemsubtot = round(rec.sitem_num * rec.sitem_price)
            rec.sitem_subtot = mysitemsubtot
        return mysitemsubtot

    sitem_subtot = fields.Float(digits=(10, 0), string="小計", compute=_get_subtot)



