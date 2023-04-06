# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebstockinwizards(models.TransientModel):
    _name = "neweb.stockin_wizard"

    # @api.model
    def _get_purchaseid(self):
        mystockinrec = self.env['stock.picking'].search([('id', '=', self.env.context.get('stockin_op_id'))])
        mypurchaseno = mystockinrec.origin
        mypurchaseid = self.env['purchase.order'].search([('name', '=', mypurchaseno)])
        return mypurchaseid.id


    purchase_no = fields.Many2one('purchase.order',string="選擇採購單",compute='_get_purchaseid')
    purchase_line = fields.Many2many('neweb.pitem_list',string="進貨明細")


    @api.onchange('purchase_no')
    def onchange_client(self):
        mystockinrec = self.env['stock.picking'].search([('id','=',self.env.context.get('stockin_op_id'))])
        mypurchaseno = mystockinrec.origin
        mypurchaseid = self.env['purchase.order'].search([('name','=',mypurchaseno)])
        # print mypurchaseid.id
        ids = []
        myrec = self.env['neweb.pitem_list'].search([('pitem_id', '=', mypurchaseid.id),('pitem_stockin_complete','=',False)])
        for rec in myrec:
            ids.append(rec.id)
        res = {}
        res['domain'] = {'purchase_line': [('id', 'in', ids)]}
        return res

    def trans_stockin_list(self):
        if len(self.purchase_line) == 0 :
            raise UserError("未選取進貨明細資料...")
        mystockid = self.env.context.get('stockin_op_id')
        mystockinrec = self.env['stock.picking'].search([('id', '=', self.env.context.get('stockin_op_id'))])
        mystockinrec.write({'stockin_checkyn': False})
        for line in self.purchase_line:
            print ("%s,%s" % (line.id,mystockid))
            self.env.cr.execute("select genstockinline(%s,%s)" % (line.id,mystockid))


    def trans_stockin_all(self):
        mystockid = self.env.context.get('stockin_id')
        mypurorder = self.env['neweb.stockin_wizard'].search([('id','=',mystockid)])

        mypurchaseid = self.env['purchase.order'].search([('name', '=', mypurorder.purchase_no)])
        myrec = self.env['neweb.pitem_list'].search(
            [('pitem_id', '=', mypurchaseid.id), ('pitem_stockin_complete', '=', False)])

        for line in myrec:
            self.env.cr.execute("select genstockinline(%s,%s)" % (line.id, mystockid))
