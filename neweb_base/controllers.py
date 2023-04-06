# -*- coding: utf-8 -*-
from odoo import http

# class BaseExt(http.Controller):
#     @http.route('/base_ext/base_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_ext/base_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_ext.listing', {
#             'root': '/base_ext/base_ext',
#             'objects': http.request.env['base_ext.base_ext'].search([]),
#         })

#     @http.route('/base_ext/base_ext/objects/<model("base_ext.base_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_ext.object', {
#             'object': obj
#         })