# _*_ coding: utf-8 _*_
# Author: Peter Wu

from odoo import models, fields, api
from odoo.osv.orm import except_orm


class mainequipmentinherit(models.Model):
    _inherit = "maintenance.equipment"

    brand = fields.Char(size=20, string=u"廠牌")
    in_date = fields.Date(string=u"進廠日期")
    name_desc = fields.Char(size=20, string=u"機台名稱")
    cost = fields.Float(digits=(10,0),string=u"購價")

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise except_orm(u"資料錯誤", u"未輸入設備名稱資料")
        if 'department_id' in vals and not vals['department_id']:
            raise except_orm(u"資料錯誤", u"未輸入部門資料")
        if 'name' in vals and vals['name']:
            myname = vals['name']
            vals['name'] = myname.upper()
            equip_rec = self.env['maintenance.equipment'].search([('name', 'ilike', myname)])
            if equip_rec:
                raise except_orm(u"資料錯誤", u"機台設備重複 ==> %s" % equip_rec.name)
        rec = super(mainequipmentinherit, self).create(vals)
        return rec

    @api.multi
    def write(self, vals):
        # myid = self.id
        if 'name' in vals and not vals['name']:
            raise except_orm(u"資料錯誤", u"未輸入設備名稱資料")
        if 'department_id' in vals and not vals['department_id']:
            raise except_orm(u"資料錯誤", u"未輸入部門資料")
        if 'name' in vals and vals['name']:
            myname = vals['name']
            vals['name'] = myname.upper()
            equip_rec = self.env['maintenance.equipment'].search([('name', 'ilike', myname)])
            if equip_rec and len(equip_rec) > 1:
                raise except_orm(u"資料錯誤", u"機台設備重複 ==> %s" % myname)
        rec = super(mainequipmentinherit, self).write(vals)
        return rec
