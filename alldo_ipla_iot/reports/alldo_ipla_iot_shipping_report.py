# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api

class Reportstockshippingreport(models.AbstractModel):
    _name = 'report.alldo_ipla_iot.stockpicking_report'
    _description = "銷(出)貨單"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_ipla_iot.stockpicking_report'].search([])
        # print(docs)
        res_doc = []
        shipping_doc = []
        for line1 in docs:
            for line in line1.report_line:
                reportno = line1.name
                shippingdate = line1.report_date
                iplaaddress = line1.partner_id.street
                iplatel = line1.partner_id.phone
                iplafax = line1.partner_id.fax
                iplamemo = line1.report_memo
                iplatotuntaxamount = line1.tot_untax_amount
                iplatottaxamount = line1.tot_tax_amount
                iplatotamount = line1.tot_amount
                partnername = line1.partner_id.name
                partnertel = line1.partner_id.phone
                partnervat = line1.partner_id.vat

                if line.prod_num==0:
                    proditem =' '
                    prodno=' '
                    prodnum=' '
                    produom=' '
                    prodprice=' '
                    sumprice=' '
                    linememo = ' '
                else:
                    proditem = line.item
                    prodno = '['+line.prod_no.default_code + ']'+line.prod_no.name
                    prodnum = line.prod_num
                    produom='PCS'
                    prodprice = '0'
                    sumprice = '0'
                    if not line.line_memo:
                        linememo = ' '
                    else:
                        linememo = line.line_memo
                temp = {
                    'report_no':reportno ,
                    'shipping_date':shippingdate,
                    'ipla_address':iplaaddress,
                    'ipla_tel':iplatel,
                    'ipla_fax':iplafax,
                    'ipla_memo': iplamemo,
                    'ipla_totuntaxamount':iplatotuntaxamount,
                    'ipla_tottaxamount':iplatottaxamount,
                    'ipla_totamount':iplatotamount,
                    'partner_name':partnername,
                    'partner_tel':partnertel,
                    'partner_vat':partnervat,
                    'prod_item':proditem,
                    'prod_no':prodno,
                    'prod_num':prodnum,
                    'prod_uom':produom,
                    'prod_price':prodprice,
                    'sum_price':sumprice,
                    'line_memo':linememo,
                }

                shipping_doc.append(temp)
            temp1 = {
                'shippingno': line1.name,
                'reportmemo': line1.report_memo,
                'shipping_line': shipping_doc,
            }
            res_doc.append(temp1)
        docargs = {


            'doc_ids': docids,
            'doc_model': 'alldo_ipla_iot.stockpicking_report',
            'docs': res_doc,
        }
        return docargs


