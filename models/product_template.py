from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    rel_product_brand_ids = fields.One2many("rel.product.brand", "product_template_id")
    # brand_count = fields.Integer(string="Brands", store=True, compute="compute_brand_count")
    attribute_line_brand_ids = fields.One2many('product.template.attribute.line', 'product_tmpl_id',
                                               'Product Attributes',
                                               copy=True,
                                               domain=[('is_brand', '=', True)])
    attribute_line_variant_ids = fields.One2many('product.template.attribute.line', 'product_tmpl_id',
                                                 'Product Attributes',
                                                 copy=True,
                                                 domain=[('is_brand', '=', False)])
    brand_in_description_sale = fields.Boolean(default=True, string="Use Vendor Brand in Description Sale")


    description_sale = fields.Text(compute="_compute_description_sale",
                                   inverse="_inverse_description_sale",
                                   store=True)


    description_sale_header = fields.Text(
        'Sales Description', translate=True,
        help="A description of the Product that you want to communicate to your customers. "
             "This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note")

    # def _compute_brand_count(self):
    #     return

    def _inverse_description_sale(self):
        for product in self:
            if not product.brand_in_description_sale:
                product.description_sale_header = product.description_sale
            else:
                product.description_sale_header = product.description_sale_header

    @api.depends('description_sale_header', 'attribute_line_brand_ids', 'brand_in_description_sale', 'description_sale')
    def _compute_description_sale(self):
        for product in self:
            if product.brand_in_description_sale and len(product.attribute_line_brand_ids) > 0:
                product.description_sale = ""
                if product.description_sale_header:
                    product.description_sale += product.description_sale_header
                for brand in product.attribute_line_brand_ids:
                    brand_desc = brand.attribute_id.name
                    if brand.code:
                        brand_desc += " " + brand.code
                    if brand.description:
                        brand_desc += " " + brand.description
                    if brand_desc:
                        product.description_sale += " | " + brand_desc
