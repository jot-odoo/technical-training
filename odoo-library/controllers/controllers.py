# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-library(http.Controller):
#     @http.route('/odoo-library/odoo-library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-library/odoo-library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-library.listing', {
#             'root': '/odoo-library/odoo-library',
#             'objects': http.request.env['odoo-library.odoo-library'].search([]),
#         })

#     @http.route('/odoo-library/odoo-library/objects/<model("odoo-library.odoo-library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-library.object', {
#             'object': obj
#         })
