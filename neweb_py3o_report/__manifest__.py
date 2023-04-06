# -*- coding: utf-8 -*-
# Author : Peter Wu

{
    'name': u"<13>.NEWEB PY3O報表",
    'version': '1.0',
    'summary': "NEWEB PY3O Report Template",
    'sequence': 15,
    'description': """NEWEB PY3O Report Template.... """,
    'author': "ALLDO Technology,Peter Wu",
    'category': 'Reports',
    'depends': ['neweb_project','neweb_repair','neweb_purchase','neweb_stockin' ],
    'data': [
              'views/py3onewebproject.xml',
              'views/py3onewebpurchaserequire.xml',
              'views/py3osaleorder.xml',
              'views/py3onewebrepair.xml',
              'reports/neweb_py3o_report.xml',    # 成本分析 py3o

    ],
    'installable': True,
    'application': True,

}
