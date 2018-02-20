# -*- coding: utf-8 -*-
from odoo import http


class Odoojs(http.Controller):

    @http.route('/odoojs/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['odoojs.teacher']

        return http.request.render('odoojs.index', {
            'teachers': Teachers.search([])
        })

    # @http.route('/odoojs/<name>/', auth='public')
    # def index(self, name):
    #     return '<h1>{}</h1>'.format(name)
    #
    #
    # @http.route('/odoojs/<int:id>/', auth='public')
    # def index(self, id):
    #     Teachers = http.request.env['odoojs.teacher']
    #     return '<h1>{}</h1>'.format(Teachers.search([('id','=',id)]).name)