# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class cloudrentNewContract(models.Model):
    _name = "cloudrent.contract"
    _description = "CloudRent合約管理"
    _order = "project_no,name desc"

    @api.depends('member_pid','house_id')
    def _get_memberno(self):
        for rec in self:
            if not rec.house_id.house_no:
                myhouseno = ' '
            else:
                myhouseno = rec.house_id.house_no
            if not rec.member_pid:
                mymemberpid = ' '
            else:
                mymemberpid = rec.member_pid
            rec.member_no = myhouseno + '-' + mymemberpid

    name = fields.Char(string="合約編號",default='New',copy=False)
    project_no = fields.Many2one('cloudrent.household_house',string="案名",required=True)
    member_pid = fields.Char(string="身分證號",required=True)
    contract_type = fields.Selection([('1','新約'),('2','續約')],string="合約類型",default='1')
    house_id = fields.Many2one('cloudrent.household_house_line', string="入住房間")
    house_id1 = fields.Many2one('cloudrent.household_house_line', string="入住房間(續約)")
    member_no = fields.Char(string="住戶編號")
    member_name = fields.Char(string="住戶姓名")
    member_email = fields.Char(string="EMAIL")
    income_date = fields.Date(string="入住日期")
    start_rental = fields.Date(string="起租日期")
    end_rental = fields.Date(string="退租日期")
    house_rental_fee = fields.Float(digits=(10, 0), string="房屋租金")
    house_rental_desc = fields.Char(string="房屋租金說明")
    house_management_fee = fields.Float(digits=(10, 0), string="房屋管理費")
    house_management_desc = fields.Char(string="房屋管理費說明")
    parking_space_rent = fields.Float(digits=(10, 0), string="車位租金")
    parking_rent_desc = fields.Char(string="車位租金說明")
    parking_management = fields.Float(digits=(10, 0), string="車位管理費")
    parking_management_desc = fields.Char(string="車位管理費說明")
    lo_parking_management = fields.Float(digits=(10, 0), string="機車位管理費")
    lo_parking_desc = fields.Char(string="機車位管理費說明")
    water_fee = fields.Float(digits=(10, 0), string="水費", deault=0)
    member_sex = fields.Selection([('F', '女'), ('M', '男'), ('O', '其他')], string="性別")
    member_age = fields.Selection(
        [('1', '11 - 20'), ('2', '21 - 30'), ('3', '31 - 40'), ('4', '41 - 50'), ('5', '51 - 60'), ('6', '61 - 70'),
         ('7', '71 - 80'), ('8', '81 - 90'), ('9', '90 以上')], string="年齡")
    member_amount = fields.Integer(string="住戶人數")
    member_address1 = fields.Char(string="聯絡地址1")
    member_address2 = fields.Char(string="聯絡地址2")
    member_phone1 = fields.Char(string="聯絡電話1")
    member_phone2 = fields.Char(string="聯絡電話2")
    member_phone3 = fields.Char(string="聯絡電話3")
    member_phone4 = fields.Char(string="聯絡電話4")
    member_desc = fields.Text(string="備註")
    member_deposit = fields.Float(digits=(10, 0), string="租戶押金", default=0)
    states = fields.Selection([('1','草稿'),('2','已生效'),('3','已失效')],string="合約狀態",default='1')
    active = fields.Boolean(string="ACTIVE", default=True)
    contract_attachment = fields.Binary(string="合約PDF")
    user_id = fields.Many2one('res.users', string="使用者")
    contract_emeter_line = fields.One2many('cloudrent.contract_emeter','contract_id',copy=False)
    contract_close_line = fields.One2many('cloudrent.contract_close','contract_id',copy=False)
    member_signature = fields.Char(string="租戶簽名")

    def name_get(self):
        result = []
        for myrec in self:
            if not myrec.house_id1:
                myhouseno = myrec.house_id.house_no
            else:
                myhouseno = myrec.house_id1.house_no
            myname = "[%s]%s-%s" % (myrec.name,myhouseno,myrec.member_name)
            result.append((myrec.id, myname))
        return result

    @api.onchange('member_pid')
    def onclientchangepid(self):
        myrec = self.env['cloudrent.household_member'].search([('member_pid','=',self.member_pid)])
        if myrec:
            self.contract_type='2'
            self.house_id=myrec.house_id.id

    def run_contract_action(self):     # 合約啟動生效
        if not self.member_no:
            raise UserError("""住戶編號不能空值！""")

        if self.contract_type=='2':     # 續約
            self.env.cr.execute("""select gencontractdone(%d,'2')""" % self.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select run_contract_payment(%d)""" % self.id)
            self.env.cr.execute("""commit""")
            # self.env.cr.execute("""select gennewcontractemeter(%d)""" % self.id)
            # self.env.cr.execute("""commit""")
            import datetime
            today = datetime.date.today()
            CurrentDateTime = datetime.datetime.now()
            date = CurrentDateTime.date()
            cyear = date.strftime('%Y')
            payrec = self.env['cloudrent.member_payment']
            myres = payrec.create({'payment_year': cyear, 'member_id': self.house_id.member_id.id, 'house_id': self.house_id.id,'tt_date': today, 'account_date': today})
            self.env.cr.commit()
            self.env.cr.execute("""select genpaydeposit(%d,%d,'%s')""" % (myres.id, self.id, self.member_deposit))
            self.env.cr.execute("""commit""")
            myres.gen_confirm()
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message']='合約啟動生效完成'
            return {
                'name':'Success',
                'type':'ir.actions.act_window',
                'view_type':'form',
                'view_mode':'form',
                'res_model':'sh.message.wizard',
                'views':[(view.id,'form')],
                'view_id':view.id,
                'target':'new',
                'context':context,
                }
        else:         # 新約
            self.env.cr.execute("""select chkcontractemeter(%d)""" % self.id)
            myres = self.env.cr.fetchone()[0]
            if not myres:
                raise UserError("""合約電錶起始度數尚未設定""")

            myrec = self.env['cloudrent.household_member']
            myres = myrec.create({'member_no':self.member_no,'member_name':self.member_name,'member_pid':self.member_pid,
                          'member_email':self.member_email,'income_date':self.income_date,'start_rental':self.start_rental,
                          'end_rental':self.end_rental,'house_rental_fee':self.house_rental_fee,'house_rental_desc':self.house_rental_desc,
                          'house_management_fee':self.house_management_fee,'house_management_desc':self.house_management_desc,
                          'parking_space_rent':self.parking_space_rent,'parking_rent_desc':self.parking_rent_desc,
                          'parking_management':self.parking_management,'parking_management_desc':self.parking_management_desc,
                          'lo_parking_management':self.lo_parking_management,'lo_parking_desc':self.lo_parking_desc,'water_fee':self.water_fee,
                          'member_sex':self.member_sex,'member_age':self.member_age,'member_amount':self.member_amount,
                          'member_address1':self.member_address1,'member_address2':self.member_address2,'member_phone1':self.member_phone1,
                          'member_phone2':self.member_phone2,'member_phone3':self.member_phone3,'member_phone4':self.member_phone4,
                          'member_desc':self.member_desc,'member_deposit':self.member_deposit,'active':True,'house_id':self.house_id.id})

            myres.run_account_payment()  # 展開account payment
            self.env.cr.execute("""select gennewcontractemeter(%d)""" % self.id)
            self.env.cr.execute("""commit""")

            import datetime
            today = datetime.date.today()
            CurrentDateTime = datetime.datetime.now()
            date = CurrentDateTime.date()
            cyear = date.strftime('%Y')
            payrec = self.env['cloudrent.member_payment']
            myres = payrec.create({'payment_year':cyear,'member_id':self.house_id.member_id.id,'house_id':self.house_id.id,'tt_date':today,'account_date':today})
            self.env.cr.commit()
            self.env.cr.execute("""select genpaydeposit(%d,%d,'%s')""" % (myres.id,self.id,self.member_deposit))
            self.env.cr.execute("""commit""")

            myres.gen_confirm()
            self.states='2'
            self.env.cr.execute("""select gencontractdone(%d,'1')""" % self.id)
            self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='租戶合約建立完成'
        return {
            'name':'Success',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }

    def run_contract_deactive(self):   # 合約解約失效
        A=2

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('cloudrent.contract') or _('New')
        res = super(cloudrentNewContract, self).create(vals)
        self.env.cr.execute("""select gencontractemeter(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    @api.onchange('project_no','house_id')
    def onchangeproj(self):
        if self.house_id:
            myrec = self.env['cloudrent.household_house_line'].search([('house_id', '=', self.project_no.id)])
            ids = []
            for item in myrec:
                ids.append(item.id)
            res = {}
            res['domain'] = {'house_id': [('id', 'in', ids)]}
            return res

    def write(self, vals):
        #if self.states=='2':
        #    raise UserError("合約已確認,無法變更資料")
        res = super(cloudrentNewContract, self).write(vals)
        self.env.cr.execute("""select gencontractemeter(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        return res

    def unlink(self):
        if self.states=='2':
            raise UserError("合約已生效確認,無法刪除資料")
        res = super(cloudrentNewContract, self).unlink()
        return res

    def run_contract_active(self):
        A=1


class cloudrentContractEmeter(models.Model):
    _name = "cloudrent.contract_emeter"

    @api.depends('contract_id')
    def _get_emeter_unit(self):
        for rec in self:
            rec.emeter_unit = rec.contract_id.house_id.price_unit

    @api.depends('emeter_id')
    def _get_used_scale(self):
        for rec in self:
            self.env.cr.execute("""select max(used_scale) from cloudrent_household_used_line where used_emeter_id=%d""" % rec.emeter_id.id)
            rec.current_scale = self.env.cr.fetchone()[0]

    # @api.depends('current_scale')
    # def _get_start_scale(self):
    #     for rec in self:
    #         # self.env.cr.execute("""select max(used_scale) from cloudrent_household_used_line where used_emeter_id=%d""" % rec.emeter_id.id)
    #         rec.start_scale = rec.current_scale

    contract_id = fields.Many2one('cloudrent.contract',ondelete='cascade')
    emeter_id = fields.Many2one('cloudrent.household_electric_meter', string="電錶")
    start_scale = fields.Float(digits=(10, 2), string="合約電錶啟始度數")
    current_scale = fields.Float(digits=(10, 2), string="目前電錶度數",compute=_get_used_scale)
    emeter_unit = fields.Float(digits=(5, 1), string="度單價",compute=_get_emeter_unit)


class cloudrentContractCloseLine(models.Model):
    _name = "cloudrent.contract_close"
    _description = "合約解約押金返還明細"

    @api.depends('member_110v_start','member_110v_end','contract_id.contract_emeter_line.emeter_unit')
    def _get_110v_amount(self):
        for rec in self:
            rec.member_110v_amount = round((rec.member_110v_end - rec.member_110v_start) * rec.contract_id.contract_emeter_line[0].emeter_unit)

    @api.depends('member_220v_start', 'member_220v_end', 'contract_id.contract_emeter_line.emeter_unit')
    def _get_220v_amount(self):
        for rec in self:
            rec.member_220v_amount = round((rec.member_220v_end - rec.member_220v_start) * rec.contract_id.contract_emeter_line[0].emeter_unit)

    @api.depends('contract_id.house_id.member_id')
    def _get_110v_current_scale(self):
        for rec in self:
            self.env.cr.execute("""select get_110v_cscale(%d)""" % rec.contract_id.house_id.member_id.id)
            rec.member_110v_end = self.env.cr.fetchone()[0]

    @api.depends('contract_id.house_id.member_id')
    def _get_220v_current_scale(self):
        for rec in self:
            self.env.cr.execute("""select get_220v_cscale(%d)""" % rec.contract_id.house_id.member_id.id)
            rec.member_220v_end = self.env.cr.fetchone()[0]


    @api.depends('contract_id')
    def _get_emeter_complete(self):
        for rec in self:
            self.env.cr.execute("""select get_emeter_complete(%d)""" % rec.contract_id.id)
            rec.member_emeter_complete = self.env.cr.fetchone()[0]

    @api.depends('contract_id')
    def _get_member_deposit(self):
        for rec in self:
            if rec.contract_id:
                try:
                    self.env.cr.execute("""select get_member_deposit(%d)""" % rec.contract_id.id)
                    rec.member_deposit = self.env.cr.fetchone()[0]
                except Exception as inst:
                    rec.member_deposit = 0
            else:
                rec.member_deposit = 0

    @api.depends('member_emeter_complete','member_110v_amount','member_220v_amount')
    def _get_emeter_noncomplete(self):
        for rec in self:
            rec.member_emeter_noncomplete = rec.member_emeter_complete - (rec.member_110v_amount + rec.member_220v_amount)

    @api.depends('contract_id')
    def _get_landlord_noncomplete(self):
        for rec in self:
            rec.member_landlord_noncomplete = rec.contract_id.house_id.member_id.member_account_balance

    @api.depends('member_deposit','member_emeter_noncomplete','member_landlord_noncomplete','member_management_fee','household_clean_fee','other_impairment')
    def _get_return_amount(self):
        for rec in self:
            rec.member_return_amount = rec.member_deposit - rec.member_emeter_noncomplete - rec.member_landlord_noncomplete - rec.member_management_fee - rec.household_clean_fee - rec.other_impairment

    @api.depends('contract_id')
    def _get_110v_start(self):
        for rec in self:
            self.env.cr.execute("""select get110vstart(%d)""" % rec.contract_id.id)
            rec.member_110v_start=self.env.cr.fetchone()[0]

    @api.depends('contract_id')
    def _get_220v_start(self):
        for rec in self:
            self.env.cr.execute("""select get220vstart(%d)""" % rec.contract_id.id)
            rec.member_220v_start = self.env.cr.fetchone()[0]

    @api.depends('contract_id')
    def _get_management_fee(self):
        for rec in self:
            self.env.cr.execute("""select getnonmanagementfee(%d)""" % rec.contract_id.id)
            rec.member_management_fee = self.env.cr.fetchone()[0]

    contract_id = fields.Many2one('cloudrent.contract',ondelete='cascade')
    member_deposit = fields.Float(digits=(10, 0), string="合約押金",compute=_get_member_deposit)
    member_110v_start = fields.Float(digits=(10, 2), string="110V合約啟始度數",compute=_get_110v_start)
    member_110v_end = fields.Float(digits=(10, 2), string="110V目前度數",compute=_get_110v_current_scale)
    member_220v_start = fields.Float(digits=(10, 2), string="220V合約啟始度數",compute=_get_220v_start)
    member_220v_end = fields.Float(digits=(10, 2), string="220V目前度數",compute=_get_220v_current_scale)
    member_110v_amount = fields.Integer(string="110V用電合計金額",compute=_get_110v_amount)
    member_220v_amount = fields.Integer(string="220V用電合計金額",compute=_get_220v_amount)
    member_emeter_complete = fields.Integer(string="已繳電費總計",compute=_get_emeter_complete)
    member_emeter_noncomplete = fields.Integer(string="應繳電費餘額",compute=_get_emeter_noncomplete)
    member_landlord_noncomplete = fields.Integer(string="應繳租金餘額",compute=_get_landlord_noncomplete)
    member_management_fee = fields.Integer(string="尚欠管理費",compute=_get_management_fee)
    household_clean_fee = fields.Integer(string="房務清潔費")
    other_impairment = fields.Integer(string="其他減損")
    member_return_amount = fields.Integer(string="應退回金額計",compute=_get_return_amount)