# -*- coding: utf-8 -*-
# Author : Peter Wu
{
    'name': "CloudRent 租屋住戶合約模組",
    'version': '13.0',
    'summary': "CloudRent 租屋住戶合約模組",
    'description': """CloudRent 租屋住戶合約管理模組""",
    'author': "ALLDO Technology CO.,LTD.",
    'category': 'HouseHold Manager Contract',
    'depends': ['cloudrent_household'],
    'data': [
             'data/cloudrent_contract_data.xml',
             'security/cloudrent_contract_security.xml',
             'security/cloudrent_contract_security1.xml',
             'security/ir.model.access.csv',
             'views/cloudrent_contract.xml',
             'views/cloudrent_contract_seq.xml',
             'wizards/cloudrent_contract_wizard.xml',
             'views/cloudrent_member_contract.xml',
             'views/cloudrent_contract_actiondone.xml',
             'views/cloudrent_landlord_contract.xml',
             'wizards/cloudrent_landlord_contract_wizard.xml',
             'wizards/cloudrent_contract_close_wizard.xml',
             'wizards/cloudrent_new_contract_wizard.xml',
             'views/cloudrent_contract_menu.xml',
              ],
    'installable': True,
    'application': True,

}
