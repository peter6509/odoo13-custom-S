# -*- coding: utf-8 -*-
# Author : Peter Wu




from odoo import models, api


class Reportoutsourcingreport(models.AbstractModel):
    _name = 'report.alldo_acme_iot.outsourcing_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        res_doc = []
        outsourcing_doc = []
        docs=self.env['alldo_acme_iot.outsuborder'].search([('id','in',docids)])
        self.env.cr.execute("select genlastoutsuborder(%d)" % docs.id)
        self.env.cr.execute("commit")
        for line1 in docs.prodout_line:
            if not line1.out_good_num:
                myprodnum = 0
            else:
                myprodnum = line1.out_good_num
            self.env.cr.execute("select getsuborderprod(%d,'%s')" % (line1.product_no.id,docs.eng_type))
            myproddesc = self.env.cr.fetchone()[0]
            temp = {
               'prodoutdatetime': line1.prodout_datetime,
               # 'productno': "["+ line1.product_no.default_code +"]" + line1.product_no.name,
                'productno': myproddesc,
               'productname': line1.product_no.name,
               'prodnum': myprodnum,
               'produom': 'pcs',
               'outdesc': line1.out_desc,
               'prodprice': 0,
               'subtotal':0,
            }
            outsourcing_doc.append(temp)
        if not docs.outsuborder_memo:
            mymemo = ' '
        else:
            mymemo = docs.outsuborder_memo.replace('\n','\\n').replace('\r','')
        temp1 = {
            'name': docs.name,
            'purchaseno': docs.purchase_no.name,
            'cusname': docs.cus_name.name,
            'cusaddress': docs.cus_name.street,
            'cuscontract': ' ',
            'custel': docs.cus_name.phone,
            'blanknum': docs.blank_num,
            'lastblanknum': docs.last_blank_num,
            'outplasticframe1':docs.out_plastic_frame1,
            'outplasticframe2': docs.out_plastic_frame2,
            'outpallet': docs.out_pallet,
            'outmemo' : mymemo,
            'outsourcing_line': outsourcing_doc,
            'ordernum': docs.order_num,
        }
        res_doc.append(temp1)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_acme_iot.outsuborder',
            'docs': res_doc,
        }
        return docargs


