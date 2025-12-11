# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Membre de bibliothèque'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Membre'

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    member_number = fields.Char(string='Numéro de membre', required=True, copy=False)
    date_start = fields.Date(string='Début adhésion', default=fields.Date.today)
    date_end = fields.Date(string='Fin adhésion')
    state = fields.Selection([
        ('active', 'Actif'),
        ('suspended', 'Suspendu'),
        ('expired', 'Expiré'),
    ], string='État', default='active')
