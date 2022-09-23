from odoo import fields, models, api


class RelProductBrand(models.Model):
    _name = 'rel.product.brand'
    _description = 'rel.product.brand'
    product_brand_id = fields.Many2one("product.brand")
    product_template_id = fields.Many2one("product.template")
    brand_note = fields.Text(string="Text")
    brand_type = fields.Selection([('luxury','Luxury'),('common','Common'),('damage','Damage')])
    isGood = fields.Boolean(string="is Good?", default=False)

