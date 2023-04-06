# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo import exceptions


class newebtravel(models.Model):
    _name = "neweb_sale_analysis.travel_report"
    _description = "出差申請報告單"

    @api.depends('travel_member')
    def memberchange(self):
        mymember = ""
        for rec in self.travel_member:
            mymember = mymember + rec.resource_id.name + '/'
        self.travel_man = mymember
        return mymember

    name = fields.Char(size=15,string="表單號碼",copy=False,index=True,default=lambda self: _('New'))
    user_id = fields.Many2one('res.users',string="申請人")
    emp_id = fields.Many2one('hr.employee',string="員工編號")
    ext = fields.Char(size=10,string="分機")
    department_id = fields.Many2one('hr.department',string="部門代號")
    travel_start_date = fields.Date(string="出差啟始日期")
    travel_end_date = fields.Date(string="出差截止日期")
    travel_member = fields.Many2many('hr.employee',string="出差人員")
    travel_man = fields.Text(string="出差人員名字",store=True,compute=memberchange,track_visibility='always')
    travel_addr = fields.Text(string="出差地點")
    travel_event = fields.Text(string="出差事由")
    travel_doc = fields.Text(string="出差報告")
    travel_attach = fields.Many2many('ir.attachment',string="出差報告附件")
    travel_day = fields.Integer(string="出差日數")
    is_signed = fields.Boolean(string="是否授信",default=False)

    @api.onchange('user_id')
    def onchangeuserid(self):
        try:
            self.env.cr.execute("""select getuserdept(%d)""" % self.user_id.id)
            myres = self.env.cr.fetchone()[0]
            self.department_id = myres
        except:
            A=1

    @api.onchange('name')
    def onchangename(self):
        try:
            self.env.cr.execute("""select getemp(%d)""" % self.env.uid)
            myres = self.env.cr.fetchone()[0]
            self.emp_id = myres
            self.user_id = self.env.uid
        except:
            A=1


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


    def copy(self, default=None):
        default = dict(default or {})
        default.update({'name':self.env['ir.sequence'].next_by_code('neweb_sale_analysis.travel_report')})
        return super(newebtravel, self).copy(default)


    @api.model
    def create(self, vals):
        if 'user_id' in vals and not vals['user_id']:
            raise exceptions.UserError("申請人不能空白,請確認")
        if 'emp_id' in vals and not vals['emp_id']:
            raise exceptions.UserError("員工編號不能空白,請確認")
        if 'department_id' in vals and not vals['department_id']:
            raise exceptions.UserError("部門代號不能空白,請確認")

        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('neweb_sale_analysis.travel_report') or _('New')
        res = super(newebtravel,self).create(vals)
        self.env.cr.execute("select computeday(%d)" % res.id)
        self.env.cr.execute("commit")
        return res


    def write(self, vals):
        if 'user_id' in vals and not vals['user_id']:
            raise exceptions.UserError("申請人不能空白,請確認")
        if 'emp_id' in vals and not vals['emp_id']:
            raise exceptions.UserError("員工編號不能空白,請確認")
        if 'department_id' in vals and not vals['department_id']:
            raise exceptions.UserError("部門代號不能空白,請確認")
        res = super(newebtravel, self).write(vals)
        self.env.cr.execute("select computeday(%d)" % self.id)
        self.env.cr.execute("commit")
        return res