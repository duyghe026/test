# -*- coding: utf-8 -*-
{
    'name': "My pet - minhng.info",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "minhng.info",
    'website': "https://minhng.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [],
    # 'qweb': ['static/src/xml/*.xml'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_views.xml',
    ],

    'installable': True,
    'application': True,
}
