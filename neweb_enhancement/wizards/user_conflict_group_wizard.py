# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class userconflictgroupwizard(models.TransientModel):
    _name = "neweb_enhancement.conflict_group"

    desc = fields.Char(string="描述")

    def conflict_group(self):
        # users = self.env['res.users'].search([])
        # for user in users:
        #     user.groups_id =  [
        #             (3, self.env.ref('base.group_portal').id),
        #             (3, self.env.ref('base.group_public').id),
        #         ]
        # self.env.cr.execute("""delete from res_groups_users_rel where gid=21 and uid >= 259""")
        # self.env.cr.execute("""commit""")
        self.env.cr.execute("""select cktaxdisplay();""")
        self.env.cr.execute("""commit""")

