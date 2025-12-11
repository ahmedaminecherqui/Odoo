# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryBorrow(models.Model):
    _name = 'library.book.borrow'
    _description = 'Emprunt de livre'
    _rec_name = 'book_id'

    book_id = fields.Many2one('library.book', string='Livre', required=True, domain=[('state', '=', 'available')])
    member_id = fields.Many2one('library.member', string='Membre', required=True)
    borrow_date = fields.Date(string='Date emprunt', default=fields.Date.today, required=True)
    return_date = fields.Date(string='Date retour prévue')
    date_returned = fields.Date(string='Date retour réelle')
    state = fields.Selection([
        ('ongoing', 'En cours'),
        ('returned', 'Retourné'),
        ('late', 'En retard'),
    ], string='État', default='ongoing', compute='_compute_state', store=True)

    @api.depends('return_date', 'date_returned')
    def _compute_state(self):
        today = fields.Date.today()
        for record in self:
            if record.date_returned:
                record.state = 'returned'
            elif record.return_date and record.return_date < today:
                record.state = 'late'
            else:
                record.state = 'ongoing'
