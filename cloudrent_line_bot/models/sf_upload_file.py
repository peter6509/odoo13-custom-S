# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)

from odoo import api, fields, models
from odoo.exceptions import UserError
import os
from os import walk, remove
from os.path import join, splitext
import base64
import urllib.request
from urllib.parse import urlunparse


class NewModule(models.Model):
    _inherit = 'product.template'

    product_pdf = fields.Binary(string='產品工程圖檔')


class SFUploadFilePath(models.Model):
    _name = 'sf.upload.filepath'

    image_path = fields.Char(string="上傳照片圖檔的路徑")
    pdf_path = fields.Char(string="上傳產品PDF的路徑")

    @api.model
    def create(self, vals):
        if 'path' in vals and not vals['image_path']:
            raise UserError("上傳照片圖檔路徑不能為空值")
        if 'path' in vals and not vals['pdf_path']:
            raise UserError("上傳產品PDF路徑不能為空值")
        image_num = self.env['sf.upload.filepath'].search_count([])
        pdf_num = self.env['sf.upload.filepath'].search_count([])
        if image_num > 0 or pdf_num > 0:
            raise UserError("只能設定一筆檔案路徑")
        res = super(SFUploadFilePath, self).create(vals)
        return res

    # 上傳圖檔示例如下：
    # image = urllib2.urlopen('http://ddd.com/somepics.jpg').read()
    #
    # image_base64 = base64.encodestring(image)
    #
    # product.image_medium = image_base64 // (new api v9)

    def automatic_upload_image(self):
        path_ids = self.search([])
        if path_ids.image_path:
            for root, dirs, files in walk(path_ids.image_path):
                for f in files:
                    fullpath = join(root, f)
                    # print(fullpath)
                    file_name = splitext(f)[0]
                    fullpath_all = 'file://' + fullpath
                    image = urllib.request.urlopen(fullpath_all).read()
                    # image_base64 = base64.encodebytes(image)
                    image_base64 = base64.b64encode(image)
                    product = self.env['product.template'].search([('default_code', 'like', file_name)], limit=1)
                    if product:
                        product_get = self.env['product.product'].search([('product_tmpl_id', '=', product.id)], limit=1)
                        if product_get:
                            product_get.image_variant_1920 = image_base64
                            product.image_1920 = image_base64
                            os.remove(fullpath)
                            self._cr.commit()

    def automatic_upload_pdf(self):
        path_ids = self.search([])
        if path_ids.pdf_path:
            for root, dirs, files in walk(path_ids.pdf_path):
                for f in files:
                    fullpath = join(root, f)
                    # print(fullpath)
                    file_name = splitext(f)[0]
                    fullpath_all = 'file://' + fullpath
                    pdf = urllib.request.urlopen(fullpath_all).read()
                    pdf_base64 = base64.encodebytes(pdf)
                    product = self.env['product.template'].search([('default_code', 'like', file_name)], limit=1)
                    if product:
                        product.product_pdf = pdf_base64
                        os.remove(fullpath)
                        self._cr.commit()