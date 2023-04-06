# -*- coding: utf-8 -*-
# Author : Peter Wu
{
    'name': "ERA 租屋住戶合約模組",
    'version': '13.0',
    'summary': "ERA 租屋住戶合約模組",
    'description': """ERA 租屋住戶合約管理模組""",
    'author': "LANSIR Technology CO.,LTD.",
    'category': 'HouseHold Manager Contract',
    'depends': ['era_household'],
    'data': [
             'data/era_contract_data.xml',
             'security/era_contract_security.xml',
             'security/era_contract_security1.xml',
             'security/ir.model.access.csv',
             'views/era_contract.xml',
             'views/era_contract_seq.xml',
             'wizards/era_contract_wizard.xml',
             'views/era_member_contract.xml',
             'views/era_contract_actiondone.xml',
             'views/era_landlord_contract.xml',
             'wizards/era_landlord_contract_wizard.xml',
             'wizards/era_contract_close_wizard.xml',
             'views/era_contract_menu.xml',
              ],
    'installable': True,
    'application': True,

}
