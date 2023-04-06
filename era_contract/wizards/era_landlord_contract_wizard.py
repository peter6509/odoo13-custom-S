# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class EraLandlordContractWizard(models.TransientModel):
    _name = "era.landlord_contract_wizard"

    landlord_pid = fields.Char(string="房東身分證號", required=True)
    landlord_name = fields.Char(string="房東姓名", required=True)
    contract_type = fields.Selection([('1', '新約'), ('2', '續約')], string="簽約類型", default='1')

    def run_landlord_contract_gen(self):
        self.env.cr.execute("""select chk_landlord('%s')""" % (self.landlord_pid))
        # mres '1'表新landlord '2'已建檔 landlord
        myres = self.env.cr.fetchone()[0]
        if myres=='1' and self.contract_type=='2':
            raise UserError("此 房東身份字號 查無建檔！,不能是續約！,只能選新約！")
        if myres=='2' and self.contract_type=='1':
            raise UserError("此 身份字號是已簽約房東,不能是新約,只能選續約!")

        myrec=self.env['era.landlord_contract']
        recid = myrec.create({'landlord_pid': self.landlord_pid,'landlord_name':self.landlord_name, 'contract_type': self.contract_type})
        if myres == '2' :  # 續約
            self.env.cr.execute("""select gencontractlandlord(%d)""" % (recid.id))
            self.env.cr.execute("""commit""")
        myviewid = self.env.ref('era_contract.view_landlord_contract_form')
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'era.landlord_contract',
            'res_id': recid.id or False,
            'view_id': myviewid.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }


