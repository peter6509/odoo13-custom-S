# -*- coding: utf-8 -*-
# Author : Peter Wu

{
    'name': "CloudRent 租屋住戶修繕記錄",
    'version': '13.0',
    'summary': "CloudRent 租屋住戶修繕記錄",
    'description': """CloudRent 租屋住戶修繕記錄(flow)""",
    'author': "ALLDO Technology CO.,LTD.",
    'category': 'CloudRent HouseHold Reapir',
    'depends': ['sh_message'],
    'data': ['data/maintenance_seq_data.xml',
             'security/ir.model.access.csv',
             'security/cloudrent_household_maintenance_rule.xml',
             'views/cloudrent_member_care.xml',
             'views/cloudrent_household_maintenance.xml',
             'wizards/cloudrent_maintenance_wizard.xml',

             'views/cloudrent_maintenance_menu.xml',
              ],
    'installable': True,
    'application': True,

}

