# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class alldoaccountmovereport(models.AbstractModel):
    _name ="report.alldo_acme_iot.alldo_acme_iot_accountmove_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        # print(docids)
        # self.env.cr.execute("""delete from alldo_acme_iot_accountmove_selectitem ;""")
        # self.env.cr.execute("""commit""")
        # for rec in docids:
        #     self.env.cr.execute("""select genaccountmovereport(%d,%d)""" % (self.env.uid, rec))
        #     self.env.cr.execute("""commit""")
        docs = self.env['alldo_acme_iot.accountmove_selectitem'].search([])
        # print(docs)
        res_doc = []
        for line in docs:
            line_ids=[]
            for line1 in line.account_move_line:
                temp1 = {'accountdate' : line1.account_date,
                        'salesno' : line1.sales_no,
                        'ref' : line1.ref,
                        'prodno' : line1.prod_no.default_code,
                        'proddesc' : line1.prod_no.name,
                        'prodnum' : line1.prod_num,
                        'prodprice' : line1.prod_price,
                        'amountuntaxnum' : line1.amount_untax_num,
                        }
                line_ids.append(temp1)

            temp = {
                'reportno': line.name,
                'reportdate': line.report_date,
                'partnername' : line.partner_id.name,
                'contractname' : line.contract_man.name,
                'contracttel' : line.contract_tel,
                'startenddate': line.startenddate,
                'amountuntaxtotal' : line.amount_untax_total,
                'amounttax' : line.amount_tax,
                'amounttaxtotal' : line.amount_tax_total,
                'vat' : line.partner_id.vat,
                'selectitem_line' : line_ids,
                'amountbalance' : line.amount_balance,
                'totalrealamount' : line.total_real_amount,
                'taiwanreceipt': line.taiwan_receipt,

            }
            res_doc.append(temp)

        docargs = {
            'doc_ids': docids,
            'doc_model': 'alldo_acme_iot_accountmove_selectitem',
            'docs': res_doc,
        }
        return docargs