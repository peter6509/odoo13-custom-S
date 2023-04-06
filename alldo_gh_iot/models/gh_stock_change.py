# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime

class GHStockChang(models.Model):
    _name = "alldo_gh_iot.stock_change"
    _description = "產品變更料號及庫位"
    _order = "change_date desc"
    _rec_name = "change_date"

    @api.depends('change_line')
    def _get_stock_num(self):
        for rec in self:
            num = 0
            for rec1 in rec.change_line:
                num = num + 1
            rec.change_count = num


    change_date = fields.Date(string="轉換日期",default=datetime.today())
    change_owner = fields.Many2one('res.users',string="轉換人員",default=lambda self:self.env.uid)
    change_memo = fields.Char(string="轉換說明")
    change_line = fields.One2many('alldo_gh_iot.stock_change_line','change_id',copy=False)
    is_change = fields.Boolean(string="是否已過帳?",default=False)
    change_count = fields.Integer(string="筆數",compute=_get_stock_num)
    active = fields.Boolean(string="歸檔",default=True)

    def copy(self, default=None):
        raise UserError("不允許複製程序")
        res = super(GHStockChang, self).copy()
        return res

    def write(self, vals):
        mycount = self.env['alldo_gh_iot.stock_change'].search_count([('id','=',self.id),('is_change','=',True)])
        if mycount > 0:
            raise UserError("已過帳了,不能再異動")
        res = super(GHStockChang, self).write(vals)

        return res


    def unlink(self):
        if self.is_change==True:
            raise UserError("已產生調撥單且驗證了,不能刪除了")
        res = super(GHStockChang, self).unlink()
        return res

    def run_stock_change(self):
        myuserid = self.change_owner.id
        myrec1 = self.env['alldo_gh_iot.company_stockloc'].search([])
        mytransloc = myrec1.trans_loc.id
        myrec = self.env['stock.picking'].search([])
        for rec in self.change_line:
            ## 來源倉(實) 原料號 => 移轉到 trans location(虛) 位置
            myres = myrec.create(
                {'picking_type_id': 5, 'location_id': rec.origin_loc.id, 'location_dest_id': mytransloc,
                 'move_type': 'direct',
                 'user_id': myuserid, 'origin': '轉換產品從成品倉移動到轉換位置', 'partner_id': 1,
                 'move_line_ids': [
                     (0, 0, {'product_id': rec.origin_prod.id, 'company_id': 1, 'location_id': rec.origin_loc.id,
                             'location_dest_id': mytransloc, 'product_uom_id': 1, 'qty_done': rec.trans_num})]})
            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()

            ## trans locatuion(虛) => 移轉到 目的倉(實)位置 轉換後料號
            myres1 = myrec.create(
                {'picking_type_id': 5, 'location_id': mytransloc, 'location_dest_id': rec.complete_loc.id,
                 'move_type': 'direct',
                 'user_id': myuserid, 'origin': '轉換產品從轉換位置移動到毛胚倉', 'partner_id': 1,
                 'move_line_ids': [
                     (0, 0, {'product_id': rec.complete_prod.id, 'company_id': 1, 'location_id': mytransloc,
                             'location_dest_id': rec.complete_loc.id, 'product_uom_id': 1,
                             'qty_done': rec.trans_num})]})
            myres1.action_confirm()
            self.env.cr.commit()
            myres1.action_done()
            self.env.cr.commit()
            rec.update({'trans1_picking':myres.id,'trans2_picking':myres1.id})
        self.write({'is_change':True})

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '物料轉換調撥完成！'
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


    def run_stock_change_archive(self):
        self.env.cr.execute("""update alldo_gh_iot_stock_change set active=false where id=%d""" % self.id)
        self.env.cr.execute("""commit""")

class GHStockChangeLine(models.Model):
    _name = "alldo_gh_iot.stock_change_line"
    _description = "產品變更料號及庫位明細"

    @api.depends()
    def _get_prodloc(self):
        for rec in self:
            myrec = self.env['alldo_gh_iot.company_stockloc'].search([])
            rec.origin_loc = myrec.prod_loc.id

    @api.depends()
    def _get_blankloc(self):
        for rec in self:
            myrec = self.env['alldo_gh_iot.company_stockloc'].search([])
            rec.complete_loc = myrec.blank_loc.id



    change_id = fields.Many2one('alldo_gh_iot.stock_change',ondelete='cascade')
    origin_prod = fields.Many2one('product.product',string="原產品",required=True)
    origin_loc = fields.Many2one('stock.location',string="原庫位",required=True,store=True,default=lambda self:self. _get_prodloc)
    complete_prod = fields.Many2one('product.product',string="轉換後產品",required=True)
    complete_loc = fields.Many2one('stock.location',string="轉換後庫位",required=True,store=True,default=lambda self:self._get_blankloc)
    trans_num = fields.Integer(string="轉換數量")
    trans1_picking = fields.Many2one('stock.picking',string="調撥單1")
    trans2_picking = fields.Many2one('stock.picking',string="調撥單2")

    @api.onchange('origin_prod')
    def onchangeprod(self):
        myrec = self.env['alldo_gh_iot.company_stockloc'].search([])
        self.origin_loc = myrec.prod_loc.id
        self.complete_loc = myrec.blank_loc.id