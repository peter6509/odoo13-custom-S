# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class ReportSaleOrder(models.AbstractModel):
    _name = 'report.alldo_acme_iot.alldo_acme_iot_wkorder_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # print(docids)
        self.env.cr.execute("""delete from alldo_acme_iot_wkorder_selectitem ;""")
        self.env.cr.execute("""commit""")
        for rec in docids:
            # print(rec)
            self.env.cr.execute("""select genwkorderreport(%d,%d)""" % (self.env.uid,rec))
            self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genselectitemreport()""")
        self.env.cr.execute("""commit""")
        docs = self.env['alldo_acme_iot.wkorder_printsheet'].search([])
        # print(docs)
        res_doc = []
        for line in docs:
            if line.workorder_memo:
                mywkordermemo = line.workorder_memo.replace("\n", "\\n").replace('/', ',')
            else:
                mywkordermemo = ' '
            temp = {
                'name': line.name,
                'productno': line.product_no,
                'cusname': line.cus_name.name.replace('(','[').replace(')',']'),
                'ordernum': line.order_num,
                'engtype': line.eng_type,
                'shippingdate': line.shipping_date,
                'workordermemo': mywkordermemo.replace('\n','\\n').replace('(','[').replace(')',']'),
                'castingblank': line.product_blank1.default_code +'('+ line.product_blank1.name+')'

            }
            res_doc.append(temp)

        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_acme_iot.wkorder_printsheet',
            'docs': res_doc,
        }
        return docargs


