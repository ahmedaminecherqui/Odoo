# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Catégorie de livre'
    _parent_store = True

    name = fields.Char(string='Nom', required=True, translate=True)
    parent_id = fields.Many2one('library.category', string='Parent', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many('library.category', 'parent_id', string='Enfants')
