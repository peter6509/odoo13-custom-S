# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo  import models,fields,api
from odoo.exceptions import UserError

class trackingrepairparts(models.TransientModel):
    _name = "neweb_repair.tracking_parts_wizard"

    prod = fields.Many2one('product.product',string="領用零件",required=True)



    def tracking_parts(self):
        self.env.cr.execute("select trackingparts(%d)" % self.prod.id)
        myrec = self.env.cr.fetchall()
        if myrec:
            myrepair = self.env['neweb_repair.repair'].search([('id','in',myrec[0])])
            ids = []

            for rec in myrepair:
                ids.append(rec.id)
            if myrepair:
                mydomain = []
                mydomain.append(('id', 'in', ids))
        else:
            raise UserError("報修無此料號領用記錄..")


        return {'view_name': '報修記錄',
                'name': ('專報修零組件領用追蹤作業'),

                'res_model': 'neweb_repair.repair',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'domain' : mydomain,
                # 'res_id': myrec.id,
                'view_mode': 'tree,form',
                'view_type': 'form',
                'flags': {'action_buttons': True},
                }


    # mydomain = []
    # mydomain.append(('owner_dept', '=', self.asset_dept.id))
    # return {'view_name': 'newebassetsearchdeptwizard',
    #         'name': ('設備資產依使用單位過濾(使用單位:%s)' % self.asset_dept.name),
    #         'res_model': 'neweb_asset.asset',
    #         'context': self._context,
    #         'type': 'ir.actions.act_window',
    #         'target': 'main',
    #         'domain': mydomain,
    #         'flags': {'form': {'action_buttons': True, 'options': {'mode': 'edit'}}},
    #         'view_mode': 'tree,form',
    #         'view_type': 'form'
    #         }



