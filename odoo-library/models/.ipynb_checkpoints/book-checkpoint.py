# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book Info'

    name = fields.Char(string="Title", required=True)
    authors = fields.Char(string='Authors') # These really should be many2many fields but we haven't gotten that far yet.
    editors = fields.Char(string='Editors') # many2many
    publisher = fields.Char(string='Publisher') # many2one
    publicationYear = fields.Integer(string='Publication Year')
    isbn = fields.Char(string='ISBN', default='0000000000000')
    genre = fields.Selection(string='Genre', selection=[
        ('horror', 'Horror'), ('scifi', 'Science Fiction'), ('fantasy', 'Fantasy'), ('romance', 'Romance')]) # many2many
    note = fields.Text(string='Notes')
    
#     rental_id = fields.Many2many(comodel_name='library.rental', string='Rental')
    
    @api.onchange('isbn')
    def _onchange_isbn(self):
        if(len(self.isbn) != 13):
            raise ValidationError(f'The ISBN must be 13 characters long! Yours is too {"short" if len(self.isbn) < 13 else "long"}!')
