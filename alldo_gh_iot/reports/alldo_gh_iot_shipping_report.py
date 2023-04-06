# -*- coding: utf-8 -*-
# Author : Peter Wu




from odoo import models, api


class Reportstockshippingreport(models.AbstractModel):
    _name = 'report.alldo_gh_iot.stockpicking_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_gh_iot.stockpicking_report'].search([])
        # print(docs)
        res_doc = []
        shipping_doc = []
        for line1 in docs:
            for line in line1.report_line:
                reportno = line1.name
                shippingdate = line1.report_date
                jhaddress = '桃園市楊梅區行善路32巷16號'
                jhtel = '03-4757712'
                jhfax = '03-4757701'
                jhmemo = line1.report_memo
                jhtotuntaxamount = line1.tot_untax_amount
                jhtottaxamount = line1.tot_tax_amount
                jhtotamount = line1.tot_amount
                jhtottaxamount= '0'
                jhtotuntaxamount= '0'
                jhtotamount= '0'
                partnername = line1.partner_id.name
                partnertel = line1.partner_id.phone
                partnervat = line1.partner_id.vat

                if line.prod_num==0:
                    # continue
                    proditem =' '
                    prodno=' '
                    prodnum=' '
                    produom=' '
                    prodprice=' '
                    sumprice=' '
                    linememo = ' '
                else:
                    proditem = line.item
                    prodno = line.prod_no.default_code
                    prodnum = line.prod_num
                    produom='PCS'
                    prodprice = '0'
                    sumprice = '0'
                    if not line.line_memo:
                        linememo = ' '
                    else:
                        linememo = line.line_memo
                if line.prod_num1==0:
                    proditem1 =' '
                    prodno1=' '
                    prodnum1=' '
                    produom1=' '
                    prodprice1=' '
                    sumprice1=' '
                    linememo1 = ' '
                else:
                    proditem1 = line.item1
                    prodno1 = line.prod_no1.default_code
                    prodnum1 = line.prod_num1
                    produom1 ='PCS'
                    prodprice1 = '0'
                    sumprice1 = '0'
                    if not line.line_memo1:
                        linememo1 = ' '
                    else:
                        linememo1 = line.line_memo1
                if line.prod_num2==0:
                    proditem2 =' '
                    prodno2 =' '
                    prodnum2 =' '
                    produom2 =' '
                    prodprice2 =' '
                    sumprice2 =' '
                    linememo2 = ' '
                else:
                    proditem2 = line.item2
                    prodno2 = line.prod_no2.default_code
                    prodnum2 = line.prod_num2
                    produom2 ='PCS'
                    prodprice2 = '0'
                    sumprice2 = '0'
                    if not line.line_memo2:
                        linememo2 = ' '
                    else:
                        linememo2 = line.line_memo2
                if line.prod_num3==0:
                    proditem3 =' '
                    prodno3 =' '
                    prodnum3 =' '
                    produom3 =' '
                    prodprice3 =' '
                    sumprice3 =' '
                    linememo3 = ' '
                else:
                    proditem3 = line.item3
                    prodno3 = line.prod_no3.default_code
                    prodnum3 = line.prod_num3
                    produom3 ='PCS'
                    prodprice3 = '0'
                    sumprice3 = '0'
                    if not line.line_memo3:
                        linememo3 = ' '
                    else:
                        linememo3 = line.line_memo3
                if line.prod_num4==0:
                    proditem4 =' '
                    prodno4 =' '
                    prodnum4 =' '
                    produom4 =' '
                    prodprice4 =' '
                    sumprice4 =' '
                    linememo4 = ' '
                else:
                    proditem4 = line.item4
                    prodno4 = line.prod_no4.default_code
                    prodnum4 = line.prod_num4
                    produom4 ='PCS'
                    prodprice4 = '0'
                    sumprice4 = '0'
                    if not line.line_memo4:
                        linememo4 = ' '
                    else:
                        linememo4 = line.line_memo4



                temp = {
                    'report_no':reportno ,
                    'shipping_date':shippingdate,
                    'jh_address':jhaddress,
                    'jh_tel':jhtel,
                    'jh_fax':jhfax,
                    'jh_memo': jhmemo,
                    'jh_totuntaxamount':jhtotuntaxamount,
                    'jh_tottaxamount':jhtottaxamount,
                    'jh_totamount':jhtotamount,
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
                    'prod_item1': proditem1,
                    'prod_no1': prodno1,
                    'prod_num1': prodnum1,
                    'prod_uom1': produom1,
                    'prod_price1': prodprice1,
                    'sum_price1': sumprice1,
                    'line_memo1': linememo1,
                    'prod_item2': proditem2,
                    'prod_no2': prodno2,
                    'prod_num2': prodnum2,
                    'prod_uom2': produom2,
                    'prod_price2': prodprice2,
                    'sum_price2': sumprice2,
                    'line_memo2': linememo2,
                    'prod_item3': proditem3,
                    'prod_no3': prodno3,
                    'prod_num3': prodnum3,
                    'prod_uom3': produom3,
                    'prod_price3': prodprice3,
                    'sum_price3': sumprice3,
                    'line_memo3': linememo3,
                    'prod_item4': proditem4,
                    'prod_no4': prodno4,
                    'prod_num4': prodnum4,
                    'prod_uom4': produom4,
                    'prod_price4': prodprice4,
                    'sum_price4': sumprice4,
                    'line_memo4': linememo4,
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
            'doc_model': 'alldo_gh_iot.stockpicking_report',
            'docs': res_doc,
        }
        return docargs


