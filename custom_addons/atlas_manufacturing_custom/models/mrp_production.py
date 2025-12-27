
from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    atlas_real_cost = fields.Float(string="Coût Réel (MAD)", compute="_compute_atlas_real_cost", store=True)

    @api.depends('move_raw_ids.state', 'move_raw_ids.quantity')
    def _compute_atlas_real_cost(self):
        for production in self:
            cost = 0.0
            for move in production.move_raw_ids:
                if move.state == 'done':
                    # Simplified cost: quantity * standard_price of the product
                    cost += move.quantity * move.product_id.standard_price
            production.atlas_real_cost = cost
