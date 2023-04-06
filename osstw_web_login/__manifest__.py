# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '登入頁面模組',
    'version': '13.0',
    'category': 'Web',
    'description': """

    登入頁面修改成自己的頁面

    """,
    'summary': 'login web',
    'sequence': 45,
    'depends': [
        'web',
    ],
    'data': [
        'views/osstw_web_templates.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
