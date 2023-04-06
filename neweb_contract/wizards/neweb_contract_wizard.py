# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime


class newcontractbuild(models.TransientModel):
    _name = "neweb_contract.newcontract_build"

    project_no = fields.Many2one('neweb.project',string="專案編號")

    # project_no = fields.Many2one('neweb.project',string="專案編號",
    #             domain=lambda self:[('contract_build_mark','=',False),
    #             ('transation_type','in',[self.env.ref('neweb_project.neweb_transationtype_4').id,
    #                                      self.env.ref('neweb_project.neweb_transationtype_5').id,
    #                                      self.env.ref('neweb_project.neweb_transationtype_7').id,
    #                                      self.env.ref('neweb_project.neweb_transationtype_8').id,])])

    # @api.model
    def import_from_project(self):
        mycontractid = self.env.context.get('contract_id',False)
        # print "%s" % mycontractid
        myprojid = self.project_no.id
        myprojname = self.project_no.name
        mycount = self.env['neweb_contract.contract'].search_count([('project_no','=',myprojname)])
        if mycount > 0 :
            raise UserError("此成本分析已建立合約了！")
        if mycontractid != False and myprojid != False :
           self._cr.execute("select gen_projtocontract(%s,%d)" % (mycontractid,myprojid))
           self._cr.execute("commit;")
           myprojrec = self.env['neweb.project'].search([('id','=',myprojid)])
           myprojrec.write({'contract_build_mark':True})

        return {'view_name': 'newcontractbuild',
                'name': ('成本分析匯入合約維護作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_contract.contract',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': mycontractid,
                'view_mode': 'form',
                'view_type': 'tree,form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }
