# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api


class respartnerinherit1(models.Model):
    _inherit = "res.partner"

    survey_mark = fields.Boolean(string="發送滿意度調查?", default=False)


    def name_get(self):
        result = []
        for myrec in self:
            if not myrec.is_company:
                myname = "%s" % myrec.name
            else:
                myname = "%s,%s" % (myrec.parent_id.name or '-', myrec.name)
            myname = myrec.name
            if self.env.context.get('show_address1') == True:
                myname = "%s,%s" % (myrec.name,myrec.street)
            else:
                myname = "%s" % myrec.name
            result.append((myrec.id, myname))
        return result
