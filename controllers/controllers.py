# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/gokomodoSale(http.Controller):
#     @http.route('//mnt/extra-addons/gokomodo_sale//mnt/extra-addons/gokomodo_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/gokomodo_sale//mnt/extra-addons/gokomodo_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/gokomodo_sale.listing', {
#             'root': '//mnt/extra-addons/gokomodo_sale//mnt/extra-addons/gokomodo_sale',
#             'objects': http.request.env['/mnt/extra-addons/gokomodo_sale./mnt/extra-addons/gokomodo_sale'].search([]),
#         })

#     @http.route('//mnt/extra-addons/gokomodo_sale//mnt/extra-addons/gokomodo_sale/objects/<model("/mnt/extra-addons/gokomodo_sale./mnt/extra-addons/gokomodo_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/gokomodo_sale.object', {
#             'object': obj
#         })
