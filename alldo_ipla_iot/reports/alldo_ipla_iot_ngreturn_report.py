# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class Reportngreturnreport(models.AbstractModel):
    _name = 'report.alldo_ipla_iot.ngreturn_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['alldo_ipla_iot.ngreturn_report'].search([])
        # print(docs)
        res_doc = []
        ngreturn_doc = []
        for line1 in docs:
            for line in line1.report_line:
                reportno = line1.name
                ngreturndate = line1.report_date
                iplaaddress = '桃園市楊梅區行善路32巷16號'
                iplatel = '03-4757712'
                iplafax = '03-4757701'
                iplamemo = line1.report_memo
                partnername = line1.partner_id.name
                partnertel = line1.partner_id.phone
                partnervat = line1.partner_id.vat

                if line.m_ng_num == 0 and line.p_ng_num == 0:
                    proditem =' '
                    prodno=' '
                    mngnum=' '
                    pngnum=' '
                    produom = ' '
                    linememo = ' '
                    mpngnum = ' '
                else:
                    proditem = line.item
                    prodno = line.prod_no.name
                    mngnum = line.m_ng_num
                    pngnum = line.p_ng_num
                    mpngnum = line.m_ng_num + line.p_ng_num
                    produom = 'PCS'
                    if not line.line_memo:
                        linememo = ' '
                    else:
                        linememo = line.line_memo
                if line.m_ng_num1 == 0 and line.p_ng_num1 == 0:
                    proditem1 =' '
                    prodno1=' '
                    mngnum1=' '
                    pngnum1=' '
                    produom1 = ' '
                    linememo1 = ' '
                    mpngnum1 = ' '
                else:
                    proditem1 = line.item1
                    prodno1 = line.prod_no1.name
                    mngnum1 = line.m_ng_num1
                    pngnum1 = line.p_ng_num1
                    mpngnum1 = line.m_ng_num1 + line.p_ng_num1
                    produom1 = 'PCS'
                    if not line.line_memo1:
                        linememo1 = ' '
                    else:
                        linememo1 = line.line_memo1
                if line.m_ng_num2 == 0 and line.p_ng_num2 == 0:
                    proditem2 =' '
                    prodno2 =' '
                    mngnum2 =' '
                    pngnum2 =' '
                    produom2 = ' '
                    linememo2 = ' '
                    mpngnum2 = ' '
                else:
                    proditem2 = line.item2
                    prodno2 = line.prod_no2.name
                    mngnum2 = line.m_ng_num2
                    pngnum2 = line.p_ng_num2
                    mpngnum2 = line.m_ng_num2 + line.p_ng_num2
                    produom2 = 'PCS'
                    if not line.line_memo2:
                        linememo2 = ' '
                    else:
                        linememo2 = line.line_memo2
                if line.m_ng_num3 == 0 and line.p_ng_num3 == 0:
                    proditem3 =' '
                    prodno3=' '
                    mngnum3=' '
                    pngnum3=' '
                    produom3 = ' '
                    linememo3 = ' '
                    mpngnum3 = ' '
                else:
                    proditem3 = line.item3
                    prodno3 = line.prod_no3.name
                    mngnum3 = line.m_ng_num3
                    pngnum3 = line.p_ng_num3
                    mpngnum3 = line.m_ng_num3 + line.p_ng_num3
                    produom3 = 'PCS'
                    if not line.line_memo3:
                        linememo3 = ' '
                    else:
                        linememo3 = line.line_memo3
                if line.m_ng_num4 == 0 and line.p_ng_num4 == 0:
                    proditem4 =' '
                    prodno4 =' '
                    mngnum4 =' '
                    pngnum4 =' '
                    produom4 = ' '
                    linememo4 = ' '
                    mpngnum4 = ' '
                else:
                    proditem4 = line.item4
                    prodno4 = line.prod_no4.name
                    mngnum4 = line.m_ng_num4
                    pngnum4 = line.p_ng_num4
                    mpngnum4 = line.m_ng_num4 + line.p_ng_num4
                    produom4 = 'PCS'
                    if not line.line_memo4:
                        linememo4 = ' '
                    else:
                        linememo4 = line.line_memo4

                temp = {
                    'report_no':reportno ,
                    'ngreturn_date':ngreturndate,
                    'ipla_address':iplaaddress,
                    'ipla_tel':iplatel,
                    'ipla_fax':iplafax,
                    'ipla_memo': iplamemo,
                    'partner_name':partnername,
                    'partner_tel':partnertel,
                    'partner_vat':partnervat,
                    'prod_item':proditem,
                    'prod_no':prodno,
                    'm_ng_num':mngnum,
                    'p_ng_num':pngnum,
                    'mp_ng_num' :mpngnum,
                    'prod_uom':produom,
                    'line_memo':linememo,
                    'prod_item1': proditem1,
                    'prod_no1': prodno1,
                    'm_ng_num1':mngnum1,
                    'p_ng_num1':pngnum1,
                    'mp_ng_num1':mpngnum1,
                    'prod_uom1': produom1,
                    'line_memo1': linememo1,
                    'prod_item2': proditem2,
                    'prod_no2': prodno2,
                    'm_ng_num2':mngnum2,
                    'p_ng_num2':pngnum2,
                    'mp_ng_num2':mpngnum2,
                    'prod_uom2': produom2,
                    'line_memo2': linememo2,
                    'prod_item3': proditem3,
                    'prod_no3': prodno3,
                    'm_ng_num3':mngnum3,
                    'p_ng_num3':pngnum3,
                    'mp_ng_num3':mpngnum3,
                    'prod_uom3': produom3,
                    'line_memo3': linememo3,
                    'prod_item4': proditem4,
                    'prod_no4': prodno4,
                    'm_ng_num4':mngnum4,
                    'p_ng_num4':pngnum4,
                    'mp_ng_num4':mpngnum4,
                    'prod_uom4': produom4,
                    'line_memo4': linememo4,
                }

                ngreturn_doc.append(temp)
            temp1 = {
                'ngreturnno': line1.name,
                'ngreturnmemo': line1.report_memo,
                'ngreturn_line': ngreturn_doc,
            }
            res_doc.append(temp1)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_ipla_iot.ngreturn_report',
            'docs': res_doc,
        }
        return docargs


