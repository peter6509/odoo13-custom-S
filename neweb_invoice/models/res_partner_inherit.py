# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class NewebInvoicePartnerInherit(models.Model):
    _inherit = "res.partner"

    def name_get(self):
        result = []
        for myrec in self:
            if not myrec.is_company:
                myname = "%s" % myrec.name
            else:
                myname = "%s,%s" % (myrec.parent_id.name or '-', myrec.name)
            myname = myrec.name
            if myrec.env.context.get('show_address1') == True:
                myname = "%s,%s" % (myrec.name,myrec.street)
            elif myrec.env.context.get('show_sname') == True and myrec.is_company == True and myrec.comp_sname :
                myname = "%s" % myrec.comp_sname
            else:
                myname = "%s" % myrec.name
            result.append((myrec.id, myname))
        return result
