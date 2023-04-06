# -*- coding: utf-8 -*-
# Author : Peter Wu




from odoo import models, api


class Reportoutsourcingreport2(models.AbstractModel):
    _name = 'report.alldo_acme_iot.outsourcing_report2'

    @api.model
    def _get_report_values(self, docids, data=None):
        res_doc = []
        outsourcing_doc = []
        docs=self.env['alldo_acme_iot.outsuborder'].search([('id','in',docids)])
        self.env.cr.execute("select genlastoutsuborder(%d)" % docs.id)
        self.env.cr.execute("commit")
        for line1 in docs.prodout_line:
            if line1.last_record:
                if not line1.out_good_num:
                    myprodnum = 0
                else:
                    myprodnum = line1.out_good_num
                self.env.cr.execute("select getsuborderprod(%d,'%s')" % (line1.product_no.id,docs.eng_type))
                myproddesc = self.env.cr.fetchone()[0]
                temp = {
                   'prodoutdatetime':  ' ',
                   # 'productno': "["+ line1.product_no.default_code +"]" + line1.product_no.name,
                    'productno': ' ',
                   'productname': ' ',
                   'prodnum': ' ',
                   'produom': ' ',
                   'outdesc': ' ',
                   'prodprice': ' ',
                   'subtotal': ' ',
                }
                outsourcing_doc.append(temp)
        if not docs.outsuborder_memo:
            mymemo = ' '
        else:
            mymemo = docs.outsuborder_memo.replace('\n','\\n').replace('\r','')
        temp1 = {
            'name': ' ',
            'purchaseno': ' ',
            'cusname': ' ',
            'cusaddress':  ' ',
            'cuscontract': ' ',
            'custel': ' ',
            'blanknum':  ' ',
            'lastblanknum': ' ',
            'outplasticframe1':' ',
            'outplasticframe2': ' ',
            'outpallet': ' ',
            'outmemo' : ' ',
            'outsourcing_line':  ' ',
            'ordernum': ' ',
        }
        res_doc.append(temp1)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_acme_iot.outsuborder',
            'docs': res_doc,
        }
        return docargs


