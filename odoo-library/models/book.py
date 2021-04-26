# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book Info'

    authors = fields.Char(string='Authors')
    editors = fields.Char(string='Editors')
    publisher = fields.Char(string='Publisher')
    publicationYear = fields.Integer(string='Publication Year')
    isbn = fields.Char(string='ISBN')
    genre = fields.Selection(string='Genre', selection=[(
        'horror', 'Horror'), ('scifi', 'Science Fiction'), ('fantasy', 'Fantasy'), ('romance', 'Romance')])
