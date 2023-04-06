# -*- coding: utf-8 -*-
# Author : Peter Wu


from datetime import datetime
from odoo import models,fields,api

class GhPurchaseOrderInherit2(models.Model):
    _inherit = "purchase.order"

    def custom_report(self):
        puritem = []
        for item in self.order_line:
            if item.product_id :
                self.env.cr.execute("""select getoldesc(%d)""" % item.id)
                ol_desc = self.env.cr.fetchone()[0]
                puritem.append(
                    {"prodname": item.product_id.default_code if item.product_id.default_code else ' ',
                     "prodmaterial": item.prod_material if item.prod_material else ' ',
                     "prodspec": item.prod_spec if item.prod_spec else ' ',
                     "prodqty": int(item.product_qty),
                     "produom": item.product_uom.name if item.product_uom else ' ',
                     "dateplanned": item.date_planned.strftime('%Y-%m-%d'),
                     "prodprice": '{:,d}'.format(int(item.price_unit)),
                     "pricesubtotal": '{:,d}'.format(int(item.product_qty * item.price_unit)),
                     "proddeliver": item.prod_deliver if item.prod_deliver else ' ',
                     "oldesc": ol_desc,
                     })

        partnername = self.partner_id.name
        if self.state=='purchase':
            date_approve = self.date_approve.strftime('%Y-%m-%d')
        else:
            date_approve = self.date_order.strftime('%Y-%m-%d')
        mynowdate = self.create_date.strftime('%Y-%m-%d')
        amountuntaxed1 = '{:,d}'.format(int(self.amount_untaxed))
        amounttax1 = '{:,d}'.format(int(self.amount_tax))
        amounttotal1 = '{:,d}'.format(int(self.amount_total))
        values = {"order1_line": puritem,
                  "dateapprove": date_approve,
                  "amountuntaxed": amountuntaxed1,
                  "amounttax": amounttax1,
                  "amounttotal": amounttotal1,
                  "nowdate": mynowdate,
                  }
        return values
