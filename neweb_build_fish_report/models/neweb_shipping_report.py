# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request
import pytz

class newebshippingreport(models.Model):
    _inherit = "stock.picking"

    def custom_report(self):
        stockinlines = []
        stockoutlines=[]
        nitem=1
        for item in self.stockin_line:
            stockinlines.append(
                {"stockinitem": nitem,
                 "stockinmachinetype": item.stockin_machinetype if item.stockin_machinetype else ' ',
                 "stockinmodeltype": item.stockin_modeltype if  item.stockin_modeltype else ' ',
                 "stockinprodno": item.stockin_prodno if item.stockin_prodno else ' ',
                 "stockinspec": item.stockin_spec if item.stockin_spec else ' ',
                 'stockindesc': item.stockin_desc if item.stockin_desc else ' ',
                 "stockinserial": item.stockin_serial if item.stockin_serial else ' ',
                 "stockinnum": item.stockin_num1 if item.stockin_num1 else ' ',
                 })
            nitem = nitem + 1
        nitem1 = 1
        for item1 in self.stockship_line:
            stockoutlines.append(
                {"stockshipitem": nitem1,
                 "stockshipmodeltype": item1.stockship_modeltype if item1.stockship_modeltype else ' ',
                 "stockshipspec": item1.stockship_spec if item1.stockship_spec else ' ',
                 "stockshipdesc": item1.stockship_desc if item1.stockship_desc else ' ',
                 "stockshipnum": round(item1.stockship_num) if item1.stockship_num else ' ',
                 "prodserial" : item1.prod_serial if item1.prod_serial else ' ',

                })
            nitem1 = nitem1 + 1
        if not self.origin:
            myorigin = ' '
        else:
            myorigin = self.origin
        if not self.partner_id:
            mypartnername=' '
        else:
            mypartnername = self.partner_id.name
        if not self.stockin_type:
            mystockintype = ' '
        else:
            mystockintype = self.stockin_type
        if not self.scheduled_date:
            myscheduleddate = ' '
        else:
            myscheduleddate = self.scheduled_date
        if not self.stockin_checkman:
            mystockincheckman = ' '
        else:
            mystockincheckman = self.stockin_checkman.name
        if not self.stockout_proj_no:
            mystockprojno = ' '
        else:
            mystockprojno = self.stockout_proj_no
        if not self.stockout_customer1:
            mystockoutcusname = ' '
        else:
            mystockoutcusname = self.stockout_customer1.name
        if not self.stockout_shipaddr:
            mystockoutaddr = ' '
        else:
            mystockoutaddr = self.stockout_shipaddr
        if not self.stockout_type:
            mystockouttype = ' '
        else:
            mystockouttype = self.stockout_type
        if not self.neweb_user_id:
            myusername = ' '
        else:
            myusername = self.neweb_user_id.employee_ids.resource_id.name

        if not self.neweb_phone:
            myphone = ' '
        else:
            myphone = self.neweb_phone
        if not self.neweb_email:
            myemail = ' '
        else:
            myemail = self.neweb_email
        if not self.neweb_outmemo:
            myoutmemo = ' '
        else:
            myoutmemo = self.neweb_outmemo
        if not self.neweb_address:
            myaddress = ' '
        else:
            myaddress = self.neweb_address
        if not self.neweb_fax:
            myfax= ' '
        else:
            myfax = self.neweb_fax
        if not self.stockout_custel:
            mycustel = ' '
        else:
            mycustel = self.stockout_custel
        values = {"stockin_line": stockinlines,
                  "stockship_line":stockoutlines,
                  "origin" : myorigin,                     # 採購單號  bf
                  "partnername": mypartnername,            # 進貨廠商 / 客戶名稱  bf
                  "stockintype": mystockintype,            # 進貨原因  bf
                  "scheduleddate": myscheduleddate,        # 進貨日期 / 出貨日期  bf
                  "stockincheckman" : mystockincheckman,   # 檢測工程師
                  "stockoutprojno" : mystockprojno,        # 專案編號
                  "stockoutcusname" : mystockoutcusname,   # 聯絡人
                  "stockoutcustel" : mycustel,             # 聯絡人電話
                  "stockoutshipaddr" : mystockoutaddr,     # 送貨地址
                  "stockouttype" : mystockouttype,         # 出貨原因
                  "newebusername" : myusername,            # NEWEB聯絡人
                  "newebphone" : myphone,                  # NEWEB電話
                  "newebemail" : myemail,                  # NEWEB EMAIL
                  "neweboutmemo" : myoutmemo,              # NEWEB 出貨備註
                  "newebaddress" : myaddress,              # NEWEB 地址
                  "newebfax" : myfax,                      # NEWEB FAX
                  }
        return values

    def action_print_shipping(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_shipping_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }



