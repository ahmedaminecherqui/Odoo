# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    loyalty_points = fields.Float(string='Points de Fidélité', default=0.0, readonly=True, help="1 MAD = 1 point")
