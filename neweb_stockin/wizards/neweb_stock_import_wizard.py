# -*- coding: utf-8 -*-
# Author : Peter Wu


import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import sys

XL_CELL_EMPTY = 0
XL_CELL_TEXT = 1
XL_CELL_NUMBER = 2
XL_CELL_DATE = 3
XL_CELL_BOOLEAN = 4
XL_CELL_ERROR = 5
XL_CELL_BLANK = 6


class stockimportwizard(models.TransientModel):
    _name = "neweb_stockin.stock_import_wizard"

    excel_file = fields.Binary(string="上傳EXCEL檔案",attachment=False)
   

    def stock_action_import(self):

        if not self.excel_file:
            raise UserError("檔案錯誤,沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)

        nstartrow = 2
        nendrow = sheet.nrows
            # print "%s" % nendrow
        # reload(sys)
        sys.setdefaultencoding('utf-8')
        self.ensure_one()
        myinventoryid = self.env.context.get('inventory_id')
        #inventory_rec = self.env['stock.inventory.line'].search([('inventory_id', '=', self.env.context.get('inventory_id'))])

        if not self.excel_file:
            raise UserError("沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)

        stock_rec = self.env['stock.inventory'].search([('id','=',myinventoryid)])
        mylocationid = stock_rec.location_id

        for row in range(nstartrow -1, nendrow):

            cell = sheet.cell(row, 1)
            myprodid = False
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myprodtype = u'' + str((cell.value).decode('utf-8'))  # 產品料號
               #print "%s" % myprodtype
               myprodname = '%'+myprodtype+'%'
               self.env.cr.execute("select id from product_template where name like '%s'" % myprodname)
               myprodid = self.env.cr.fetchone()


            cell = sheet.cell(row, 2)
            mystocknum = 0
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               if cell.ctype == XL_CELL_NUMBER :
                  mystocknum = float(sheet.cell(row, 2).value)  # 數量
               else:
                  mystocknum = 0

            if myprodid:
               print ("%d %d %d %d" % (stock_rec.id, mylocationid.id, myprodid[0], mystocknum))
               self.env.cr.execute("select updateinventoryline(%d,%d,%d,%d)" % (stock_rec.id,mylocationid.id,myprodid[0],mystocknum))
               self.env.cr.execute("commit")

        return {'view_name': 'stockimportwizard',
                'name': ('盤點明細資料'),
                'views': [[False, 'form'], ],
                'res_model': 'stock.inventory',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                # 'domain': mydomain,
                'res_id': myinventoryid,
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                'view_mode': 'form',
                'view_type': 'form'
                }

