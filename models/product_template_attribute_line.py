from odoo import fields, models


class ProductTemplateAttributeLine(models.Model):
    _inherit = "product.template.attribute.line"
    is_Brand = fields.Boolean(string="Is Brand?", related='attribute_id.is_Brand')
    description = fields.Text(string="Description")
    code = fields.Char(string="Code")
    type = fields.Selection([('original', 'Original'),
                             ('custom', 'Custom')],
                            default='original')
