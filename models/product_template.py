from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    rel_product_brand_ids = fields.One2many("rel.product.brand", "product_template_id")


