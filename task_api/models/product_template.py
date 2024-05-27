from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    api_field = fields.Char(string="Api Field")
