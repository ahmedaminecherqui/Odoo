# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    points_earned = fields.Float(string='Points à gagner', compute='_compute_points_earned', store=True)

    @api.depends('amount_total')
    def _compute_points_earned(self):
        for order in self:
            # 1 MAD = 1 Point
            order.points_earned = order.amount_total

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.partner_id:
                order.partner_id.loyalty_points += order.points_earned
        return res
