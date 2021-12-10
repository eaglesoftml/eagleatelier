#-*- coding: utf-8 -*-
from odoo import models, fields, api

class client(models.Model):
    _inherit = "res.partner"
    _name = "res.partner"
    _description = "client"

    dos = fields.Float(string="Dos")
    epaule = fields.Float("Epaule")
    epaulemache = fields.Float("Epaule Mache")
    poitrine = fields.Float("poitrine")
    taille  = fields.Float("T.Taille")
    longs = fields.Float("Long.S")
    longt = fields.Float("Long.T")
    bassin = fields.Float("Bassin")
    manche = fields.Float("Manche")
    longhaut = fields.Float("Long.Haut")
    ceinture = fields.Float("Ceinture")
    longpantalon = fields.Float("Long.Pantalon")
    longrobe = fields.Float("Long.Robe")
    cuisse = fields.Float("Cuisse")
    longjup = fields.Float("Long.Jube")
    bas = fields.Float("Bas")
    model = fields.Char("Model")
    sexe = fields.Selection(selection=[('masculin', 'Masculin'), ('feminin', 'Feminin')])

