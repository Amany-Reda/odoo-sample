{
    'name': 'Some Changes In Sale',
    'version': '16.0.0.0',
    'summary': 'Modifiy sale module',
    'description': """This module helps to modify some things in sales""",
    'website': 'https://www.gate-its.com',
    'author': "Gate By Amany",
    'category': 'Sales/Quotation',
    'depends': [
        'sale',
        'hr',
        'product',
    ],
    'data': [
        'views/sale_order_views.xml',
        'views/sale_order_line_views.xml',
        'report/sale_order_report.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'license': 'AGPL-3',
    'auto_install': False,
    'category': 'Inventory',
}