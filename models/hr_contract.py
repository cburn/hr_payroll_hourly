# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrContract(models.Model):
    _inherit = 'hr.contract'

    salary_unit = fields.Selection([('yearly', 'Annual Wage'),
                                    ('monthly', 'Monthly Wage'),
                                    ('daily', 'Daily Wage'),
                                    ('hourly', 'Hourly Wage')],
                                    string="Salary Per", default="monthly",
                                    required=True)
