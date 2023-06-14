# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import fields, models, api, _
from odoo.exceptions import UserError, RedirectWarning


class acmeproductinherit(models.Model):
    _inherit = "product.template"

    product_blank = fields.Char(string="鑄件說明")
    product_blank1 = fields.Many2one('product.template',string="鑄件材質")
    eng_line = fields.One2many('alldo_acme_iot.eng_order', 'prod_id', string="工程別明細", copy=False)
    inspect_line = fields.One2many('alldo_acme_iot.workorder_inspect', 'product_id', copy=False)
    mold_line = fields.One2many('alldo_acme_iot.product_mold','product_id',copy=False)
    sale_ok = fields.Boolean('Can be Sold', default=False)
    purchase_ok = fields.Boolean('Can be Purchased', default=False)
    cus_no = fields.Many2one('res.partner', string="所屬客戶")
    prod_version = fields.Char(string="版別")
    blank_weight = fields.Float(digits=(10,3),string="粗胚重量")
    casting_weight = fields.Float(digits=(10,3),string="鑄件重量")
    prod_weight = fields.Float(digits=(10,3),string="成品重量")
    mold_id = fields.Many2one('alldo_acme_iot.acme_mold', string="模具編號")
    is_mixmaterial = fields.Boolean(string="是一個混合原料？",default=False)
    ng_ratio = fields.Float(digits=(4,2),string="NG Ratio",default=3.00)
    material_onhand = fields.Float(digits=(10,0),string="原料在手數量",default=0)
    safe_num = fields.Float(digits=(10,0),string="安全存量",default=0)
    is_lowsafe = fields.Boolean(string="低於安全存量")
    prod_pdf = fields.Binary(string="產品圖檔")
    firstprod_checklist = fields.One2many('alldo_acme_iot.first_prod_checklist','checklist_id',string="首件檢查表")
    #########  鑄造作業標準書  #########
    sandcore = fields.Integer(string="砂芯數")
    material = fields.Char(string="材質")
    cave = fields.Integer(string="穴數")
    casting_posture = fields.Char(string="澆鑄姿勢")
    mold_temp = fields.Integer(string="模具溫度(℃)")
    mold_temp_updown = fields.Integer(string="模具溫度上下限(℃)")
    aluminum_temp = fields.Integer(string="鋁湯溫度(℃)")
    aluminum_temp_updown = fields.Integer(string="鋁湯溫度上下限(℃)")
    casting_duration = fields.Integer(string="澆鑄時間(秒)")
    casting_duration_updown = fields.Integer(string="澆鑄時間上下限(秒)")
    open_mold_duration = fields.Integer(string="開模時間(秒)")






    def lowsafealert(self):
        self.env.cr.execute("""select getislowsafe()""")
        self.env.cr.execute("""commit""")


    @api.model
    def create(self, vals):
        if 'default_code' in vals and not vals['default_code']:
            raise UserError("未輸入 料號！")
        if 'default_code' in vals and vals['default_code']:
            mydefaultcode = vals['default_code']
            mycount = self.env['product.product'].search_count([('default_code', '=', mydefaultcode)])
            if mycount > 0:
                raise UserError("料號已重複！")
        if 'default_code' in vals and vals['default_code'] and 'barcode' in vals and not vals['barcode']:
            vals['barcode'] = vals['default_code']
        if 'blank_weight' in vals and vals['blank_weight'] > 0 and not vals['mold_id']:
            raise UserError("鑄件需要設定模具綁定！")
        if 'blank_weight' in vals and vals['blank_weight'] > 0 and not vals['product_blank1']:
            raise UserError("鑄件說明需要綁定！")
        vals['invoice_policy']='delivery'
        res = super(acmeproductinherit, self).create(vals)
        self.env.cr.execute("""select autogencastingeng(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def _write(self, vals):
        res = super(acmeproductinherit, self)._write(vals)
        for rec in self:
            self.env.cr.execute("""select checkprodqcline(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            if not myres:
                raise UserError("產品質檢工程別不存在,請檢查！")
            self.env.cr.execute("""select autogencastingeng(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select setprodengorder(%d)""" % rec.id)
            self.env.cr.execute("""commit""")

        return res


class alldoacmeiotproductengorder(models.Model):
    _name = "alldo_acme_iot.eng_order"
    _description = "產品途程配置"
    _order = "sequence,id"

    sequence = fields.Integer(string="SEQ", default=10)
    prod_id = fields.Many2one('product.template', ondelete='cascade')
    eng_type = fields.Char(string="途程編號")
    is_outsourcing = fields.Boolean(string="委外？",default=False)
    partner_id = fields.Many2one('res.partner',string="委外加工商")
    eng_order = fields.Integer(string="途程序列")
    standard_num = fields.Integer(string="標準量")
    prod_real_num = fields.Integer(string="近三月實際量(H)")
    image = fields.Binary('操作說明')
    image_filename = fields.Char("Image Filename")
    mold_cavity = fields.Integer(string="模穴數",default=1)
    eng_desc = fields.Text(string="途程說明")
    equip_id = fields.Many2one('maintenance.equipment',string="排程機台")


    def run_production_real(self):
        self.env.cr.execute("""select genprodrealnum()""")
        self.env.cr.execute("""commit""")








class alldoacmeiotworkorderinspect(models.Model):
    _name = "alldo_acme_iot.workorder_inspect"
    _description = "工單產品加工檢驗要求"
    _order = "sequence,id"

    sequence = fields.Integer(string="SEQ", default=10)
    eng_type = fields.Char(string="途程別")
    product_id = fields.Many2one('product.template', ondelete='cascade')
    inspect_name = fields.Char(string="名稱")
    inspect_size = fields.Char(string="檢驗尺寸")
    drawing_tolerance = fields.Char(string="圖面公差")
    real_work_size = fields.Char(string="實作尺寸")
    correct_no = fields.Char(string="補正號碼")
    inspect_point = fields.Char(string="量測頻率")
    inspect_tool = fields.Many2one('alldo_acme_iot.measure_tool', string="量測工具")

class alldoacmeiotmold(models.Model):
    _name = "alldo_acme_iot.product_mold"
    _description = "產品模具"
    _order = "sequence,id"

    sequence = fields.Integer(string="SEQ", default=10)
    eng_type = fields.Char(string="途程編號")
    product_id = fields.Many2one('product.template', ondelete='cascade')
    mold_id = fields.Many2one('alldo_acme_iot.acme_mold',string="模具編號")
    active = fields.Boolean(string="啟用",default=True)


class AllDoProdCheckList(models.Model):
    _name = "alldo_acme_iot.first_prod_checklist"
    _description = "生產首件檢查表"
    _order = "checklist_seq"

    checklist_id = fields.Many2one('product.template', ondelete='cascade')
    checklist_seq = fields.Integer(string="SEQ")
    checklist_item = fields.Many2one('alldo_acme_iot.checklist_item',string="檢查項目",required=True)
    checklist_value = fields.Char(string="標準值")


class AllDoAcmeIotChecklistItem(models.Model):
    _name = "alldo_acme_iot.checklist_item"
    _description = "檢查項目"

    name =  fields.Char(string="檢查項目",required=True)

    @api.model
    def create(self, vals):
        if 'name' in vals:
            mycount = self.env['alldo_acme_iot.checklist_item'].search_count([('name', '=', vals['name'])])
            if mycount > 0:
                raise UserError("檢查項目已重複！")
        res = super(AllDoAcmeIotChecklistItem, self).create(vals)
        return res


