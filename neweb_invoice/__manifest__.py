# -*- coding: utf-8 -*-
# Author : Peter Wu
#

{
    'name': '<8>.NEWEB 發票開立申請',
    'license': 'LGPL-3',
    'version': '13.0',
    'category': 'Project Invoice Open',
    'sequence': 11,
    "website": "http://www.lansir.com.tw",
    "author": "LANSIR Technology",
    'depends': ['base', 'neweb_project','neweb_contract',],
    'data': [
              'security/ir.model.access.csv',
              'security/neweb_invoice_sendmail_security.xml',
              'security/neweb_inv_reminder_alert_security.xml',
              'wizards/neweb_invoice_wizard.xml',
              'views/neweb_invoice.xml',
              'data/neweb_invoiceopen_approve_mail.xml',
              'data/neweb_invoiceopen_reject_mail.xml',
              'data/neweb_invoice_payment_mail.xml',
              'data/neweb_reminder_template.xml',
              'data/neweb_weekly_alert.xml',
              # 'data/neweb_invoiceopen_sequence.xml',
              'security/neweb_invoiceopen_rule.xml',
              'views/neweb_invoiceopen_inherit.xml',
              'views/neweb_invoiceopen_inherit1.xml',
              'views/neweb_projinvoice_download.xml',
              'wizards/neweb_proj_inv_wizard.xml',
              'views/neweb_invoice_sendmail.xml',
              'views/neweb_inv_reminder.xml',
              'views/neweb_inv_alert.xml',
             ],
    'application': True,
    'installable': True,
    'description': '<8>.NEWEB 發票開立申請',
    'summary': '<8>.NEWEB 發票開立申請'
}

