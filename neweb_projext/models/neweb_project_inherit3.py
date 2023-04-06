# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebprojectinherit3(models.Model):
    _inherit = "neweb.projsaleitem"


    prod_stockoutnum = fields.Float(string="已出貨數量",default=0)
    prod_stockout_complete = fields.Boolean(string="出貨完成否",default=False)
    is_can_update = fields.Boolean()
    not_chiout = fields.Boolean(string="不匯出進銷存",default=False)

    def selectyn(self):
        for rec in self:
            if rec.not_chiout==False:
                rec.not_chiout=True
            else:
                rec.not_chiout=False


    @api.model
    def create(self, vals):
        res = super(newebprojectinherit3, self).create(vals)
        self.env.cr.execute("""update neweb_project set purchase_yn=False where id=%d""" % res.saleitem_id.id)
        return res


    def write(self, vals):
        res = super(newebprojectinherit3, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select checkispur(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            if not (self.env.user.has_group("neweb_project.neweb_sa50_assi") or
                    self.env.user.has_group("neweb_project.neweb_cs30_dir") or
                    self.env.user.has_group("neweb_project.neweb_cs50_assi")) and myres :
                raise UserError("已採購無法異動資料了！")
        return res

    def unlink(self):
        for rec in self:
            self.env.cr.execute("""select checkispur(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            if not (self.env.user.has_group("neweb_project.neweb_sa50_assi") or
                    self.env.user.has_group("neweb_project.neweb_cs30_dir") or
                    self.env.user.has_group("neweb_project.neweb_cs50_assi")) and myres:
                raise UserError("已採購無法刪除了！")
        res = super(newebprojectinherit3, self).unlink()
        return res