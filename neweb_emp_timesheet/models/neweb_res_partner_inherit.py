# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebrespartnerinherit(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        result = []
        for myrec in self:
            # if not myrec.is_company:
            #     myname = u"%s" % myrec.name
            # else:
            #     myname = u"%s,%s" % (myrec.parent_id.name or '-', myrec.name)
            # myname = myrec.name
            if self.env.context.get('show_address1') == True:
                myname = u"%s,%s" % (myrec.name, myrec.street)
            else:
                if self.env.context.get('shortname') == True :
                    myname = u"%s" % myrec.comp_sname
                else:
                    myname = u"%s" % myrec.name
            result.append((myrec.id, myname))
        return result

