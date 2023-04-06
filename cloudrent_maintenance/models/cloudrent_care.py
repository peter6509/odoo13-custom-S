# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class CloudRentCre(models.Model):
    _name = "cloudrent.member_care"
    _description = "租戶訪視記錄"

    care_date = fields.Date(string="訪視日期")
    care_date1 = fields.Char(string="訪視日期")
    care_man = fields.Many2one('res.users',string="訪視人員",default=lambda self:self.env.uid)
    house_id = fields.Many2one('cloudrent.household_house_line',string="租房")
    member_id = fields.Many2one('cloudrent.household_member',string="租戶")
    care_text = fields.Text(string="訪視狀況說明")
    care_img1 = fields.Binary(string="照片一")
    care_img2 = fields.Binary(string="照片二")
    care_img3 = fields.Binary(string="照片三")


class CloudRentHouseholdMemberInherit(models.Model):
    _inherit = "cloudrent.household_member"

    care_line = fields.One2many('cloudrent.member_care','member_id',copy=False)
