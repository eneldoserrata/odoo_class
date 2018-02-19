# -*- coding: utf-8 -*-
from odoo import http

# class Pycaribbean(http.Controller):
#     @http.route('/pycaribbean/pycaribbean/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pycaribbean/pycaribbean/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pycaribbean.listing', {
#             'root': '/pycaribbean/pycaribbean',
#             'objects': http.request.env['pycaribbean.pycaribbean'].search([]),
#         })

#     @http.route('/pycaribbean/pycaribbean/objects/<model("pycaribbean.pycaribbean"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pycaribbean.object', {
#             'object': obj
#         })