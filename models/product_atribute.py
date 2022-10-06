from odoo import fields, models


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'
    is_brand = fields.Boolean(string="is Brand?", default=False)

