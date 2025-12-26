
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    # Exemples de champs spécifiques ou de logique pour la conformité marocaine
    l10n_ma_tax_report = fields.Boolean(string="Inclus dans le rapport de TVA", default=True)
    
    # Logique pour forcer l'analytique sur les comptes de charges (classe 6 en PCN)
    @api.constrains('line_ids')
    def _check_analytic_on_expenses(self):
        for move in self:
            for line in move.line_ids:
                if line.account_id.code and line.account_id.code.startswith('6') and not line.analytic_distribution:
                    # On pourrait lever une exception ici ou logger un avertissement
                    pass
