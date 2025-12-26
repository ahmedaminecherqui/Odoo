
from odoo import models, fields

class StockLocation(models.Model):
    _inherit = 'stock.location'

    abc_category = fields.Selection([
        ('a', 'Category A (Fast Moving)'),
        ('b', 'Category B (Medium Moving)'),
        ('c', 'Category C (Slow Moving)'),
    ], string='ABC Category', default='c', help="ABC classification based on product rotation speed.")
