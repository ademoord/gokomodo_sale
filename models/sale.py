from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    business_model = fields.Selection([
        ('retail', 'Retail'),
        ('corporate', 'Corporate'),
        ('subscription', 'Subscription')
    ], string='Business Model', required=True)

    def _compute_name(self):
        for order in self:
            short_name = {
                'retail': 'RT',
                'corporate': 'CORP',
                'subscription': 'SUB'
            }.get(order.business_model, '')
            order.name = f'[{short_name}]-{order.name}'

    def _compute_display_name(self):
        for order in self:
            short_name = {
                'retail': 'RT',
                'corporate': 'CORP',
                'subscription': 'SUB'
            }.get(order.business_model, '')
            order.display_name = f'[{short_name}]-{order.name}'

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    business_model = fields.Selection(related='order_id.business_model', store=True)

    @api.model
    def create(self, vals):
        sale_order_line = super(SaleOrderLine, self).create(vals)
        
        if sale_order_line.order_id.business_model == 'retail':
            retail_tax = self.env['account.tax'].search([('name', '=', 'Retail Tax')], limit=1)
            if retail_tax:
                sale_order_line.tax_id = [(4, retail_tax.id)]
        elif sale_order_line.order_id.business_model == 'corporate':
            corporate_tax = self.env['account.tax'].search([('name', '=', 'Corp Tax')], limit=1)
            if corporate_tax:
                sale_order_line.tax_id = [(4, corporate_tax.id)]
        elif sale_order_line.order_id.business_model == 'subscription':
            subscription_tax = self.env['account.tax'].search([('name', '=', 'Sub Tax')], limit=1)
            if subscription_tax:
                sale_order_line.tax_id = [(4, subscription_tax.id)]
        
        _logger.info("=============SALE ORDER LINE VALS=============")
        _logger.info(sale_order_line)
        
        return sale_order_line
