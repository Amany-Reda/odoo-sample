{
    'name': 'show payment date in invoice tree',
    'version': '17.0.0.0',
    'summary': 'show payment date for customer in invoice tree',
    'description': """This module helps to show payment date for customer in invoice tree""",
    'author': "Gate By Amany",
    'category': 'Account/Customer/Invoices',
    'website': "https://www.gate-its.com",
    'company': 'Gate ITS',
   'depends': [
        'account',
        'base_setup',
        'analytic',
        'portal',
        'digest'
    ],
    'data': [
        'views/account_move_views.xml',
     ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}