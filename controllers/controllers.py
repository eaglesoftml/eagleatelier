# -*- coding: utf-8 -*-
# from odoo import http


# class Atelier(http.Controller):
#     @http.route('/atelier/atelier/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/atelier/atelier/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('atelier.listing', {
#             'root': '/atelier/atelier',
#             'objects': http.request.env['atelier.atelier'].search([]),
#         })

#     @http.route('/atelier/atelier/objects/<model("atelier.atelier"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('atelier.object', {
#             'object': obj
#         })
