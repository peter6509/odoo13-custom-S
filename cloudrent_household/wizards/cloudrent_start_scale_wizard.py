# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class cloudrentstartscalewizard(models.TransientModel):
    _name = "cloudrent_household.start_scale_wizard"

    @api.depends()
    def _get_currentym(self):
        self.env.cr.execute("""select max(bill_ym) from cloudrent_household_bill_line""")
        myres=self.env.cr.fetchone()[0]
        self.bill_ym = myres
        return myres

    @api.depends('project_no','house_no','emeter_id','bill_ym')
    def _get_origin_scale(self):
        originscale = 0
        myrec = self.env['cloudrent.household_bill_line'].search([('bill_id','=',self.house_no.id),('bill_ym','=',self.bill_ym),('emeter_id','=',self.emeter_id.id)])
        if not myrec:
            myrec = self.env['cloudrent.household_bill_line_his'].search([('bill_id','=',self.house_no.id),('bill_ym','=',self.bill_ym),('emeter_id','=',self.emeter_id.id)])
            if myrec:
               originscale = myrec.emeter_start_scale
        else:
            originscale = myrec.emeter_start_scale
        self.origin_scale = originscale
        return originscale


    project_no = fields.Many2one('cloudrent.household_house',string="專案別",required=True)
    house_no = fields.Many2one('cloudrent.household_house_line',string="房號",required=True)
    emeter_id = fields.Many2one('cloudrent.household_electric_meter',string="電錶",required=True)
    bill_ym = fields.Char(size=7,string="年月(YYYY-MM)",required=True,default=_get_currentym)
    origin_scale = fields.Float(digits=(13,2),string="原始度數",compute=_get_origin_scale)
    change_scale = fields.Float(digits=(13,2),string="變更度數",required=True)

    @api.onchange('project_no')
    def onchangeprojno(self):
        myrec = self.env['cloudrent.household_house_line'].search([('house_id','=',self.project_no.id)])
        ids=[]
        for rec in myrec:
            ids.append(rec.id)
        return {'domain': {'house_no': [('id', '=', ids)]}}

    @api.onchange('house_no')
    def onchangehouseno(self):
        myrec = self.env['cloudrent.household_electric_meter'].search([('emeter_id','=',self.house_no.id)])
        ids = []
        for rec in myrec:
            ids.append(rec.id)
        return {'domain': {'emeter_id': [('id', '=', ids)]}}

    def run_change_scale(self):
        self.env.cr.execute("""select genemeterchange(%d)""" % self.id)
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '房號：%s 電錶:%s 度數變更成功！' % (self.house_no.house_no,self.emeter_id.emeter_name)
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