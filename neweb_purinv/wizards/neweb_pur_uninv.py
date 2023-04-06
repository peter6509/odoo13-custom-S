# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo import exceptions
# import odoo.addons.decimal_precision as dp


class newebuninvselect(models.TransientModel):
    _name = "neweb.uninvselect"

    uninvoice_list = fields.Many2one('purchase.order', string="採購單號", domain=[('invoice_complete','=',False)])


    def select_pur(self):
        myid = self.env.context.get('invoiceopen_id')
        # print("invoiceopen id:%d" % myid)
        self.env.cr.execute("select getpurinvdata(%s,%s)" % (myid,self.uninvoice_list.id))
        if not myid:
            raise exceptions.UserError("沒有採購內容項目,請確認")
        return {'view_name': 'newebunpurinvselect',
                'name': ('請款資料明細'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_purinv.invoice',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myid,
                'flags': {'action_buttons': True,'initial_mode':'edit' },
                'view_mode': 'form',
                'view_type': 'form'
                }


# class newebunpurinv(models.Model):
#     _name = "neweb.unpurinv"
#
#     name = fields.Char(string="採購單號")
#     invitem_line = fields.One2many('neweb.unpurinvitem','invitem_id',copy=True, string="採購清單")
#
#     @api.multi
#     def noselect(self):
#
#         return {'view_name': 'newebunpurinv',
#                 'name': ('請款作業'),
#                 'views': [[False,'form'], [False, 'tree']],
#                 'res_model': 'neweb_purinv.invoice',
#                 'context': self._context,
#                 'type': 'ir.actions.act_window',
#                 'target': 'main',
#                 'domain': [(1,'=',1)],
#                 'view_mode': 'tree,form',
#                 'view_type': 'tree',
#                 'flags': {'action_buttons': True, },
#                 }
#
#
#
#     @api.multi
#     def selectbtn(self):
#         mypurinvid = self.env.context.get("purinv_id")
#         mypurno = self.env['neweb.unpurinv'].search([('id','=',mypurinvid)]).name
#         mypurchaserec = self.env['purchase.order'].search([('name','=',mypurno)])
#         mypurinvrec = self.env['neweb_purinv.invoice'].search([])
#         # mypitemlistrec = self.env['neweb.pitem_list'].search([])
#         res = mypurinvrec.create({'invoice_partner':mypurchaserec.partner_id.id,'taxes_id':mypurchaserec.taxes_id.id})
#         myrec = self.env['neweb.unpurinvitem'].search([('selectyn','=',True),('prod_sum','>',0)])
#         for rec in myrec:
#             res.write({'invoice_line':[(0,0,{'inv_prodspec':rec.prod_desc,'cus_partner':mypurchaserec.partner_id.comp_sname,
#                                              'purchase_no':mypurno,'pitem_origin_no':rec.pitem_origin_no,'pitem_id':rec.purseq_id,
#                                              'invoice_sum':rec.prod_sum})]})
#             mypitemrec = self.env['neweb.pitem_list'].search([('id','=',rec.purseq_id)])
#             self.env.cr.execute("select updateapselect(%s,%s)" % (rec.purseq_id,True))
#             self.env.cr.execute("commit")
#             # mypitemrec.write({'ap_select':True})
#         self.env.cr.execute("""select checkpurapselect(%d)""" % mypurchaserec.id)
#         self.env.cr.execute("commit")
#
#         return {'view_name': 'newebunpurinv',
#                 'name': ('請款作業'),
#                 'views': [[False, 'form'], [False, 'tree']],
#                 'res_model': 'neweb_purinv.invoice',
#                 'context': self._context,
#                 'type': 'ir.actions.act_window',
#                 'target': 'current',
#                 'res_id': res.id,
#                 'view_mode': 'form',
#                 'view_type': 'form',
#                 'flags':{'action_buttons':True,'initial_mode':'edit'},
#                 }
#
#
#     @api.multi
#     def selectall(self):
#         mypurinvid = self.env.context.get("purinv_id")
#         mypurno = self.env['neweb.unpurinv'].search([('id', '=', mypurinvid)]).name
#         mypurchaserec = self.env['purchase.order'].search([('name', '=', mypurno)])
#
#         mypurinvrec = self.env['neweb_purinv.invoice'].search([])
#         res = mypurinvrec.create(
#             {'invoice_partner': mypurchaserec.partner_id.id, 'taxes_id': mypurchaserec.taxes_id.id})
#         myrec = self.env['neweb.unpurinvitem'].search([('prod_sum', '>', 0)])
#         for rec in myrec:
#             res.write({'invoice_line': [
#                 (0, 0, {'inv_prodspec': rec.prod_desc, 'cus_partner': mypurchaserec.partner_id.comp_sname,
#                         'purchase_no': mypurno, 'pitem_origin_no': rec.pitem_origin_no, 'pitem_id': rec.purseq_id,
#                         'invoice_sum': rec.prod_sum})]})
#             mypitemrec = self.env['neweb.pitem_list'].search([('id', '=', rec.purseq_id)])
#             self.env.cr.execute("select updateapselect(%s,%s)" % (rec.purseq_id, True))
#             self.env.cr.execute("commit")
#             # mypitemrec.write({'ap_select': True})
#         self.env.cr.execute("""select checkpurapselect(%d)""" % mypurchaserec.id)
#         self.env.cr.execute("commit")
#         return {'view_name': 'newebunpurinv',
#                 'name': ('請款作業'),
#                 'views': [[False, 'form'], [False, 'tree']],
#                 'res_model': 'neweb_purinv.invoice',
#                 'context': self._context,
#                 'type': 'ir.actions.act_window',
#                 'target': 'main',
#                 'res_id': res.id,
#                 'view_mode': 'form',
#                 'view_type': 'form',
#                 'flags': {'action_buttons': True, 'initial_mode': 'edit'},
#                 }
#
#
#
# class newebunpurinvitem(models.Model):
#     _name = "neweb.unpurinvitem"
#
#     invitem_id = fields.Many2one('neweb.unpurinv',require=True,ondelete='cascade')
#     purseq_id = fields.Integer(string="源ID")
#     prod_modeltype = fields.Char(string="機種-機型/料號")
#     prod_desc = fields.Char(string="規格說明")
#     prod_num = fields.Float(digits=dp.get_precision('Product Unit of Measure'), string="數量", default=1)
#     prod_price = fields.Float(digits=dp.get_precision('Product Price'), string="單價")
#     prod_sum = fields.Float(digits=dp.get_precision('product sum Price'),string="合計")
#     prod_tax = fields.Many2one('account.tax', string='Taxes')
#     prod_tottax = fields.Float(digits=(10,0),string="合計(含税)")
#     supplier = fields.Many2one('res.partner', string="廠商", domain=[('supplier', '=', True)])
#     selectyn = fields.Boolean(default=False,string="選")
#     pitem_origin_no = fields.Char(string="來源單號")
#
#     @api.multi
#     def get_select(self):
#         for rec in self:
#             if rec.selectyn == True:
#                 rec.update({'selectyn': False})
#             else:
#                 rec.update({'selectyn': True})
#
