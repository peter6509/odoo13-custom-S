# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime


class contractinherit(models.Model):
    _inherit = "neweb_contract.contract"

    contract_no = fields.Char(size=20,string="合約編號")
    ae1 = fields.Many2many('hr.employee', string="工程師")
    inspection_line = fields.One2many('neweb_contract.inspection_list','inspection_id',copy=True)
    repaire_line = fields.One2many('neweb_contract.repaire_list','repaire_id',copy=True)
    main_cost = fields.Float(digits=(10,0),string="維護金額")
    main_manpower_cost = fields.Float(digits=(10,0),string="維護人力金額")
    subscribe_build = fields.Boolean(string="是否已展開定保明細")
    dr_line = fields.One2many('neweb_contract.dr_practice','dr_id',copy=True)
    dr_time = fields.Integer(string="回覆演練次數")
    need_training = fields.Boolean(string="是否需教育訊練",default=False)
    training_line = fields.One2many('neweb_contract.training','training_id',copy=True)
    revenue_analysis_mark = fields.Boolean(string="是否已產生專案分攤", default=False)
    routine_maintenance_new = fields.Many2one('neweb.routine_maintenance', string="定期維護條款")
    main_service_rule_new = fields.Many2one('neweb.main_service_rule', string="維護服務時段")
    ae1_name = fields.Char(string="工程師")
    ae1_dept = fields.Char(string="工程師部門")




    is_closed = fields.Boolean(string="是否已結案",default=False)

    # @api.multi
    def set_closed(self):
        for rec in self:
            rec.update({'is_closed':True})

    is_signed = fields.Boolean(string="是否授權",default=False)

    # @api.multi
    def set_signed(self):
    	for rec in self:
    		rec.update({'is_signed':True})

    # @api.multi
    def set_reject(self):
        for rec in self:
            rec.update({'is_closed':False , 'is_signed':False})


    @api.model
    def create(self, vals):
        # if 'contract_no' in vals and not vals['contract_no']:
        #     raise UserError("未輸入合約編號,請確認..")
        if 'contract_no' in vals and vals['contract_no']:
            mycontractno=vals['contract_no']
            mycount=self.env['neweb_contract.contract'].search_count([('contract_no','=',mycontractno)])
            if mycount > 0 :
               raise UserError("合約編號已重複,請確認")
        if 'project_no' in vals and vals['project_no']:
            myprojectno = vals['project_no']
            mycount1 = self.env['neweb_contract.contract'].search_count([('project_no', '=', myprojectno)])
            if mycount1 > 0:
                raise UserError("專案成本分析單號已重複,請確認")

        rec = super(contractinherit, self).create(vals)
        if self.contract_no:
           rec.write({'name':self.contract_no})
        return rec


    def write(self, vals):
        if 'contract_no' in vals and not vals['contract_no']:
            raise UserError("合約編號不能空白,請確認")
        myid=self.id
        rec = super(contractinherit, self).write(vals)
        myrec=self.env['neweb_contract.contract'].search([('id','=',myid)])
        if myrec.contract_no != myrec.name and myrec.contract_no:
            myrec.write({'name': myrec.contract_no})
        return rec


    def subscribe_run(self):
        # print "start step"
        mycontractid = self.env.context.get('contract_id',False)
        mycontractrec = self.env['neweb_contract.contract'].search([('id','=',mycontractid)])
        if mycontractrec.maintenance_start_date == False or mycontractrec.maintenance_end_date == False  :
           raise UserError("起迄時間不完整,請確認!!")
        mystartdate = mycontractrec.maintenance_start_date
        myenddate = mycontractrec.maintenance_end_date
        if mystartdate >= myenddate :
           raise UserError("輸入的維護的起迄日期有問題,請確認!!")

        if mycontractrec.routine_maintenance_new.id == '1':
            inspectionmode = '1'
        elif mycontractrec.routine_maintenance_new.id == '2':
            inspectionmode = '3'
        elif mycontractrec.routine_maintenance_new.id == '3':
            inspectionmode = '2'
        elif mycontractrec.routine_maintenance_new.id == '4':
            inspectionmode = '4'
        else:
            inspectionmode = '5'
        # print "step 1"
        myuid = self.env.uid
        self._cr.execute("select gen_contract_list(%s,%s,%d)" % (mycontractid,inspectionmode,myuid))
        self._cr.execute("commit;")
        self._cr.execute("""select update_plan_ins_calendar(%d,%d)""" % (mycontractid,myuid))
        self._cr.execute("commit;")
        # print "step 2"
        mycontractrec.write({'subscribe_build':True})
        return {'view_name': 'contractinherit',
                'name': ('合約維護作業'),
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


class inspectionlist(models.Model):
    _name = "neweb_contract.inspection_list"
    _description = '定檢明細記錄'

    inspection_id = fields.Many2one('neweb_contract.contract',ondelete='cascade')
    subscribe_date = fields.Date(string="預訂定檢日")
    actual_date = fields.Date(string="實際定檢日")
    inspection_man = fields.Many2many('res.users',string="工程師")
    inspection_memo = fields.Text(string="備註")
    inspection_attach = fields.Many2many('ir.attachment', string="附件")
    subscribe_year = fields.Char(size=4,string="年度")


    def unlink(self):
        myid = self.inspection_id.id
        res = super(inspectionlist,self).unlink()
        self.env.cr.execute("select check_inspection(%s)" % myid)
        self.env.cr.execute("commit")
        return res


class repairelist(models.Model):
    _name = "neweb_contract.repaire_list"
    _description = '報修明細記錄'

    repaire_id = fields.Many2one('neweb_contract.contract',required=True,ondelete='cascade')
    repaire_date = fields.Date(string="報修日期")
    repaire_man = fields.Many2many('res.users',string='工程師')
    repaire_memo = fields.Text(string="備註")
    repaire_attach = fields.Many2many('ir.attachment',string="附件")

class drpractice(models.Model):
    _name = "neweb_contract.dr_practice"
    _description = '回復演練明細記錄'

    dr_id = fields.Many2one('neweb_contract.contract',required=True,ondelete='cascade')
    dr_date = fields.Date(string="回復演練日期")
    dr_description = fields.Text(string="演練說明")
    dr_attach = fields.Many2many('ir.attachment',string="附件")

class training(models.Model):
    _name = "neweb_contract.training"
    _description = '教育訓練明細記錄'

    training_id = fields.Many2one('neweb_contract.contract',required=True,ondelete='cascade')
    training_date = fields.Date(string="教育訓練日期")
    training_desc = fields.Text(string="教育訓練說明")