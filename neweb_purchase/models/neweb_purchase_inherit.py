# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class purchasemanager(models.Model):
    _name="neweb_purchase.purchase_manager"
    _description = '採購主辦配置'

    name = fields.Many2one('hr.employee',string='採購主辦')

    @api.model
    def create(self, vals):
        if self.env['neweb_purchase.purchase_manager'].search_count([]) > 0:
           raise UserError("主辦已有資料,不能再新增了!")

        rec = super(purchasemanager, self).create(vals)
        return rec




class newebpitemlist(models.Model):
    _name = "neweb.pitem_list"
    _description = '採購明細記錄'
    _order = "pitem_litem,id"


    @api.depends('pitem_num', 'pitem_price')
    def _amount_all(self):
        for pitem in self:
            amounttot = pitem.pitem_num * pitem.pitem_price
            pitem.update({'pitem_sum': amounttot})

    @api.depends('pitem_num', 'pitem_stockin_num')
    def _get_stockin_complete(self):
        for order in self:
            if order.pitem_num == order.pitem_stockin_num and order.pitem_num > 0:
                order.update({'pitem_stockin_complete': 1})

    @api.depends('pitem_price')
    def _get_pitemprice1(self):
        for rec in self:
            mypitemprice1=round(rec.pitem_price)
            rec.pitem_price1 = mypitemprice1
            return mypitemprice1

    @api.depends('pitem_sum')
    def _get_pitemsum1(self):
        for rec in self:
            mypitemsum1 = round(rec.pitem_sum)
            rec.pitem_sum1 = mypitemsum1
            return mypitemsum1

    pitem_id = fields.Many2one('purchase.order',required=True, ondelete='cascade')
    pitem_machine_type = fields.Char(string="機種")
    pitem_model_type = fields.Char(string="機種-機型/料號")
    prod_id = fields.Many2one('product.template',string="庫存料號")
    pitem_prod_no = fields.Char(string="料號")
    pitem_spec = fields.Char(string="規格說明")
    pitem_warranty = fields.Char(string="保固期限")
    pitem_num = fields.Float(digits=(10,0),string="數量",required=True)
    pitem_price =  fields.Float(digits=(13,2),string="單價",required=True)
    pitem_price1 = fields.Float(digits=(13,0),string="bf單價",compute=_get_pitemprice1)
    pitem_sum = fields.Float(digits=(13,0),store=True, readonly=True, compute=_amount_all)
    pitem_sum1 = fields.Float(digits=(13,0),string="bf小計",compute=_get_pitemsum1)
    pitem_status = fields.Selection([('1','銷貨'),('2','維護')],string="物品狀態",default='1')
    pitem_origin_no = fields.Char(string="來源編號")
    pitem_origin_id = fields.Integer(string="來源ID")
    pitem_origin_type = fields.Char(string="來源別 'R'申購, 'P'專案")
    pitem_stockin_num = fields.Float(digits=(10,0),string="已進數量",default=0)
    pitem_stockin_complete = fields.Boolean(store=True,compute=_get_stockin_complete)
    purchase_no = fields.Char(related='pitem_id.name',string="採購單號")
    pitem_delete_yn = fields.Boolean(string="是否能刪除",default=True,)
    ap_select = fields.Boolean(string="Invoice Select",default=False)
    pur_memo = fields.Text(string="備註")
    sequence = fields.Integer(string="SEQ",default=20)
    chi_select = fields.Boolean(string="進銷存勾選",default=False)
    chi_purchase_no = fields.Char(string="進銷存單號",default='')
    pitem_item = fields.Integer(string="項次")
    pitem_litem = fields.Float(digits=(5, 1), string="項次")

    # @api.model
    # def create(self, vals):
    #     res = super(newebpitemlist ,self).create(vals)
    #     if self.pitem_id.state != 'draft' or self.pitem_id.state != 'sent':
    #         raise UserError("採購單已確認,無法更改明細行,請確認!")
    #     return res


    def write(self, vals):

        res = super(newebpitemlist, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select genpitemlitem1(%d)""" % rec.pitem_id.id)
            self.env.cr.execute("""commit;""")
        return res


    # def unlink(self):
    #     for rec in self:
    #         self.env.cr.execute("select purchaseitemunlink(%s)" % rec.id)
    #     return super(newebpitemlist,self).unlink()







    def name_get(self):
        result = []
        for myrec in self:
            mytext1 = myrec.pitem_machine_type
            if not mytext1:
                mytext1 = "-"
            mytext2 = myrec.pitem_model_type
            if not mytext2:
                mytext2 = "-"
            mytext3 = myrec.pitem_prod_no
            if not mytext3:
                mytext3 = "-"
            mytext4 = myrec.pitem_spec
            if not mytext4:
                mytext4 = "-"
            mytext5 = myrec.pitem_num
            if not mytext5:
                mytext5 = "1"
            else:
                mytext5 = str(myrec.pitem_num)
            mytext6 = myrec.pitem_stockin_num
            if not mytext6:
                mytext6 = '0'
            else :
                mytext6 = str(myrec.pitem_stockin_num)


            mypuritem = "[單號:%s][機種:%s][機型:%s][料號:%s][規格:%s][採購量:%s][已到量:%s]" % (
            myrec.purchase_no, mytext1, mytext2, mytext3, mytext4, mytext5,mytext6)
            result.append((myrec.id, mypuritem))
        return result


class newebpurchaseinherit(models.Model):
    _inherit = "purchase.order"
    _description = "採購訂單"

    @api.depends('order_line.date_planned', 'create_date')
    def _compute_date_planned(self):
        for order in self:
            min_date = (datetime.today() + relativedelta(days=3)).strftime('%Y-%m-%d')
            for line in order.order_line:
                if not min_date or line.date_planned < min_date:
                    min_date = line.date_planned
            if min_date:
                order.date_planned = min_date

    # @api.multi
    # def neweb_proj_import(self):
    #     raise UserError("趕工中....")

    @api.depends('order_line.price_total', 'display_line.pitem_num', 'display_line.pitem_price', 'taxes_id')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                # FORWARDPORT UP TO 10.0
                if order.company_id.tax_calculation_rounding_method == 'round_globally':
                    taxes = line.taxes_id.compute_all(line.price_unit, line.order_id.currency_id, line.product_qty,
                                                      product=line.product_id, partner=line.order_id.partner_id)
                    amount_tax += sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
                else:
                    amount_tax += line.price_tax
            order.update({
                'amount_untaxed': order.currency_id.round(amount_untaxed),
                'amount_tax': order.currency_id.round(amount_tax),
                'amount_total': amount_untaxed + amount_tax,
                # 'pitem_untax' : order.currency_id.round(amount_untaxed),
                # 'pitem_tax':  order.currency_id.round(amount_tax),
                # 'pitem_amounttot': amount_untaxed + amount_tax,
            })
            myamount_untax = myamount_tax = 0.0
            for line in order.display_line:
                myamount_untax += (line.pitem_num * line.pitem_price)
                # amount_tax += round(line.pitem_num * line.pitem_price * 0.05)
                # if self.taxes_id:
                #     myamount_tax += round(line.pitem_num * line.pitem_price * (self.taxes_id.amount / 100))
                # else:
                #     myamount_tax += round(line.pitem_num * line.pitem_price * 0.05)
            if self.taxes_id:
                myamount_tax = round(myamount_untax * (self.taxes_id.amount / 100))
            else:
                myamount_tax = round(myamount_untax  * 0.05)

            order.update({
                'pitem_untax': myamount_untax,
                'pitem_tax': myamount_tax,
                'pitem_amounttot': myamount_untax + myamount_tax,
            })

    def _get_pur_reciver(self):
        for rec in self:
            myrec = self.env['neweb_purchase.purchase_manager'].search([])[0]
            if myrec:
               myreciver = myrec.name.name
            else:
               myreciver = ' '
            rec.purchase_reciver = myreciver
            return myreciver

    @api.depends('pitem_untax')
    def _get_pitem_untax1(self):
        for rec in self:
            mypitemuntax=round(rec.pitem_untax)
            rec.pitem_untax1 = mypitemuntax
            return mypitemuntax

    @api.depends('pitem_tax')
    def _get_pitem_tax1(self):
        for rec in self:
            mypitemtax = int(rec.pitem_tax)
            rec.pitem_tax1 = mypitemtax
            return mypitemtax

    @api.depends('pitem_amounttot')
    def _get_pitem_amounttot1(self):
        for rec in self:
            mypitemamounttot = round(rec.pitem_amounttot)
            rec.pitem_amounttot1 = mypitemamounttot
            return mypitemamounttot

    purchase_type = fields.Selection([('1','銷售'),('2','維護')],string="採購單性質")
    display_line = fields.One2many('neweb.pitem_list','pitem_id', copy=True, string="明細資料",track_visibility="onchange")
    pitem_untax = fields.Float(digits=(13,0),string="合計", store=True, compute=_amount_all)
    pitem_untax1 = fields.Float(digits=(13,0),string="bf合計",compute=_get_pitem_untax1)
    pitem_tax = fields.Float(digits=(10,0),string="營業稅", store=True, compute=_amount_all)
    pitem_tax1 = fields.Float(digits=(10, 0), string="營業稅", compute=_get_pitem_tax1)
    # date_planned = fields.Datetime(string="預定交期", index=True, oldname='minimum_planned_date')
    pitem_amounttot = fields.Float(digits=(13,0),string="總價", store=True, compute=_amount_all)
    pitem_amounttot1 = fields.Float(digits=(13, 0), string="總價", compute=_get_pitem_amounttot1)
    taxes_id = fields.Many2one('account.tax', string='Taxes',
                               domain=['|', ('active', '=', False), ('active', '=', True),
                                       ('type_tax_use', '=', 'purchase')],default=lambda self:self.env['account.tax'].search([('type_tax_use','=','purchase')],limit=1))
    purchase_loc = fields.Selection([('1','交貨地點'),('2','維護地點'),('3','服務地點')],string="地點",default='1')
    purchase_company = fields.Text(string="公司名稱",default=lambda self:self.env.ref("base.main_company").name)
    purchase_reciver = fields.Text(string="收件人/連絡人")
    purchase_deliver = fields.Text(string="寄送地址/維護地址/客戶地址",default=lambda self:self.env.ref("base.main_company").partner_id.street)
    deliver_phone = fields.Char(string="電話",default=lambda self:self.env['neweb_purchase.purchase_manager'].search([]).name.work_phone)
    deliver_date = fields.Date(string="From",default=lambda self:fields.datetime.now())
    deliver_date1 = fields.Date(string="To",default=lambda self:fields.datetime.now())
    pur_rec_type_t = fields.Selection([('1','收件人'),('2','連絡人')],default='1')
    pur_rec_address_t = fields.Selection([('1','寄送地址'),('2','維護地址'),('3','客戶地址')],default='1')
    pur_rec_date_t = fields.Selection([('1','交貨日期'),('2','維護日期'),('3','服務日期')],default='1')
    user_id = fields.Many2one('res.users',string="代號")
    partner_contact = fields.Many2one('res.partner',string="聯絡人")
    is_signed = fields.Boolean(string="是否授信",default=False)
    invoiceok = fields.Boolean(string="已請款否?",default=False)
    purchase_memo = fields.Text(string="備註")
    purchase_othernote = fields.Text(string="合約說明")
    payment_desc = fields.Char(string="付款說明")
    pay_term = fields.Char(size=10,string="月結天數")
    purchase_default_receiver = fields.Text(string="採購承辦人",default=lambda self:self.env['neweb_purchase.purchase_manager'].search([])[0].name.name or False)


    def name_get(self):
        result = []
        for myrec in self:
            mypurname = "%s:[%s: $%s] " % (myrec.name,myrec.currency_id.name,myrec.pitem_amounttot)
            result.append((myrec.id, mypurname))
        return result


    @api.onchange("partner_id")
    def onchange_partner_id(self):
        res = {}
        if self.partner_id:
            res['domain'] = {'partner_contact': [('parent_id', '=', self.partner_id.id),('is_company','=',False)]}
            # mypaymentterm = self.env['res.partner'].search([('id','=',self.partner_id.id)]).pay_term
            # if mypaymentterm:
            #    self.pay_term = mypaymentterm
        return res


    is_closed = fields.Boolean(string="是否結案",default=False)

    def set_closed(self):
        for rec in self:
            rec.update({'is_closed':True,'state': 'done'})


    def set_reject(self):
        for rec in self:
            rec.update({'is_closed':False , 'is_signed':False,'state': 'draft'})

    ### WKF SEND MAIL PROCEDURE
    ###   type='1' 所有簽核人員    type='2' 送件者


    # @api.model
    def get_approve_emails(self):
        self.env.cr.execute("select wkfsendmail('%s',%d,'%s')" % (self.name, self.id, '2'))
        mylist = self.env.cr.fetchall()
        myids = self.env['res.users'].search([('id', 'in', mylist)])
        all_mails = []
        for item in myids:
            all_mails.append(item.employee_ids.work_email)
        return ','.join(str(mail) for mail in all_mails)

    # @api.model
    def get_reject_emails(self):
        self.env.cr.execute("select wkfsendmail('%s',%d,'%s')" % (self.name, self.id, '2'))
        mylist = self.env.cr.fetchall()
        myids = self.env['res.users'].search([('id', 'in', mylist)])
        all_mails = []
        for item in myids:
            all_mails.append(item.employee_ids.work_email)
        return ','.join(str(mail) for mail in all_mails)


    def send_approve_mail(self):
        myrec = self.env['purchase.order'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_purchase', 'mail_neweb_purchase_wkf_approve')[1]
        except ValueError:
            template_id = False
        # ctx = self.env.context.copy()
        # ctx.update({
        #     'default_model': 'purchase.order',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'mail_post_autofollow': True,
        #     'custom_layout': "neweb_purchase.mail_neweb_purchase_wkf_approve"
        # })
        self.env['mail.template'].browse(template_id).send_mail(myid)
        # template_id = ir_model_data.get_object_reference('neweb_purchase', 'mail_neweb_purchase_wkf_approve')[1]
        # self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, template_id, self.id, force_send=True,
        #                                      context=self.with_context(ctx))


    def send_reject_mail(self):
        myrec = self.env['purchase.order'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_purchase', 'mail_neweb_purchase_wkf_reject')[1]
        except ValueError:
            template_id = False
        # ctx = self.env.context.copy()
        # ctx.update({
        #     'default_model': 'purchase.order',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'mail_post_autofollow': True,
        #     'custom_layout': "neweb_purchase.mail_neweb_purchase_wkf_reject"
        # })
        self.env['mail.template'].browse(template_id).send_mail(myid)
        # template_id = ir_model_data.get_object_reference('neweb_purchase', 'mail_neweb_purchase_wkf_reject')[1]
        # # myrec.write({'state': 'sent'})
        # self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, template_id, self.id, force_send=True,
        #                                      context=self.with_context(ctx))

    def _get_phone(self):
        mymanagerphone = self.env['neweb_purchase.purchase_manager'].search([]).name.work_phone
        print ("%s" % mymanagerphone)
        return mymanagerphone



    @api.model
    def create(self,vals):
        # myrec=self.env['res.company'].search([('id','=',1)])
        # vals['deliver_phone']=myrec.phone
        rec = super(newebpurchaseinherit, self).create(vals)
        # myrec1 = self.env['res.partner'].search([('id','=',rec.partner_id.id)])
        # if myrec1 and not myrec1.pay_term:
        #     self.env.cr.execute("""update purchase_order set payment_term_id=%d,pay_term='%s' where id=%d""" % (myrec1.cus_payment.id,myrec1.pay_term,rec.id))
        genprodid = self.env.ref('neweb_project.neweb_product_purchase_1')
        myname = self.env['product.template'].search([('id', '=', genprodid.id)])
        myrec = self.env['purchase.order'].search([('id','=',rec.id)])
        myname = vals.get('name')
        if len(myname) > 0 :
           newname = myname[:2]+str(int(myname[2:4])-11).zfill(2)+myname[4:]
           self.env.cr.execute("""select chkpono('%s')""" % newname)
           newname = self.env.cr.fetchone()[0]
           self.env.cr.execute("""update purchase_order set name='%s' where id=%d""" % (newname,rec.id))
           # myrec.write({'name':newname})
        mypitemrec = self.env['neweb.pitem_list'].search([('pitem_id','=',rec.id)])
        if mypitemrec :
           mytaxesid = myrec.taxes_id
          # print mytaxesid
           myownerid = self.env.uid
           purid = rec.id
           myprodid = genprodid.id
           self.env.cr.execute("select genpurline(%s,%s,%s,%s);" % (myownerid,purid,myprodid,mytaxesid.id))
           self.env.cr.execute("commit;")
           self.env.cr.execute("select genpurchasetaxesid(%s);" % (purid))
        self.env.cr.execute("""select check_projreqno(%d)""" % rec.id)
        self.env.cr.execute("""select check_origin(%d)""" % rec.id)
        return rec

    def write(self, vals):
        rec = super(newebpurchaseinherit, self).write(vals)
        # myrec1 = self.env['res.partner'].search([('id', '=', self.partner_id.id)])
        # if myrec1 and myrec1.pay_term:
        #     self.env.cr.execute("""update purchase_order set payment_term_id=%d,pay_term='%s' where id=%d""" % (myrec1.cus_payment.id, myrec1.pay_term, self.id))
        purid = self.id
        # raise UserError("%s" % purid)
        genprodid = self.env.ref('neweb_project.neweb_product_purchase_1')
        myownerid = self.env.uid
        myprodid = genprodid.id
        myrec = self.env['purchase.order'].search([('id','=',purid)])
        # mylinrec = self.env['purchase.order.line'].search([('order_id', '=', purid)])
        mytaxesid = myrec.taxes_id
        mypitemrec = self.env['neweb.pitem_list'].search([('pitem_id', '=', purid)])
        if mypitemrec :
           self.env.cr.execute("select genpurline(%s,%s,%s,%s);" % (myownerid,purid,myprodid,mytaxesid.id))
           self.env.cr.execute("commit;")
           self.env.cr.execute("select genpurchasetaxesid(%s);" % (purid))
           # mylinrec.write({'taxes_id':[(6,0,mytaxesid.id)]})
        self.env.cr.execute("""select check_projreqno(%d)""" % self.id)
        self.env.cr.execute("""select check_origin(%d)""" % self.id)
        return rec


    def unlink(self):
        # self.env.cr.execute("select wkfisstart(%d)" % int(self.x_wkf_state))
        # isstart = self.env.cr.fetchone()
        # if not isstart[0]:
        #     raise UserError("表單已送簽核,不能刪除")
        myid = self.id
        res = super(newebpurchaseinherit,self).unlink()
        self.env.cr.execute("""select purorderunlink(%d)""" % myid)
        return res

    def purchase_change_price(self):
        self.env.cr.execute("""select purchase_change_price(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '採購回寫成本分析單價完成！'
        return {
                'name': '系統通知訊息',
                 'type': 'ir.actions.act_window',
                  'view_type': 'form',
                  'view_mode': 'form',
                  'res_model': 'sh.message.wizard',
                  'views': [(view.id, 'form')],
                  'view_id': view.id,
                  'target': 'new',
                  'context': context,
                }



    def button_confirm(self):
        for order in self:
            purchaseno = self.name
            dateorder = self.date_order1
            partnerid = self.partner_id.id
            if order.state not in ['draft', 'sent']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step' \
                    or (order.company_id.po_double_validation == 'two_step' \
                                and order.amount_total < self.env.user.company_id.currency_id.compute(
                            order.company_id.po_double_validation_amount, order.currency_id)) \
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()

                # 採購單確認後回寫專案 => 採購單號 ＆ 金額
                # myname = order.name
                # myprojid = self.env['neweb.projsaleitem'].search([('purchase_no','like',myname)],limit=1)
                # print "%d" % myprojid.saleitem_id.id

                self.env.cr.execute("select purchasecommit(%d,%d)" % (order.id, 1))
                self.env.cr.execute("""commit""")
                self.env.cr.execute("select updatepurnum(%d)" % order.id)
                self.env.cr.execute("""commit""")
                self.env.cr.execute("select purupdateprojanalysis(%d)" % order.id)
                self.env.cr.execute("""commit""")
                self.env.cr.execute("""select purchase_change_price(%d)""" % order.id)
                self.env.cr.execute("""commit""")
                self.env.cr.execute("select getprojid(%d)" % order.id)
                myprojid = self.env.cr.fetchone()
                if myprojid[0]:
                    self.env.cr.execute("""select proj_rcal_cost(%d)""" % myprojid[0])
                    self.env.cr.execute("""commit""")


            else:
                order.write({'state': 'to approve'})
            if self.foreign_purchase==False:
                myrec = self.env['stock.picking']
                myres = myrec.create({'picking_type_id': 1,
                                      'location_id': 4,
                                      'location_dest_id': 8,
                                      'move_type': 'direct',
                                      'company_id': 1,
                                      'date': dateorder,
                                      'origin': purchaseno,
                                      'stockin_type': '1',
                                      'stockout_type': '1',
                                      'state': 'assigned',
                                      'partner_id': partnerid,
                                      'product_id': 1,
                                      'move_lines': [
                                          (0, 0,
                                           {'product_id': 1, 'company_id': 1, 'location_id': 4, 'name': '採購商品',
                                            'date': dateorder,
                                            'date_expected': dateorder, 'procure_method': 'make_to_stock',
                                            'location_dest_id':8, 'product_uom_qty': 1, 'product_uom': 1,
                                            })]})

        return True


    def button_cancel(self):
        for order in self:
            for pick in order.picking_ids:
                if pick.state == 'done':
                    raise UserError(
                        _('Unable to cancel purchase order %s as some receptions have already been done.') % (
                        order.name))
            for inv in order.invoice_ids:
                if inv and inv.state not in ('cancel', 'draft'):
                    raise UserError(
                        _("Unable to cancel this purchase order. You must first cancel related vendor bills."))

            for pick in order.picking_ids.filtered(lambda r: r.state != 'cancel'):
                pick.action_cancel()
            # TDE FIXME: I don' think context key is necessary, as actions are not related / called from each other
            try:
                if not self.env.context.get('cancel_procurement'):
                    procurements = order.order_line.mapped('procurement_ids')
                    procurements.filtered(lambda r: r.state not in ('cancel', 'exception') and r.rule_id.propagate).write(
                        {'state': 'cancel'})
                    procurements.filtered(
                        lambda r: r.state not in ('cancel', 'exception') and not r.rule_id.propagate).write(
                        {'state': 'exception'})
                    moves = procurements.filtered(lambda r: r.rule_id.propagate).mapped('move_dest_id')
                    moves.filtered(lambda r: r.state != 'cancel').action_cancel()
            except Exception as inst:
                A=1

            self.env.cr.execute("select purchasecommit(%d,%d)" % (order.id, 2))
        self.write({'state': 'cancel'})

    def regen_origin_id(self):
        self.env.cr.execute("""select genpuroriginid(%d)""" % self.id)
        self.env.cr.execute("""commit""")




class purchaseorderlinewizard(models.Model):
    _inherit = "purchase.order.line"
    _order = "id asc"

    pitem_modeltype = fields.Char(string="機種-機型/料號")
    pitem_serial = fields.Char(string="序號")
    pitem_no = fields.Char(string="料號")
    write_type = fields.Selection([('1','I'),('2','C')],default='1',string="寫入方式")




