# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning
import datetime
# import odoo.addons.decimal_precision as dp
import psycopg2, sys

class projsitemmodeltype1(models.Model):
    _name = "neweb.sitem_modeltype1"
    _description = "機型名稱"

    name = fields.Char(string="機型名稱")
    active = fields.Boolean(string="ARCHIVE",default=True)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("機型名稱不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.sitem_modeltype1'].search([('name', '=', myname)])
            if myrec:
                raise UserError("機型名稱重複建立了,請確認")
        rec = super(projsitemmodeltype1, self).create(vals)
        return rec

class projcustom(models.Model):
    _name = "neweb.projcustom"  ## 專案客戶
    _description = '成本分析專案客戶基本資料'

    cus_id = fields.Many2one('neweb.project', required=True, ondelete='cascade')
    cus_type = fields.Selection(
        [('1', '簽約客戶公司地址'), ('2', '維護客戶公司地址'), ('3', '設備維護地址'), ('4', '專案送貨地址'), ('5', '發票寄送地址')], string="類別",
        default='1')
    cus_address = fields.Char(string="公司地址")
    cus_phone = fields.Char(string="公司電話")
    cus_fax = fields.Char(string="公司傳真")
    cus_memo = fields.Text(string="備註")


class projcuscontact(models.Model):
    _name = "neweb.projcontact"  ## 專案連絡人
    _description = '成本分析專案連絡人'

    # @api.model
    # def _get_contact_id(self):
    #     return [('parent_id', '=', self.contact_id.cus_name.id)]

    contact_id = fields.Many2one('neweb.project', required=True, ondelete='cascade')
    contact_type = fields.Many2one('neweb.contacttype', string="人員別")
    contact_name = fields.Many2one('res.partner', string="姓名",
                                   domain=lambda self: ['|', ('parent_id', '=', self.contact_id.cus_name.id),
                                                        ('parent_id', '=', self.contact_id.main_cus_name.id)])
    contact_function = fields.Char(string="職稱")
    contact_phone = fields.Char(string="電話")
    contact_mobile = fields.Char(string="手機")
    contact_email = fields.Char(string="Email")
    contact_fax = fields.Char(string="傳真")


    def name_get(self):
        result = []
        for myrec in self:
            mycontactname = "%s" % (myrec.contact_name.display_name)
            result.append((myrec.id, mycontactname))
        return result

    @api.onchange('create_uid')
    def onchangeclient1(self):
        res = {}
        if self.contact_id.cus_name.name :
            mycontact = self.contact_id.cus_name.name
            res['domain'] = {'contact_name': ['|', ('parent_id', '=', self.contact_id.cus_name.id),
                                              ('parent_id', '=', self.contact_id.main_cus_name.id)]}
        return res

    @api.onchange('contact_name')
    def onchangecontact(self):
        myrec = self.env['res.partner'].search([('id', '=', self.contact_name.id)])
        self.contact_function = myrec.function
        self.contact_phone = myrec.phone
        self.contact_mobile = myrec.mobile
        self.contact_email = myrec.email
        self.contact_fax = myrec.fax
        self.contact_type = myrec.contact_type.id


class projprodset(models.Model):
    _name = "neweb.prodset"  ## 專案進貨採購 組別分類
    _description = '成本分析組別配置'
    _order = "sequence,id"

    name = fields.Char(string="產品組別")
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("產品組別不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.prodset'].search([('name', '=', myname)])
            if myrec:
                raise UserError(("產品組別 => ％s 重複建立了,請確認") % myname)
        rec = super(projprodset, self).create(vals)
        return rec


class projmaintype(models.Model):
    _name = "neweb.projmaintype"
    _description = '成本分析維護說明配置'
    _order = "sequence,id"

    name = fields.Char(string="維護說明")
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("維護說明不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.projmaintype'].search([('name', '=', myname)])
            if myrec:
                raise UserError(("維護說明 => ％s 重複建立了,請確認") % myname)
        rec = super(projmaintype, self).create(vals)
        return rec


class engmaintype(models.Model):
    _name = "neweb.engmaintype"  ## 專案維護方式
    _description = '成本分析專案維護方式配置'
    _order = "sequence,id"

    name = fields.Char(string="維護方式")
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("維護方式不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.engmaintype'].search([('name', '=', myname)])
            if myrec:
                raise UserError(("維護方式 => ％s 重複建立了,請確認") % myname)
        rec = super(engmaintype, self).create(vals)
        return rec




class projsaleitemline(models.Model):
    _name = "neweb.projsaleitem"  ## 專案進貨＆採購明細
    _description = '成本分析專案進貨採購明細'

    @api.depends('prod_num', 'prod_price')
    def _cal_subtot(self):
        for prodset in self:
            mysubtot = prodset.prod_num * prodset.prod_price
            prodset.update({'prod_subtot': mysubtot})

    @api.depends('prod_price')
    def _get_prodprice(self):
        for rec in self:
            myprodprice=round(rec.prod_price)
            rec.prod_price1 = myprodprice
            return myprodprice

    @api.depends('prod_revenue')
    def _get_prodrevenue(self):
        for rec in self:
            myprodrevenue = round(rec.prod_revenue)
            rec.prod_revenue1 = myprodrevenue
            return myprodrevenue

    @api.depends('prod_subtot')
    def _get_subtot(self):
        for rec in self:
            mysubtot= round(rec.prod_subtot)
            rec.prod_subtot1 = mysubtot
            return mysubtot

    saleitem_id = fields.Many2one('neweb.project', required=True, ondelete='cascade')
    prod_set = fields.Many2one('neweb.prodset', string="產品組別")
    prod_modeltype = fields.Char(string="機種-機型/料號")
    prod_modeltype1 = fields.Many2one('neweb.sitem_modeltype1',string="機型名稱")
    prod_serial = fields.Text(string="序號")
    prod_no = fields.Char(string="料號")
    prod_desc = fields.Text(string="規格說明")
    prod_num = fields.Float(digits=(10,0), string="數量", default=1)
    prod_price = fields.Float(digits=(13,2), string="單價")
    prod_price1 = fields.Float(digits=(10,0),compute=_get_prodprice)
    prod_revenue = fields.Float(digits=(13,2), string="銷價")
    prod_revenue1 = fields.Float(digits=(10, 0), compute=_get_prodrevenue)
    prod_subtot = fields.Float(digits=(13,2), string="小計", store=False, compute=_cal_subtot)
    prod_subtot1 = fields.Float(digits=(10, 0), compute=_get_subtot)
    supplier = fields.Many2one('res.partner', string="廠商", domain=[('supplier_rank', '=', 1), ('parent_id', '=', False)])
    paymark_date = fields.Date(string="請款日")
    cost_type = fields.Many2one('neweb.costtype', string="成本類型")
    warranty = fields.Char(string="保固期限")
    origin_warranty = fields.Integer(string="原廠保固月數")
    neweb_warranty = fields.Integer(string="NEWEB保固月數")
    origin_start_date = fields.Date(string="原廠保固起始日")
    origin_end_date = fields.Date(string="原廠保固截止日")
    neweb_start_date = fields.Date(string="Neweb保固起始日")
    neweb_end_date = fields.Date(string="Neweb保固截止日")
    prod_brand = fields.Many2one('neweb.prodbrand', string="品牌")
    project_no = fields.Char(related="saleitem_id.name", string="專案編號")
    purchase_no = fields.Char(string="採購單號")
    prod_purnum = fields.Float(digits=(10,0), string="已採購量", default=0)
    purok = fields.Boolean(string="已採購完成？")

    @api.onchange('prod_num', 'prod_purnum')
    def _onclientchange(self):
        for rec in self:
            # print "%s  %s" % (rec.prod_num, rec.prod_purnum)
            if rec.prod_num != rec.prod_purnum:
                rec.update({'purok': 0})
            else:
                rec.update({'purok': 1})




class newebprojanalysis(models.Model):
    _name = "neweb.projanalysis"
    _order = "analysis_id desc,analysis_sequence asc"
    _description = '成本分析成本分類分析'

    @api.depends('analysis_revenue', 'analysis_cost')
    def _analysis_profit(self):
        for analysis in self:
            if analysis.analysis_revenue == 0:
                analysis.update({'analysis_profit': 0})
            else:
                analysis.update({'analysis_profit': round(analysis.analysis_revenue) - round(analysis.analysis_cost),
                                 })

    @api.depends('analysis_revenue', 'analysis_cost')
    def _analysis_profitrate(self):
        for analysis in self:
            if analysis.analysis_revenue == 0:
                analysis.update({'analysis_profitrate': 0, })
            else:
                if analysis.analysis_revenue == 0:
                    analysis.update({'analysis_profit': 0})
                else:
                    analysis.update({'analysis_profitrate': ((round(analysis.analysis_revenue) - round(analysis.analysis_cost)) / round(analysis.analysis_revenue)) * 100, })

    @api.depends('analysis_revenue')
    def _get_analysisrevenue(self):
        for rec in self:
            myrev = round(rec.analysis_revenue)
            rec.analysis_revenue1 = myrev
            return myrev

    @api.depends('analysis_cost')
    def _get_analysiscost(self):
        for rec in self:
            mycost = round(rec.analysis_cost)
            rec.analysis_cost1 = mycost
            return mycost

    @api.depends('analysis_profit')
    def _get_analysisprofit(self):
        for rec in self:
            myprofit = round(rec.analysis_profit)
            rec.analysis_profit1 = myprofit
            return myprofit

    analysis_id = fields.Many2one('neweb.project', required=True, ondelete='cascade')
    analysis_costtype = fields.Many2one('neweb.costtype', string="類別", required=True)
    analysis_revenue = fields.Float(digits=(13,0), string="收入金額", default=0)
    analysis_revenue1 = fields.Float(digits=(10, 0),compute=_get_analysisrevenue)
    analysis_cost = fields.Float(digits=(13,0), string="成本金額", default=0)
    analysis_cost1 = fields.Float(digits=(10, 0),compute=_get_analysiscost)
    analysis_profit = fields.Float(digits=(13,0), string="毛利金額", store=False,compute=_analysis_profit)
    analysis_profit1 = fields.Float(digits=(10, 0), compute=_get_analysisprofit)
    analysis_profitrate = fields.Float(digits=(5, 2), string="毛利率",store=False,
                                       compute=_analysis_profitrate)
    analysis_sequence = fields.Integer(string="排序")


    @api.model
    def create(self, vals):
        rec = super(newebprojanalysis, self).create(vals)
        return rec


    def write(self, vals):
        rec = super(newebprojanalysis, self).write(vals)
        return rec

class newebsetupcostline(models.Model):
    _name = "neweb.setupcost_line"
    _description =u"建置成本歸屬"
    _order = "name"

    @api.depends('r6_revenue', 'nt_revenue', 'networking_revenue')
    def _get_subtot(self):
        for rec in self:
            rec.update({'subtot_revenue': (rec.r6_revenue + rec.nt_revenue + rec.networking_revenue)})

    @api.depends('r6_revenue')
    def _get_r6revenue(self):
        for rec in self:
            myr6revenue = round(rec.r6_revenue)
            rec.r6_revenue1 = myr6revenue
            return myr6revenue

    @api.depends('nt_revenue')
    def _get_ntrevenue(self):
        for rec in self:
            myntrevenue = round(rec.nt_revenue)
            rec.nt_revenue1 = myntrevenue
            return myntrevenue

    @api.depends('networking_revenue')
    def _get_nwrevenue(self):
        for rec in self:
            mynwrevenue = round(rec.networking_revenue)
            rec.networking_revenue1 = mynwrevenue
            return mynwrevenue

    @api.depends('pm_revenue')
    def _get_pmrevenue(self):
        for rec in self:
            mypmrevenue = round(rec.pm_revenue)
            rec.pm_revenue1 = mypmrevenue
            return mypmrevenue

    @api.depends('subtot_revenue')
    def _get_subrevenue(self):
        for rec in self:
            mysubrevenue = round(rec.subtot_revenue)
            rec.subtot_revenue1 = mysubrevenue
            return mysubrevenue
    

    project_id = fields.Many2one('neweb.project',ondelete='cascade')
    name = fields.Selection([('1','收入(手動)'),('2','零件設備成本(自動)'),('3','委外成本(自動)'),('4','委外成本(手動)'),('5','工時(手動)')],string="類別")
    r6_revenue = fields.Float(digits=(11,0),string="R6")
    r6_revenue1 = fields.Float(digits=(10,0),compute=_get_r6revenue)
    r6_percent = fields.Float(digits=(5,2),string="R6%")
    nt_revenue = fields.Float(digits=(11,0),string="NT")
    nt_revenue1 = fields.Float(digits=(10, 0),compute=_get_ntrevenue)
    nt_percent = fields.Float(digits=(5,2),string="NT%")
    networking_revenue = fields.Float(digits=(11,0),string="Networking")
    networking_revenue1 = fields.Float(digits=(10, 0),compute=_get_nwrevenue)
    networking_percent = fields.Float(digits=(5, 2), string="Networking%")
    pm_revenue = fields.Float(digits=(11,2),string="PS")
    pm_revenue1 = fields.Float(digits=(10,0),compute=_get_pmrevenue)
    pm_percent = fields.Float(digits=(5,2),string="PS%")
    subtot_revenue = fields.Float(digits=(13,0),string="合計",compute=_get_subtot)
    subtot_revenue1 = fields.Float(digits=(10, 0),compute=_get_subrevenue)



class newebmaincostline(models.Model):
    _name = "neweb.maincost_line"
    _description =u"維護成本歸屬"
    _order = "name"

    @api.depends('r6_revenue','nt_revenue','networking_revenue','support_revenue')
    def _get_subtot(self):
        for rec in self:
            rec.update({'subtot_revenue':round(rec.r6_revenue+rec.nt_revenue+rec.networking_revenue+rec.support_revenue)})

    @api.onchange('r6_percent')
    def onchanger6(self):
        for rec in self:
            rec.update({'keytype': '2',
                        'r6_revenue': ((rec.subtot_revenue1 - rec.support_revenue) * round((rec.r6_percent / 100), 2))})

    @api.onchange('nt_percent')
    def onchangent(self):
        for rec in self:
            rec.update({'keytype': '2',
                        'nt_revenue': ((rec.subtot_revenue1 - rec.support_revenue) * round((rec.nt_percent / 100), 2))})

    @api.onchange('networking_percent')
    def onchangenetworking(self):
        for rec in self:
            rec.update({'keytype': '2', 'networking_revenue': (
                        (rec.subtot_revenue1 - rec.support_revenue) * round((rec.networking_percent / 100), 2))})

    @api.depends('r6_revenue')
    def _get_r6revenue(self):
        for rec in self:
            myr6revenue = round(rec.r6_revenue)
            rec.r6_revenue1 = myr6revenue
            return myr6revenue

    @api.depends('nt_revenue')
    def _get_ntrevenue(self):
        for rec in self:
            myntrevenue = round(rec.nt_revenue)
            rec.nt_revenue1 = myntrevenue
            return myntrevenue

    @api.depends('networking_revenue')
    def _get_nwrevenue(self):
        for rec in self:
            mynwrevenue = round(rec.networking_revenue)
            rec.networking_revenue1 = mynwrevenue
            return mynwrevenue

    @api.depends('support_revenue')
    def _get_sprevenue(self):
        for rec in self:
            mysprevenue = round(rec.support_revenue)
            rec.support_revenue1 = mysprevenue
            return mysprevenue

    @api.depends('subtot_revenue')
    def _get_subrevenue(self):
        for rec in self:
            mysubrevenue = round(rec.subtot_revenue)
            rec.subtot_revenue1 = mysubrevenue
            return mysubrevenue

    project_id = fields.Many2one('neweb.project',ondelete='cascade')
    name = fields.Selection([('1','收入(手動)'),('2','零件設備成本(自動)'),('3','委外成本(自動)'),('4','委外成本(手動)')],string="類別")
    r6_revenue = fields.Float(digits=(11,0),string="R6")
    r6_revenue1 = fields.Float(digits=(10, 0),compute=_get_r6revenue)
    r6_percent = fields.Float(digits=(5,2),string="R6%")
    nt_revenue = fields.Float(digits=(11,0),string="NT")
    nt_revenue1 = fields.Float(digits=(10, 0),compute=_get_ntrevenue)
    nt_percent = fields.Float(digits=(5,2),string="NT%")
    networking_revenue = fields.Float(digits=(11,0),string="Networking")
    networking_revenue1 = fields.Float(digits=(10, 0),compute=_get_nwrevenue)
    networking_percent = fields.Float(digits=(5, 2), string="Networking%")
    support_revenue = fields.Float(digits=(11,0),string="Support+駐點")
    support_revenue1 = fields.Float(digits=(10, 0),compute=_get_sprevenue)
    support_percent = fields.Float(digits=(5, 2), string="Support+駐點 %")
    subtot_revenue = fields.Float(digits=(13, 0), string="合計",compute=_get_subtot)
    subtot_revenue1 = fields.Float(digits=(13,0),string="SUBTOT")
    keytype = fields.Selection([('1','revenue'),('2','percent')],string="輸入模式",default='1')


class newebproject(models.Model):
    _name = "neweb.project"
    _description = "成本分析主檔"
    # _inherit = ['mail.thread', 'ir.needaction_mixin']
    _order = 'name desc'

    @api.depends('analysis_line.analysis_revenue', 'analysis_line.analysis_cost')
    def _amount_analysis1(self):
        for analysis in self:
            tot_revenue = tot_cost = 0
            for line in analysis.analysis_line:
                tot_revenue += round(line.analysis_revenue)
                tot_cost += round(line.analysis_cost)
            analysis.total_analysis_revenue = tot_revenue
            return tot_revenue


    @api.depends('analysis_line.analysis_revenue', 'analysis_line.analysis_cost')
    def _amount_analysis2(self):
        for analysis in self:
            tot_revenue = tot_cost = 0
            for line in analysis.analysis_line:
                tot_revenue += round(line.analysis_revenue)
                tot_cost += round(line.analysis_cost)
            analysis.total_analysis_cost=tot_cost
            return tot_cost


    @api.depends('analysis_line.analysis_revenue', 'analysis_line.analysis_cost')
    def _amount_analysis3(self):
        for analysis in self:
            tot_revenue = tot_cost = 0
            for line in analysis.analysis_line:
                tot_revenue += round(line.analysis_revenue)
                tot_cost += round(line.analysis_cost)
            # analysis.update({'total_analysis_profit': tot_revenue - tot_cost})
            analysis.total_analysis_profit = round(tot_revenue - tot_cost)
            return round(tot_revenue - tot_cost)

    @api.depends('analysis_line.analysis_revenue', 'analysis_line.analysis_cost')
    def _amount_analysis4(self):
        for analysis in self:
            tot_revenue = tot_cost = 0
            for line in analysis.analysis_line:
                tot_revenue += line.analysis_revenue
                tot_cost += line.analysis_cost
            if tot_revenue == 0:
                my_profitrate = 0
            else:
                if tot_revenue == 0:
                    my_profitrate = 0
                else:
                    my_profitrate = ((tot_revenue - tot_cost) / tot_revenue) * 100
            analysis.total_analysis_profitrate = my_profitrate
            return my_profitrate
            # analysis.update({'total_analysis_profitrate': my_profitrate})

    # @api.depends('saleitem_line.prod_num', 'saleitem_line.prod_price', 'taxes_id')
    @api.depends('saleitem_line')
    def _amount_all1(self):
        amount_untaxed  = 0
        for order in self.saleitem_line:
            amount_untaxed = amount_untaxed + round(order.prod_num * order.prod_price)
        self.total_saleitem = amount_untaxed
        return amount_untaxed


    @api.depends('saleitem_line', 'taxes_id')
    def _amount_all2(self):
        amount_tax = 0
        for order in self.saleitem_line:
            if self.taxes_id:
                amount_tax += round(order.prod_num * order.prod_price * (self.taxes_id.amount / 100))
            else:
                amount_tax += round(order.prod_num * order.prod_price * 0.05)
        self.total_saleitem_tax = amount_tax
        return amount_tax



    # @api.depends('saleitem_line', 'taxes_id')
    # def _amount_all3(self):
    #     amount_tot = amount_untaxed = amount_tax = 0.0
    #     for order in self.saleitem_line:
    #         if self.taxes_id:
    #             amount_tax += round(order.prod_num * order.prod_revenue * (self.taxes_id.amount / 100))
    #         else:
    #             amount_tax += round(order.prod_num * order.prod_revenue * 0.05)
    #         amount_untaxed = amount_untaxed + (order.prod_num * order.prod_revenue)
    #         amount_tot = amount_tot + (amount_untaxed + amount_tax)
    #     self.total_saleitem_amount = amount_tot
    #     return amount_tot

    @api.depends('total_saleitem','total_saleitem_tax')
    def _amount_all3(self):
        mysalitemtot = 0
        for rec in self:
            mysalitemtot = rec.total_saleitem + rec.total_saleitem_tax
            rec.total_saleitem_amount = rec.total_saleitem + rec.total_saleitem_tax
            return mysalitemtot



    @api.depends('proj_main_type')
    def _get_projmaintypedesc(self):
        mydesc=''
        for rec in self.proj_main_type:
            mydesc += rec.name
            mydesc += '/'
        if len(mydesc) > 0 :
            mydesc = mydesc[:-1]
        self.projmaintype_desc = mydesc


    @api.depends('transation_type')
    def _get_transationdesc(self):
        mydesc=''
        for rec in self.transation_type:
            mydesc += rec.name
            mydesc += '/'
        if len(mydesc) > 0 :
            mydesc = mydesc[:-1]
        self.transation_desc= mydesc

    @api.depends('cus_name')
    def _get_sale_member(self):
        try:
            for rec in self:
                myrec = self.env['res.partner'].search([('id', '=', self.cus_name.id)])
                ids = ""
                if myrec:
                    for rec1 in myrec.member_ids:
                        ids += ","
                        ids += str(rec1.id)
                    rec.update({'sales_member': ids})
        except Exception as inst:
            self.sales_member=' '

    def _check_user_group(self):
        for rec in self:
            rec.is_sales = False
            if self.user_has_groups('neweb_project.neweb_project_sale'):
                rec.is_sales = True

    name = fields.Char(size=20, string="專案編號", required=True)
    parent_projno = fields.Char(size=100, string="來源專案")
    proj_branch = fields.Many2one('neweb.projbranch', string="專案成本區域")
    proj_sale = fields.Many2one('hr.employee', string="專案業務")
    cus_name = fields.Many2one('res.partner', string="專案客戶", required=True)
    main_cus_name = fields.Many2one('res.partner', string="維護客戶", required=True)
    proj_cus_ids = fields.One2many('neweb.projcustom', 'cus_id', copy=True, string="專案相關地址",track_visibility="onchange")
    proj_contact_ids = fields.One2many('neweb.projcontact', 'contact_id', copy=True, string="專案相關連絡人",track_visibility="onchange")
    sno = fields.Char(size=20, string="統一編號")
    comp_cname = fields.Char(size=150, string="中文名稱")
    comp_sname = fields.Char(size=20, string="中文簡稱")
    comp_ename = fields.Char(size=50, string="英文名稱")
    cate_type = fields.Many2one('neweb.buscate', string="行業別")
    transation_type = fields.Many2many('neweb.transationtype', string="交易類別",  required=True)
    group_name = fields.Char(size=150, string="集團名稱")
    setup_date = fields.Date(string="預定裝機日")
    shipping_date = fields.Date(string="預定交貨日")
    shipping_type = fields.Selection([('1', '一次交貨'), ('2', '可分批交貨')], string="交貨方式", default='2')
    proj_pay_type = fields.Selection(
        [('1', '一次付清'), ('2', '月初'), ('3', '月末'), ('4', '雙月初'), ('5', '雙月末'), ('6', '季初'),
         ('7', '季末'), ('8', '半年初'), ('9', '半年末'), ('10', '年初'), ('11', '年末'),
         ('12', '分期付款'),('13','其他')], string="專案付款方式", default='1')
    proj_pay = fields.Many2one('account.payment.term', string="付款條件")
    acc_close_day = fields.Char(size=20, string="請款日")
    pay_term = fields.Char(size=10, string="月結天數")
    payto_date = fields.Char(size=20, string="撥款日")
    acc_close_day1 = fields.Char(size=20, string="結帳日")
    other_date = fields.Char(size=50, string="其他款日說明")
    acc_receivable = fields.Selection([('2', '郵寄'), ('3', '電匯'), ('4', '親領')], string="請款方式", default='2')
    post_date = fields.Char(size=10, string="郵寄款日")
    post_term = fields.Char(size=10, string="郵寄款天期票")
    post_envelop = fields.Selection([('1', '是'), ('2', '否')], string="是否回郵信封")
    tt_date = fields.Char(size=10, string="電匯每月日期")
    self_receive_date = fields.Char(size=10, string="親領每月日期")
    self_rece_stamp = fields.Selection([('1', "無"), ('2', "收款章"), ('3', "發票章"), ('4', "大小章")], string="親領需攜帶",
                                       default='1')
    description = fields.Text(string="說明")
    memo = fields.Text(string="備註")
    analysis_line = fields.One2many('neweb.projanalysis', 'analysis_id', copy=True, string="成本分析",track_visibility="onchange")
    saleitem_line = fields.One2many('neweb.projsaleitem', 'saleitem_id', copy=True, string="專案進貨＆採購明細",track_visibility="onchange")
    total_saleitem = fields.Float(digits=(13,0), string="合計(未稅)", compute=_amount_all1,store=True,track_visibility="always")
    taxes_id = fields.Many2one('account.tax', string='Taxes',
                               domain=['|', ('active', '=', False), ('active', '=', True),
                                       ('type_tax_use', '=', 'sale')], default='1')
    total_saleitem_tax = fields.Float(digits=(13,0), string="5%營業稅",store=True,compute=_amount_all2,track_visibility="always")
    total_saleitem_amount = fields.Float(digits=(13,0), string="總計(含稅)",store=True,compute=_amount_all3,track_visibility="always")
    total_analysis_revenue = fields.Float(digits=(13,0), string="總收入金額",compute=_amount_analysis1)
    total_analysis_cost = fields.Float(digits=(13,0), string="總成本金額",compute=_amount_analysis2)
    total_analysis_profit = fields.Float(digits=(13,0), string="總毛利金額",compute=_amount_analysis3)
    total_analysis_profitrate = fields.Float(digits=(5, 2), string="總毛利率", compute=_amount_analysis4)
    setup_type = fields.Selection([('1', '是'), ('2', '否')], string="工程師內部組裝", default='1')
    eng_assign = fields.Selection([('1', '需至客戶端裝機'), ('2', '否'), ('3', '其他')], string="工程師派工", default='1')
    setup_description = fields.Text(string="裝機說明")
    #  保固說明
    origin_warranty_desc = fields.Text(string="原廠保固說明")
    neweb_warranty_desc = fields.Text(string="藍新保固說明")
    neweb_manpower_desc = fields.Text(string="藍新人力說明")
    other_warranty_desc = fields.Text(string="其他保固說明")
    warranty_start_date = fields.Date(string="保固啟始日")
    warranty_end_date = fields.Date(string="保固終止日")

    # 政府專案說明
    decision_date = fields.Date(string="決標日")
    acceptance_step = fields.Char(string="專案驗收階段(X)")
    complete_days = fields.Char(string="驗收完工日(X)")
    send_letter_date = fields.Date(string="預計發函日")
    acceptance_date = fields.Date(string="預計驗收日")
    acceptance_other_desc = fields.Text(string="其他說明")

    # 專案驗收說明
    proj_step = fields.Char(string="專案驗收階段")
    proj_complete_days = fields.Char(string="專案驗收完工日")
    proj_acceptance_date = fields.Date(string="預計驗收日")
    proj_paytype = fields.Text(string="專案付款方式")
    proj_other_desc = fields.Text(string="其他說明")

    proj_main_type = fields.Many2many('neweb.projmaintype', string="維護案說明")
    main_start_date = fields.Date(string="維護開始日")
    main_end_date = fields.Date(string="維護截止日")
    eng_main_type = fields.Many2one('neweb.engmaintype', string="維護方式")
    main_paytype = fields.Selection([('1', '月初'), ('2', '月底')], string="付款方式", default='1')
    old_contact_revenue = fields.Float(digits=(13,0), string="舊約收入")
    old_contact_cost = fields.Float(digits=(13,0), string="舊約成本")
    main_other = fields.Text(string='其他說明(X)')
    ship_type = fields.Selection([('1', '貨送藍新'), ('2', '直送客戶端'), ('3', '其他'), ('4', '無')], string="送貨說明",
                                 default='1')
    ship_description = fields.Text(string="說明")
    invoice_type = fields.Selection([('1', '隨貨開立發票'), ('2', '待業務通知'), ('3', '完工後隨工單開立發票'), ('4', '其他')],
                                    string="開立發票說明", default='2')
    invoice_description = fields.Text(string="說明")
    assign_no = fields.Char(string="裝機單號")
    state = fields.Selection([('1', '新單'), ('2', '提交'), ('3', '派工'), ('4', '完工'), ('5', '結案'), ('6', '合約'), ('7', '過期')], string="狀態",default='1')
    purchase_yn = fields.Boolean(string="是否採購", default=False)
    sale_no = fields.Char(string="銷單號碼")
    opentrender = fields.Boolean(string="是否為標案", default=False)
    maintenanceyn = fields.Boolean(string="是否為維護", default=False)
    warrantyyn = fields.Boolean(string="是否為保固", default=False)
    projectyn = fields.Boolean(string="是否為專案", default=False)
    cus_project = fields.Char(string="客戶專案/標案名稱")
    cus_order = fields.Char(string="客戶訂單/標案號碼")
    is_sales = fields.Boolean(conmpute=_check_user_group, store=False)
    sales_member = fields.Char(compute=_get_sale_member,store=True, string="業務員")
    contract_build_mark = fields.Boolean(default=False, string="產生合約維護記錄否?")
    proj_cost_case = fields.Selection([('1', '30萬以下,GP 8%以上'),
                                       ('2', '30萬以下,GP 8%以下,及30-120萬 GP 8%以上'),
                                       ('3', '30-120萬 GP8%以下,及120-1500萬內'),
                                       ('4', '1500萬以上'),
                                       ('5', '30萬以下,GP 8%以上;維護案'),
                                       ('6', '30萬以下,GP 8%以下,及30-120萬 GP 8%以上;維護案'),
                                       ('7', '30-120萬 GP8%以下,及120-1500萬內;維護案'),
                                       ('8', '1500萬以上;維護案'),
                                       ], store=True, default='1')
    proj_main_case = fields.Char(string="是否維修建置案", store=True, default='N')
    is_signed = fields.Boolean(string="是否授權", default=False)
    transation_desc = fields.Char(string="交易類別說明", store=False, compute=_get_transationdesc)
    projmaintype_desc = fields.Char(string="維護案說明", store=False, compute=_get_projmaintypedesc)
    firstgen = fields.Integer(default=0)
    discount_amount = fields.Float(digits=(10, 0), string="報價單優惠總價(含税)")
    proj_status = fields.Char(string="成本歸戶狀態", default="Balance")
    proj_status1 = fields.Char(string="收入平衡狀態", default="Balance")
    setupcost_ids = fields.One2many('neweb.setupcost_line', 'project_id', copy=False,track_visibility="onchange")
    maincost_ids = fields.One2many('neweb.maincost_line', 'project_id', copy=False,track_visibility="onchange")
    have_contract = fields.Selection([('Y', u'有合約'), ('N', u'無合約')], string=u"有無合約？", default='N')
    proj_write_num = fields.Integer(string=u"專案變動次數", default=0)

    def regen_costdeptdata(self):   # 成本歸戶重新計算
        self.env.context = dict(self.env.context)
        self.env.context.update({'proj_op_id': self.id})
        #myprojid = self.env.context.get('proj_op_id')
        myprojid = self.id
        self.env.cr.execute("""delete from neweb_setupcost_line where project_id=%d ;""" % myprojid)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from neweb_maincost_line where project_id=%d ;""" % myprojid)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gencostdeptdata(%d)""" % myprojid)
        self.env.cr.execute("""commit""")
        # 已將 genmainsuprev 功能 寫在 gencostdeptdata中了
        # self.env.cr.execute("""select genmainsuprev(%d)""" % myprojid)
        # self.env.cr.execute("""commit""")
        self.env.cr.commit()
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '成本歸戶重新計算完成！'
        return {
                'name': '系統通知訊息',
                 'type': 'ir.actions.act_window',
                  'view_type': 'form',
                  'view_mode': 'form',
                  'res_model': 'sh.message.wizard',
                  'views': [(view.id, 'form')],
                  'view_id': view.id,
                  'target': 'new',
                  'context': context,
                }
        mystatus = ''
        mystatus1 = ''
        # self.env.cr.execute("""select get_discount_amount(%d)""" % self.id)
        # mydiscountamount = self.env.cr.fetchone()[0]
        # self.env.cr.execute("select updatecalcost(%d)" % self.id)
        # analysis_status = self.env.cr.fetchone()[0]
        # if not analysis_status:
        #     mystatus1 = "成本分析收入金額總計不合,請確認！報價單優惠總價(未税):NT$ %s" % mydiscountamount
        # else:
        #     mystatus1 = 'Balance'
        # raise UserError(mystatus)
        # self.env.cr.execute("""select clearcostline(%d)""" % self.id)
        # self.env.cr.execute("""commit""")
        # self.env.cr.execute("""select gencostdeptdata(%d)""" % self.id)
        # self.env.cr.execute("""commit""")
        # self.env.cr.execute("""select getsetupanalysistotrev(%d)""" % self.id)
        # mysetupanalysisrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupanalysistotcost(%d)""" % self.id)
        # mysetupanalysiscost = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmainanalysistotrev(%d)""" % self.id)
        # mymainanalysisrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmainanalysistotcost(%d)""" % self.id)
        # mymainanalysiscost = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupdeptrev(%d)""" % self.id)
        # mysetupdeptrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupdeptcost(%d)""" % self.id)
        # mysetupdeptcost = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmaindeptrev(%d)""" % self.id)
        # mymaindeptrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmaindeptcost(%d)""" % self.id)
        # mymaindeptcost = self.env.cr.fetchone()[0]
        #
        # if abs(mysetupanalysisrev - mysetupdeptrev) > 10:
        #     mystatus = mystatus + '(建置)成本分析收入:%s ,(建置)歸戶收入:%s 不合！' % (mysetupanalysisrev, mysetupdeptrev)
        # elif abs(mymainanalysisrev - mymaindeptrev) > 10:
        #     mystatus = mystatus + '(維護)成本分析收入:%s ,(維護)歸戶收入:%s 不合！' % (mymainanalysisrev, mymaindeptrev)
        # elif abs(mysetupanalysiscost - mysetupdeptcost) > 10:
        #     mystatus = mystatus + '(建置)成本分析成本:%s ,(建置)歸戶成本:%s 不合！' % (mysetupanalysiscost, mysetupdeptcost)
        # elif abs(mymainanalysiscost - mymaindeptcost) > 10:
        #     mystatus = mystatus + '(維護)成本分析成本:%s ,(維護)歸戶成本:%s 不合！' % (mymainanalysiscost, mymaindeptcost)
        # else:
        #     mystatus = 'Balance'
        # if mystatus == 'Balance':
        #     self.env.cr.execute(
        #         """update neweb_project set proj_status='Balance',proj_write_num=0 where id=%d""" % self.id)
        # else:
        #     self.env.cr.execute(
        #         """update neweb_project set proj_status='%s',proj_write_num=coalesce(proj_write_num,0)+1 where id=%d""" % (mystatus, self.id))
        # if mystatus1 == 'Balance':
        #     self.env.cr.execute("""update neweb_project set proj_status1='Balance' where id=%d""" % self.id)
        # else:
        #     self.env.cr.execute("""update neweb_project set proj_status1='%s' where id=%d""" % (mystatus1, self.id))
        # self.env.cr.execute("""commit""")

    @api.onchange('transation_type')
    def onchangeclient(self):
        istrender = self.env.ref('neweb_project.neweb_transationtype_1')
        ismaintenance1 = self.env.ref('neweb_project.neweb_transationtype_7')
        ismaintenance2 = self.env.ref('neweb_project.neweb_transationtype_8')
        iswarranty1 = self.env.ref('neweb_project.neweb_transationtype_3')
        iswarranty2 = self.env.ref('neweb_project.neweb_transationtype_4')
        iswarranty3 = self.env.ref('neweb_project.neweb_transationtype_5')
        isproject = self.env.ref('neweb_project.neweb_transationtype_10')
        project = False
        warranty = False
        trenderyn = False
        maintenance = False
        for rec in self.transation_type:
            if rec.id == istrender.id:
                trenderyn = True
            if rec.id == ismaintenance1.id or rec.id == ismaintenance2.id:
                maintenance = True
            if rec.id == iswarranty1.id or rec.id == iswarranty2.id or rec.id == iswarranty3.id:
                warranty = True
            if rec.id == isproject.id:
                project = True
        self.update(
            {'opentrender': trenderyn, 'maintenanceyn': maintenance, 'warrantyyn': warranty, 'projectyn': project})
        # return { 'type': 'ir.actions.client',
        #         'tag':'reload'}


    def set_signed(self):
        myrec = self.env['neweb.project'].search([('id', '=', self.id)])
        for rec in self:
            rec.update({'is_signed': True, 'state': '3'})
        myrec.send_approve_mail()

    is_closed = fields.Boolean(string="是否結案", default=False)


    def set_closed(self):
        for rec in self:
            rec.update({'is_closed': True, 'state': '5'})


    def set_reject(self):
        myrec = self.env['neweb.project'].search([('id', '=', self.id)])
        for rec in self:
            rec.update({'is_closed': False, 'is_signed': False, 'state': '1'})
        myrec.send_reject_mail()

    ### WKF SEND MAIL PROCEDURE
    ###   type='1' 所有簽核人員    type='2' 送件者
    ###


    def get_approve_emails(self):
        self.env.cr.execute("select wkfsendmail('%s',%d,'%s')" % (self.name, self.id, '1'))
        mylist = self.env.cr.fetchall()
        myids = self.env['res.users'].search([('id', 'in', mylist)])
        all_mails = []
        for item in myids:
            all_mails.append(item.employee_ids.work_email)
        return ','.join(str(mail) for mail in all_mails)


    def get_reject_emails(self):
        self.env.cr.execute("select wkfsendmail('%s',%d,'%s')" % (self.name, self.id, '2'))
        mylist = self.env.cr.fetchall()
        myids = self.env['res.users'].search([('id', 'in', mylist)])
        all_mails = []
        for item in myids:
            all_mails.append(item.employee_ids.work_email)
        return ','.join(str(mail) for mail in all_mails)


    def send_approve_mail(self):
        myrec = self.env['neweb.project'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_project', 'mail_neweb_project_wkf_approve')[1]
        except ValueError:
            template_id = False

        self.env['mail.template'].browse(template_id).sudo().send_mail(myid)


    def send_reject_mail(self):
        myrec = self.env['neweb.project'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_project', 'mail_neweb_project_wkf_reject')[1]
        except ValueError:
            template_id = False
        self.env['mail.template'].browse(template_id).sudo().send_mail(myid)


    def owner_project_data(self):
        myid = str(self.env.uid)

        tree_id = self.env.ref("neweb_project.neweb_project_tree")
        form_id = self.env.ref("neweb_project.neweb_project_form")
        return {
            "type": 'ir.actions.act_window',
            "name": 'Owner Project Data',
            "view_type": 'form',
            "view_mode": 'tree,form',
            "res_model": 'neweb.project',
            "domain": [(myid, 'in', 'sales_member')],
            "views": [[tree_id.id, 'tree'], [form_id.id, 'form']],
            "target": 'new',
        }


    def proj_recal(self):
        self.env.context = dict(self.env.context)
        self.env.context.update({'proj_op_id': self.id})
        myprojid = self.id
        try:
            self.env.cr.execute("""delete from neweb_projanalysis where analysis_id=%d""" % myprojid)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("select proj_cal_cost(%s)" % myprojid)
        except Exception as inst:
            raise UserError("明細數據不完整,請確認!")
        self.env.cr.commit()
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '成本分析重算完成！'
        return {
                'name': '系統通知訊息',
                 'type': 'ir.actions.act_window',
                  'view_type': 'form',
                  'view_mode': 'form',
                  'res_model': 'sh.message.wizard',
                  'views': [(view.id, 'form')],
                  'view_id': view.id,
                  'target': 'new',
                  'context': context,
                }
        # mystatus = ''
        # mystatus1 = ''
        # self.env.cr.execute("""select get_discount_amount(%d)""" % self.id)
        # mydiscountamount = self.env.cr.fetchone()[0]
        # self.env.cr.execute("select updatecalcost(%d)" % self.id)
        # analysis_status = self.env.cr.fetchone()[0]
        # if not analysis_status:
        #     mystatus1 = "成本分析收入金額總計不合,請確認！報價單優惠總價(未税):NT$ %s" % mydiscountamount
        # else:
        #     mystatus1 = 'Balance'
        #     # raise UserError(mystatus)
        # self.env.cr.execute("""select clearcostline(%d)""" % self.id)
        # self.env.cr.execute("""commit""")
        # self.env.cr.execute("""select gencostdeptdata(%d)""" % self.id)
        # self.env.cr.execute("""commit""")
        # self.env.cr.execute("""select getsetupanalysistotrev(%d)""" % self.id)
        # mysetupanalysisrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupanalysistotcost(%d)""" % self.id)
        # mysetupanalysiscost = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmainanalysistotrev(%d)""" % self.id)
        # mymainanalysisrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmainanalysistotcost(%d)""" % self.id)
        # mymainanalysiscost = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupdeptrev(%d)""" % self.id)
        # mysetupdeptrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupdeptcost(%d)""" % self.id)
        # mysetupdeptcost = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmaindeptrev(%d)""" % self.id)
        # mymaindeptrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmaindeptcost(%d)""" % self.id)
        # mymaindeptcost = self.env.cr.fetchone()[0]
        #
        # if abs(mysetupanalysisrev - mysetupdeptrev) > 10:
        #     mystatus = mystatus + '(建置)成本分析收入:%s ,(建置)歸戶收入:%s 不合！' % (mysetupanalysisrev, mysetupdeptrev)
        # elif abs(mymainanalysisrev - mymaindeptrev) > 10:
        #     mystatus = mystatus + '(維護)成本分析收入:%s ,(維護)歸戶收入:%s 不合！' % (mymainanalysisrev, mymaindeptrev)
        # elif abs(mysetupanalysiscost - mysetupdeptcost) > 10:
        #     mystatus = mystatus + '(建置)成本分析成本:%s ,(建置)歸戶成本:%s 不合！' % (mysetupanalysiscost, mysetupdeptcost)
        # elif abs(mymainanalysiscost - mymaindeptcost) > 10:
        #     mystatus = mystatus + '(維護)成本分析成本:%s ,(維護)歸戶成本:%s 不合！' % (mymainanalysiscost, mymaindeptcost)
        # else:
        #     mystatus = 'Balance'
        # if mystatus == 'Balance':
        #     self.env.cr.execute(
        #         """update neweb_project set proj_status='Balance',proj_write_num=0 where id=%d""" % self.id)
        # else:
        #     self.env.cr.execute(
        #         """update neweb_project set proj_status='%s',proj_write_num=coalesce(proj_write_num,0)+1 where id=%d""" % (mystatus, self.id))
        # if mystatus1 == 'Balance':
        #     self.env.cr.execute("""update neweb_project set proj_status1='Balance' where id=%d""" % self.id)
        # else:
        #     self.env.cr.execute("""update neweb_project set proj_status1='%s' where id=%d""" % (mystatus1, self.id))
        # self.env.cr.execute("""commit""")



    def proj_delete(self):
        # myprojid = self.env.context.get('proj_op_id')
        self.env.context = dict(self.env.context)
        self.env.context.update({'proj_op_id':self.id})
        myprojid = self.id
        self.env.cr.execute("""select getprojhaspurchase(%d)""" % myprojid)
        myres = self.env.cr.fetchone()
        if myres[0]:
            raise UserError("已有進行採購動作,無法刪除明細了！")
        self.env.cr.execute("select proj_delsaleitem_cost(%d)" % myprojid)
        self.env.cr.execute("delete from neweb_projsaleitem where saleitem_id=%d" % myprojid)

    def _get_trender(self):
        istrender = self.env.ref('neweb_project.neweb_transationtype_1')
        trenderyn = False
        for rec in self.transation_type:
            if rec.id == istrender.id:
                trenderyn = True
            self.opentrender = trenderyn
        return trenderyn


    def _get_maintenance(self):
        ismaintenance1 = self.env.ref('neweb_project.neweb_transationtype_7')
        ismaintenance2 = self.env.ref('neweb_project.neweb_transationtype_8')
        maintenance = False
        for rec in self.transation_type:
            if rec.id == ismaintenance1.id or rec.id == ismaintenance2.id:
                maintenance = True
            self.maintenanceyn = maintenance
        return maintenance


    def _get_warranty(self):
        iswarranty1 = self.env.ref('neweb_project.neweb_transationtype_3')
        iswarranty2 = self.env.ref('neweb_project.neweb_transationtype_4')
        iswarranty3 = self.env.ref('neweb_project.neweb_transationtype_5')
        warranty = False
        for rec in self.transation_type:
            if rec.id == iswarranty1.id or rec.id == iswarranty2.id or rec.id == iswarranty3.id:
                warranty = True
            self.warrantyyn = warranty
        return warranty


    def _get_project(self):
        isproject = self.env.ref('neweb_project.neweb_transationtype_10')
        project = False
        for rec in self.transation_type:
            if rec.id == isproject.id:
                project = True
            self.projectyn = project
        return project


    @api.model
    def create(self, vals):
        rec = super(newebproject, self).create(vals)
        # self.env.cr.execute("select proj_cal_cost(%d)" % rec.id)
        # self.env.cr.execute("""commit""")
        # self.env.cr.execute("select proj_cal_prodset(%d)" % rec.id)
        # self.env.cr.execute("select getmaincase(%d)" % rec.id)
        return rec


    def write(self, vals):

        if 'cus_project' in vals and not vals['cus_project']:
            raise UserError("未輸入 客戶專案/標案名稱,請確認...")

        rec = super(newebproject, self).write(vals)
        if 'warrantyyn' in vals and vals['warrantyyn'] == True:
            self._cr.execute("""select check_warrantyyn(%d)""" % self.id)
            mytype = self._cr.fetchone()
            # if mytype[0] == '2' :
            #    raise UserError("保固起始 or 截止日期未輸入,請確認...")
            if mytype[0] == '1':
                raise UserError("保固相關說明全空白,至少要有一項說明...")
        if 'opentrender' in vals and vals['opentrender'] == True:
            self._cr.execute("""select check_opentrender(%d)""" % self.id)
            mytype1 = self._cr.fetchone()
            if mytype1[0] == '1':
                raise UserError("政府專案說明全空白,至少要有一項說明...")
        if 'maintenanceyn' in vals and vals['maintenanceyn'] == True:
            self._cr.execute("""select check_maintenanceyn(%d)""" % self.id)
            mytype2 = self._cr.fetchone()
            if mytype2[0] == '1':
                raise UserError("維護案說明全空白,至少要有一項說明...")
        if 'projectyn' in vals and vals['projectyn'] == True:
            self._cr.execute("""select check_projectyn(%d)""" % self.id)
            mytype3 = self._cr.fetchone()
            if mytype3[0] == '1':
                raise UserError("專案驗收說明全空白,至少要有一項說明...")

        myrec = self.env['neweb.project'].search([('id', '=', self.id)])
        # self.env.cr.execute("select proj_rcal_cost(%d)" % self.id)
        # self.env.cr.execute("""commit""")

        self.env.cr.execute("select proj_cal_prodset(%d)" % self.id)
        # self.env.cr.execute("select getmaincase(%d)" % self.id)
        myeng = self.env['neweb.proj_eng_assign'].sudo().search([('proj_no', '=', self.id)])
        if myeng:
            myeng.write({'assign_man_desc': self.setup_description})
        return rec


    def unlink(self):
        for rec in self:
            mysaleno = rec.sale_no
            myid = rec.id
            if myid:
                self.env.cr.execute("""select getprojhaspurchase(%d)""" % rec.id)
                myres = self.env.cr.fetchone()
                if myres[0]:
                    raise UserError("已有採購記錄,不能刪除成本分析！")
            res = super(newebproject, rec).unlink()
            myrec = self.env['sale.order'].search([('name', '=', mysaleno)])
            if myrec:
                myrec.write({'trans_yn': False, 'state': 'draft'})
            mysalenocheck = self.env['neweb.salenocheck'].search([('sale_no', '=', myrec.name)])
            if mysalenocheck:
                mysalenocheck.write({'trans_proj': False})
            return res
        # model_obj = self.env['ir.model.data']
        # data_id = model_obj._get_id('neweb_project', 'neweb_project_tree')
        # view_id = model_obj.browse(data_id).res_id
        # tree_id = self.env.ref("neweb_project.neweb_project_tree")
        # return {
        #     'name': 'Neweb Project',
        #     'view_type': 'tree',
        #     "view_mode": 'tree,form',
        #     'res_model': 'neweb.project',
        #     'type': 'ir.actions.act_window',
        #     # 'search_view_id': tree_id.id,
        #     'views': [(tree_id.id, 'tree'), (False, 'form')],
        #     'target': 'new',
        # }



    def neweb_eng_assign_form(self):
        myprojid = self.env.context.get('proj_op_id')
        # print "assign step1"
        # myprojname = self.env['neweb.project'].search([('id', '=', self.env.context.get('proj_op_id'))])
        myprojname = self.env['neweb.project'].search([('id', '=', self.id)])
        myassignmandesc = myprojname.setup_description
        myids = []
        if myprojname.setup_type == '1' and myprojname.eng_assign == '1':
            myids = [1, 2]
        elif myprojname.setup_type == '1' and myprojname.eng_assign != '1':
            myids = [1]
        elif myprojname.setup_type != '1' and myprojname.eng_assign == '1':
            myids = [2]
        else:
            myids = []
        # if not myprojname.saleitem_line:
        #     raise UserError("尚未建立進貨＆採購明細...請確認！")
        myeng = self.env['neweb.proj_eng_assign'].search([('proj_no', '=', myprojname.id)])
        myproj_rec = self.env['neweb.project'].search([('id', '=', myprojname.id)])
        if not myeng:
            # raise UserError("請先執行建立派工單作業")

            # raise UserError("(%s) %s" % (myproj_rec.cus_name.id,myproj_rec.proj_sale.id))
            mysetup_contact = ""
            mysetup_contact_phone = ""
            mysetup_contact_mobile = ""
            if myproj_rec.proj_contact_ids:
                mysetup_contact = myproj_rec.proj_contact_ids[0].contact_name.id
                mysetup_contact_phone = myproj_rec.proj_contact_ids[0].contact_phone
                mysetup_contact_mobile = myproj_rec.proj_contact_ids[0].contact_mobile
            myproj_rec.write({'state': '2'})
            myaddress1 = ""
            myaddress2 = ""
            for cus_rec in myproj_rec.proj_cus_ids:
                if cus_rec.cus_type == "1":
                    myaddress1 = cus_rec.cus_address
                else:
                    myaddress2 = cus_rec.cus_address
            if myaddress2 == "":
                myaddress2 = myaddress1

            # raise UserError("OK")

            myeng_rec = self.env['neweb.proj_eng_assign']
            myengid = myeng_rec.create(
                {'proj_no': myproj_rec.id, 'assign_no': myproj_rec.name, 'proj_cus_name': myproj_rec.cus_name.id,
                 'proj_sale': myproj_rec.proj_sale.id, 'setup_address': myaddress2, 'assign_man_desc': myassignmandesc,
                 'setup_contact': mysetup_contact, 'setup_contact_phone': mysetup_contact_phone,
                 'setup_contact_mobile': mysetup_contact_mobile, 'setup_date': myproj_rec.setup_date,
                 'setup_desc': [(6, 0, myids)], 'setup_other_desc': myproj_rec.setup_description,
                 'assign_man_subject': myproj_rec.cus_project})

            myeng_rec = self.env['neweb.proj_eng_assign'].search([('id', '=', myengid.id)])
            for myitem in myproj_rec.saleitem_line:
                myeng_rec.write(
                    {'proj_setup_line': [
                        (0, 0, {'prod_set': myitem.prod_set.id, 'prod_modeltype': myitem.prod_modeltype,
                                'prod_serial': myitem.prod_serial, 'prod_no': myitem.prod_no,
                                'prod_desc': myitem.prod_desc, 'prod_num': myitem.prod_num})]})
            myproj_rec.write({'assign_no': myproj_rec.name})
            # mydomain = []
            # mydomain.append(('id', '=', myengid.id))
            viewid = self.env.ref('neweb_project.neweb_assign_inherit_form3').id
            # viewid = self.env.ref('neweb_project.neweb_assign_form').id
            return {'view_name': 'projengassignwizard',
                    'name': ('專案派工維護'),
                    'views': [[False, 'form'], ],
                    'view_id': viewid,
                    'res_model': 'neweb.proj_eng_assign',
                    'context': self._context,
                    'type': 'ir.actions.act_window',
                    'target': 'main',
                    # 'domain': mydomain,
                    'res_id': myengid.id,
                    'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                    'view_mode': 'form',
                    'view_type': 'form'
                    }
        else:

            # mydomain = []
            # mydomain.append(('id', '=', myengid.id))
            viewid = self.env.ref('neweb_project.neweb_assign_inherit_form3').id
            return {'view_name': 'newebproject',
                    'name': ('專案派工維護'),
                    'views': [[False, 'form'], ],
                    'view_id': viewid,
                    'res_model': 'neweb.proj_eng_assign',
                    'context': self._context,
                    'type': 'ir.actions.act_window',
                    'target': 'main',
                    # 'domain': mydomain,
                    'res_id': myeng.id,
                    'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                    'view_mode': 'form',
                    'view_type': 'form'
                    }


    def neweb_project_copy(self):

        default = {}
        # myprojid = self.env.context.get('proj_op_id')
        myproj = self.env['neweb.project'].search([('id', '=', self.env.context.get('proj_op_id'))])
        mybranch = self.env['neweb.projbranch'].search([('id', '=', myproj.proj_branch.id)])
        myprefixcode = mybranch.prefixcode
        mynow = datetime.datetime.now()
        myyy = str(mynow.year - 1911)
        myyear = myyy[1:]
        mymm = str(mynow.month)
        mymonth = mymm.zfill(2)
        myym = myyear + mymonth
        newname = ""
        gencode_rec = self.env['neweb.projgencode'].search([('name', '=', myym), ('prefixcode', '=', myprefixcode)])
        if gencode_rec:
            strcode = str(gencode_rec.gencode + 1)
            mycode = strcode.zfill(3)
            newname = "%sSVC%s-%s" % (myprefixcode, myym, mycode)
            gencode_rec.gencode += 1
        else:
            newname = "%sSVC%s-001" % (myprefixcode, myym)
            gencode_rec.create({'name': myym, 'prefixcode': myprefixcode, 'gencode': 1})

        default['name'] = newname
        default['parent_projno'] = self.name
        project_copy = super(newebproject, self).copy(default=default)

        return {'view_name': 'projcopywizard',
                'name': ('專案複製作業'),
                'views': [[False, 'form'], [False, 'tree'], ],
                'res_model': 'neweb.project',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'self',
                # 'domain': mydomain,
                'res_id': project_copy.id,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }


    def get_projsaleitem_export(self):
        import io
        import base64
        # from odoo.addons import decimal_precision as dp
        from datetime import datetime, timedelta, date
        import xlsxwriter
        myproj = self.env.context.get("proj_op_id")
        myrec =self.env['neweb.project'].search([('id','=',myproj)])
        self.env.cr.execute("select projsaleitemexport(%s)" % myproj)
        projrec = self.env['neweb.projsaleitem_export'].search([])
       
        if projrec:
            myprojno = myrec[0].name
            myxlsfilename = "PROJECT_%s_%s.xlsx" % (myprojno, datetime.now().strftime("%Y%m%d"))
            mysubject = "PROJECT_%s_%s.xlsx" % (myprojno, datetime.now().strftime("%Y%m%d"))
            output = io.BytesIO()

            wb = xlsxwriter.Workbook(output, {'in_memory': True})
          
            wb.set_properties({
                'title': '專案銷項資訊匯出',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'NEWEB INFO',
                'company': '藍新資訊股份有限公司',
                'category': '專案銷項資訊匯出',
                'keywords': '專案銷項資訊匯出',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})
            ws = wb.add_worksheet("專案銷項資訊匯出檔")


            ########################################
            title_format = wb.add_format()
            title_format.set_font_size(30)
            title_format.set_bold()
            title_format.set_underline(2)
            title_format.set_font_color('black')
            title_format.set_align('left')
            title_format.set_align('vcenter')
            ########################################
            head_format = wb.add_format()
            head_format.set_font_size(15)
            head_format.set_border(2)
            head_format.set_font_color('yellow')
            head_format.set_fg_color('blue')
            head_format.set_align('center')
            head_format.set_align('vcenter')
            ########################################
            okc_content_format = wb.add_format()
            okc_content_format.set_font_size(15)
            okc_content_format.set_border(1)
            okc_content_format.set_font_color('black')
            okc_content_format.set_align('center')
            okc_content_format.set_align('vcenter')
            okc_content_format.set_text_wrap()
            #########################################

            okl_content_format = wb.add_format()
            okl_content_format.set_font_size(15)
            okl_content_format.set_border(1)
            okl_content_format.set_font_color('black')
            okl_content_format.set_align('left')
            okl_content_format.set_align('vcenter')
            okl_content_format.set_text_wrap()

            #########################################
            ngc_content_format = wb.add_format()
            ngc_content_format.set_font_size(15)
            ngc_content_format.set_border(1)
            ngc_content_format.set_font_color('red')
            ngc_content_format.set_italic()
            ngc_content_format.set_fg_color('yellow')
            ngc_content_format.set_align('center')
            ngc_content_format.set_align('vcenter')
            ngc_content_format.set_text_wrap()
            ##########################################
            ngl_content_format = wb.add_format()
            ngl_content_format.set_font_size(15)
            ngl_content_format.set_border(1)
            ngl_content_format.set_font_color('red')
            ngl_content_format.set_italic()
            ngl_content_format.set_fg_color('yellow')
            ngl_content_format.set_align('left')
            ngl_content_format.set_align('vcenter')
            ngl_content_format.set_text_wrap()
            ##########################################
            currency_format = wb.add_format({'num_format': '###,###,##0.00'})
            currency_format.set_font_size(15)
            currency_format.set_border(1)
            currency_format.set_font_color('black')
            currency_format.set_align('right')
            currency_format.set_align('vcenter')
            currency_format.set_text_wrap()


            titles1 = ['產品組別', '項次', '品牌', '共契組別-項次', '機種-機型/料號','機型名稱', '序號', '維護期間', '規格說明', '數量', '優惠單價',
                       '優惠總價', '成本單價', '報價廠商','成本類型','成本*數量','毛利','毛利率','部門']
            title_width = [20, 20, 20, 40, 40, 40, 20, 20, 60, 20, 20, 20, 20, 20,20,20,20,20,20]

            row = 0

            col = 0
            for title in titles1:
                ws.write(row, col, title, head_format)
                myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
                ws.set_row(row, 30)
                ws.set_column(myloc, title_width[col])
                col += 1

            ws.freeze_panes(row + 1, 0)
            row += 1
            nitem = 1

            for line in projrec:
                myrow = row + 1
                if line.prodnum == 0 or line.dis_price == 0:
                    mysum1 = 0
                else:
                    mysum1 = line.prodnum * line.dis_price
                if line.prod_price == 0 or line.prodnum == 0 :
                    mysum2 = 0
                else:
                    mysum2 = line.prodnum * line.prod_price
                if mysum2 == 0:
                    mysum3 = 0
                else:
                    mysum3 = round(((mysum1 - mysum2)/mysum2),2)
                ws.write(row, 0, line.prodset if line.prodset else ' ', okl_content_format)
                ws.write(row, 1, line.saleitem_item if line.saleitem_item else ' ', okl_content_format)
                ws.write(row, 2, line.prodbrand if line.prodbrand else ' ', okl_content_format)
                ws.write(row, 3, ' ', okl_content_format)
                ws.write(row, 4, line.prodmodeltype if line.prodmodeltype else ' ', okl_content_format)
                ws.write(row, 5, line.prodmodeltype1 if line.prodmodeltype1 else ' ', okl_content_format)
                ws.write(row, 6, line.prodserial if line.prodserial else ' ', okl_content_format)
                ws.write(row, 7, line.maintenance_term if line.maintenance_term else ' ', okl_content_format)
                ws.write(row, 8, line.proddesc if line.proddesc else ' ', okl_content_format)
                ws.write(row, 9, line.prodnum if line.prodnum else ' ', okc_content_format)
                ws.write(row, 10, line.dis_price if line.dis_price else ' ', okc_content_format)
                ws.write(row, 11, mysum1, okc_content_format)
                ws.write(row, 12, line.prod_price if line.prod_price else ' ',okc_content_format)
                ws.write(row, 13, line.supplier if line.supplier else ' ', okl_content_format)
                ws.write(row, 14, line.costtype if line.costtype else ' ', okl_content_format)
                ws.write(row, 15,  mysum2, okc_content_format)
                ws.write(row, 16,  (mysum1 - mysum2), okc_content_format)
                ws.write(row, 17, mysum3, okc_content_format)
                ws.write(row, 18, line.cost_dept if line.cost_dept else ' ', okl_content_format)
                row += 1
                nitem += 1

            wb.close()
            output.seek(0)
            myxlsfile = base64.standard_b64encode(output.getvalue())
            output.close()

            myprojcount = self.env['neweb.projsaleitem_export'].search_count([])
            if myprojcount > 0:
                myrec = self.env['neweb.export_excel_download']
                myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})

                myviewid = self.env.ref('neweb_project.neweb_export_download_tree')

                return {
                    'view_name': 'newebexportexcel',
                    'name': ('成本分析明細匯出'),
                    'type': 'ir.actions.act_window',
                    'res_model': 'neweb.export_excel_download',
                    'view_id': myviewid.id,
                    'flags': {'action_buttons': True},
                    'view_type': 'form',
                    'view_mode': 'tree',
                    'target': 'main'}

# class NewebProjImportTag(models.Model):
#     _name = "neweb.projtag"
#
#     proj_id = fields.Integer(string="TAG ID")