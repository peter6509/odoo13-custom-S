# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudrentNewContractWizard(models.TransientModel):
    _name = "cloudrent.new_contract_wizard"

    project_no = fields.Many2one('cloudrent.household_house', string="案名", required=True)
    member_pid = fields.Char(string="租戶身分證號", required=True)
    contract_type = fields.Selection([('1', '新約'), ('2', '續約')], string="簽約類型", default='1')

    def run_contract_gen(self):
        self.env.cr.execute("""select chk_member(%d,'%s')""" % (self.project_no.id,self.member_pid))
        # mres '1'表新member '2'已建檔 member但此案場不存在 '3'已建檔 member但此案場已存在且入住 '4'已建檔 member但此案場已存在但未入住
        myres = self.env.cr.fetchone()[0]
        if (myres=='1' or myres=='2') and self.contract_type=='2':
            raise UserError("此 身份字號 屬新租戶查無建檔！,不能是續約！,只能選新約！")
        if myres=='3' and self.contract_type=='1':
            raise UserError("此 身份字號是已入住租戶,不能是新約,只能選續約!")

        myrec=self.env['cloudrent.contract']
        recid = myrec.create({'project_no': self.project_no.id, 'member_pid': self.member_pid, 'contract_type': self.contract_type})
        if myres in ('2','3','4'):
            self.env.cr.execute("""select gencontractmember(%d,'%s')""" % (recid.id,myres))
            self.env.cr.execute("""commit""")
        myviewid = self.env.ref('cloudrent_contract.view_contract_form')
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'cloudrent.contract',
            'res_id': recid.id or False,
            'view_id': myviewid.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }



