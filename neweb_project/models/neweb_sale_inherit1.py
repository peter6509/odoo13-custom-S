# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class newebsaleinherit1(models.Model):
    _inherit = "sale.order"

    @api.depends('user_id')
    def _get_address(self):
        for rec in self:
            myaddress = ' '
            try:
                myempworkphone = self.env['hr.employee'].search([('user_id', '=', rec.user_id.id)])[0].work_phone
            except Exception as inst:
                myempworkphone = ' '
            if myempworkphone:
                if myempworkphone[1:3] == '02' or myempworkphone[0:2] == '02':
                    myaddress = '台北市內湖區行忠路42號2F'
                    # rec.update({'branch_address': '台北市內湖區行忠路42號2F'})
                elif myempworkphone[1:3] == '07' or myempworkphone[0:2] == '07':
                    myaddress = '高雄市前鎮區中山二路260號21樓A1'
                    # rec.update({'branch_address': '高雄市前鎮區中山二路260號21樓A1'})
                elif myempworkphone[1:3] == '04' or myempworkphone[0:2] == '04':
                    myaddress = '台中市南區工學一街197巷32號'
                    # rec.update({'branch_address': '台中市南區工學一街197巷32號'})
                elif myempworkphone[1:3] == '03' or myempworkphone[0:2] == '03':
                    myaddress = '新竹市東區慈雲路118號12樓之5'
                    # rec.update({'branch_address': '新竹市東區慈雲路118號12樓之5'})
                else:
                    myaddress = '台北市內湖區行忠路42號2F'
                    # rec.update({'branch_address': '台北市內湖區行忠路42號2F'})
            else:
                myaddress = '台北市內湖區行忠路42號2F'
            rec.branch_address = myaddress
            return myaddress

    @api.depends('user_id')
    def _get_phone(self):
        for rec in self:
            myphone=' '
            try:
                myempworkphone = self.env['hr.employee'].search([('user_id', '=', rec.user_id.id)])[0].work_phone
            except Exception as inst:
                myempworkphone = ''
            if myempworkphone:
                if myempworkphone[1:3] == '02' or myempworkphone[0:2] == '02':
                    myphone= '(02)-27956660'
                    # rec.update({'branch_phone': '(02)-27956660'})
                elif myempworkphone[1:3] == '07' or myempworkphone[0:2] == '07':
                    myphone = '(07)-3348739'
                    # rec.update({'branch_phone': '(07)-3348739'})
                elif myempworkphone[1:3] == '04' or myempworkphone[0:2] == '04':
                    myphone = '(04)-22650205'
                    # rec.update({'branch_phone': '(04)-22650205'})
                elif myempworkphone[1:3] == '03' or myempworkphone[0:2] == '03':
                    myphone = '(03)-5777388'
                    # rec.update({'branch_phone': '(03)-5777388'})
                else:
                    myphone = '(02)-27956660'
                    # rec.update({'branch_phone': '(02)-27956660'})
            else:
                myphone = '(02)-27956660'
            rec.branch_phone = myphone
            return myphone

    @api.depends('user_id')
    def _get_fax(self):
        for rec in self:
            myfax = ' '
            try:
                myempworkphone = self.env['hr.employee'].search([('user_id', '=', rec.user_id.id)])[0].work_phone
            except Exception as inst:
                myempworkphone = ' '
            if myempworkphone:
                if myempworkphone[1:3] == '02' or myempworkphone[0:2] == '02':
                    myfax='(02)-27955510'
                    # rec.update({'branch_fax': '(02)-27955510'})
                elif myempworkphone[1:3] == '07' or myempworkphone[0:2] == '07':
                    myfax='(07)-3345639'
                    # rec.update({'branch_fax': '(07)-3345639'})
                elif myempworkphone[1:3] == '04' or myempworkphone[0:2] == '04':
                    myfax=' '
                    # rec.update({'branch_fax': ''})
                elif myempworkphone[1:3] == '03' or myempworkphone[0:2] == '03':
                    myfax='(03)-5777380'
                    # rec.update({'branch_fax': '(03)-5777380'})
                else:
                    myfax = ' '
                    # rec.update({'branch_fax': ''})
            else:
                myfax='(02)-27955510'
            rec.branch_fax = myfax
            return myfax

    project_name = fields.Char(string="專案名稱")
    branch_address = fields.Char(string="分公司地址",compute=_get_address)
    branch_phone = fields.Char(string="分公司電話",compute=_get_phone)
    branch_fax = fields.Char(string="分公司傳真",compute=_get_fax)






