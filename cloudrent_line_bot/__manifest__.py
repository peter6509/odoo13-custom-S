# -*- coding: utf-8 -*-
{
    'name': 'CloudRent Line Bot',
    'category': 'Tools',
    'version': '13.0',
    "author" : 'Peter Wu',
    'website' : 'http://www.alldo.com',
    'description':
        """CloudRent Line Bot""",
    'depends': ['web', 'cloudrent_household'],
    'data': [
        'views/cloudrent_household_member.xml',
        'views/cloudrent_household_member_history.xml',
        'views/line_bot.xml',
        'security/ir.model.access.csv',
        'views/default_data.xml',
        'views/cloudrent_send_line_message.xml',
        'wizards/cloudrent_send_message_wizard.xml',
        'views/line_notify_configure.xml',
        'views/cloudrent_linelog.xml',
        'views/cloudrent_paymentlog.xml',
        'views/cloudrent_maintenancelog.xml',
        'views/cloudrent_line_send_menu.xml',
    ],
    'installable': True,
    'application': True,
}

