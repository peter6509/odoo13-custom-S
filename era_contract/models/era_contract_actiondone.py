# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ERAContractActionDone(models.Model):
    _name = "era.contract_action_done"
    _description = "合約觸發自動排定入租退租程序"

    action_date = fields.Date(string="執行日期")
    action_type = fields.Selection([('IN','租戶入住'),('OUT','租戶退租')],string="執行類別")
    member_id = fields.Many2one('era.household_member',string="租戶")
    contract_id = fields.Many2one('era.contract',string="合約")
    change_houseid = fields.Boolean(string="有換房?",default=False)
    action_status = fields.Selection([('YES','已執行'),('NO','未執行')],default='NO')
    active = fields.Boolean(string="ACTIVE",default=True)

    def run_hour_action(self):   # CRON JOB 每小時執行一次
        self.env.cr.execute("""select gencontractactiondone()""")
        self.env.cr.execute("""commit""")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.action_date, myrec.contract_id.name)
            result.append((myrec.id, myname))
        return result



