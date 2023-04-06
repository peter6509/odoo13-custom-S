# -*- coding: utf-8 -*-
# Author : Peter Wu

{
    'name': "ERA_EXT 租屋住戶管理模組",
    'version': '13.0',
    'summary': "ERA_EXT 租屋住戶管理模組",
    'description': """ERA_EXT 租屋住戶管理模組(住戶日用電度數記錄/租戶儲值收款記錄/費用對帳記錄Line租戶)""",
    'author': "LANSIR Technology CO.,LTD.",
    'category': 'HouseHold Manager',
    'depends': [],
    'data': [
            'security/era_household_security1.xml',
              'security/ir.model.access.csv',
              'security/era_household_rule.xml',
              'views/era_household_landlord.xml',
              'views/era_member_inherit.xml',
              'views/era_household_inherit.xml',
              'wizards/era_account_balance_wizard.xml',
              'views/era_landlord_menu.xml',
              ],
    'installable': True,
    'application': True,

}
