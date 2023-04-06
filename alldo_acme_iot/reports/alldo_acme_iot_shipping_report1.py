# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api

class Reportstockshippingreport1(models.AbstractModel):
    _name = 'report.alldo_acme_iot.stockpicking_report1'
    _description = "銷貨單"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_acme_iot.stockpicking_report1'].search([])
        # print(docs)
        res_doc = []
        shipping_doc = []
        for line1 in docs:
            for line in line1.report_line:
                taiinv = line1.taiwan_receipt
                reportno = line1.name
                shippingdate = line1.report_date
                if not line1.partner_id.street:
                    acmeaddress = ' '
                else:
                    acmeaddress = line1.partner_id.street.replace('\n','\\n').replace('\r','')
                acmetel = line1.partner_id.phone
                acmefax = line1.partner_id.fax
                if not line1.report_memo:
                    acmememo = ' '
                else:
                    acmememo = line1.report_memo.replace('\n','\\n').replace('\r','')
                acmetotuntaxamount = line1.tot_untax_amount
                acmetottaxamount = line1.tot_tax_amount
                acmetotamount = line1.tot_amount
                partnername = line1.partner_id.name
                partnertel = line1.partner_id.phone
                partnervat = line1.partner_id.vat
                reporttype = '銷貨單'
                if line.prod_num==0:
                    proditem =' '
                    prodno=' '
                    prodnum=0
                    produom=' '
                    prodprice=0
                    sumprice=' '
                    linememo = ' '
                else:
                    proditem = line.item
                    prodno = '['+line.prod_no.default_code + ']'+line.prod_no.name
                    prodnum = line.prod_num
                    produom= line.prod_uom
                    prodprice = line.prod_price
                    sumprice = line.sum_price
                    if not line.line_memo:
                        linememo = ' '
                    else:
                        linememo = line.line_memo
                temp = {
                    'reporttype': '應收帳款明細表',
                    'report_no':reportno ,
                    'shipping_date':shippingdate,
                    'acme_address':acmeaddress,
                    'acme_tel':acmetel,
                    'acme_fax':acmefax,
                    'acme_memo': acmememo,
                    'acme_totuntaxamount':acmetotuntaxamount,
                    'acme_tottaxamount':acmetottaxamount,
                    'acme_totamount':acmetotamount,
                    'partner_name':partnername,
                    'partner_tel':partnertel,
                    'partner_vat':partnervat,
                    'prod_item':proditem,
                    'prod_no':prodno,
                    'prod_num':prodnum,
                    'prod_uom':produom,
                    'prod_price':prodprice,
                    'sum_price':(prodnum * prodprice),
                    'line_memo':linememo,
                }

                shipping_doc.append(temp)
            temp1 = {
                'reporttype':'應收帳款明細表',
                'taiwan_receipt': taiinv,
                'shippingno': line1.name,
                'reportmemo': line1.report_memo,
                'shipping_line': shipping_doc,
            }
            res_doc.append(temp1)
        docargs = {


            'doc_ids': docids,
            'doc_model': 'alldo_acme_iot.stockpicking_report1',
            'docs': res_doc,
        }
        return docargs


