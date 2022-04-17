# -*- coding: utf-8 -*-
# from odoo import http


# class CustomCrm(http.Controller):
#     @http.route('/custom_crm/custom_crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_crm/custom_crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_crm.listing', {
#             'root': '/custom_crm/custom_crm',
#             'objects': http.request.env['custom_crm.custom_crm'].search([]),
#         })

#     @http.route('/custom_crm/custom_crm/objects/<model("custom_crm.custom_crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_crm.object', {
#             'object': obj
#         })
