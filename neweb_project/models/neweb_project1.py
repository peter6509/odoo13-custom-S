# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebbuscate(models.Model):
    _name = "neweb.buscate"  ## 客戶行業別
    _description = "成本分析客戶行業別基礎配置"
    _order = "sequence,id"

    name = fields.Char(string="行業別", required=True)
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("行業別不能為空值！"))
        if 'name' in vals and vals['name']:
            cname = vals['name']
            nrec = self.env['neweb.buscate'].search([('name', '=', cname)])
            if nrec:
                raise UserError(("行業別 ％s 已重複") % cname)
        rec = super(newebbuscate, self).create(vals)
        return rec


class projcontacttype(models.Model):
    _name = "neweb.contacttype"
    _description = "成本分析人員別基礎配置"
    _order = "sequence,id"

    name = fields.Char(string="人員別", required=True)
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("人員別不能為空值！"))
        if 'name' in vals and vals['name']:
            cname = vals['name']
            nrec = self.env['neweb.contacttype'].search([('name', '=', cname)])
            if nrec:
                raise UserError(("人員別 ％s 已重複") % cname)
        rec = super(projcontacttype, self).create(vals)
        return rec


class newebpartner(models.Model):
    _inherit = "res.partner"
    _description = '合作夥伴基礎配置'

    @api.depends('emp_ids')
    def _get_is_my_partner(self):
        myid = self.env.uid
        ismypartner=False
        for rec in self.emp_ids:
            myrec = self.env['hr.employee'].search([('id','=',rec.id)])
            for rec1 in myrec:
                if rec1.user_id.id == myid:
                    ismypartner=True
            rec.is_my_partner = ismypartner
            return ismypartner


    sno = fields.Char(string="統一編號")
    vat = fields.Char(string="國際稅碼(統編)")
    comp_sname = fields.Char(string="中文簡稱")
    comp_ename = fields.Char(string="英文名稱")
    cate_type = fields.Many2one('neweb.buscate', string="行業別")
    group_name = fields.Char(string="集團名稱")
    proj_pay_type = fields.Selection([('11', '一次付清'),('1', '月初'), ('2', '月末'), ('3', '雙月初'), ('4', '雙月末'),
                                      ('5', '季初'),('6', '季末'), ('7', '半年初'), ('8', '半年末'), ('9', '年初'),
                                      ('10', '年末'), ('12','分期付款'),('13', '其他')], string="專案付款方式", default='11')
    proj_pay = fields.Char(string="付款條件")
    acc_close_day = fields.Char(string="請款日")
    pay_term = fields.Char(string="月結天數")
    payto_date = fields.Char(string="撥款日")
    other_date = fields.Char(string="其他撥款日說明")
    acc_receivable = fields.Selection([('2', '郵寄'), ('3', '電匯'), ('4', '親領')], string="請款方式",default='2')
    post_date = fields.Char(string="郵寄款日")
    post_term = fields.Char(string="郵寄款天期票")
    post_envelop = fields.Selection([('1', '是'), ('2', '否')], string="是否回郵信封")
    tt_date = fields.Char(string="電匯每月日期")
    self_receive_date = fields.Char(string="親領每月日期")
    self_rece_stamp = fields.Selection([('1', "無"), ('2', "收款章"), ('3', "發票章"), ('4', "大小章")], string="親領需攜帶",default='1')
    description = fields.Text(string="說明")
    memo = fields.Text(string="備註")
    is_company = fields.Boolean(string='Is a Company', default=False)
    contact_type = fields.Many2one('neweb.contacttype', string="人員別")
    proj_saleid = fields.Many2many('res.users', 'partner_user_tag_rel', 'partner_id', 'user_id', string="專案負責業務")
    company_type = fields.Selection(string='Company Type',selection=[('person', 'Individual'), ('company', 'Company')], default='person', readonly=False)
    member_ids = fields.Many2many('res.users','partner_user_tag_rel1', 'partner_id', 'user_id', string="專案成本分析業務組員1")
    emp_ids = fields.Many2many('hr.employee', string="專案成本分析業務組員2")
    is_my_partner = fields.Boolean(string="是我的業務夥伴？",compute=_get_is_my_partner)
    cus_payment = fields.Many2one('account.payment.term', string="付款條件")
    pm_ids = fields.Many2many('hr.employee','partner_pm_emp_rel','partner_id','emp_id',string="維運報修通知PM")


class projgencode(models.Model):
    _name = "neweb.projgencode"
    _description = '成本分析流水號編碼'

    name = fields.Char(string="民國年月", required=True)
    gencode = fields.Integer(string="流水號")
    prefixcode = fields.Char(string="區域碼")




class projtransationtype(models.Model):
    _name = "neweb.transationtype"
    _description = '成本分析交易類別基礎配置'
    _order = "sequence,id"

    name = fields.Char(string="交易類別")
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("交易類別不能為空值！"))
        if 'name' in vals and vals['name']:
            cname = vals['name']
            nrec = self.env['neweb.transationtype'].search([('name', '=', cname)])
            if nrec:
                raise UserError(("交易類別 ％s 已重複") % cname)
        rec = super(projtransationtype, self).create(vals)
        return rec




class projprodbrand(models.Model):
    _name = "neweb.prodbrand"
    _description = '成本分析品牌基礎配置'
    _order = "sequence,id"

    name = fields.Char(string="品牌", required=True)
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("品牌不能為空值！"))
        if 'name' in vals and vals['name']:
            cname = vals['name']
            nrec = self.env['neweb.prodbrand'].search([('name', '=', cname)])
            if nrec:
                raise UserError(("品牌 ％s 已重複") % cname)
        rec = super(projprodbrand, self).create(vals)
        return rec

class projselect(models.TransientModel):
    _name = "neweb.proj_select"
    _description = '專案編號精靈選擇暫存檔'

    name = fields.Char(string="專案編號")
    saleitem_line = fields.One2many('neweb.proj_saleitem_select', 'saleitem_id', copy=True)

    # @api.multi
    def myprojselect(self):
        raise UserError("%s" % self.env.context_get('proj_select_id'))

    @api.depends('saleitem_line.active_select')
    def myprojselectall(self):
        for rec in self.saleitem_line:
            rec.active_select = True

    @api.depends('saleitem_line.active_select')
    def myprojselectallnot(self):
        for rec in self.saleitem_line:
            rec.active_select = False


class projsaleitemselect(models.TransientModel):
    _name = "neweb.proj_saleitem_select"
    _description = '成本分析明細精靈選擇暫存檔'

    active_select = fields.Boolean(default=False)
    prod_set = fields.Many2one('neweb.prodset', string="產品組別")
    prod_modeltype = fields.Char(string="機種-機型")
    prod_serial = fields.Char(string="序號")
    prod_no = fields.Char(string="料號")
    prod_desc = fields.Char(string="規格說明")
    prod_num = fields.Integer(string="數量", default=1)
    saleitem_id = fields.Many2one('neweb.proj_select', required=True, ondelete='cascade')

class projbranch(models.Model):
    _name = "neweb.projbranch"
    _description = '成本分析專案前置碼配置'

    name = fields.Char(string="分區")
    prefixcode = fields.Char(string="專案前綴碼")

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("分區不能為空值！"))
        if 'prefixcode' in vals and not vals['prefixcode']:
            raise UserError(("專案前綴碼不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.projbranch'].search([('name', '=', myname)])
            if myrec:
                raise UserError(("分區 => ％s 重複建立了,請確認") % myname)
        if 'prefixcode' in vals and vals['prefixcode']:
            myprefixcode = vals['prefixcode']
            myrec = self.env['neweb.projbranch'].search([('prefixcode', '=', myprefixcode)])
            if myrec:
                raise UserError(("專案前綴碼 => ％s 重複建立了,請確認") % myprefixcode)
        rec = super(projbranch, self).create(vals)
        return rec


class projcosttype(models.Model):
    _name = "neweb.costtype"  ## 專案成本類別
    _description = '成本分析專案成本類別配置'
    _order = "sequence,id"

    name = fields.Char(string="成本類別")
    costtype_sequence = fields.Integer(string="排序")
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("成本類別不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.costtype'].search([('name', '=', myname)])
            if myrec:
                raise UserError(("成本類別 => ％s 重複建立了,請確認") % myname)
        rec = super(projcosttype, self).create(vals)
        return rec

class newebresuser(models.Model):
    _inherit = "res.users"
    _description = '使用者基本配置'

    partner_ids = fields.Many2many('res.partner', 'user_partner_tag_rel', 'user_id', 'partner_id', string="負責客戶群")




