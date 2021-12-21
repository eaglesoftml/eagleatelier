#-- coding: utf-8 --
from odoo import models, fields, api

class client(models.Model):
    _inherit = "res.partner"
    _name = "res.partner"
    _description = "client"
    #Commun
    dos = fields.Float(string="Dos")
    epaule = fields.Float("Epaule")
    epaulemache = fields.Float("Epaule Mache")
    poitrine = fields.Float("poitrine")
    ceinture = fields.Float("Ceinture")
    longs = fields.Float("Long.S")
    longt = fields.Float("Long.T")
    longpantalon = fields.Float("Long.Pantalon")
    cuisse = fields.Float("Cuisse")
    bas = fields.Float("Bas")
    model = fields.Char("Model")
    #Homme
    coup = fields.Float("coup")
    patte = fields.Float("patte")
    #Femme
    taille = fields.Float("taille")
    bassin = fields.Float("Bassin")
    manche = fields.Float("Manche")
    longhaut = fields.Float("Long.Haut")
    longrobe = fields.Float("Long.Robe")
    longjup = fields.Float("Long.Jube")

    sexe = fields.Selection(selection=[('masculin', 'Masculin'), ('feminin', 'Feminin')], required=True)