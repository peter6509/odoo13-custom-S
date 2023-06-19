# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebcontractinherit1(models.Model):
    _inherit = "neweb_contract.contract"


    routine_maintenance_new = fields.Many2one('neweb.routine_maintenance',string="定期維護條款")
    main_service_rule_new = fields.Many2one('neweb.main_service_rule',string="維護服務時段")


    @api.model
    def create(self, vals):

        res = super(newebcontractinherit1,self).create(vals)
        self.env.cr.execute("""select gen_warn_user(%d)""" % res.id)
        self.env.cr.execute("""select check_inspection_method(%d)""" % res.id)
        self.env.cr.execute("""select satisfaction_check(%d)""" % res.id)
        return res


    def write(self, vals):
        # if 'routine_maintenance_new' in vals and not vals['routine_maintenance_new'] :
        #     raise UserError("定期維護條款不能空值,請確認...")
        # if 'main_service_rule_new' in vals and not vals['main_service_rule_new'] :
        #     raise UserError("維護服務時段不能空值,請確認...")
        res = super(newebcontractinherit1,self).write(vals)
        if self.routine_maintenance_new == False :
            raise UserError("定期維護條款不能空值,請確認...")
        if self.main_service_rule_new == False :
            raise UserError("維護服務時段不能空值,請確認...")
        self.env.cr.execute("""select gen_warn_user(%d)""" % self.id)
        self.env.cr.execute("""select check_inspection_method(%d)""" % self.id)
        self.env.cr.execute("""select satisfaction_check(%d)""" % self.id)
        self.env.cr.execute("""select gencontractae1(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        return res

    def gen_contract_line1byid(self):
        self.env.cr.execute("""select gencontractline1byid(%d)""" % self.id)
        self.env.cr.execute("""commit""")
