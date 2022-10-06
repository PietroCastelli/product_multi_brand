from odoo import fields, models


class ProductTemplateAttributeLine(models.Model):
    _inherit = "product.template.attribute.line"
    is_brand = fields.Boolean(string="Is Brand?", related='attribute_id.is_brand')
    description = fields.Text(string="Description")
    code = fields.Char(string="Code")
    type = fields.Selection([('original', 'Original'),
                             ('compatible', 'Compatible')],
                            default='original')

    def migration(self):
        products = self.env['product.template'].search([('vendor_brand_ids','!=',False)])
        attribute_brand = self.env['product.attribute'].search([('is_brand','=',True)],limit = 1)
        for p in products:
            p.attribute_line_brand_ids = self.env['product.template.attribute.line']
            for vendor_brand in p.vendor_brand_ids:
                name = vendor_brand.brand_id.name.upper()
                attribute_value = attribute_brand.value_ids.filtered(lambda l:l.name == name)
                if not attribute_value:
                    print('not found ' + name)
                    attribute_value = self.env['product.attribute.value'].create([{
                        'name':name,
                        'attribute_id':attribute_brand.id
                    }])

                attribute_line = self.env['product.template.attribute.line'].create([{
                        'product_tmpl_id': p.id,
                        'attribute_id': attribute_brand.id,
                        'value_ids': [(6, 0, [attribute_value.id])],
                        'description':vendor_brand.description,
                        'code': vendor_brand.brand_code,
                        'type': vendor_brand.brand_type
                    }])
                p.attribute_line_brand_ids |= attribute_line


