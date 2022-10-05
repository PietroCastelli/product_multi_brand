from odoo import fields, models


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'
    is_Brand = fields.Boolean(string="is Brand?", related="attribute_id.is_Brand", store=True)
    image_brand = fields.Image("Brand image")
