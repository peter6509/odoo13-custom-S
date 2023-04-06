# -*- coding: utf-8 -*-
{
    'name': 'Line Bot',
    'category': 'Tools',
    'version': '1.0',
    "author" : 'Helmi Dhaoui',
    'website' : 'http://tunisofts.com',
    'description':
        """Line Bot""",
    'depends': ['web', 'era_household'],
    'data': [
        'views/era_household_member.xml',
        'views/era_household_member_history.xml',
        'views/line_bot.xml',

        'security/ir.model.access.csv',

        'views/default_data.xml',
    ],
    'installable': True,
}

