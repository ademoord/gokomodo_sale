# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /mnt/extra-addons/gokomodo_sale(models.Model):
#     _name = '/mnt/extra-addons/gokomodo_sale./mnt/extra-addons/gokomodo_sale'
#     _description = '/mnt/extra-addons/gokomodo_sale./mnt/extra-addons/gokomodo_sale'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
