# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models

class ir_attachment_check(models.Model):
    _inherit = 'ir.attachment'

    def check(self, cr, uid, ids, mode, context=None, values=None):
        res_ids = {}
        if ids:
            if isinstance(ids, (int, long)):
                ids = [ids]
            cr.execute('SELECT DISTINCT res_model, res_id, create_uid FROM ir_attachment WHERE id = ANY (%s)', (ids,))
            for rmod, rid, create_uid in cr.fetchall():
                if not (rmod and rid):
                    continue
                res_ids.setdefault(rmod,set()).add(rid)
        if values:
            if values.get('res_model') and values.get('res_id'):
                res_ids.setdefault(values['res_model'],set()).add(values['res_id'])
        ima = self.pool.get('ir.model.access')
        for model, mids in res_ids.items():
            # ignore attachments that are not attached to a resource anymore when checking access rights
            # (resource was deleted but attachment was not)
            if not self.pool.get(model):
                continue
            existing_ids = self.pool[model].exists(cr, uid, mids)
            ima.check(cr, uid, model, mode)
            self.pool[model].check_access_rule(cr, uid, existing_ids, mode, context=context)
