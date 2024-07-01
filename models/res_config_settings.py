from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    retail_tax_ids = fields.Many2many(
        'account.tax', 'config_retail_tax_rel', 'config_id', 'tax_id', string='Retail Taxes')
    corporate_tax_ids = fields.Many2many(
        'account.tax', 'config_corporate_tax_rel', 'config_id', 'tax_id', string='Corporate Taxes')
    subscription_tax_ids = fields.Many2many(
        'account.tax', 'config_subscription_tax_rel', 'config_id', 'tax_id', string='Subscription Taxes')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('sale.retail_tax_ids', self.retail_tax_ids.ids)
        self.env['ir.config_parameter'].sudo().set_param('sale.corporate_tax_ids', self.corporate_tax_ids.ids)
        self.env['ir.config_parameter'].sudo().set_param('sale.subscription_tax_ids', self.subscription_tax_ids.ids)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            retail_tax_ids=[(6, 0, self.env['ir.config_parameter'].sudo().get_param('sale.retail_tax_ids', default=[]))],
            corporate_tax_ids=[(6, 0, self.env['ir.config_parameter'].sudo().get_param('sale.corporate_tax_ids', default=[]))],
            subscription_tax_ids=[(6, 0, self.env['ir.config_parameter'].sudo().get_param('sale.subscription_tax_ids', default=[]))],
        )
        return res