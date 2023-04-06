# -*- coding: utf-8 -*-
# Author : Peter Wu




from odoo import models, api


class Reportprodoutreport(models.AbstractModel):
    _name = 'report.alldo_acme_iot.prodout_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        res_doc = []
        prodout_doc = []
        docs=self.env['alldo_acme_iot.prodout'].search([('id','in',docids)])
        # self.env.cr.execute("select genlastoutsuborder(%d)" % docs.id)
        # self.env.cr.execute("commit")
        for line1 in docs.prodout_line:
            if not line1.out_good_num:
                myprodnum = 0
            else:
                myprodnum = line1.out_good_num
            self.env.cr.execute("select getsuborderprod(%d,'%s')" % (line1.product_no.id,line1.eng_type))
            myproddesc = self.env.cr.fetchone()[0]
            temp = {
               'prodoutdatetime': docs.prodout_date,
               'name': line1.prodout_no.name,
               'productno': myproddesc,
               'productname': line1.product_no.name,
               'prodnum': myprodnum,
               'produom': 'pcs',
               'outdesc': line1.prodout_desc,
               'prodprice': 0,
               'subtotal':0,
            }
            prodout_doc.append(temp)
        if not docs.prodout_memo:
            mymemo = ' '
        else:
            mymemo = docs.prodout_memo.replace('\n','\\n').replace('\r','')
        temp1 = {
            'purchaseno': ' ',
            'cusname': docs.partner_id.name,
            'cusaddress': docs.partner_id.street,
            'cuscontract': ' ',
            'custel': docs.partner_id.phone,
            'blanknum': 0,
            'lastblanknum': 0,
            'outplasticframe1':docs.tot_plastic_frame1,
            'outplasticframe2': docs.tot_plastic_frame2,
            'outpallet': docs.tot_pallet,
            'outmemo' : mymemo,
            'prodout_line': prodout_doc,
            'ordernum': 0,
        }
        res_doc.append(temp1)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_acme_iot.prodout',
            'docs': res_doc,
        }
        return docargs


