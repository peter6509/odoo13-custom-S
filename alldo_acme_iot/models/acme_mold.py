# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo import http
from odoo.http import request, Response
import webbrowser

class acmemold(models.Model):
    _name = "alldo_acme_iot.acme_mold"
    _description = "模具主檔"

    name = fields.Char(string="模具說明",required=True)
    mold_no = fields.Char(string="模具編號",required=True)
    mold_barcode = fields.Char(string="模具條碼")
    mold_ver = fields.Char(string="版次說明")
    partner_id = fields.Many2one('res.partner',string="所屬客戶")
    mold_create_date = fields.Date(string="開模日期")
    mold_supplier_id = fields.Many2one('res.partner', string="開模廠商")
    lifespan_times = fields.Integer(string="模具壽命到期次數設定")
    current_times = fields.Integer(string="目前生產次數")
    maintenance_spantime = fields.Integer(string="下一次保養次數")
    active = fields.Boolean(string="啟用",default=True)
    main_line = fields.One2many('alldo_acme_iot.mold_maintenance_line','mold_id',string="維護明細")
    preprod_line = fields.One2many('alldo_acem_iot.mold_preprod_line', 'mold_id', string="生產模具準備履歷")
    image = fields.Binary('模具文件')
    image_filename = fields.Char("Image Filename")
    mold_cavity = fields.Integer(string="模穴數", default=1)
    work_man = fields.Integer(string="鑄造人數",default=1)

    def run_finereport(self):
        self.env.cr.execute("""select genparai('%s',%d)""" % ('tag.0001',228))
        self.env.cr.execute("""commit""")
        webbrowser.open('http://localhost:8075/webroot/decision/view/report?viewlet=WorkBook1.cpt',new=2,autoraise=True)



    def name_get(self):
        result = []
        for record in self:
            result.append(
                (record.id, '[%s]%s' % (record.mold_no,record.partner_id.name)))
        return result

    @api.onchange('mold_no')
    def onchangemoldno(self):
        self.mold_barcode = self.mold_no

    # @api.model
    # def create(self, vals):
    #     if ''
    #     res = super(acmemold, self).create(vals)
    #     return res


class acmemainline(models.Model):
    _name = 'alldo_acme_iot.mold_maintenance_line'
    _description = "模具維修記錄履歷"

    mold_id = fields.Many2one('alldo_acme_iot.acme_mold',ondelete='cascade')
    main_date = fields.Date(string="維護日期")
    span_times = fields.Integer(string="模具已累計的次數")
    mold_partner = fields.Many2one('res.partner',string="維修廠商")
    main_desc = fields.Text(string="維護說明")
    image = fields.Binary('模具維護文件')
    image_filename = fields.Char("Image Filename")

class acmemoldpreprodline(models.Model):
    _name = "alldo_acem_iot.mold_preprod_line"
    _description = "模具生產前準備履歷"

    mold_id = fields.Many2one('alldo_acme_iot.acme_mold', ondelete='cascade')
    preprod_type = fields.Selection([('P','備模(PREP)'),('L','架模(LOAD)'),('3','烘模(BAKE)')],string="類別")
    preprod_date = fields.Datetime(string="準備日期時間")
    preprod_owner = fields.Many2one('hr.employee',string="責任者")

class acmefinereportpara(models.Model):
    _name = "alldo_acme_iot.finereport_para"
    _description = "FineReport 參數檔"

    finereport_key = fields.Char(string="KEY")
    finereport_cvalue = fields.Char(string="Cvalue")
    finereport_ivalue = fields.Integer(string="Ivalue")






