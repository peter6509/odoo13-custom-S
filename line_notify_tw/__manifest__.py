# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)

{
    'name': 'Line Notify Messages',
    'version': '12.0.1.0',
    'summary': '用來做為員工訂閱公司Line Notify的通知訊息',
    'description': '採用Line Notify並讓員工自行訂閱後，可接收從ODOO發送的消息通知',
    'category': 'Tools',
    'author': 'Jason Wu(jaronemo@msn.com)',
    'depends': ['base', 'web', 'hr', 'mail'],
    'data': ['security/line_notify_group.xml',
             'security/ir.model.access.csv',
             'views/line_notify_configure.xml',
             'views/hr_employee.xml',
             'wizard/line_notify_send.xml'],
    'installable': True,
    'auto_install': False,
}