# -*- encoding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_session_product = fields.Boolean(
        string='Use as Session Product',
        help='Check this to use as a Product for Session Fee',
        default=False)
