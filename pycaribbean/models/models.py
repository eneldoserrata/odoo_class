# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pycaribbean(models.Model):
    _name = 'pycaribbean'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char("Name")
    speaker_id = fields.Many2one("speaker")
    age = fields.Integer("Age")
    tags = fields.Many2many("tags")
    assistant_ids = fields.One2many("assistant", "pycaribbean_id")


class Tags(models.Model):
    _name = 'tags'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()


class Speaker(models.Model):
    _name = 'speaker'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char("Name")

class Assistant(models.Model):
    _name = 'assistant'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()
    pycaribbean_id = fields.Many2one("pycaribbean")