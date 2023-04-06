# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class ReportSaleOrder1(models.AbstractModel):
    _name = 'report.alldo_gh_iot.alldo_gh_iot_wkorder_report1'

    @api.model
    def _get_report_values(self, docids, data=None):
        # print(docids)
        self.env.cr.execute("""delete from alldo_gh_iot_wkorder_selectitem1""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""insert into alldo_gh_iot_wkorder_selectitem1(report_owner) values (%d)""" % self.env.uid)
        self.env.cr.execute("""commit""")
        wkrec=[]
        for docid in docids:
            self.env.cr.execute("""select getgroupmo(%d)""" % docid)
            myres = self.env.cr.fetchall()
            for rec in myres:
                wkrec.append(rec[0])
        wkrec=list(dict.fromkeys(wkrec))
        for rec in wkrec:
            self.env.cr.execute("""select genwkorderreport1(%d,%d)""" % (self.env.uid,rec))
            self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genselectitemreport1()""")
        self.env.cr.execute("""commit""")
        docs = self.env['alldo_gh_iot.wkorder_printsheet1'].search([])
        #print(docs)
        res_doc = []
        for line in docs:
            if line.productdesc:
                myproductdesc = line.productdesc.replace("\n", "\\n").replace("<","(").replace(">",")")
            else:
                myproductdesc = ' '
            temp = {
                'productno': line.product_no,
                'productdesc': myproductdesc,
                'ordernum': line.order_num,
                'blank_num': line.blank_num,
                'blankinputdate' : line.blank_input_date,
                'shippingdate': line.shipping_date,
                'wkname1': line.wk_name1,
                'wkname2': line.wk_name2,
                'wkname3': line.wk_name3,
                'wkname4': line.wk_name4,
                'wkname5': line.wk_name5,
                'wkname6': line.wk_name6,
                'wkname7': line.wk_name7,
                'wkname8': line.wk_name8,
            }
            res_doc.append(temp)

        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_gh_iot.wkorder_printsheet1',
            'docs': res_doc,
        }
        return docargs


