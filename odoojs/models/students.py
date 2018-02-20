from odoo import models, fields


class Student(models.Model):
    _name = "odoojs.student"
    _order = "sequence"
    name = fields.Char("Nombre")
    matricula = fields.Integer("Matricula")
    bird_date = fields.Datetime("Fecha de nacimiento")
    sequence = fields.Integer('Orden', help="Sequence for the handle.",default=10)
    course_id = fields.Many2one("odoojs.course")    
    
