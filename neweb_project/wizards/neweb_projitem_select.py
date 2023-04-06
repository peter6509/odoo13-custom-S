# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError


class projitemselect(models.TransientModel):
    _name = "neweb.proj_item_select"

    proditem_line = fields.Many2many('neweb.proj_saleitem_select', string="專案明細匯入派工")

    # @api.multi
    def toggle_select(self):
        allrec = self.env['neweb.proj_saleitem_select'].search([])
        myid = self.env.context.get('proj_assign_id')
        myrec = self.env['neweb.proj_eng_assign'].search([('id', '=', myid)])
        for rec in allrec:
            myrec.write({'proj_setup_line': [(0, 0, {'prod_set': rec.prod_set.id, 'prod_modeltype': rec.prod_modeltype,
                                                     'prod_serial': rec.prod_serial, 'prod_no': rec.prod_no,
                                                     'prod_desc': rec.prod_desc, 'prod_num': rec.prod_num})]})

    # @api.multi
    def project_import(self):
        # allrec = self.env['neweb.proj_saleitem_select'].search([('id','in',lambda r:r._get_selectid)])
        myid = self.env.context.get('proj_assign_id')
        myrec = self.env['neweb.proj_eng_assign'].search([('id', '=', myid)])
        for rec in self.proditem_line:
            myrec.write({'proj_setup_line': [(0, 0, {'prod_set': rec.prod_set.id, 'prod_modeltype': rec.prod_modeltype,
                                                     'prod_serial': rec.prod_serial, 'prod_no': rec.prod_no,
                                                     'prod_desc': rec.prod_desc, 'prod_num': rec.prod_num})]})
