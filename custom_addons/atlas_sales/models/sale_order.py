# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('to_approve', 'À Approuver')], ondelete={'to_approve': 'set default'})

    def action_confirm(self):
        for order in self:
            if order.amount_total > 50000 and order.state != 'to_approve':
                order.write({'state': 'to_approve'})
                # Send notification or whatever
                return True
        return super(SaleOrder, self).action_confirm()

    def action_approve(self):
        self.write({'state': 'sent'})
        return self.action_confirm()
