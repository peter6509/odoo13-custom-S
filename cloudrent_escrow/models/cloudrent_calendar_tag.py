# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentSaleCalendarTag(models.Model):
    _name = "cloudrent.sale_calendar_tag"
    _description = "業務行事曆標籤"

    name = fields.Char(string="標籤名稱",required=True)
    active = fields.Boolean(string="ACTIVE",default=True)

    @api.model
    def create(self, vals):
        mycount = self.env['cloudrent.sale_calendar_tag'].search_count([('name','=',vals['name'])])
        if mycount > 0:
            raise UserError("""標籤已重複！""")

        res = super(CloudRentSaleCalendarTag, self).create(vals)
        return res


class CloudRentVisitCalendarTag(models.Model):
    _name = "cloudrent.visit_calendar_tag"
    _description = "管理師行事曆標籤"

    name = fields.Char(string="標籤名稱", required=True)
    active = fields.Boolean(string="ACTIVE", default=True)

    @api.model
    def create(self, vals):
        mycount = self.env['cloudrent.visit_calendar_tag'].search_count([('name', '=', vals['name'])])
        if mycount > 0:
            raise UserError("""標籤已重複！""")

        res = super(CloudRentVisitCalendarTag, self).create(vals)
        return res

class CloudRentRepairCalendarTag(models.Model):
    _name = "cloudrent.repair_calendar_tag"
    _description = "修繕行事曆標籤"

    name = fields.Char(string="標籤名稱", required=True)
    active = fields.Boolean(string="ACTIVE", default=True)

    @api.model
    def create(self, vals):
        mycount = self.env['cloudrent.repair_calendar_tag'].search_count([('name', '=', vals['name'])])
        if mycount > 0:
            raise UserError("""標籤已重複！""")

        res = super(CloudRentRepairCalendarTag, self).create(vals)
        return res
