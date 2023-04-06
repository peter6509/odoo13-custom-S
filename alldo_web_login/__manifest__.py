# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '99.ＡllDo 登入頁面模組',
    'version': '13.0',
    'category': 'Web',
    'description': """

    AllDo 登入頁面修改成自己的頁面

    """,
    'summary': 'login web',
    'sequence': 99,
    'depends': [
        'web',
    ],
    'data': [
        'views/alldo_web_templates.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
