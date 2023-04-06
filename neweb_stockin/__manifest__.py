#_*_ coding: utf-8 _*_
# Author : Peter Wu


{
    'name': u'<3>.NEWEB 進出貨管理模組',
    'license': 'LGPL-3',
    'version': '1.0',
    'category': 'Stock management',
    'sequence': 4,
    "website": "http://www.lansir.com.tw",
    "author": "LANSIR Technology",
    'depends': ['product', 'purchase','stock','web',],
    'data': [
             'security/ir.model.access.csv',
             'security/neweb_stock_menu_security.xml',
             'views/neweb_stockin_selectable1.xml',
             'wizards/neweb_stockinqc_wizard.xml',
             'wizards/neweb_stockin_qcedit.xml',
             'wizards/neweb_stockin_qcout.xml',
             'views/neweb_stockout_selectable1.xml',
             'views/neweb_stock_categ.xml',
             'views/neweb_stockds_selectable.xml',
             'data/neweb_stockincheck_emailtemplate.xml',
             'views/neweb_stockpicking_inherit.xml',
             # # 'data/neweb_stockinqc_emailtemplate.xml',   # 刪除
             'wizards/neweb_qcsendmail_wizard.xml',
             'wizards/neweb_stock_import_wizard.xml',
             # 'views/neweb_stock_inventory_inherit.xml',    # 要更改
             # 'views/neweb_stockquant_inherit.xml',         # 要更改
             'views/neweb_stockpicking_inherit1.xml',
             'data/neweb_stocking_sequence.xml',
             'views/neweb_stockout_inherit.xml',
             'views/neweb_stockout_inherit1.xml',
             'views/neweb_stockout_inherit2.xml',
             'views/neweb_stockout_inherit3.xml',
             'views/product_template_inherit.xml',
             'views/product_template_inherit1.xml',
             'views/neweb_company_stockloc.xml',
            'views/neweb_stockmoveline_inherit.xml',
            'views/neweb_stockmoveline1_inherit.xml',
            'views/neweb_stockmoveline2_inherit.xml',
             ],
    'application': True,
    'installable': True,
    'description': u'<3>.NEWEB 進出貨管理模組',
    'summary': u'<3>.NEWEB 進出貨管理模組',
}
