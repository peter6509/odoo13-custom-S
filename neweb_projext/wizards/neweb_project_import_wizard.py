# -*- coding: utf-8 -*-
# Author: Peter Wu

import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError,Warning
import sys
from datetime import datetime

XL_CELL_EMPTY = 0
XL_CELL_TEXT = 1
XL_CELL_NUMBER = 2
XL_CELL_DATE = 3
XL_CELL_BOOLEAN = 4
XL_CELL_ERROR = 5
XL_CELL_BLANK = 6


class projimportinheritwizard(models.TransientModel):
    _inherit = "neweb.saleitem_import_wizard"

    def converdate(self, s):
        try:
            s = str(int(s))
        except ValueError:
            date_dt = ''
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = '日期格式不對！ : %s ' % s
            return {
                'name': '日期格式錯誤！',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context,
            }

        if len(s) == 6 or len(s) == 7 or len(s) == 8:
            if len(s) == 6:
                year_s = s[:2]
                mon = s[2:4]
                day = s[4:]
                year = str(int(year_s) + 1911)
            if len(s) == 7:
                year_s = s[:3]
                mon = s[3:5]
                day = s[5:]
                year = str(int(year_s) + 1911)
            if len(s) == 8:
                year = s[:4]
                mon = s[4:6]
                day = s[6:]
            date_str = year + '-' + str(mon) + '-' + str(day)
            try:
                date_dt = datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = '日期格式不對！ : %s ' % date_str
                return {
                    'name': '日期格式錯誤！',
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'sh.message.wizard',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'context': context,
                }
        else:
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = '日期格式不對！ : %s ' % s
            return {
                'name': '日期格式錯誤！',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context,
            }
        return (date_dt)

    def check_import(self):
        # self.env.cr.execute("""update neweb_project set proj_import_status=TRUE where id = %d""" % self.env.context.get('proj_op_id'))
        if self.start_row == 1 :
            raise UserError("數值錯誤,ROW啟始數值從 2 開始")
        if self.start_row < 0 or self.end_row < 0:
            raise UserError("數值錯誤,ROW數值不能小於0")
        if self.start_row > self.end_row:
            raise UserError("數值錯誤,啟始ROW數值大於結止ROW")

        if not self.excel_file:
            raise UserError("檔案錯誤,沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)
        if self.start_row > 0 or self.end_row > 0:
            nstartrow = self.start_row
            if self.end_row > sheet.nrows:
               nendrow = sheet.nrows
            else:
               nendrow = self.end_row
        else:
            nstartrow = 2
            nendrow = sheet.nrows
            # print "%s" % nendrow
        # reload(sys)
        # sys.setdefaultencoding('utf-8')


        if not self.excel_file:
            raise UserError("沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)

        myamounttot = 0

        for row in range(nstartrow - 1, nendrow):
            cell = sheet.cell(row, 9)
            mysitemnum = 0
            try:
                if cell.ctype == XL_CELL_EMPTY:
                    view = self.env.ref('sh_message.sh_message_wizard')
                    view_id = view and view.id or False
                    context = dict(self._context or {})
                    context['message'] = '第 %d 筆的數量值不能空值' % row
                    return {
                        'name': '數量值錯誤！',
                        'type': 'ir.actions.act_window',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'sh.message.wizard',
                        'views': [(view.id, 'form')],
                        'view_id': view.id,
                        'target': 'new',
                        'context': context,
                    }

                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    if cell.ctype == XL_CELL_NUMBER:
                        mysitemnum = float(sheet.cell(row, 9).value)  # 數量
                    else:
                        view = self.env.ref('sh_message.sh_message_wizard')
                        view_id = view and view.id or False
                        context = dict(self._context or {})
                        context['message'] = '第 %d 筆的數量必需大於 0' % row
                        return {
                            'name': '數量值錯誤！',
                            'type': 'ir.actions.act_window',
                            'view_type': 'form',
                            'view_mode': 'form',
                            'res_model': 'sh.message.wizard',
                            'views': [(view.id, 'form')],
                            'view_id': view.id,
                            'target': 'new',
                            'context': context,
                        }

            except Exception as inst:
                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = '第 %d 筆的數量值格式錯誤' % row
                return {
                    'name': '數量值格式錯誤！',
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'sh.message.wizard',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'context': context,
                }

            cell = sheet.cell(row, 10)
            mysitemprice = 0
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    if cell.ctype == XL_CELL_NUMBER:
                        mysitemprice = float(sheet.cell(row, 10).value)  # 單價
                    else:
                        mysitemprice = 0
            except Exception as inst:
                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = '第 %d 筆的單價值格式錯誤' % row
                return {
                    'name': '單價值格式錯誤！',
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'sh.message.wizard',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'context': context,
                }

            myamounttot = myamounttot + (mysitemnum * mysitemprice)

        if myamounttot == 0:
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = '整張單的總收入不能為0 !'
            return {
                'name': '銷單總收入 = 0 ！',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context,
            }


        for row in range(nstartrow - 1, nendrow):
            cell = sheet.cell(row, 0)

            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
               myprodset = '' + str(cell.value)  # 產品組別
               myprodset1 = myprodset.replace(' ','').replace('/','').replace(' ','').upper()
               myprodsetrec = self.env['neweb.prodset'].search([('name1','=ilike',myprodset1)])
               if not myprodsetrec and myprodset1.isalnum():
                   view = self.env.ref('sh_message.sh_message_wizard')
                   view_id = view and view.id or False
                   context = dict(self._context or {})
                   context['message'] = '第 %d 筆的 產品組別值查無此產品組別：%s' % (row,myprodset)
                   return {
                       'name': '產品組別值格式錯誤！',
                       'type': 'ir.actions.act_window',
                       'view_type': 'form',
                       'view_mode': 'form',
                       'res_model': 'sh.message.wizard',
                       'views': [(view.id, 'form')],
                       'view_id': view.id,
                       'target': 'new',
                       'context': context,
                   }



            cell = sheet.cell(row, 2)
            myprodsetid = False
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    mysitembrand = '' + str(cell.value)  # 品牌
                    myprodset = self.env['neweb.prodbrand'].search([('name', '=ilike', mysitembrand)])
                    if not myprodset and mysitembrand.isalnum():
                        view = self.env.ref('sh_message.sh_message_wizard')
                        view_id = view and view.id or False
                        context = dict(self._context or {})
                        context['message'] = '第 %d 筆的 品牌值查無此品牌:%s' % (row,mysitembrand)
                        return {
                            'name': '品牌值格式錯誤！',
                            'type': 'ir.actions.act_window',
                            'view_type': 'form',
                            'view_mode': 'form',
                            'res_model': 'sh.message.wizard',
                            'views': [(view.id, 'form')],
                            'view_id': view.id,
                            'target': 'new',
                            'context': context,
                        }

            except Exception as inst:
                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = '第 %d 筆的 品牌值查無此品牌:%s' % (row,mysitembrand)
                return {
                    'name': '品牌值格式錯誤！',
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'sh.message.wizard',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'context': context,
                }



            cell = sheet.cell(row, 7)
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mymaindate = '' + str(cell.value)  # 維護起迄日期
                mymaindate = mymaindate.strip()
                if mymaindate == '':
                    myresult = True
                else:
                    if not mymaindate[0:8].isdigit() and not mymaindate[0:8].isalnum() and cell.ctype not in (XL_CELL_EMPTY):
                        view = self.env.ref('sh_message.sh_message_wizard')
                        view_id = view and view.id or False
                        context = dict(self._context or {})
                        context['message'] = '第 %d 筆的 維護起始日期 %s 不合法,請確認' % (row, mymaindate[0:8])
                        return {
                            'name': '維護起始日期格式錯誤！',
                            'type': 'ir.actions.act_window',
                            'view_type': 'form',
                            'view_mode': 'form',
                            'res_model': 'sh.message.wizard',
                            'views': [(view.id, 'form')],
                            'view_id': view.id,
                            'target': 'new',
                            'context': context,
                        }
                    mymainstart = self.converdate(mymaindate[0:8])
                    # print "%d %s" % (row, mymainstart)
                    try:
                        myresult = datetime.strftime(mymainstart, '%Y-%m-%d %H:%M:%S')
                    except Exception as inst:
                        view = self.env.ref('sh_message.sh_message_wizard')
                        view_id = view and view.id or False
                        context = dict(self._context or {})
                        context['message'] = '第 %d 筆的 維護起始日期 %s 不合法,請確認!' % (row, mymainstart)
                        return {
                            'name': '維護起始日期格式錯誤！',
                            'type': 'ir.actions.act_window',
                            'view_type': 'form',
                            'view_mode': 'form',
                            'res_model': 'sh.message.wizard',
                            'views': [(view.id, 'form')],
                            'view_id': view.id,
                            'target': 'new',
                            'context': context,
                        }

                    if not mymaindate[9:].isdigit() and not mymaindate[9:].isalnum() :
                        view = self.env.ref('sh_message.sh_message_wizard')
                        view_id = view and view.id or False
                        context = dict(self._context or {})
                        context['message'] = '第 %d 筆的 維護截止日期 %s 不合法,請確認' % (row, mymaindate[9:])
                        return {
                            'name': '維護截止日期格式錯誤！',
                            'type': 'ir.actions.act_window',
                            'view_type': 'form',
                            'view_mode': 'form',
                            'res_model': 'sh.message.wizard',
                            'views': [(view.id, 'form')],
                            'view_id': view.id,
                            'target': 'new',
                            'context': context,
                        }
                    else:
                        mymainend = self.converdate(mymaindate[9:])
                        # print "%s" % mymainend
                        try:
                            myresult = datetime.strftime(mymainend, '%Y-%m-%d %H:%M:%S')
                        except Exception as inst:
                            view = self.env.ref('sh_message.sh_message_wizard')
                            view_id = view and view.id or False
                            context = dict(self._context or {})
                            context['message'] = '第 %d 筆的 維護截止日期 %s 不合法,請確認!' % (row, mymainend)
                            return {
                                'name': '維護截止日期格式錯誤！',
                                'type': 'ir.actions.act_window',
                                'view_type': 'form',
                                'view_mode': 'form',
                                'res_model': 'sh.message.wizard',
                                'views': [(view.id, 'form')],
                                'view_id': view.id,
                                'target': 'new',
                                'context': context,
                            }



            cell = sheet.cell(row, 9)
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                try:
                    if str(sheet.cell(row,9).value).isalnum():
                       int(sheet.cell(row,9).value)
                except Exception as inst:
                    view = self.env.ref('sh_message.sh_message_wizard')
                    view_id = view and view.id or False
                    context = dict(self._context or {})
                    context['message'] = '第 %d 筆的 數量 %s 不合法,請確認!' % (row, sheet.cell(row,9).value)
                    return {
                        'name': '數量格式錯誤！',
                        'type': 'ir.actions.act_window',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'sh.message.wizard',
                        'views': [(view.id, 'form')],
                        'view_id': view.id,
                        'target': 'new',
                        'context': context,
                    }


            cell = sheet.cell(row, 10)
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                try:
                    if str(sheet.cell(row,10).value).isalnum():
                        int(sheet.cell(row,10).value)
                except Exception as inst:
                    view = self.env.ref('sh_message.sh_message_wizard')
                    view_id = view and view.id or False
                    context = dict(self._context or {})
                    context['message'] = '第 %d 筆的 優惠銷價 %s 不合法,請確認!' % (row, sheet.cell(row, 10).value)
                    return {
                        'name': '優惠銷價格式錯誤！',
                        'type': 'ir.actions.act_window',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'sh.message.wizard',
                        'views': [(view.id, 'form')],
                        'view_id': view.id,
                        'target': 'new',
                        'context': context,
                    }


            cell = sheet.cell(row, 12)
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                try:
                    if str(sheet.cell(row, 12).value).isalnum():
                        int(sheet.cell(row, 12).value)
                except Exception as inst:
                    view = self.env.ref('sh_message.sh_message_wizard')
                    view_id = view and view.id or False
                    context = dict(self._context or {})
                    context['message'] = '第 %d 筆的 成本單價 %s 不合法,請確認!' % (row, sheet.cell(row, 12).value)
                    return {
                        'name': '成本單價格式錯誤！',
                        'type': 'ir.actions.act_window',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'sh.message.wizard',
                        'views': [(view.id, 'form')],
                        'view_id': view.id,
                        'target': 'new',
                        'context': context,
                    }



            cell = sheet.cell(row, 13)
            mysupplier = False
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mysuppliername = '' + str(cell.value)  # 供應商
               mysupplierrec = self.env['res.partner'].search([('name','=ilike',mysuppliername),('active','=',True),('is_company','=',True)])
               if not mysupplierrec and mysuppliername.isalnum() :
                   view = self.env.ref('sh_message.sh_message_wizard')
                   view_id = view and view.id or False
                   context = dict(self._context or {})
                   context['message'] = '第 %d 筆的 供應商 %s 資料庫沒記錄,請確認!' % (row, sheet.cell(row, 13).value)
                   return {
                       'name': '供應商格式錯誤！',
                       'type': 'ir.actions.act_window',
                       'view_type': 'form',
                       'view_mode': 'form',
                       'res_model': 'sh.message.wizard',
                       'views': [(view.id, 'form')],
                       'view_id': view.id,
                       'target': 'new',
                       'context': context,
                   }

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '檢查 EXCEL 匯入檔格式沒問題,可以匯入 !'
        return {
            'name': '格式檢驗完成！',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }


