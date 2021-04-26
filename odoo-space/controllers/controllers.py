# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-space(http.Controller):
#     @http.route('/odoo-space/odoo-space/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-space/odoo-space/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-space.listing', {
#             'root': '/odoo-space/odoo-space',
#             'objects': http.request.env['odoo-space.odoo-space'].search([]),
#         })

#     @http.route('/odoo-space/odoo-space/objects/<model("odoo-space.odoo-space"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-space.object', {
#             'object': obj
#         })
