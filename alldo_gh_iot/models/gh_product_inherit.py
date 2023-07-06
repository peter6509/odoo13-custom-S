# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import fields, models, api, _
from odoo.exceptions import UserError, RedirectWarning


class ghproductinherit(models.Model):
    _inherit = "product.template"

    product_blank = fields.Char(string="毛胚")
    blank_no = fields.Many2one('product.product', string="毛胚料號")
    eng_line = fields.One2many('alldo_gh_iot.eng_order', 'prod_id', string="工程別明細", copy=False)
    inspect_line = fields.One2many('alldo_gh_iot.workorder_inspect', 'product_id', copy=False)
    sale_ok = fields.Boolean('Can be Sold', default=False)
    purchase_ok = fields.Boolean('Can be Purchased', default=False)
    cus_no = fields.Many2one('res.partner', string="所屬客戶")
    prod_version = fields.Char(string="版別")
    wkorder_memo = fields.Text(string="工單額外備註",default=' ')
    sale_ok = fields.Boolean(string="可用於銷售",default=True)
    is_blank = fields.Boolean(string="毛胚",default=False)
    ship_check_onhand = fields.Boolean(string="出貨要檢查總庫庫存?",default=False)
    stock_location = fields.Char(string="代加工商")
    prod_material = fields.Char(string="材質")
    prod_spec = fields.Char(string="規格")
    prod_deliver = fields.Char(string="指送")
    prod_location = fields.Char(string="儲位")
    cutter_line = fields.One2many('alldo_gh_iot.cutter','cutter_id',string="刀具",copy=False)
    equip_id = fields.Many2one('maintenance.equipment', string="機台")
    outsub_memo = fields.Text(string="委外備註")
    purchase_memo = fields.Text(string="採購備註")

    @api.model
    def create(self, vals):
        if 'default_code' in vals and not vals['default_code']:
            raise UserError("未輸入 料號！")
        if 'default_code' in vals and vals['default_code']:
            mycount = self.env['product.template'].search_count([('default_code', '=', vals['default_code'])])
            if mycount > 0:
                raise UserError("料號已重複！")
        if 'default_code' in vals and vals['default_code'] and 'barcode' in vals and not vals['barcode']:
            vals['barcode'] = vals['default_code']
        # if 'sale_ok' in vals :
        # vals['sale_ok'] = True
        res = super(ghproductinherit, self).create(vals)
        self.env.cr.execute("""select genblankengorder(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def _write(self, vals):
        res = super(ghproductinherit, self)._write(vals)
        for rec in self:
            # self.env.cr.execute("""select checkprodqcline(%d)""" % rec.id)
            # myres = self.env.cr.fetchone()[0]
            # if not myres:
            #     raise UserError("產品質檢工程別不存在,請檢查！")
            self.env.cr.execute("""select setprodengorder(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genblankengorder(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genavgdataline(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res


class alldoghiotproductengorder(models.Model):
    _name = "alldo_gh_iot.eng_order"
    _description = "產品加工工程別"
    _order = "sequence,id"
    # _rec_name = "ent_type"

    sequence = fields.Integer(string="SEQ", default=10)
    prod_id = fields.Many2one('product.template', ondelete='cascade')
    eng_type = fields.Char(string="工程別名稱")
    is_outsourcing = fields.Boolean(string="委外工程？",default=False)
    is_package = fields.Boolean(string="包裝工序？",default=False)
    partner_id = fields.Many2one('res.partner',string="委外加工商")
    eng_order = fields.Integer(string="工程序列")
    cnc_prog = fields.Char(string="程式代號")
    clamping_power = fields.Char(string="夾持壓力")
    standard_num = fields.Integer(string="標準量(H)")
    prod_real_num = fields.Integer(string="近三月實際量(H)")
    image = fields.Binary('稼動說明')
    image_filename = fields.Char("Image Filename")
    mold_cavity = fields.Integer(string="模穴數",default=1)
    replace_std = fields.Integer(string="架機標準(H)")
    replace_real_time = fields.Integer(string="架機均值(H)")
    is_combine = fields.Boolean(string="有中暫停",default=False)
    equip_id = fields.Many2one('maintenance.equipment',string="機台")
    single_time = fields.Integer(string="單件時間(S)")
    prod_rate = fields.Float(digits=(5,2),string="佔比(%)")

    def name_get(self):
        res = []
        for rec in self:
            myname = "%s" % (rec.eng_type)
            res += [(rec.id, myname)]
        return res

    def run_production_real(self):
        self.env.cr.execute("""select genprodrealnum()""")
        self.env.cr.execute("""commit""")

class alldoghiotworkorderinspect(models.Model):
    _name = "alldo_gh_iot.workorder_inspect"
    _description = "工單產品加工檢驗要求"
    _order = "sequence,id"

    sequence = fields.Integer(string="SEQ", default=10)
    eng_type = fields.Char(string="工程別")
    product_id = fields.Many2one('product.template', ondelete='cascade')
    inspect_name = fields.Char(string="名稱")
    inspect_size = fields.Char(string="檢驗尺寸")
    drawing_tolerance = fields.Char(string="圖面公差")
    real_work_size = fields.Char(string="實作尺寸")
    correct_no = fields.Char(string="補正號碼")
    inspect_point = fields.Char(string="量測頻率")
    inspect_tool = fields.Many2one('alldo_gh_iot.measure_tool', string="量測工具")

class AlldoGhIotCutter(models.Model):
    _name = "alldo_gh_iot.cutter"
    _description = "產品使用刀具記錄"

    cutter_id = fields.Many2one('product.template',ondelete='cascade')
    prod_date = fields.Date(string="日期")
    prod_eng_type = fields.Many2one('alldo_gh_iot.eng_order',string="工程別")
    prod_eng_type1 = fields.Char(string="工程別")
    cutter_desc = fields.Text(string="品名規格描述")

    # @api.onchange('prod_date')
    # def onchangeproddate(self):
    #     myid = self.cutter_id.id
    #     myrec = self.env['alldo_gh_iot.eng_order'].search([('prod_id','=',self.cutter_id.id)])
    #     myids = []
    #     for rec in myrec:
    #         myids.append(rec.id)
    #     return {'domain': {'prod_eng_type': [('id', 'in', myids)]}}



