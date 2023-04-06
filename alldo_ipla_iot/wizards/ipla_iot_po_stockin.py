# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class iplaiotpostockin(models.TransientModel):
    _name = "alldo_ipla_iot.po_stockin_wizard"
    _description = "製造生產單完工入庫"

    po_id = fields.Many2one('alldo_ipla_iot.po_wkorder',string="客戶訂單")
    mo_no = fields.Many2one('alldo_ipla_iot.workorder', string="入庫工單")
    wo_no = fields.Many2one('mrp.production',string="製造生產單")
    product_no = fields.Many2one('product.product',string="產品",required=True)
    pre_prod_num = fields.Float(string="未入庫生產數")
    ng_num = fields.Float(string="NG數量")
    prod_num = fields.Float(digits=(10,2),string="良品入庫數",compute='_get_stockinnum')
    is_close = fields.Boolean(string="是否已完工結案？",default=False)
    stockin_owner = fields.Many2one('res.users',string="入帳人員",default=lambda self:self.env.uid)



    @api.depends('pre_prod_num','ng_num')
    def _get_stockinnum(self):
        self.prod_num = self.pre_prod_num - self.ng_num


    @api.onchange('product_no')
    def onchangeproductno(self):
        myrec = self.env['alldo_ipla_iot.workorder'].search([('product_no','=',self.product_no.id),('state','not in',['4','5'])])
        ids=[]
        for rec in myrec:
            ids.append(rec.id)
        return {'domain': {'mo_no': [('id', 'in', ids)]}}

    @api.onchange('po_id')
    def onclientchangepo(self):
        self.env.cr.execute("""select getpoprod(%d)""" % self.po_id.id)
        myprodid = self.env.cr.fetchone()[0]
        return {'domain': {'product_no': [('id', '=', myprodid)]}}

    @api.onchange('mo_no')
    def onclientchangepo(self):
        self.wo_no = self.mo_no.mrp_prod_id.id
        self.env.cr.execute("""select getmopreprodnum(%d)""" % self.mo_no.id)
        self.pre_prod_num = self.env.cr.fetchone()[0]


    def run_po_stockin(self):
        ## 產線線邊倉
        myuncompletelocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].uncomplete_loc.id
        ## 毛胚倉
        myblanklocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].blank_loc.id
        if self.prod_num > 0 or self.ng_num > 0 :
            myrec = self.env['stock.picking'].search([])
            myres = myrec.create({'picking_type_id':5,'location_id':myuncompletelocid,'location_dest_id':myblanklocid,'move_type':'direct',
                                  'user_id':self.stockin_owner.id,'origin':self.mo_no.name,
                                  'move_line_ids':[(0,0,{'product_id':self.product_no.id,'company_id':1,'location_id':myuncompletelocid,
                                                 'location_dest_id':myblanklocid,'product_uom_id': self.product_no.product_tmpl_id.uom_id.id,'qty_done':self.prod_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            mywkrec = self.env['alldo_ipla_iot.workorder'].search([('id','=',self.mo_no.id)])
            mywkprodinnum = mywkrec.prodin_num + self.prod_num
            mywkrec.write({'prodin_num': mywkprodinnum})

            if self.ng_num > 0 :
                self.env.cr.execute("""select genwkorderqcrecord(%d,%s)""" % (self.mo_no.id,self.ng_num))
                self.env.cr.execute("""commit""")
                self.env.cr.execute("""select postockinqcline(%d,%s,%s)""" % (self.mo_no.id,self.pre_prod_num,self.ng_num))
                self.env.cr.execute("""commit""")




        if self.is_close==True:  # 工單全數完工
            self.env.cr.execute("""select setallmoclose(%d)""" % self.mo_no.id)
            self.env.cr.execute("""commit""")
            myworec = self.env['mrp.production'].search([('id','=',self.mo_no.mrp_prod_id.id)])
            if myworec:
                myworec.button_mark_done()
                self.env.cr.commit()

        self.env.cr.execute("""select completepreprodnum(%d)""" % self.mo_no.id)
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '工單產品入庫完成輸入完成！'
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
