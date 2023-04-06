# -*- encoding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebprojtoanalysiswizard(models.TransientModel):
    _name = "neweb_projectcontract.contract_to_analysis_wizard"

    contract_no = fields.Many2one('neweb_contract.contract',domain=lambda self:[('revenue_analysis_mark','=',False),('maintenance_start_date','!=',False),('maintenance_end_date','!=',False)],string="合約編號")



    def contractgenanalysis_run(self):

       contractid = self.contract_no.id
       contractno = self.contract_no.name
       self.env.cr.execute("""select contracthasproject(%d)""" % contractid)
       myres = self.env.cr.fetchone()
       if not myres[0]:
           raise UserError("尚未建立成本分析資訊")
       self.env.cr.execute("select gencontractanalysis(%s)" % contractid)
       # self.env.cr.execute("commit")
       myrec = self.env['neweb_projectcontract.revenue_cost_analysis'].search([('contract_no','=',contractno)])
       mydomain=[]
       mydomain.append(('id','=',myrec.id))


       return {'view_name': 'newebprojtoanalysiswizard',
               'name': ('專案合約分攤維護作業'),
               'views': [[False, 'form'],],
               'res_model': 'neweb_projectcontract.revenue_cost_analysis',
               'context': self._context,
               'type': 'ir.actions.act_window',
               'target': 'main',
               #'domain' : mydomain,
               'res_id' : myrec.id,
               'view_mode': 'form',
               'view_type': 'form',
               'flags': {'action_buttons': True,'initial_mode':'edit'},
              }
