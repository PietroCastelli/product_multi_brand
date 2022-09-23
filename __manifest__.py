# -*- coding: utf-8 -*-
{
    'name': "Product Multi Brand",
    
    'summary': "extension for invenory app",
  
    'license': 'OPL-1',

    'author': "STeSI Srl",

    'category': '',
  
    'version': '14.0.0.1',
  
    'website': "http://www.stesi.eu",

    # any module necessary for this one to work correctly
    'depends': ['stock','product_brand','product'],
    
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/brand_menu.xml'
    ],

    'application': False,
}
