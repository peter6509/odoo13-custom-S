# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebprojectrevenuecost(models.Model):
    _name = "neweb_projectcontract.revenue_cost_analysis"


    sales_id = fields.Many2one('hr.employee',string="業務代表")
    contract_no = fields.Char(string="合約編號")
    project_no = fields.Char(string="專案編號")
    customer_name = fields.Many2one('res.partner',string="客戶名稱")
    start_date = fields.Date(string="開始日期")
    end_date = fields.Date(string="截止日期")
    main_type = fields.Many2one('neweb.routine_maintenance',string="維護方式")
    project_rev_amount = fields.Float(digits=(10,0),string='收入總額(未稅)')
    payment_type = fields.Selection([('1', '一次付清'),('2', '月初'), ('3', '月末'), ('4', '雙月初'), ('5', '雙月末'), ('6', '季初'),
                                      ('7', '季末'), ('8', '半年初'), ('9', '半年末'), ('10', '年初'), ('11', '年末'),
                                       ('12', '其他')], string="付款方式", default='1')
    project_cost_amount = fields.Float(digits=(10,0),string="成本總額(未稅)")
    supplier_name = fields.Many2one('res.partner',string="廠商名稱")
    revenue_line = fields.One2many('neweb_projectcontract.revenue_analysis','revenue_id',copy=True)
    cost_line = fields.One2many('neweb_projectcontract.cost_analysis','cost_id',copy=True)

    @api.model
    def create(self,vals):
        if not vals['contract_no'] or not vals['project_no']:
           raise UserError("合約編號 or 專案編號不能空值")
        if 'contract_no' in vals and vals['contract_no']:
           mycontractno = vals['contract_no']
           mycount = self.env['neweb_projectcontract.revenue_cost_analysis'].search_count([('contract_no','=',mycontractno)])
           if mycount > 0 :
              raise UserError("合約編號已重複,請確認...")
        res=super(newebprojectrevenuecost,self).create(vals)
        res.write({'revenue_analysis_mark':True})
        return res


    def write(self,vals):
        if 'contract_no' in vals and not vals['contract_no']:
           raise UserError("合約編號不能空值")
        if 'project_no' in vals and not vals['project_no']:
           raise UserError("專案編號不能空值,請確認...")
        res = super(newebprojectrevenuecost,self).write(vals)
        return res


    def unlink(self):
        mycontractname = self.contract_no
        self.env.cr.execute("""select getcontractid('%s')""" % mycontractname)
        myres = self.env.cr.fetchone()
        if myres[0] > 0 :
           myrec = self.env['neweb_contract.contract'].search([('id','=',myres[0])])
           if myrec:
              myrec.write({'revenue_analysis_mark':False})
        res = super(newebprojectrevenuecost,self).unlink()
        return res


    def name_get(self):
        result = []
        for myrec in self:
            myprojcontactname = "%s-%s-%s" % (myrec.project_no,myrec.contract_no,myrec.customer_name.name)
            result.append((myrec.id, myprojcontactname))
        return result

    def clear_revenue_cost(self):
        A = 1


    def gen_revenue_cost(self):
        mycontractid = self.env.context.get('contract_id')
        myrec = self.env['neweb_projectcontract.revenue_cost_analysis'].search([('id','=',mycontractid)])
        mycontractno = myrec.contract_no
        #myprojectno = myrec.project_no
        myrec = self.env['neweb_contract.contract'].search([('name','=',mycontractno)])
        mycontractid = myrec.id
        self.env.cr.execute("""select contracthasproject(%d)""" % mycontractid)
        myres = self.env.cr.fetchone()
        if not myres[0]:
            raise UserError("尚未建立成本分析資訊")
        self.env.cr.execute("select gencontractanalysis(%s)" % mycontractid)
        self.env.cr.execute("commit")
        myrec = self.env['neweb_projectcontract.revenue_cost_analysis'].search([('contract_no', '=', mycontractno)])
        mydomain = []
        mydomain.append(('id', '=', myrec.id))

        return {'view_name': 'newebprojtoanalysiswizard',
                'name': ('專案合約分攤維護作業'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb_projectcontract.revenue_cost_analysis',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                # 'domain' : mydomain,
                'res_id': myrec.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }


class newebprojectrevenue(models.Model):
    _name = "neweb_projectcontract.revenue_analysis"

    revenue_id = fields.Many2one('neweb_projectcontract.revenue_cost_analysis',required=True,ondelete='cascade')
    revenue_date = fields.Date(string="日期")
    revenue_amount = fields.Float(digits=(10,1),string="平均分攤金額")
    itemnum = fields.Integer(string="項次")

class newebprojectcost(models.Model):
    _name = "neweb_projectcontract.cost_analysis"

    cost_id = fields.Many2one('neweb_projectcontract.revenue_cost_analysis',required=True,ondelete='cascade')
    cost_date = fields.Date(string="日期")
    vendor_no = fields.Many2one('res.partner',string="供應商")
    purchase_no = fields.Many2one('purchase.order',string="採購單號")
    cost_type = fields.Many2one('neweb_purchase.costtype', string="成本類型")
    cost_amount = fields.Float(digits=(10,1),string="平均分攤金額")
    itemnum = fields.Integer(string="項次")


class newebprojectcontracttemp(models.Model):
    _name = "neweb_projectcontract.costtemp"


    vendor_no = fields.Many2one('res.partner', string="供應商")
    purchase_no = fields.Many2one('purchase.order', string="採購單號")
    cost_type = fields.Many2one('neweb_purchase.costtype', string="成本類型")
    total_amount = fields.Float(digits=(10, 1), string="金額")
