# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request, route

import json


class PaymentPortal(http.Controller):

    @route('/mes/get_qc_order', type='http', auth='public', cors='*', csrf=False)
    def get_qc_order(self):
        fqc_order = request.env['mes.fqc.order'].sudo().search([])
        qc_list = []
        for data in fqc_order:
            barcode_line = []
            pic_line = []
            for line in data.qc_barcode_ids:
                barcode_line.append({
                    'barcode_seq': line.barcode_seq,
                    'barcode_name': line.barcode_name,
                })
            for line in data.qc_pic_ids:
                pic_line.append({
                    'pic_seq': line.pic_seq,
                    'pic_name': line.pic_name,
                })
        qc_list.append({
            'name': data.name,
            'date': data.date.strftime("%Y-%m-%d %H:%M:%S"),
            'mo_number': data.mo_number,
            'qc_prod_no': data.qc_prod_no,
            'qc_lot_number': data.qc_lot_number,
            'barcode_line': barcode_line,
            'pic_line': pic_line
        })
        return str(qc_list)
