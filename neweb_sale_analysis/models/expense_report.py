# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api,_
from odoo import exceptions


class newebexpense(models.Model):
    _name = "neweb_sale_analysis.expense_report"
    _description = "一般費用申報單"

    @api.depends('emp_no')
    def _get_dept(self):
        for rec in self:
            rec.update({'dept_id': rec.emp_no.department_id.id})

    @api.depends('exp_line')
    def _get_expsum(self):
        totsum = 0
        for rec in self.exp_line:
            totsum += rec.exp_money
        self.exp_sum = totsum
        return totsum
        # self.update({'exp_sum':totsum})

    name = fields.Char(string="費用申報單號",default="New",copy=False)
    emp_no = fields.Many2one('hr.employee',string="員工姓名")
    exp_sum =fields.Float(digits=(6,0),string="費用總金額",store=True,compute=_get_expsum)
    exp_type = fields.Selection([('1','一般'),('2','出差')],string="費用類別",default='1')
    travel_no = fields.Many2one('neweb_sale_analysis.travel_report',string="出差單單號")
    exp_line = fields.One2many('neweb_sale_analysis.expense_line','exp_id',string="費用明細",copy=True,track_visibility="onchange")
    cf_sumline = fields.One2many('neweb_sale_analysis.cf_sumline','exp_id',string="印表統計",copy=False,track_visibility="onchange")
    is_signed = fields.Boolean(string="是否授信",default=False)
    dept_id = fields.Many2one('hr.department',string="部門",compute=_get_dept)
    perm_member = fields.Many2many('hr.employee','hr_employee_expense_report_rel','exp_id','emp_id',string="有權限名單")

    def re_index_item(self):
        self.env.cr.execute("""select explineitem(%d)""" % self.id)
        self.env.cr.execute("""commit""")

    @api.onchange('name')
    def onchangename(self):
        try:
            self.env.cr.execute("""select getemp(%d)""" % self.env.uid)
            myres = self.env.cr.fetchone()[0]
            self.emp_no = myres
        except:
            A=1

    def copy(self, default=None):
        default = dict(default or {})
        default.update({'name':self.env['ir.sequence'].next_by_code('neweb_sale_analysis.expense_report')})
        return super(newebexpense, self).copy(default)


    def re_gen_cfsumline(self):
        self.env.cr.execute("""select runcfsumline(%d)""" % self.id)
        self.env.cr.execute("""commit""")


    def set_signed(self):
    	for rec in self:
    		rec.update({'is_signed':True})

    is_closed = fields.Boolean(string="是否結案",default=False)


    def set_closed(self):
        for rec in self:
            rec.update({'is_closed':True})

    def set_reject(self):
        for rec in self:
            rec.update({'is_closed':False , 'is_signed':False})

    @api.model
    def create(self, vals):
        if vals['exp_type']=='2' and not vals['travel_no']:
            raise exceptions.UserError("費用申報類型為出差,必須選擇出差單號,請確認")
        if 'emp_no' in vals and not vals['emp_no']:
            raise exceptions.UserError("申請人不能空白,請確認")


        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('neweb_sale_analysis.expense_report') or _('New')
        res = super(newebexpense, self).create(vals)
        self.env.cr.execute("""select resortexpense(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select runcfsumline(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genexpperm(%d)""" % res.id)
        self.env.cr.execute("""commit""")

        return res


    def write(self, vals):
        if 'emp_no' in vals and not vals['emp_no']:
            raise exceptions.UserError("申請人不能空白,請確認")

        res = super(newebexpense, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select resortexpense1(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select runcfsumline(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genexpperm(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res



    # @api.onchange('emp_no')
    # def onclientchangeempno(self):
    #     emplist=[]
    #     myrec = self.env['neweb_sale_analysis.travel_report'].search([('emp_id','=',self.emp_no)])
    #     for rec in myrec:
    #         emplist.append(rec.id)
    #         for rec1 in rec.travel_member:
    #             emplist.append(rec1.id)
    #     return {'domain': {'travel_no': [('id', 'in', emplist)]}}





class newebexpenseline(models.Model):
    _name = "neweb_sale_analysis.expense_line"
    _description = "一般費用申報單明細"
    _order = "seq_item"

    @api.depends('exp_event')
    def _get_expevent(self):
        for rec in self:
            if not rec.exp_event:
                rec.expevent=' '
            else:
                rec.expevent = rec.exp_event.name

    @api.depends('exp_attach')
    def _get_expattach(self):
        for rec in self:
            if not rec.exp_attach:
                rec.expattach = ' '
            else:
                rec.expattach = rec.exp_attach.name


    sequence = fields.Integer(string="SEQ",default=20)
    nitem = fields.Integer(string="Item")
    seq_item = fields.Float(disits=(4,1),string="序")
    exp_id = fields.Many2one('neweb_sale_analysis.expense_report',required=True,ondelete='cascade')
    exp_date = fields.Char(size=5,string="日期",required=True,default='-')
    exp_date1 = fields.Date(string="日期",require=True)
    exp_item = fields.Many2one('neweb_sale_analysis.expenseitem',string="項目",required=True)
    exp_event = fields.Many2one('neweb_sale_analysis.expenseevent',string="事由")
    expevent = fields.Char(string="expevent",compute=_get_expevent)
    exp_location = fields.Text(string="地點")
    exp_desc = fields.Text(string="其他說明(參訪客戶/對象)")
    exp_attach = fields.Many2one('neweb_sale_analysis.expensedoc',string="檢附單據")
    expattach = fields.Char(string="expattach",compute=_get_expattach)
    exp_money = fields.Float(digits=(6,0),string="金額")
    exp_update = fields.Boolean(string="update", default=False)





class newebexpenseitem(models.Model):
    _name = "neweb_sale_analysis.expenseitem"
    _description = "一般費用報支項目說明"

    name = fields.Char(string="費用報支項目說明",required=True)
    sequence = fields.Integer(string="SEQ", default=20)



    @api.model
    def create(self, vals):
        myname = vals['name']
        mycount = self.env['neweb_sale_analysis.expenseitem'].search_count([('name','=',myname)])
        if mycount > 0 :
           raise exceptions.UserError("費用報支項目說明已重覆！")
        res = super(newebexpenseitem,self).create(vals)
        return res


class newebexpenseevent(models.Model):
    _name = "neweb_sale_analysis.expenseevent"
    _description = "一般費用報支事由說明"

    name = fields.Char(string="費用報支事由說明",required=True)
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        myname = vals['name']
        mycount = self.env['neweb_sale_analysis.expenseevent'].search_count([('name', '=', myname)])
        if mycount > 0:
            raise exceptions.UserError("費用報支是由說明已重覆！")
        res = super(newebexpenseevent, self).create(vals)
        return res

class newebexpensedoc(models.Model):
    _name = "neweb_sale_analysis.expensedoc"

    name = fields.Char(string="費用報支檢附單據說明",required=True)
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        myname = vals['name']
        mycount = self.env['neweb_sale_analysis.expensedoc'].search_count([('name', '=', myname)])
        if mycount > 0:
            raise exceptions.UserError("費用報支檢附單據說明已重覆！")
        res = super(newebexpensedoc, self).create(vals)
        return res

class newebnewebcfsumline(models.Model):
    _name = "neweb_sale_analysis.cf_sumline"

    @api.depends('sumline_exp_item')
    def _get_sumlinepitem(self):
        for rec in self:
            if not rec.sumline_exp_item:
                rec.sumlineexpitem=' '
            else:
                rec.sumlineexpitem=rec.sumline_exp_item.name

    @api.depends('sum_tot')
    def _get_sumtot(self):
        for rec in self:
            rec.sumtot = '{:,d}'.format(int(rec.sum_tot))



    exp_id = fields.Many2one('neweb_sale_analysis.expense_report', required=True, ondelete='cascade')
    sumline_exp_item = fields.Many2one('neweb_sale_analysis.expenseitem', string="項目")
    sumlineexpitem = fields.Char('sumline',compute=_get_sumlinepitem)
    sum_tot = fields.Float(string="金額合計")
    sumtot = fields.Char(string="sumtot",compute=_get_sumtot)
    exp_update = fields.Boolean(string="update", default=False)



