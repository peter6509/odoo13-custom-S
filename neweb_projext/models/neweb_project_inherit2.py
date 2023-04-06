# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError,Warning


class newebprojectinherit2(models.Model):
    _inherit = "sale.order"

    credit_limit = fields.Float(string="信用額度")
    credit_rulelist = fields.Text(string="信用條件")
    project_no = fields.Many2one('neweb.project',string="成本分析")


    @api.onchange('partner_id')
    def onchangepartner(self):
        myrec = self.env['res.partner'].search([('id','=',self.partner_id.id)])
        if myrec :
           self.credit_limit = myrec.credit_limit
           self.credit_rulelist = myrec.credit_rulelist
           self.user_id = self.env.uid


    def del_saleorder(self):
        mysaleid = self.env.context.get('saleid')
        mysalecount = self.env['sale.order'].search_count([('id','=',mysaleid),('state','=','draft')])
        if mysalecount > 0:
            myname = self.env['sale.order'].search([('id','=',mysaleid)]).name
            self.env.cr.execute("""delete from sale_order where id=%d""" % mysaleid)
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message']='報價單:%s 已刪除完成！' % myname
            return {
                'name':'刪除成功！',
                'type':'ir.actions.act_window',
                'view_type':'form',
                'view_mode':'form',
                'res_model':'sh.message.wizard',
                'views':[(view.id,'form')],
                'view_id':view.id,
                'target':'new',
                'context':context,
                }
        else:
            raise UserError('此報價單已無法刪除了！')
