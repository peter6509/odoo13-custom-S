# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api,SUPERUSER_ID
from odoo.exceptions import UserError
import math
# import odoo.addons.decimal_precision as dp


class salenocheck(models.Model):
    _name = "neweb.salenocheck"
    _description = '銷售單號版次記錄檔'

    sale_no = fields.Char(string="銷單號碼")
    vernum = fields.Integer(string="版次", default=1)
    trans_proj = fields.Boolean(string="是否已轉專案", default=False)


class quotationinclude(models.Model):
    _name = "neweb.quotation_include"
    _description = '銷售服務內容基礎配置'
    _order = "sequence,id"

    name = fields.Char(string="服務內容")
    sequence = fields.Integer(string="SEQ", default=20)


class callserviceresponse(models.Model):
    _name = "neweb.call_service_response"
    _description = '銷售叫修時效基礎配置'
    _order = "sequence,id"

    name = fields.Char(string="叫修時效")
    sequence = fields.Integer(string="SEQ", default=20)

class newebsaleinherit(models.Model):
      _inherit ="sale.order"
      _description = "銷售主檔"

      @api.depends('sitem_untax')
      def _get_sitemuntax(self):
          for rec in self:
              rec.sitem_untax1 = round(rec.sitem_untax)

      @api.depends('sitem_tax')
      def _get_sitemtax(self):
          for rec in self:
              rec.sitem_tax1 = round(rec.sitem_tax)

      @api.depends('sitem_amounttot')
      def _get_sitemamounttot(self):
          for rec in self:
              rec.sitem_amounttot1 = round(rec.sitem_amounttot)

      @api.depends('display_line')
      def _get_sitemuntax1(self):
          for order in self:
              myamount_untax = myamount_tax = 0
              for line in order.display_line:
                  myamount_untax += (line.sitem_num * line.sitem_price)
              order.sitem_untax = myamount_untax
              return myamount_untax

      @api.depends('display_line','taxes_id')
      def _get_sitemtax1(self):
          for order in self:
              myamount_untax = myamount_tax = 0
              for line in order.display_line:
                  myamount_untax += (line.sitem_num * line.sitem_price)
                  if self.taxes_id:
                      myamount_tax = round(myamount_untax * self.taxes_id.amount/100)
                  else:
                      myamount_tax = round(myamount_untax * 0.05)
              order.sitem_tax = myamount_tax
              return myamount_tax

      @api.depends('sitem_untax','sitem_tax')
      def _get_sitemamounttot1(self):
          myamounttot = 0
          for order in self:
              myamounttot += round(order.sitem_untax) + round(order.sitem_tax)
              order.sitem_amounttot = myamounttot
              return myamounttot

      @api.depends('sitem_amounttot')
      def _get_disamount(self):
          mydisamount = 0
          for order in self:
              order.discount_amount = order.sitem_amounttot
              return mydisamount

      display_line = fields.One2many('neweb.sitem_list','sitem_id', copy=True, string="明細資料",track_visibility="onchange")
      sitem_untax = fields.Float(digits=(13,2), string="合計",store=True,compute=_get_sitemuntax1)
      sitem_untax1 = fields.Float(digits=(10,0),string="合計",compute=_get_sitemuntax)
      sitem_tax = fields.Float(digits=(13,2), string="營業稅",store=True,compute=_get_sitemtax1)
      sitem_tax1 = fields.Float(digits=(8,0),string="營業稅",compute=_get_sitemtax)
      sitem_amounttot = fields.Float(digits=(13,2), string="總價",store=True,compute=_get_sitemamounttot1)
      sitem_amounttot1 = fields.Float(digits=(10,0),string="總價",compute=_get_sitemamounttot)
      taxes_id = fields.Many2one('account.tax', string='Taxes',
                                 domain=['|', ('active', '=', False), ('active', '=', True),
                                         ('type_tax_use', '=', 'sale')],
                                 default=lambda self: self.env['account.tax'].search(
                                     [('type_tax_use', '=', 'sale')], limit=1))
      trans_yn = fields.Boolean(string="是否轉專案",store=False,default='_get_transyn')
      neweb_memo = fields.Text(string="其它說明")
      #user_id = fields.Many2one('res.users',string="業務人員")

      discount_amount = fields.Float(digits=(10,0),string="本案給予優惠總價(含税)",store=True,compute=_get_disamount)
      payment_term = fields.Char(string="分期付款？期：")
      open_account_day = fields.Selection([('1','30天'),('2','45天'),('3','60天'),('4','90天'),('5','120天')],string="付款天數")
      maintenance_payment_type = fields.Selection([('1','每年為一期，期初付款'),('2','每半年為一期，期初付款'),('3','每三個月(季)為一期，期初付款'),
                                                   ('4','每三個月(季)為一期，期末付款'),('5','每月為一期，期初付款'),('6','每月為一期，期末付款'),
                                                   ('7','其他')],string="維護付款條件",default='1')
      project_payment_type = fields.Selection([('1','貨到後月結日給付現金或即期支票交付(第一次交易為貨到現金票)'),
                                               ('2','簽約30%,交貨40%,驗收30%'),
                                               ('3','簽約40%,交貨50%,驗收10%'),
                                               ('4','交貨40%,建置50%,驗收10%'),
                                               ('5','交貨90%,驗收10%'),('6','其他')],string="銷售專案付款",default='2')
      delivery_term = fields.Selection([('1','30天'),('2','45天'),('3','60天')],string="交貨期限",default='2')
      service_rule = fields.Selection([('1','保固'),('2','維護')],string="服務條款",default='1')
      warranty_service_rule = fields.Char(string="保固服務條款",default="依原廠保固條款提供保固服務。")
      warranty_service_rule1 = fields.Selection([('1','藍新提供三個月保固服務。'),('2','藍新提供六個月保固服務。'),('3','藍新提供一年保固服務。')],string="保固服務條款",default='3')
      maintenance_service_rule = fields.Selection([('1','週一至週五，每日8點至19點，一日共11小時(5*11)'),
                                                   ('2','週一至週五，每日9點至17點，一日共8小時(5*8)'),
                                                   ('3','週一至週日，每日24小時(7*24)')],string="維護服務時段",default='2')
      routine_maintenance = fields.Selection([('1','每月'),('2','每雙月(每二個月)'),('3','每季(每三個月)')],string="定期維護",default='1')
      # partner_id = fields.Many2one('res.partner', string='Customer', readonly=True,
      #                              states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
      #                              required=True, change_default=True, index=True, track_visibility='always')
      maintenance_start = fields.Date(string="維護啟始日")
      maintenance_end = fields.Date(string="維護截止日")
      quotation_include = fields.Many2one('neweb.quotation_include',string="報價服務說明")
      call_service_response = fields.Many2one('neweb.call_service_response',string="叫修時效")
      quotation_term = fields.Integer(string="有效天數",default=30)
      mobile_phone = fields.Char(string="行動電話")
      work_phone = fields.Char(string="工作電話")
      contact_id = fields.Many2one('res.partner',string="客戶聯絡人")
      quotation_memo = fields.Text(string="備註")



      def cancel_saleorderline(self):
          mysaleorderid = self.env.context.get('saleorderid')
          self.env.cr.execute("""select cancel_saleorderline(%d)""" % mysaleorderid)



      @api.onchange('partner_id')
      def onchange_partnerid(self):
          if self.partner_id:
              myrec = self.env['res.partner'].search([('parent_id', '=', self.partner_id.id)])
              mypaymentterm = myrec.payment_days
              mytermtype = '3'
              if mypaymentterm and mypaymentterm <= 30 :
                  mytermtype = '1'
              elif mypaymentterm and mypaymentterm > 30 and mypaymentterm <= 45 :
                  mytermtype = '2'
              elif mypaymentterm and mypaymentterm > 45 and mypaymentterm <= 60 :
                  mytermtype = '3'
              elif mypaymentterm and mypaymentterm > 60 and  mypaymentterm <= 90 :
                  mytermtype = '4'
              elif mypaymentterm and mypaymentterm > 90 and mypaymentterm <= 120 :
                  mytermtype = '5'
              else :
                  mytermtype = '5'
              self.open_account_day = mytermtype

              ids = []
              for item in myrec:
                  ids.append(item.id)
              res = {}

              # print "%s" % ids
              res['domain'] = {'contact_address': [('id', 'in', ids)]}
              return res

      # @api.onchange('partner_id')
      # def onchange_partnerid1(self):
      #     if self.partner_id:
      #         myrec = self.env['res.partner'].search([('parent_id', '=', self.partner_id.id)])
      #         ids = []
      #         for item in myrec:
      #             ids.append(item.id)
      #         res = {}
      #
      #         # print "%s" % ids
      #         res['domain'] = {'contact_id':[('id', 'in', ids)]}
      #         return res



      def partner_updatevat(self):
          self.env.cr.execute("select updatevat();")
          self.env.cr.execute("commit")

      # @api.depends('payment_term_id')
      # def _get_paymentday(self):
      #     for rec in self:
      #         if not rec.payment_term_id:
      #            return
      #         paymentdays = rec.payment_term_id.line_ids[0].days
      #         #print "%s" % paymentdays
      #         if paymentdays == 30:
      #            res = '1'
      #         elif paymentdays == 45:
      #            res = '2'
      #         elif paymentdays == 60:
      #            res ='3'
      #         elif paymentdays == 90:
      #            res = '4'
      #         elif paymentdays == 120:
      #            res = '5'
      #         else:
      #            res = '1'
      #         rec.update({'open_account_day':res})



      # @api.onchange('delivery_term')
      # def onchange_client(self):
      #     myuserid = self.env['res.users'].search([('id','=',self.env.uid)])
      #     myempid = myuserid.employee_ids[0].id
      #     self.env.cr.execute("select getownpartner(%d)" % myempid)
      #     mylist = self.env.cr.fetchall()
      #     myrec = self.env['res.partner'].search([('id','in',mylist)])
      #     ids=[]
      #     for item in myrec:
      #         ids.append(item.id)
      #     res={}
      #     #print "%s" % ids
      #     res['domain']={'partner_id':[('id','in',ids)]}
      #     return res


      is_signed = fields.Boolean(string="是否授信",default=False)


      def set_signed(self):
      	for rec in self:
      		rec.update({'is_signed':True,'state':'sale'})

      is_closed = fields.Boolean(string="是否結案",default=False)


      def set_closed(self):
          for rec in self:
              rec.update({'is_closed':True,'state':'done'})


      def set_reject(self):
          for rec in self:
              rec.update({'is_closed':False , 'is_signed':False})


      @api.model
      def create(self, vals):
          vals['warehouse_id']=2
          vals['picking_policy']='direct'
          rec = super(newebsaleinherit, self).create(vals)
          genprodid = self.env.ref('neweb_project.neweb_product_sale_2')
          myname = self.env['product.template'].search([('id', '=', genprodid.id)])
          myrec = self.env['sale.order'].search([('id', '=', rec.id)])
          myname = vals.get('name')
          if int(myname[1:5]) - 1911 > 0 :
             newname = myname[:1] + str(int(myname[1:5]) - 1911).zfill(3) + myname[5:11]
             self.env.cr.execute("""select chksono('%s')""" % newname)
             newname = self.env.cr.fetchone()[0]
             myrec.write({'name': newname})
             salenocheck = self.env['neweb.salenocheck'].search([('sale_no','=',newname)])
             if not salenocheck :
                salenocheck.create({'sale_no':newname})
          mysitemrec = self.env['neweb.sitem_list'].search([('sitem_id', '=', rec.id)])

          if mysitemrec:
              mytaxesid = myrec.taxes_id
              # print mytaxesid
              myownerid = self.sudo().env.uid
              saleid = rec.id
              myprodid = genprodid.id
              self.env.cr.execute("select gensaleline(%s,%s,%s,%s);" % (myownerid, saleid, myprodid, mytaxesid.id))
              self.env.cr.execute("commit;")
              self.env.cr.execute("select gensaletaxesid(%s);" % saleid)
          self.env.cr.execute("select getmobilephone(%d)" % myrec.user_id.id)
          mymobilephone=self.env.cr.fetchone()[0]
          self.env.cr.execute("select getworkphone(%d)" % myrec.user_id.id)
          myworkphone = self.env.cr.fetchone()[0]
          myrec.write({'mobile_phone':mymobilephone,'work_phone':myworkphone})
          try:
              self.env.cr.execute("select sale_drop_messagefollower(%d)" % rec.id)
          except Exception as inst:
              print ("No drop mail followers")
          return rec


      def write(self, vals):
          rec = super(newebsaleinherit, self).write(vals)
          saleid = self.id
          # raise UserError("%s" % purid)
          genprodid = self.env.ref('neweb_project.neweb_product_sale_2')
          myownerid = self.env.uid
          myprodid = genprodid.id
          myrec = self.env['sale.order'].search([('id', '=', saleid)])
          mytaxesid = myrec.taxes_id
          mysitemrec = self.env['neweb.sitem_list'].search([('sitem_id', '=', saleid)])
          if mysitemrec:
              self.env.cr.execute("select gensaleline(%s,%s,%s,%s);" % (myownerid, saleid, myprodid, mytaxesid.id))
              self.env.cr.execute("commit;")
              self.env.cr.execute("select gensaletaxesid(%s);" % saleid)
          # self.env.cr.execute("select getmobilephone(%d)" % myrec.user_id.id)
          # mymobilephone = self.env.cr.fetchone()
          # self.env.cr.execute("select getworkphone(%d)" % myrec.user_id.id)
          # myworkphone = self.env.cr.fetchone()
          # myrec.write({'mobile_phone': mymobilephone, 'work_phone': myworkphone})
          try:
              self.env.cr.execute("select sale_drop_messagefollower(%d)" % saleid)
          except Exception as inst:
              print ("No drop mail followers")
          return rec

      # @api.depends('order_line.price_total','display_line.sitem_num', 'display_line.sitem_cost', 'taxes_id')
      # def _amount_all(self):
      #     """
      #     default the total amounts of the SO.
      #     """
      #     for order in self:
      #         amount_untaxed = amount_tax = 0.0
      #         # for line in order.order_line:
      #             # amount_untaxed += line.price_subtotal
      #             # if order.company_id.tax_calculation_rounding_method == 'round_globally':
      #             #     price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
      #             #     taxes = line.tax_id.default_all(price, line.order_id.currency_id, line.product_uom_qty,
      #             #                                     product=line.product_id, partner=order.partner_shipping_id)
      #             #     amount_tax += sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
      #             # else:
      #             #     amount_tax += line.price_tax
      #
      #         myamount_untax = myamount_tax = 0
      #         for line in order.display_line:
      #             myamount_untax += (line.sitem_num * line.sitem_price)
      #             if self.taxes_id:
      #                 # myamount_tax += round(line.sitem_num * line.sitem_price * (self.taxes_id.amount / 100))
      #
      #                 myamount_tax = round(myamount_untax * self.taxes_id.amount/100)
      #             else:
      #                 # myamount_tax += round(line.sitem_num * line.sitem_price * 0.05)
      #                 myamount_tax = round(myamount_untax * 0.05)
      #
      #
      #         order.sitem_untax = myamount_untax
      #         order.sitem_tax = myamount_tax
      #         order.sitem_amounttot = round(myamount_untax) + round(myamount_tax)
      #         order.discount_amount = round(myamount_untax) + round(myamount_tax)
      #         # order.update({
      #         #     'sitem_untax': myamount_untax,
      #         #     'sitem_tax': myamount_tax,
      #         #     'sitem_amounttot': round(myamount_untax) + round(myamount_tax),
      #         #     'discount_amount': round(myamount_untax) + round(myamount_tax),
      #         # })
      #


      @api.depends('name')
      def _get_transyn(self):
          for rec in self:
              mysaleno = rec.name[:10]
              hasyn = self.env['neweb.salenocheck'].search([('sale_no','=',mysaleno)])
              if hasyn :
                 rec.update({'trans_yn':hasyn.trans_proj})
              else :
                 rec.update({'trans_yn':False})



      def neweb_saleorder_copy(self):
          default = {}
          # myprojid = self.env.context.get('proj_op_id')
          mysaleorder = self.env['sale.order'].search([('id', '=', self.env.context.get('sale_op_id'))])
          mysaleno = mysaleorder.name
          mysalenocheck = self.env['neweb.salenocheck'].search([('sale_no','=',mysaleno[:10])])
          if mysalenocheck :
             mytransyn = mysalenocheck.trans_proj
             if mytransyn :
                raise  UserError("已經轉專案成本分析,不能再複製了...")
             else :
                 myvernum = mysalenocheck.vernum
                 mynewname = mysaleno[:10]+'-'+str(myvernum).zfill(2)
                 mysalenocheck.write({'vernum': myvernum + 1})

          default['name'] = mynewname
          sale_copy = super(newebsaleinherit, self).copy(default=default)

          return {'view_name': 'salecopywizard',
                  'name': ('銷單複製作業'),
                  'views': [[False, 'form'], [False, 'tree'], ],
                  'res_model': 'sale.order',
                  'context': self._context,
                  'type': 'ir.actions.act_window',
                  'target': 'self',
                  # 'domain': mydomain,
                  'res_id': sale_copy.id,
                  'flags': {'action_buttons': True},
                  'view_mode': 'form',
                  'view_type': 'form'
                  }


      def neweb_saleorder_create(self):
          default = {}
          sale_copy = super(newebsaleinherit, self).copy(default=default)

          return {'view_name': 'salecopywizard',
                  'name': ('銷單複製作業'),
                  'views': [[False, 'form'], [False, 'tree'], ],
                  'res_model': 'sale.order',
                  'context': self._context,
                  'type': 'ir.actions.act_window',
                  'target': 'self',
                  # 'domain': mydomain,
                  'res_id': sale_copy.id,
                  'flags': {'action_buttons': True},
                  'view_mode': 'form',
                  'view_type': 'form'
                  }

      @api.model
      def gen_saletoproj(self):
          A=1



class newebsitemlist(models.Model):
      _name = "neweb.sitem_list"
      _description = '銷售明細檔'

      @api.depends('sitem_price')
      def _get_addtax(self):
          for rec in self:
              rec.update({'sitem_priceaddtax': (rec.sitem_price * 1.05)})

      @api.depends('sitem_num', 'sitem_stockout_num')
      def _get_stockout_complete(self):
          for order in self:
              if order.sitem_num == order.sitem_stockout_num and order.sitem_num > 0:
                  order.update({'sitem_stockout_complete': '1'})

      @api.depends('sitem_num', 'sitem_cost')
      def _amount_all1(self):
          amountcosttot = self.sitem_num * self.sitem_cost
          self.update({'sitem_costsubtot': amountcosttot})

      @api.depends('sitem_num', 'sitem_cost', 'sitem_price')
      def _amount_all2(self):
          for sitem in self:
              if sitem.sitem_num != False and sitem.sitem_cost != False and sitem.sitem_price != False:
                  amountcosttot = sitem.sitem_num * sitem.sitem_cost
                  amountpricetot = sitem.sitem_num * sitem.sitem_price
                  if amountpricetot == 0:
                      sitem.update({'sitem_profit': 0})
                  else:
                      sitem.update({'sitem_profit': amountpricetot - amountcosttot})

      @api.depends('sitem_num', 'sitem_cost', 'sitem_price')
      def _amount_all3(self):
          for sitem in self:
              if sitem.sitem_num != False and sitem.sitem_cost != False and sitem.sitem_price != False:
                  amountcosttot = sitem.sitem_num * sitem.sitem_cost
                  amountpricetot = sitem.sitem_num * sitem.sitem_price
                  if amountpricetot == 0:
                      amountprofitrate = 0
                      sitem.sitem_profitrate = amountprofitrate
                      sitem.update({'sitem_profitrate': amountprofitrate})
                  else:
                      if amountpricetot == 0:
                          amountprofitrate = 0
                      else:
                          amountprofitrate = (amountpricetot - amountcosttot) / amountpricetot
                      sitem.update({'sitem_profitrate': amountprofitrate})

      @api.depends('sitem_num')
      def _get_sitemnum(self):
          for rec in self:
              rec.sitem_num1 = round(rec.sitem_num)

      @api.depends('sitem_price')
      def _get_sitemprice(self):
          for rec in self:
              rec.sitem_price1 = round(rec.sitem_price)

      sitem_id = fields.Many2one('sale.order',required=True, ondelete='cascade')
      sitem_modeltype = fields.Char(string="機種-機型/料號")
      sitem_modeltype1 = fields.Many2one('neweb.sitem_modeltype1',string="機型名稱")
      sitem_brand = fields.Many2one('neweb.prodbrand',string="品牌")
      sitem_desc = fields.Text(string="規格說明")
      sitem_num = fields.Float(digits=(10,0),string="數量")
      sitem_num1 = fields.Float(digits=(8,0),string="數量",compute=_get_sitemnum)
      sitem_price = fields.Float(digits=(13,2),string="優惠單價")
      sitem_price1 = fields.Float(digits=(10,0),string="優惠單價",compute=_get_sitemprice)
      sitem_priceaddtax = fields.Float(digits=(13,2),string="含税優惠單價",compute=_get_addtax)
      sitem_cost = fields.Float(digits=(13,2),string="成本單價")
      sitem_costsubtot = fields.Float(digits=(13,2),string="成本＊數量")
      sitem_profit = fields.Float(digits=(13,2),string="毛利")
      sitem_profitrate = fields.Float(digits=(5,2),string="毛利率")
      sitem_stockout_complete = fields.Boolean(store=True, compute=_get_stockout_complete)
      sale_no = fields.Char(related='sitem_id.name', string="銷售單號")
      sitem_stockout_num = fields.Float(digits=(13,2), string="已交數量", default=0)
      maintenance_start = fields.Date(string="維護起始日")
      maintenance_end = fields.Date(string="維護截止日")
      newebmaindate = fields.Text(string="維護起迄日期")
      prod_set = fields.Many2one('neweb.prodset', string="產品組別")
      supplier = fields.Many2one('res.partner', string="廠商",domain=[('supplier_rank', '=', 1), ('parent_id', '=', False)])





      @api.model
      def create(self, vals):
          saleid = vals['sitem_id']
          mysale = self.env['sale.order'].search([('id', '=', saleid)])
          if mysale:
              user1 = self.env['res.users'].browse(self.env.uid)
              if user1.has_group('neweb_project.neweb_sa50_assi') or user1.has_group('neweb_project.neweb_cs50_assi') or user1.has_group('neweb_project.neweb_cs30_dir'):
                  print ("%s" % "Can Modify Security")
              else:
                  if mysale.state not in ['draft', 'sent']:
                      raise UserError("銷售訂單已確認,無法更改明細行,請確認!")
          rec = super(newebsitemlist, self).create(vals)
          return rec

      def write(self, vals):
          saleid = self.sitem_id
          # print "%s" % saleid
          mysale = self.env['sale.order'].search([('id', '=', saleid.id)])
          # print "%s" % mysale.state
          user1 = self.env['res.users'].browse(self.env.uid)
          if user1.has_group('neweb_project.neweb_sa50_assi') or user1.has_group('neweb_project.neweb_cs50_assi') or user1.has_group('neweb_project.neweb_cs30_dir') :
             print ("%s" % "Can Modify Security")
          else:
             if mysale.state not in ['draft', 'sent']:
                 raise UserError("銷售訂單已確認,無法更改明細行,請確認!")
          rec = super(newebsitemlist, self).write(vals)






