# -*- coding: utf-8 -*-
from odoo import http

# class Odoojs(http.Controller):
#     @http.route('/odoojs/odoojs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoojs/odoojs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoojs.listing', {
#             'root': '/odoojs/odoojs',
#             'objects': http.request.env['odoojs.odoojs'].search([]),
#         })

#     @http.route('/odoojs/odoojs/objects/<model("odoojs.odoojs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoojs.object', {
#             'object': obj
#         })