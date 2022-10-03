from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    rel_product_brand_ids = fields.One2many("rel.product.brand", "product_template_id")
    brand_count = fields.Integer(string="Brands", store=True, compute="compute_brand_count")
    attribute_line_brand_ids = fields.One2many('product.template.attribute.line', 'product_tmpl_id',
                                               'Product Attributes',
                                               copy=True,
                                               domain=[('is_Brand', '=', True)])

    # attribute_line_Brand_ids = fields.One2many('product.template.attribute.line', 'attribute_Brand_id', 'Product Brand Attributes')
    # product_attribute_value_ids = fields.One2many("product.attribute.value", "product_template_id",domain="[('is_Brand','=',True)]")

    # da finire
    def compute_brand_count(self):
        return 3
