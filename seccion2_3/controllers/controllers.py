# -*- coding: utf-8 -*-
# from odoo import http


# class Seccion23(http.Controller):
#     @http.route('/seccion2_3/seccion2_3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seccion2_3/seccion2_3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('seccion2_3.listing', {
#             'root': '/seccion2_3/seccion2_3',
#             'objects': http.request.env['seccion2_3.seccion2_3'].search([]),
#         })

#     @http.route('/seccion2_3/seccion2_3/objects/<model("seccion2_3.seccion2_3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seccion2_3.object', {
#             'object': obj
#         })
