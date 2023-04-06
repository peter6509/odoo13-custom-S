# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebtodocalendar(models.Model):
    _name = "neweb_emp_timesheet.todo_calendar"
    _description = "工程師待辦事項行事曆"
    _order = "todo_datetime"
    _rec_name = 'todo_name'

    @api.depends('emp_id', 'cus_id', 'todo_origin', 'assign_no','contract_no','todo_dt')
    def _get_todoname(self):
        myname = ''
        mytype = ' '
        for rec in self:
            try:
                if rec.todo_origin == '1':
                    # mytype = '定保 For：%s' % rec.contract_no.name
                    mytype = '定保'
                elif rec.todo_origin == '2':
                    mytype = '報修%s' % rec.todo_dt
                elif rec.todo_origin == '3':
                    mytype = '人力支援派工單'
                elif rec.todo_origin == '4':
                    mytype = '裝機派工單'
                if rec.cus_id.name == False and (rec.todo_origin == '3' or rec.todo_origin == '4'):
                    if not rec.assign_no.proj_cus_name.comp_snam:
                        mycusname = rec.assign_no.proj_cus_name.name
                    else:
                        mycusname = rec.assign_no.proj_cus_name.comp_sname
                else:
                    if not rec.cus_id.comp_sname:
                        mycusname = rec.cus_id.name
                    else:
                        mycusname = rec.cus_id.comp_sname
                if rec.emp_id:
                    myname = "(%s)%s[%s]" % (mytype,mycusname,rec.emp_id.name)
                else:
                    myname = "%s(%s)" % (mycusname, mytype)
                rec.update({'todo_name': myname})
            except Exception as inst:
                rec.update({'todo_name': mytype})

    @api.depends('emp_id')
    def _get_empdept(self):
        return self.emp_id.department_id.id

    @api.depends('todo_datetime')
    def _get_todo_dt(self):
        for rec in self:
            self.env.cr.execute("""select gettododt('%s')""" % rec.todo_datetime)
            mydt=self.env.cr.fetchone()[0]
            rec.todo_dt = mydt
            return mydt

    @api.depends('ins_start_datetime','ins_end_datetime')
    def _get_ins_duration(self):
        for rec in self:
            if not rec.ins_start_datetime or not rec.ins_end_datetime:
                rec.ins_duration = 0.00
            else:
                self.env.cr.execute("""select cal_ins_dur('%s','%s')""" % (rec.ins_start_datetime,rec.ins_end_datetime))
                rec.ins_duration = self.env.cr.fetchone()[0]

    emp_id = fields.Many2one('hr.employee',string="工程師",domain=[('active','=',True)],default=lambda self:self._get_emp())
    todo_datetime = fields.Datetime(string="排定時間")
    todo_dt = fields.Char(string="排定時間",compute=_get_todo_dt)
    dept_id = fields.Many2one('hr.department', string="部門", compute=_get_empdept, store=True)
    cus_id = fields.Many2one('res.partner', string="客戶")
    assign_cus = fields.Char(string="派工客戶")
    todo_origin = fields.Selection([('1','定保'),('2','報修'),('3','人力支援派工單'),('4','裝機派工單')],string="來源單據")
    todo_completed = fields.Selection([('1','完成'),('2','未完成')],string="完成否？",default='2')
    todo_sequence = fields.Integer(string="報工完成回寫源ID")
    repair_no = fields.Many2one('neweb_repair.repair', string="報修單號")
    assign_no = fields.Many2one('neweb.proj_eng_assign',string="人力支援派工單")
    ins_start_datetime = fields.Datetime(string="合約定保開始時間")
    ins_end_datetime = fields.Datetime(string="合約定保結束時間")
    ins_duration = fields.Float(digits=(10,1),string="花費時間",compute=_get_ins_duration)
    ins_memo = fields.Text(string="說明")
    todo_name = fields.Char(compute=_get_todoname)
    contract_no = fields.Many2one('neweb_contract.contract', string="合約編號")
    ae_response_datetime = fields.Datetime(string='工程師回應時間',readonly=True)
    ae_on_site_datetime = fields.Datetime(string='工程師到場時間',readonly=True)
    ae_complete_datetime = fields.Datetime(string='工程師完成時間',readonly=True)

    def _get_emp(self):
        myuid = self.env.uid
        myemprec = self.env['hr.employee'].search([('user_id','=',myuid)])
        if myemprec:
            myres = myemprec[0].id
        else:
            myres = None
        return myres

    def response_button(self):
        if not self.ae_response_datetime:
            self.ae_response_datetime = fields.datetime.now()
            self.env.cr.execute("""select todosetrepairtime(%d,'%s')""" % (self.id,'1'))

    def onsite_button(self):
        if not self.ae_on_site_datetime and self.ae_response_datetime:
            self.ae_on_site_datetime = fields.datetime.now()
            self.env.cr.execute("""select todosetrepairtime(%d,'%s')""" % (self.id, '2'))
        elif not self.ae_response_datetime:
            raise UserError('尚未按工程師回應鈕')

    def complete_button(self):
        if not self.ae_complete_datetime and self.ae_response_datetime and self.ae_on_site_datetime:
            self.ae_complete_datetime = fields.datetime.now()
            self.env.cr.execute("""select todosetrepairtime(%d,'%s')""" % (self.id, '3'))
        elif not self.ae_response_datetime:
            raise UserError('尚未按工程師回應鈕')
        elif not self.ae_on_site_datetime:
            raise UserError('尚未按工程師到場鈕')



    @api.model
    def create(self, vals):
        raise UserError("待辦行事曆無法人為新增！")
        res = super(newebtodocalendar, self).create(vals)
        return res

    def write(self,vals):
        if 'todo_completed' in vals and not ['todo_completed']:
            raise UserError("完成否？ 欄位不能空值！")
        if 'emp_id' in vals :
            raise UserError("待辦行事曆記錄無法變更OWNER工程師！")
        res = super(newebtodocalendar,self).write(vals)
        myuid = self.env.uid
        self.env.cr.execute("""select checktodoinsdate(%d)""" % self.id)
        myres = self.env.cr.fetchone()[0]
        if myres == '2':
            A=1
            # raise UserError("輸入定保日期不能跨兩個日期！")
        elif myres == '3':
            A=2
            # raise UserError("輸入起始時間與截止時間相同！")
        # 改成 postgresql trigger 處理
        #self.env.cr.execute("""select update_todocalendar(%d,%d)""" % (self.id,myuid))
        #self.env.cr.execute("""commit""")
        return res