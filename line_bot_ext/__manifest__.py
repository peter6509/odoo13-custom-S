{
    'name': 'Line Bot Ext',
    'category': 'Tools',
    'version': '1.0',
    "author" : 'Helmi Dhaoui',
    'website' : 'http://tunisofts.com',
    'description':
        """Line Bot Ext""",
    'depends': [ 'line_bot'],
    'data': ['security/ir.model.access.csv',
             'views/era_send_line_message.xml',
             'wizards/era_send_message_wizard.xml',

             'views/era_line_send_menu.xml',
    ],
    'installable': True,
}
