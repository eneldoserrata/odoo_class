from odoo import models, fields


class Student(models.Model):
    _name = "odoojs.student"

    name = fields.Char("Nombre")
    matricula = fields.Char("Matricula")
    bird_date = fields.Datetime("Fecha de nacimiento")


