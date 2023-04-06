# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError



class newebunprojselect(models.TransientModel):
    _name = "neweb.unprojselect"

    unpurchase_list = fields.Many2one('neweb.project', string="專案單號", domain=[('purchase_yn','=',False)])


    def select_proj(self):
        myid = self.unpurchase_list.id
        self.env.cr.execute("select getprojdata(%s)" % myid)
        myid = self.env['neweb.unproj'].search([])
        if not myid:
            raise UserError("沒有需採購的項目,請確認")
        return {'view_name': 'newebunprojselect',
                'name': ('專案購貨明細資料'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb.unproj',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'res_id': myid.id,
                'flags': {'action_buttons': False},
                'view_mode': 'form',
                'view_type': 'form'
                }


class newebunproj(models.Model):
    _name = "neweb.unproj"

    name = fields.Char(string="專案單號")
    saleitem_line = fields.One2many('neweb.unprojitem','saleitem_id',copy=True, string="專案清單")


    def selectbtn(self):
        myrec = self.env['neweb.unprojitem'].search([('selectyn','=',True)])
        mypurid = self.env.context.get('pur_op_id')
        for rec in myrec:
            self.env.cr.execute("select genprojline(%s,%s)" % (rec.prodseq_id, mypurid))
        genprodid = self.env.ref('neweb_project.neweb_product_purchase_1')
        myownerid = self.env.uid
        myprodid = genprodid.id
        myrec = self.env['purchase.order'].search([('id', '=', mypurid)])

        mytaxesid = myrec.taxes_id
        mypitemrec = self.env['neweb.pitem_list'].search([('pitem_id', '=', mypurid)])
        if mypitemrec:
            self.env.cr.execute("select genpurline(%s,%s,%s,%s);" % (myownerid, mypurid, myprodid, mytaxesid.id))
            self.env.cr.execute("commit;")
            self.env.cr.execute("select genpurchasetaxesid(%s);" % (mypurid))
            self.env.cr.execute("""select getpidno(%d)""" % mypurid)
        myid = self.env['purchase.order'].search([('id','=',mypurid)])
        return {'view_name': 'newebunproj',
                'name': ('採購作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'purchase.order',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myid.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags':{'action_buttons':True,'initial_mode':'edit'},
                }

    def selectall(self):
        myrec = self.env['neweb.unprojitem'].search([])
        mypurid = self.env.context.get('pur_op_id')
        for rec in myrec:
            self.env.cr.execute("select genprojline(%s,%s)" % (rec.prodseq_id, mypurid))
        genprodid = self.env.ref('neweb_project.neweb_product_purchase_1')
        myownerid = self.env.uid
        myprodid = genprodid.id
        myrec = self.env['purchase.order'].search([('id', '=', mypurid)])

        mytaxesid = myrec.taxes_id
        mypitemrec = self.env['neweb.pitem_list'].search([('pitem_id', '=', mypurid)])
        if mypitemrec:
            self.env.cr.execute("select genpurline(%s,%s,%s,%s);" % (myownerid, mypurid, myprodid, mytaxesid.id))
            self.env.cr.execute("commit;")
            self.env.cr.execute("select genpurchasetaxesid(%s);" % (mypurid))
            self.env.cr.execute("""select getpidno(%d)""" % mypurid)
        myid = self.env['purchase.order'].search([('id', '=', mypurid)])
        return {'view_name': 'newebunproj',
                'name': ('採購作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'purchase.order',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myid.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }


    def noselect(self):
        # myrec = self.env['neweb.unpuritem'].search([])
        mypurid = self.env.context.get('pur_op_id')
        # for rec in myrec:
        #     self.env.cr.execute("select genreqline(%s,%s)" % (rec.pseq_id, mypurid))
        myid = self.env['purchase.order'].search([('id', '=', mypurid)])
        return {'view_name': 'newebunproj',
                'name': ('採購作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'purchase.order',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myid.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }



class newebunprojitem(models.Model):
    _name = "neweb.unprojitem"

    saleitem_id = fields.Many2one('neweb.unproj',ondelete='cascade')
    prodseq_id = fields.Integer(string="源ID")
    prod_modeltype = fields.Char(string="機種-機型")
    prod_serial = fields.Char(string="序號")
    prod_no = fields.Char(string="料號")
    prod_desc = fields.Char(string="規格說明")
    prod_num = fields.Float(digits=(10,0), string="數量", default=1)
    prod_purnum = fields.Float(digits=(10,0), string="已採購量", default=0)
    prod_price = fields.Float(digits=(13,2), string="單價")
    supplier = fields.Many2one('res.partner', string="廠商")
    selectyn = fields.Boolean(default=False,string="選")


    def get_select(self):
        for rec in self:
            if rec.selectyn == True:
                rec.update({'selectyn': False})
            else:
                rec.update({'selectyn': True})

