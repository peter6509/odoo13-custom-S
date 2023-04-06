# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)

from odoo import api, fields, models
import base64
from io import BytesIO
import string
import secrets

try:
    import qrcode
except ImportError:
    raise ImportError(
        '此模組必須要安裝 qrcode 才能運作，請配合安裝，謝謝!!(sudo pip3 install qrcode)')


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    qr_image = fields.Binary(string='QR Code', attachment=True, store=True)
    state_code = fields.Char(string='Line Notify state code', readonly=True)
    line_access_token = fields.Char(string='Line Access Token', readonly=True)

    def generate_secrets_code(self):
        code_list = self.search([('state_code', 'not in', False)])
        if not self.state_code:
            state_code = ''.join(secrets.choice(string.ascii_letters) for _ in range(48))
            state_check = code_list.filtered(lambda x: x.state_code not in state_code)
            if not state_check:
                self.state_code = state_code
                self.generate_qr_code()
            else:
                self.generate_secrets_code()
        else:
            self.generate_qr_code()

    def generate_qr_code(self):
        # 定義 QRcode的 參數，可調整，詳細請參閱python qrcode 規範
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # 取Line Notify Configure 參數值做為 qrcode value
        line_configure = self.env['line.notify.configure'].search([('active', '=', True), ('test_mode', '=', False)])
        # 目前只取第一筆有效的服務通知，後續在思考如何變化它。
        URL = line_configure.notify_url + 'response_type=code' + '&client_id=' + line_configure.client_id + '&redirect_uri=' + line_configure.redirect_url + '&scope=notify' + '&state=' + self.state_code
        print(URL)
        qr.add_data(URL)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        self.qr_image = qr_image

    def generate_unlink(self):
        self.ensure_one()
        if self.line_access_token:
            self.line_access_token = ''
            self.qr_image = ''
