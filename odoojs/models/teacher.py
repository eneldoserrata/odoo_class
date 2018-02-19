# -*- coding: utf-8 -*-

from odoo import models, fields, _testcapi

class Teacher(models.Model):
    _name = 'odojs.teacher'

    name = fields.Char("Profesores")
    sexo = fields.Char("Sexo")