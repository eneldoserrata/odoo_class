# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teacher(models.Model):
    _name = 'odoojs.teacher'

    name = fields.Char("Profesores")
    sexo = fields.Selection([("F","Femenino"), ("M", "Masculino")], string="Sexo")