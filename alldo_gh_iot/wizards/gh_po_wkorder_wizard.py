# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class ghiotpowkorderwizard(models.TransientModel):
    _name = "alldo_gh_iot.po_wkorder_wizard"

    po_no = fields.Char(string="客戶訂單編號")
    cus_name = fields.Many2one('res.partner', string="客戶",required=True)
    product_no = fields.Many2one('product.product', string="產品", required=True)
    order_date = fields.Date(string="下單日期",required=True)
    po_location = fields.Char(string="庫別")
    po_lock = fields.Boolean(string="倉庫產品預留鎖定?",default=False)
    po_lock_desc = fields.Char(string="預留說明",default=' ')
    shipping_date = fields.Date(string="出貨日期",required=True)
    po_num = fields.Float(digits=(10,2),string="訂單數量",default=0)
    prod_onhand = fields.Float(digits=(10, 0), string="產品在手數量")
    booking_blank = fields.Many2one('product.product', string="毛胚")
    blank_onhand = fields.Float(digits=(10, 0), string="毛胚在手數量")
    po_owner = fields.Many2one('res.users',string="建單人員",default=lambda self:self.env.uid)
    custom_system = fields.Boolean(string="平台",default=False)

    def run_powkorder_wizard(self):
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        myprodloc = mycomploc.prod_loc.id  # 公司成品庫存位置
        mypbookingloc = mycomploc.pbooking_loc.id  # 公司成品預留鎖定位置
        mybbookingloc = mycomploc.bbooking_loc.id  # 公司毛胚預留鎖定位置
        myrec= self.env['stock.picking']
        if self.prod_onhand >= self.po_num :
            if self.po_lock:
                myres = myrec.create(
                    {'picking_type_id': 5, 'location_id': myprodloc, 'location_dest_id': mypbookingloc,
                     'move_type': 'direct',
                     'user_id': self.env.uid, 'origin': '(%s)%s 鎖定需求' % (self.po_no, self.cus_name.name),
                     'move_line_ids': [
                         (0, 0,
                          {'product_id': self.product_no.id, 'company_id': 1, 'location_id': myprodloc,
                           'location_dest_id': mypbookingloc, 'product_uom_id': 1,
                           'qty_done': self.po_num})]})

                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()
            if not self.po_no:
                mypono = ' '
            else:
                mypono = self.po_no
            mycusid = self.cus_name.id
            myprodid = self.product_no.id
            odate = self.order_date
            if not self.po_location:
                mypoloc = ' '
            else:
                mypoloc = self.po_location
            mypolock = self.po_lock
            sdate = self.shipping_date
            ponum = self.po_num
            if self.po_lock:
                ppickid = myres.id
            else:
                ppickid = 0
            poowner = self.po_owner.id
            self.env.cr.execute("""select genpobooking('%s',%d,%d,'%s','%s',%s,'%s',%s,%d,%d,%d,%s,'%s')""" % (mypono,mycusid,myprodid,odate,mypoloc,mypolock,sdate,ponum,ppickid,0,poowner,self.custom_system,self.po_lock_desc))
            self.env.cr.execute("""commit""")

            if self.prod_onhand >= self.po_num:
                self.env.cr.execute("""select setpowkorderclose('%s')""" % self.po_no)
                self.env.cr.execute("""commit""")

        elif self.prod_onhand > 0 and self.prod_onhand < self.po_num :
            if self.po_lock:
                myres = myrec.create(
                    {'picking_type_id': 5, 'location_id': myprodloc, 'location_dest_id': mypbookingloc,
                     'move_type': 'direct',
                     'user_id': self.env.uid, 'origin': '(%s)%s 鎖定需求' % (self.po_no, self.cus_name.name),
                     'move_line_ids': [
                         (0, 0,
                          {'product_id': self.product_no.id, 'company_id': 1, 'location_id': myprodloc,
                           'location_dest_id': mypbookingloc, 'product_uom_id': 1,
                           'qty_done': self.prod_onhand})]})

                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()

                myres1 = myrec.create(
                    {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mybbookingloc,
                     'move_type': 'direct',
                     'user_id': self.env.uid, 'origin': '(%s)%s 鎖定需求' % (self.po_no, self.cus_name.name),
                     'move_line_ids': [
                         (0, 0,
                          {'product_id': self.booking_blank.id, 'company_id': 1, 'location_id': myblanklocid,
                           'location_dest_id': mybbookingloc, 'product_uom_id': 1,
                           'qty_done': (self.po_num - self.prod_onhand)})]})

                myres1.action_confirm()
                self.env.cr.commit()
                myres1.action_done()
                self.env.cr.commit()
            if not self.po_no:
                mypono = ' '
            else:
                mypono = self.po_no
            mycusid = self.cus_name.id
            myprodid = self.product_no.id
            odate = self.order_date
            if not self.po_location:
                mypoloc = ' '
            else:
                mypoloc = self.po_location
            mypolock = self.po_lock
            sdate = self.shipping_date
            ponum = self.po_num
            if self.po_lock:
                ppickid = myres.id
            else:
                ppickid = 0
            if self.po_lock:
                bpickid = myres1.id
            else:
                bpickid = 0
            poowner = self.po_owner.id
            self.env.cr.execute("""select genpobooking('%s',%d,%d,'%s','%s',%s,'%s',%s,%d,%d,%d,%s,'%s')""" % (mypono,mycusid,myprodid,odate,mypoloc,mypolock,sdate,ponum,ppickid,bpickid,poowner,self.custom_system,self.po_lock_desc))
            self.env.cr.execute("""commit""")
        elif self.prod_onhand <= 0 :
            if self.po_lock:
                myres = myrec.create(
                    {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mybbookingloc,
                     'move_type': 'direct',
                     'user_id': self.env.uid, 'origin': '(%s)%s 鎖定需求' % (self.po_no, self.cus_name.name),
                     'move_line_ids': [
                         (0, 0,
                          {'product_id': self.booking_blank.id, 'company_id': 1, 'location_id': myblanklocid,
                           'location_dest_id': mybbookingloc, 'product_uom_id': 1,
                           'qty_done': self.po_num})]})

                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()
            if not self.po_no:
                mypono = ' '
            else:
                mypono = self.po_no
            mycusid = self.cus_name.id
            myprodid = self.product_no.id
            odate = self.order_date
            if not self.po_location:
                mypoloc = ' '
            else:
                mypoloc = self.po_location
            mypolock = self.po_lock
            sdate = self.shipping_date
            ponum = self.po_num
            if self.po_lock:
                bpickid = myres.id
            else:
                bpickid = 0
            poowner = self.po_owner.id
            self.env.cr.execute("""select genpobooking('%s',%d,%d,'%s','%s',%s,'%s',%s,%d,%d,%d,%s,'%s')""" % (mypono,mycusid,myprodid,odate,mypoloc,mypolock,sdate,ponum,0,bpickid,poowner,self.custom_system,self.po_lock_desc))
            self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '客戶訂單/庫存鎖定輸入完成！'
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

    @api.onchange('booking_blank')
    def onclientchange(self):
        self.env.cr.execute("""select getblankonhand(%d)""" % self.booking_blank.id)
        self.blank_onhand = self.env.cr.fetchone()[0]

    @api.onchange('cus_name')
    def onchangecusname(self):
        self.env.cr.execute("""select getpartnerprod(%d)""" % self.cus_name.id)
        myrec = self.env.cr.fetchall()
        myids = []
        for rec in myrec:
            myids.append(rec[0])
        return {'domain': {'product_no': [('id', 'in', myids)]}}

    @api.onchange('product_no')
    def onchangebookingprod(self):
        self.env.cr.execute("""select getprodblank(%d)""" % self.product_no.id)
        self.booking_blank = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getprodonhand(%d)""" % self.product_no.id)
        self.prod_onhand = self.env.cr.fetchone()[0]



