# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-volunteer(http.Controller):
#     @http.route('/odoo-volunteer/odoo-volunteer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-volunteer/odoo-volunteer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-volunteer.listing', {
#             'root': '/odoo-volunteer/odoo-volunteer',
#             'objects': http.request.env['odoo-volunteer.odoo-volunteer'].search([]),
#         })

#     @http.route('/odoo-volunteer/odoo-volunteer/objects/<model("odoo-volunteer.odoo-volunteer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-volunteer.object', {
#             'object': obj
#         })
