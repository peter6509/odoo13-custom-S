# -*- coding: utf-8 -*-
# Author : Peter Wu




from odoo import models, api


class Reportoutsourcingreport(models.AbstractModel):
    _name = 'report.alldo_ipla_iot.outsourcing_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_ipla_iot.outsourcing_report'].search([])
        # print(docids)
        # print(docs)
        res_doc = []
        outsourcing_doc = []
        mypartner = ' '
        for line1 in docs:
            reportno = line1.name
            outsourcingdate = line1.report_date
            jhaddress = '桃園市楊梅區行善路32巷16號'
            jhtel = '03-4757712'
            jhfax = '03-4757701'
            jhmemo = line1.report_memo
            partnername = line1.partner_id.name
            partnertel = line1.partner_id.phone
            partnervat = line1.partner_id.vat
            for line in line1.report_line:
                if line.prod_num == 0 :
                    proditem =' '
                    prodno=' '
                    prodnum=' '
                    produom = ' '
                    linememo = ' '
                    outreturndate = ' '
                else:
                    proditem = line.item
                    prodno = line.prod_no.name
                    prodnum = line.prod_num
                    produom = 'PCS'
                    if not line.line_memo:
                        linememo = ' '
                    else:
                        linememo = line.line_memo
                    outreturndate = line.out_return_date
                if line.prod_num1 == 0 :
                    proditem1 =' '
                    prodno1=' '
                    prodnum1=' '
                    produom1 = ' '
                    linememo1 = ' '
                    outreturndate1 = ' '
                else:
                    proditem1 = line.item1
                    prodno1 = line.prod_no1.name
                    prodnum1 = line.prod_num1
                    produom1 = 'PCS'
                    if not line.line_memo1:
                        linememo1 = ' '
                    else:
                        linememo1 = line.line_memo1
                    outreturndate1 = line.out_return_date1
                if line.prod_num2 == 0 :
                    proditem2 =' '
                    prodno2 =' '
                    prodnum2 =' '
                    produom2 = ' '
                    linememo2 = ' '
                    outreturndate2 = ' '
                else:
                    proditem2 = line.item2
                    prodno2 = line.prod_no2.name
                    prodnum2 = line.prod_num2
                    produom2 = 'PCS'
                    if not line.line_memo2:
                        linememo2 = ' '
                    else:
                        linememo2 = line.line_memo2
                    outreturndate2 = line.out_return_date2
                if line.prod_num3 == 0 :
                    proditem3 =' '
                    prodno3 =' '
                    prodnum3 =' '
                    produom3 = ' '
                    linememo3 = ' '
                    outreturndate3 = ' '
                else:
                    proditem3 = line.item3
                    prodno3 = line.prod_no3.name
                    prodnum3= line.prod_num3
                    produom3 = 'PCS'
                    if not line.line_memo3:
                        linememo3 = ' '
                    else:
                        linememo3 = line.line_memo3
                    outreturndate3 = line.out_return_date3
                if line.prod_num4 == 0 :
                    proditem4 =' '
                    prodno4 =' '
                    prodnum4 =' '
                    produom4 = ' '
                    linememo4 = ' '
                    outreturndate4 = ' '
                else:
                    proditem4 = line.item4
                    prodno4 = line.prod_no4.name
                    prodnum4 = line.prod_num4
                    produom4 = 'PCS'
                    if not line.line_memo4:
                        linememo4 = ' '
                    else:
                        linememo4 = line.line_memo4
                    outreturndate4 = line.out_return_date4

                temp = {
                    'report_no':reportno ,
                    'jh_address':jhaddress,
                    'jh_tel':jhtel,
                    'jh_fax':jhfax,
                    'jh_memo': jhmemo,
                    'partner_name':partnername,
                    'partner_tel':partnertel,
                    'partner_vat':partnervat,
                    'prod_item':proditem,
                    'prod_no':prodno,
                    'prod_num':prodnum,
                    'prod_uom':produom,
                    'line_memo':linememo,
                    'out_return_date':outreturndate,
                    'prod_item1': proditem1,
                    'prod_no1': prodno1,
                    'prod_num1': prodnum1,
                    'prod_uom1': produom1,
                    'line_memo1': linememo1,
                    'out_return_date1': outreturndate1,
                    'prod_item2': proditem2,
                    'prod_no2': prodno2,
                    'prod_num2': prodnum2,
                    'prod_uom2': produom2,
                    'line_memo2': linememo2,
                    'out_return_date2': outreturndate2,
                    'prod_item3': proditem3,
                    'prod_no3': prodno3,
                    'prod_num3': prodnum3,
                    'prod_uom3': produom3,
                    'line_memo3': linememo3,
                    'out_return_date3': outreturndate3,
                    'prod_item4': proditem4,
                    'prod_no4': prodno4,
                    'prod_num4': prodnum4,
                    'prod_uom4': produom4,
                    'line_memo4': linememo4,
                    'out_return_date4': outreturndate4,
                }

                outsourcing_doc.append(temp)
            temp1 = {
                'outsourcingno': line1.name,
                'outsourcingdate' : line1.report_date,
                'reportmemo': line1.report_memo,
                'outsourcing_line': outsourcing_doc,
            }
        if mypartner != partnername:
            res_doc.append(temp1)
            mypartner = partnername
        # print(res_doc)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_ipla_iot.outsourcing_report',
            'docs': res_doc,
        }
        return docargs


