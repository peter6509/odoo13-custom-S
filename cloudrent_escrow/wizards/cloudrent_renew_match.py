# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentRenewMatch(models.TransientModel):
    _name = "cloudrent.renew_match"
    _description = "媒合合約續約作業"

    match_type = fields.Selection([('1','新約 to 續一'),('2','續一 to 續二')],string="續約類型",required=True)
    match_no = fields.Many2one('cloudrent.contract_match',string="媒合編號",required=True)

    @api.onchange('match_type')
    def onchangematchtype(self):
        myids = []
        if self.match_type == '1':
            myrec = self.env['cloudrent.contract_match'].search([('lessee_renew1','=',False),('lessee_renew2','=',False),('match_enable','=',True)])
            for rec in myrec:
                myids.append(rec.id)
        else:
            myrec = self.env['cloudrent.contract_match'].search([('lessee_renew1', '=', True), ('lessee_renew2', '=', False),('match_enable','=',True)])
            for rec in myrec:
                myids.append(rec.id)
        return {'domain': {'match_no': [('id', 'in', myids)]}}

    def run_renew_match(self):
        myrec = self.env['cloudrent.contract_match'].search([('id', '=', self.match_no.id)])
        self.env.cr.execute("""select checkrenewstatus(%d)""" % self.match_no.id)
        myres = self.env.cr.fetchone()[0]
        if myres in ('0','1'):  # 新約 -> 續一
            mynewrec = myrec.sudo().copy()
            self.env.cr.execute("""select gen_contract_renew(%d,%d)""" % (self.match_no.id,mynewrec.id))
            self.env.cr.execute("""commit""")
            return {'view_name': 'CloudRent_Renew_Match',
                    'name': ('CloudRent_Renew_Match'),
                    'views': [[False, 'form'], [False, 'tree']],
                    'res_model': 'cloudrent.contract_match',
                    'context': self._context,
                    'type': 'ir.actions.act_window',
                    'target': 'self',
                    'res_id': mynewrec.id,
                    'view_mode': 'form',
                    'view_type': 'form',
                    'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                    }
        elif myres == '2': # 續二 已無法再做補助申請了
            raise UserError("""此合約已經(續二)了,無法再補助申請!""")
