# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import UserError
from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES
import math


class stockpickinginherit(models.Model):
    _inherit = "stock.picking"

    mo_group_id = fields.Integer(string="工單群組ID")
    report_date = fields.Date(string="製表日期")
    report_no = fields.Char(string="ACME出貨單號",copy=False)
    report_memo = fields.Text(string="ACME MEMO",copy=False)

    def button_validate(self):
        self.ensure_one()
        if not self.move_lines and not self.move_line_ids:
            raise UserError(_('Please add some items to move.'))

        # Clean-up the context key at validation to avoid forcing the creation of immediate
        # transfers.
        ctx = dict(self.env.context)
        ctx.pop('default_immediate_transfer', None)
        self = self.with_context(ctx)
        ##  加入包材加入內部調撥單 (原材物料倉 -> 成品倉庫)
        myrec = self.env['alldo_acme_iot.company_stockloc'].search([])
        mymaterialloc = myrec[0].material_loc.id
        myprodloc = myrec[0].prod_loc.id
        mycustomerloc = self.partner_id.property_stock_customer.id
        mypickingtypeid = self.env.context.get('default_picking_type_id')
        mypickingid = self.env.context.get('active_id')
        mystockpickingrec = self.env['stock.picking'].search([('id','=',self.id)])

        if mypickingtypeid == 2 :  # 出貨時
            mybomids = self.env['mrp.bom'].search([('product_tmpl_id','in',[x.id for x in self.move_ids_without_package.product_id.product_tmpl_id])])
            mypackrec = self.env['stock.picking']
            mypackres = mypackrec.create({'picking_type_id': 5, 'location_id': mymaterialloc, 'location_dest_id': myprodloc,
                                  'move_type': 'direct','report_memo':'成品出貨包裝(原料倉調撥至成品倉包裝)',
                                  'user_id': self.env.uid, 'origin': mystockpickingrec.name,})

            for bomline in mybomids:
                myrec1 = self.env['alldo_acme_iot.packaging_line'].search([('bom_id','=',bomline.id)])
                # for rec in myrec1:
                for packageline in self.move_ids_without_package:
                    mynowbomid = self.env['mrp.bom'].search([('product_tmpl_id','=',packageline.product_id.product_tmpl_id.id)])
                    # if mynowbomid == bomline.id:
                    for rec in myrec1:
                        if rec.m_set_qty > 0 and rec.bom_id.id== mynowbomid.id :
                            mypackagingnum = math.ceil(packageline.product_uom_qty/rec.m_set_qty) * rec.c_set_qty
                            if mypackagingnum > 0 :
                                mypackres.write({'move_line_ids': [(0, 0, {'product_id': rec.product_id.id, 'company_id': 1,
                                                                            'location_id': mymaterialloc,
                                                                            'location_dest_id': myprodloc,
                                                                            'product_uom_id': self.product_id.product_tmpl_id.uom_id.id,
                                                                            'qty_done': mypackagingnum,
                                                                            'reference':'do_not_print',})]})
                                mypackres.action_confirm()
                                mypackres.env.cr.commit()
                                mypackres.action_done()
                                mypackres.env.cr.commit()
                # for rec in myrec1:
                for packageline in self.move_ids_without_package:
                    mynowbomid = self.env['mrp.bom'].search([('product_tmpl_id', '=', packageline.product_id.product_tmpl_id.id)])
                    # if mynowbomid == bomline.id:
                    for rec in myrec1:
                        if rec.m_set_qty > 0 and rec.bom_id.id== mynowbomid.id :
                            mypackagingnum = math.ceil(packageline.product_uom_qty/rec.m_set_qty) * rec.c_set_qty
                            if mypackagingnum > 0 :
                                self.write({'move_line_ids': [(0, 0, {'product_id': rec.product_id.id, 'company_id': 1,
                                                                            'location_id': myprodloc,
                                                                            'location_dest_id': mycustomerloc,
                                                                            'product_uom_id': self.product_id.product_tmpl_id.uom_id.id,
                                                                            'qty_done': mypackagingnum,
                                                                            'reference':'do_not_print',})]})


        # print("銷單：%s" % self.origin)
        # print("包材扣帳 default_code:%s" % self.move_ids_without_package.product_id.default_code)
        # print("包材扣帳 quantity_done:%s" % self.move_ids_without_package.quantity_done)
        # add user as a follower
        self.message_subscribe([self.env.user.partner_id.id])

        # If no lots when needed, raise error

        picking_type = self.picking_type_id
        precision_digits = self.env['decimal.precision'].precision_get('Product Unit of Measure')
        no_quantities_done = all(float_is_zero(move_line.qty_done, precision_digits=precision_digits) for move_line in self.move_line_ids.filtered(lambda m: m.state not in ('done', 'cancel')))
        no_reserved_quantities = all(float_is_zero(move_line.product_qty, precision_rounding=move_line.product_uom_id.rounding) for move_line in self.move_line_ids)
        if no_reserved_quantities and no_quantities_done:
            print('You cannot validate a transfer if no quantites are reserved nor done. To force the transfer, switch in edit more and encode the done quantities.')
            # raise UserError(_('You cannot validate a transfer if no quantites are reserved nor done. To force the transfer, switch in edit more and encode the done quantities.'))

        if (picking_type.use_create_lots or picking_type.use_existing_lots) :
            lines_to_check = self.move_line_ids
            if not no_quantities_done:
                lines_to_check = lines_to_check.filtered(
                    lambda line: float_compare(line.qty_done, 0,
                                               precision_rounding=line.product_uom_id.rounding)
                )

            for line in lines_to_check:
                product = line.product_id
                if product and product.tracking != 'none':
                    if not line.lot_name and not line.lot_id :
                        raise UserError(_('You need to supply a Lot/Serial number for product %s.') % product.display_name)

        # Propose to use the sms mechanism the first time a delivery
        # picking is validated. Whatever the user's decision (use it or not),
        # the method button_validate is called again (except if it's cancel),
        # so the checks are made twice in that case, but the flow is not broken

        sms_confirmation = self._check_sms_confirmation_popup()
        if sms_confirmation :
            return sms_confirmation

        if no_quantities_done:
            view = self.env.ref('stock.view_immediate_transfer')
            wiz = self.env['stock.immediate.transfer'].create({'pick_ids': [(4, self.id)]})
            return {
                'name': _('Immediate Transfer?'),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'stock.immediate.transfer',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'res_id': wiz.id,
                'context': self.env.context,
            }

        if self._get_overprocessed_stock_moves() and not self._context.get('skip_overprocessed_check'):
            view = self.env.ref('stock.view_overprocessed_transfer')
            wiz = self.env['stock.overprocessed.transfer'].create({'picking_id': self.id})
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'stock.overprocessed.transfer',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'res_id': wiz.id,
                'context': self.env.context,
            }

        # Check backorder should check for other barcodes
        if self._check_backorder():
            return self.action_generate_backorder_wizard()




        ##
        self.action_done()
        return

    def write(self, vals):
        res = super(stockpickinginherit, self).write(vals)
        for rec in self:
            # self.env.cr.execute("""select gennewshippingno(%d)""" % rec.id)
            # self.env.cr.execute("""commit""")
            if rec.state == 'done':
                self.env.cr.execute("""select updateshippingwkorder(%d)""" % rec.id)
                self.env.cr.execute("""commit""")
        return res

    def run_newshipping_report(self):
        # self.env.cr.execute("""delete from alldo_gh_iot_stockpicking_report""")
        # self.env.cr.execute("""commit""")
        self.env.cr.execute("""update stock_picking set report_no=null where id=%d""" % self.id)
        self.env.cr.execute("""commit""")


    def run_shipping_report(self):
        self.env.cr.execute("""delete from alldo_acme_iot_stockpicking_report""")
        self.env.cr.execute("""commit""")
        if not self.report_no:
            self.env.cr.execute("""select gennewshippingno(%d)""" % self.id)
            myreportno = self.env.cr.fetchone()[0]
        else:
            myreportno = self.report_no
        # print('%s' % myreportno)
        # 舊單

        self.env.cr.execute("""select genoldshipping('%s','1')""" % myreportno)
        self.env.cr.execute("""commit""")

        myrec = self.env['alldo_acme_iot.stockpicking_report'].search([])
        myid = myrec[0].id
        myviewid = self.env.ref('alldo_acme_iot.acme_iot_shipping_report_action')
        return {'view_name': 'acme_iot_shipping_report_action',
                'name': (u'employee info  item Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_acme_iot.stockpicking_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                'view_mode': 'form',
                'view_type': 'form'
                }


class stockpickingreportdata(models.Model):
    _name = "alldo_acme_iot.stockpicking_report"

    @api.depends('report_line')
    def _get_totuntaxamount(self):
        myuntaxamount = 0
        for rec in self.report_line:
            myuntaxamount = myuntaxamount + (rec.prod_num * rec.prod_price)
        self.tot_untax_amount = round(myuntaxamount,0)
        return round(myuntaxamount,0)

    @api.depends('report_line')
    def _get_tottaxamount(self):
        myuntaxamount = 0
        mytaxamount = 0
        for rec in self.report_line:
            myuntaxamount = myuntaxamount + (rec.prod_num * rec.prod_price)
            mytaxamount = mytaxamount + (rec.prod_num * rec.prod_price * (rec.tax_amount/100))
        # mytaxamount = round((myuntaxamount * .05), 0);
        self.tot_tax_amount = round(mytaxamount,0)
        return round(myuntaxamount,0)

    @api.depends('tot_untax_amount', 'tot_tax_amount')
    def _get_totamount(self):
        for rec in self:
            rec.tot_amount = round(rec.tot_untax_amount,0) + round(rec.tot_tax_amount,0)

    partner_id = fields.Many2one('res.partner',string="客戶")
    name = fields.Char(string="出貨單號",default=lambda self: _('New'))
    report_date = fields.Date(string="出貨日期")
    picking_id = fields.Many2one('stock.picking',string="PICKING ID")
    report_line = fields.One2many('alldo_acme_iot.stockpicking_report_line','rep_id',copy=False)
    tot_untax_amount = fields.Float(digits=(11,2),string="出貨總價",compute=_get_totuntaxamount)
    tot_tax_amount = fields.Float(digits=(7,2),string="稅金",compute=_get_tottaxamount)
    tot_amount = fields.Float(digits=(11,2),string="合計總和",compute=_get_totamount)
    report_memo = fields.Char(string="備註")
    report_type = fields.Selection([('1','出貨單'),('2','銷貨單')],string="單據類別",default='1')
    taiwan_receipt = fields.Char(string="發票號碼")




    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('alldo_acme_iot.shipping') or _('New')
    #     res = super(stockpickingreportdata, self).create(vals)
    #     return res


class stockpickingreportline(models.Model):
    _name = "alldo_acme_iot.stockpicking_report_line"

    rep_id = fields.Many2one('alldo_acme_iot.stockpicking_report',ondelete='cascade')
    item = fields.Integer(string="ITEM")
    prod_no = fields.Many2one('product.product',string="料號")
    prod_num = fields.Float(digits=(6,0),string="數量")
    prod_uom = fields.Char(string="單位",default='PCS')
    prod_price = fields.Float(digits=(10,2),string="單價")
    sum_price = fields.Float(digits=(11,2),string="金額合計")
    line_memo = fields.Char(string="說明")
    tax_amount = fields.Float(digits=(10,2),string="TAX")


class stockpickingreportdata1(models.Model):
    _name = "alldo_acme_iot.stockpicking_report1"

    @api.depends('report_line')
    def _get_totuntaxamount(self):
        myuntaxamount = 0
        for rec in self.report_line:
            myuntaxamount = myuntaxamount + (rec.prod_num * rec.prod_price)
        self.tot_untax_amount = round(myuntaxamount,0)
        return round(myuntaxamount,0)

    @api.depends('report_line')
    def _get_tottaxamount(self):
        mytaxamount = 0
        for rec in self.report_line:
            mytaxamount = mytaxamount + (rec.prod_num * rec.prod_price * (rec.tax_amount/100));
        self.tot_tax_amount = round(mytaxamount,0)
        return round(mytaxamount,0)

    @api.depends('tot_untax_amount', 'tot_tax_amount')
    def _get_totamount(self):
        for rec in self:
            rec.tot_amount = round(rec.tot_untax_amount,0) + round(rec.tot_tax_amount,0)

    partner_id = fields.Many2one('res.partner',string="客戶")
    name = fields.Char(string="銷貨單號",default=lambda self: _('New'))
    report_date = fields.Date(string="銷貨日期")
    taiwan_receipt = fields.Char(string="發票號碼")
    picking_id = fields.Many2one('stock.picking',string="PICKING ID")
    report_line = fields.One2many('alldo_acme_iot.stockpicking_report_line1','rep_id',copy=False)
    tot_untax_amount = fields.Float(digits=(12,2),string="銷貨總價",compute=_get_totuntaxamount)
    tot_tax_amount = fields.Float(digits=(10,2),string="稅金",compute=_get_tottaxamount)
    tot_amount = fields.Float(digits=(13,2),string="合計總和",compute=_get_totamount)
    report_memo = fields.Char(string="備註")




    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('alldo_acme_iot.shipping') or _('New')
    #     res = super(stockpickingreportdata, self).create(vals)
    #     return res


class stockpickingreportline1(models.Model):
    _name = "alldo_acme_iot.stockpicking_report_line1"

    rep_id = fields.Many2one('alldo_acme_iot.stockpicking_report1',ondelete='cascade')
    item = fields.Integer(string="ITEM")
    prod_no = fields.Many2one('product.product',string="料號")
    prod_num = fields.Float(digits=(6,0),string="數量")
    prod_uom = fields.Char(string="單位",default='PCS')
    prod_price = fields.Float(digits=(10,2),string="單價")
    price_tax = fields.Float(digits=(9,2),string="稅金")
    sum_price = fields.Float(digits=(13,2),string="金額合計")
    line_memo = fields.Char(string="說明")
    tax_amount = fields.Float(digits=(10, 2), string="TAX")
