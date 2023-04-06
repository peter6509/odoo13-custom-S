# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class ReportSaleOrder(models.AbstractModel):
    _name = 'report.alldo_ipla_iot.alldo_ipla_iot_wkorder_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # print(docids)
        self.env.cr.execute("""delete from alldo_ipla_iot_wkorder_selectitem""")
        self.env.cr.execute("""commit""")
        wkrec=[]
        for docid in docids:
            self.env.cr.execute("""select getgroupmo(%d)""" % docid)
            myres = self.env.cr.fetchall()
            for rec in myres:
                wkrec.append(rec[0])
        wkrec = list(dict.fromkeys(wkrec))
        for rec in wkrec:
            self.env.cr.execute("""select genwkorderreport(%d,%d)""" % (self.env.uid,rec))
            self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genselectitemreport()""")
        self.env.cr.execute("""commit""")
        docs = self.env['alldo_ipla_iot.wkorder_printsheet'].search([])
        #print(docs)
        res_doc = []
        for line in docs:
            if line.workorder_memo:
                mywkordermemo = line.workorder_memo.replace("\n", "\\n")
            else:
                mywkordermemo = ' '
            temp = {
                'name': line.name,
                'productno': line.product_no,
                'productblankname': line.product_blank,
                'pono': line.po_no,
                'ordernum': line.order_num,
                'blank_num': line.blank_num,
                'blankinputdate' : line.blank_input_date,
                'engtype': line.eng_type,
                'cncprog': line.cnc_prog,
                'clampingpower': line.clamping_power,
                'standardnum': line.standard_num,
                'shippingdate': line.shipping_date,
                'ins1name': line.ins1_name,
                'ins1size': line.ins1_size,
                'ins1tolerance': line.ins1_tolerance,
                'ins1realsize': line.ins1_real_size,
                'ins1testtype': line.ins1_testtype,
                'ins1testmode': line.ins1_testmode,
                'ins2name': line.ins2_name,
                'ins2size': line.ins2_size,
                'ins2tolerance': line.ins2_tolerance,
                'ins2realsize': line.ins2_real_size,
                'ins2testtype': line.ins2_testtype,
                'ins2testmode': line.ins2_testmode,
                'ins3name': line.ins3_name,
                'ins3size': line.ins3_size,
                'ins3tolerance': line.ins3_tolerance,
                'ins3realsize': line.ins3_real_size,
                'ins3testtype': line.ins3_testtype,
                'ins3testmode': line.ins3_testmode,
                'ins4name': line.ins4_name,
                'ins4size': line.ins4_size,
                'ins4tolerance': line.ins4_tolerance,
                'ins4realsize': line.ins4_real_size,
                'ins4testtype': line.ins4_testtype,
                'ins4testmode': line.ins4_testmode,
                'ins5name': line.ins5_name,
                'ins5size': line.ins5_size,
                'ins5tolerance': line.ins5_tolerance,
                'ins5realsize': line.ins5_real_size,
                'ins5testtype': line.ins5_testtype,
                'ins5testmode': line.ins5_testmode,
                'workordermemo': mywkordermemo,
                # 'ins6name': line.ins6_name,
                # 'ins6size': line.ins6_size,
                # 'ins6tolerance': line.ins6_tolerance,
                # 'ins6realsize': line.ins6_real_size,
                # 'ins6testtype': line.ins6_testtype,
                # 'ins6testmode': line.ins6_testmode,
            }
            res_doc.append(temp)

        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_ipla_iot.wkorder_printsheet',
            'docs': res_doc,
        }
        return docargs


