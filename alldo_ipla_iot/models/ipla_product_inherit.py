# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import fields, models, api, _
from odoo.exceptions import UserError, RedirectWarning


class iplaproductinherit(models.Model):
    _inherit = "product.template"

    product_blank = fields.Char(string="鑄件說明")
    product_blank1 = fields.Many2one('product.template',string="鑄件材質")
    eng_line = fields.One2many('alldo_ipla_iot.eng_order', 'prod_id', string="工程別明細", copy=False)
    inspect_line = fields.One2many('alldo_ipla_iot.workorder_inspect', 'product_id', copy=False)
    mold_line = fields.One2many('alldo_ipla_iot.product_mold','product_id',copy=False)
    sale_ok = fields.Boolean('Can be Sold', default=False)
    purchase_ok = fields.Boolean('Can be Purchased', default=False)
    cus_no = fields.Many2one('res.partner', string="所屬客戶")
    prod_version = fields.Char(string="版別")
    blank_weight = fields.Float(digits=(10,3),string="粗胚重量")
    casting_weight = fields.Float(digits=(10,3),string="鑄件重量")
    prod_weight = fields.Float(digits=(10,3),string="成品重量")
    mold_id = fields.Many2one('alldo_ipla_iot.ipla_mold', string="模具編號")
    is_mixmaterial = fields.Boolean(string="是一個混合原料？",default=False)
    ng_ratio = fields.Float(digits=(4,2),string="NG Ratio",default=3.00)

    # def _get_mcategprod(self):
    #     self.env.cr.execute("""select getmcategprod()""")
    #     myrec = self.env.cr.fetchall()
    #     ids = []
    #     for rec in myrec:
    #         ids.append(rec[0])
    #     return  {[('id', 'in', ids)]}
    # #
    # @api.onchange('product_blank1')
    # def onchangebankweight(self):
    #     self.env.cr.execute("""select getmcategprod()""")
    #     myrec = self.env.cr.fetchall()
    #     ids = []
    #     for rec in myrec:
    #         ids.append(rec[0])
    #     return {'domain': {'product_blank1': [('id', 'in', ids)]}}

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
            raise UserError("塑件需要設定模具綁定！")
        if 'blank_weight' in vals and vals['blank_weight'] > 0 and not vals['product_blank1']:
            raise UserError("塑件說明需要綁定！")
        vals['invoice_policy']='delivery'
        res = super(iplaproductinherit, self).create(vals)
        self.env.cr.execute("""select autogencastingeng(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def _write(self, vals):
        res = super(iplaproductinherit, self)._write(vals)
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


class alldoiplaiotproductengorder(models.Model):
    _name = "alldo_ipla_iot.eng_order"
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

    def run_production_real(self):
        self.env.cr.execute("""select genprodrealnum()""")
        self.env.cr.execute("""commit""")


class alldoiplaiotworkorderinspect(models.Model):
    _name = "alldo_ipla_iot.workorder_inspect"
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
    inspect_tool = fields.Many2one('alldo_ipla_iot.measure_tool', string="量測工具")

class alldoiplaiotmold(models.Model):
    _name = "alldo_ipla_iot.product_mold"
    _description = "產品模具"
    _order = "sequence,id"

    sequence = fields.Integer(string="SEQ", default=10)
    eng_type = fields.Char(string="途程編號")
    product_id = fields.Many2one('product.template', ondelete='cascade')
    mold_id = fields.Many2one('alldo_ipla_iot.ipla_mold',string="模具編號")
    active = fields.Boolean(string="啟用",default=True)
