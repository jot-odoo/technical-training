# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book Info'

    name = fields.Char(string="Title", required=True)
    authors = fields.Char(string='Authors') # These really should be many2many fields but we haven't gotten that far yet.
    editors = fields.Char(string='Editors') # many2many
    publisher = fields.Char(string='Publisher') # many2one
    publicationYear = fields.Integer(string='Publication Year')
    isbn = fields.Char(string='ISBN')
    genre = fields.Selection(string='Genre', selection=[
        ('horror', 'Horror'), ('scifi', 'Science Fiction'), ('fantasy', 'Fantasy'), ('romance', 'Romance')]) # many2many
