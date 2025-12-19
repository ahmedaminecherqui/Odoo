# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    purchase_alert_threshold = fields.Float(
        string="Seuil d'alerte achat",
        default=0.0,
        help="Niveau de stock en dessous duquel une alerte ou un achat doit être déclenché."
    )
