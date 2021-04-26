# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-academy(http.Controller):
#     @http.route('/odoo-academy/odoo-academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-academy/odoo-academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-academy.listing', {
#             'root': '/odoo-academy/odoo-academy',
#             'objects': http.request.env['odoo-academy.odoo-academy'].search([]),
#         })

#     @http.route('/odoo-academy/odoo-academy/objects/<model("odoo-academy.odoo-academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-academy.object', {
#             'object': obj
#         })
