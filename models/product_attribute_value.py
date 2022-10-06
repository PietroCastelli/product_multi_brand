from odoo import fields, models


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'
    is_brand = fields.Boolean(string="is Brand?", related="attribute_id.is_brand", store=True)
    image_brand = fields.Image("Brand image")
