# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError



class newebunpurchaseitem(models.TransientModel):
    _name = "neweb.unpurchase_item"

    unpurchase_list = fields.Many2one('neweb.require_purchase',string="申購單號",domain=[('state','=','1')])
    require_item = fields.Many2many('neweb.require_purchase_item', string="申購清單")


    @api.onchange('unpurchase_list')
    def onclientchange(self):
        ids=[]
        myrec = self.env['neweb.require_purchase_item'].search([('pitem_id','=',self.unpurchase_list.id)])
        for rec in myrec:
            ids.append(rec.id)
        res = {}
        res['domain'] = {'require_item':[(6,0,ids)]}
        return res
        # self.env.cr.execute("delete from neweb_unpurchase_item")
        # mypurchase = self.env['neweb.unpurchase_item'].search([])
        # mypurchase.create({'unpurchase_list':self.unpurchase_list.id})
        # mypur = self.env['neweb.unpurchase_item'].search([('unpurchase_list','=',self.unpurchase_list.id)])
        # myid = mypur.id
        # myrec = self.env['neweb.require_purchase_item'].search([('pitem_id','=',self.unpurchase_list.id)])
        #
        # for rec in myrec:
        #     self.env.cr.execute("select getunpurchaseitem(%s,%s)" % (myid,rec.id))


    def genrequire_data(self):
        if not self.unpurchase_list:
            raise UserError("未選取申購單號")
        if not self.require_item :
            raise UserError("未選取申購品項")
        mypurid = self.env.context.get('pur_op_id')
        for rec in self.require_item:
            self.env.cr.execute("select genreqline(%s,%s)" % (rec.id,mypurid))
        self.env.cr.execute("""select genpidno(%d)""" % mypurid)


    def genrequire_all(self):
        if not self.unpurchase_list:
            raise UserError("未選取申購單號")
        mypurid = self.env.context.get('pur_op_id')
        myrec = self.env['neweb.require_purchase_item'].search([('pitem_id','=',self.unpurchase_list.id)])
        for rec in myrec:
            self.env.cr.execute("select genreqline(%s,%s)" % (rec.id, mypurid))
        self.env.cr.execute("""select genpidno(%d)""" % mypurid)

#
#
# class newebrequireselectwizard(models.TransientModel):
#     _name = "neweb.require_select"
#
#     name = fields.Char(string=u"申購單號")
#     require_line = fields.One2many('neweb.require_puritem_select','pitem_id', copy=True)
#
# class newebrequirepuritemselectwizard(models.TransientModel):
#     _name = "neweb.require_puritem_select"
#
#     pitem_id =fields.Many2one('neweb.require_select', select=True, required=True, ondelete='cascade')
#     pitem_modeltype = fields.Char(string=u"機種-機型")
#     pitem_serial = fields.Char(string=u"序號")
#     pitem_no = fields.Char(string=u"料號")
#     pitem_desc = fields.Many2one('product.product', string=u"規格說明", required=True)
#     pitem_num = fields.Float(digits=dp.get_precision('Product Unit of Measure'), string=u"數量", default=1)
#     pitem_price = fields.Float(digits=dp.get_precision('Product Price'), string=u"單價")
#     supplier = fields.Many2one('res.partner', string=u"廠商", domain=[('supplier', '=', True)])
#     pitem_budget = fields.Float(digits=dp.get_precision('Product Price'), string=u"預算", store=True,
#                                  track_visibility='always')
#
#     @api.multi
#     def name_get(self):
#         result = []
#         for myrec in self:
#             myprojitem = u"%s | %s | %s | %s | %s | %s | %s" % (
#                 myrec.pitem_modeltype, myrec.pitem_serial, myrec.pitem_no, myrec.pitem_desc.name, myrec.pitem_num,myrec.pitem_price,myrec.supplier.name)
#             result.append((myrec.id, myprojitem))
#         return result
#
#
# class newebrequireimportwizard(models.TransientModel):
#     _name = "neweb.require_item_select"
#
#     require_item = fields.Many2many('neweb.require_puritem_select',string=u"申購清單")
#
#     @api.multi
#     def require_gendata(self):
#         mypur_rec = self.env['purchase.order'].search([('id','=', self.env.conext.get('pur_op_id'))])
#         for req_list in self.require_item :
#             mypur_rec.write({'order_line': [(0,0,{'product_id': req_list.pitem_desc.id,
#                                                   'price_unit': req_list.pitem_price,
#                                                   'product_qty': req_list.pitem_num,
#                                                   'pitem_modeltype' : req_list.pitem_modeltype,
#                                                   'pitem_serial' : req_list.pitem_serial,
#                                                   'pitem_no' : req_list.pitem_no})]})
#         myid = mypur_rec.id
#         return {'view_name': 'newebrequireimportwizard',
#                 'name': (u'採購明細匯入'),
#                 'views': [[False, 'form'],[False,'tree'] ],
#                 'res_model': 'purchase.order',
#                 'context': self._context,
#                 'type': 'ir.actions.act_window',
#                 'target': 'self',
#                 'res_id': myid,
#                 'flags': {'action_buttons': True},
#                 'view_mode': 'form',
#                 'view_type': 'form'
#                 }
#
#
