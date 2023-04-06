# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError



class newebunpurselect(models.TransientModel):
    _name = "neweb.unpurselect"

    unpurchase_list = fields.Many2one('neweb.require_purchase', string=u"申購單號", domain=[('state', '=', '1')])

    def select_pur(self):
        myid = self.unpurchase_list.id
        self.env.cr.execute("select getpurdata(%s)" % myid)
        myid = self.env['neweb.unpur'].search([])
        if not myid:
           raise UserError("沒有需採購項目,請確認")
        return {'view_name': 'newebunpurselect',
                        'name': ('申購明細資料'),
                        'views': [[False, 'form'],[False,'tree'] ],
                        'res_model': 'neweb.unpur',
                        'context': self._context,
                        'type': 'ir.actions.act_window',
                        'target': 'current',
                        'res_id': myid.id,
                        'flags': {'action_buttons': False},
                        'view_mode': 'form',
                        'view_type': 'form'
                        }


class newebunpur(models.Model):
    _name = "neweb.unpur"

    name = fields.Char(string="申購單號")
    require_item = fields.One2many('neweb.unpuritem','pitem_id',copy=True, string="申購清單")



    def selectbtn(self):
        myrec = self.env['neweb.unpuritem'].search([('selectyn','=',True)])
        mypurid = self.env.context.get('pur_op_id')
        for rec in myrec:
            self.env.cr.execute("select genreqline(%s,%s)" % (rec.pseq_id, mypurid))
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

        return {'view_name': 'newebunpur',
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
        myrec = self.env['neweb.unpuritem'].search([])
        mypurid = self.env.context.get('pur_op_id')
        for rec in myrec:
            self.env.cr.execute("select genreqline(%s,%s)" % (rec.pseq_id, mypurid))
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
        return {'view_name': 'newebunpur',
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
        return {'view_name': 'newebunpur',
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



class newebunpuritem(models.Model):
    _name = "neweb.unpuritem"

    pitem_id = fields.Many2one('neweb.unpur',require=True,ondelete='cascade')
    pseq_id = fields.Integer(string="源ID")
    pitem_modeltype = fields.Char(string="機種-機型/料號")
    prod_id = fields.Many2one('product.template',string="庫存料號")
    pitem_serial = fields.Char(string="序號")
    pitem_no = fields.Char(string="料號")
    pitem_desc = fields.Char(string="規格說明")
    pitem_num = fields.Float(digits=(10,0), string="數量", default=1)
    pitem_purnum = fields.Float(digits=(10,0), string="已採購量", default=0)
    pitem_price = fields.Float(digits=(13,2), string="單價")
    supplier = fields.Many2one('res.partner', string="廠商")
    selectyn = fields.Boolean(default=False,string="選")
    pur_memo = fields.Text(string="申購備註")


    def get_select(self):
        for rec in self:
            if rec.selectyn == True:
                rec.update({'selectyn': False})
            else:
                rec.update({'selectyn': True})

