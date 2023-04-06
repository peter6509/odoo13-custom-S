# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class acmepurchaseinherit(models.Model):
    _inherit = "purchase.order"

    def name_get(self):
        result = []

        for record in self:
            myprod = ''
            for rec in record.order_line:
                if myprod=='':
                    myprod = rec.product_id.default_code
                else:
                    if rec.product_id:
                        myprod = myprod + '/ ' + rec.product_id.default_code
            result.append(
                (record.id, '[%s]%s-(%s)' % (record.name, record.partner_id.name,myprod)))
        return result


    is_blank_stockin = fields.Boolean(string="(半成品)開委外加工單",default=False)
    update_loc =fields.Boolean(string="是否已異動半成品倉別",default=False)

    def purchase_loc_change(self):
        self.env.cr.execute("""select purchase_change_loc()""")
        self.env.cr.execute("""commit""")

    def button_confirm(self):
        for order in self:
            if order.state not in ['draft', 'sent']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step'\
                    or (order.company_id.po_double_validation == 'two_step'\
                        and order.amount_total < self.env.company.currency_id._convert(
                            order.company_id.po_double_validation_amount, order.currency_id, order.company_id, order.date_order or fields.Date.today()))\
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
            if order.is_blank_stockin == True:  # 半成品開立委外加工單
                self.env.cr.execute("""select getmogpseq()""")
                mymogpid = self.env.cr.fetchone()[0]
                myoutsuborderrec = self.env['alldo_acme_iot.outsuborder']
                for rec in order.order_line:
                    myrec = self.env['product.template'].search([('id', '=', rec.product_id.product_tmpl_id.id)])
                    myfirstid = 0
                    mysaleorderid = False
                    mycusid = False

                    myfurnaceprodid = self.env['alldo_acme_iot.company_stockloc'].search([]).furnace_prod_id.id
                    for rec1 in myrec.eng_line:
                        self.env.cr.execute("""select getprodengorder(%d,'%s')""" % (rec.product_id.id, rec1.eng_type))
                        myres = self.env.cr.fetchone()[0]
                        self.env.cr.execute("""select getprodengseq(%d,'%s')""" % (rec.product_id.id, rec1.eng_type))
                        myres1 = self.env.cr.fetchone()[0]
                        if rec1.is_outsourcing:
                            myid = myoutsuborderrec.create({
                                'product_no': rec.product_id.id,
                                'eng_type': rec1.eng_type + '-' + rec1.eng_desc,
                                'eng_order': myres,
                                'eng_seq': myres1,
                                'order_num': rec.product_qty,
                                'cus_name': rec1.partner_id.id if rec1.partner_id else False,
                                'shipping_date': order.date_planned,
                                'mo_group_id': mymogpid,
                                'outsuborder_memo': order.name + '/(入毛胚倉,自動開立委外加工單)',
                                'prodout_line': [(0, 0,
                                                  {'prodout_datetime': fields.datetime.now(),
                                                   'product_no': rec.product_id.id,
                                                   'out_good_num': 0,
                                                   'out_ng_num': 0,
                                                   'out_owner': self.env.uid})]})





        return True