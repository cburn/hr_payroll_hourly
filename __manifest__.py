# -*- coding: utf-8 -*-
{
    'name': "hr_payroll_hourly",

    'summary': """
        Add wage frequency to contract - monthly, weekly, hourly""",

    'description': """

    """,

    'author': "Chris Burn",
    'category': 'Human Resources',
    'version': '0.1',

    'depends': [
        'base',
        'hr_payroll',
    ],

    'data': [
        'views/hr_contract_view.xml',
    ],
}
