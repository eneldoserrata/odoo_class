# -*- coding: utf-8 -*-
from odoo import http


class Odoojs(http.Controller):

    @http.route('/odoojs/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['odoojs.teacher']

        return http.request.render('odoojs.index', {
            'teachers': Teachers.search([])
        })