# -*- coding:UTF-8 -*-

from odoo import api, fields, models


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book Info'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True)
    author_ids = fields.Many2many(string='Author',
                                  required=True,
                                  comodel_name='res.partner')
    publisher_id = fields.Many2one(string='Publisher',
                                   comodel_name='res.company')
    publication_date = fields.Date(string='Publication Date')
    genre_ids = fields.Many2many(string='Genres', comodel_name='library.genre')
    tag_ids = fields.Many2many(string='Tags', comodel_name='library.tag')
    isbn = fields.Char(string='ISBN-13')
    cover = fields.Image(string='Cover')
    description = fields.Text(string='Description')

    copy_ids = fields.One2many(string='Copies',
                               comodel_name='library.copy',
                               inverse_name='book_id')
