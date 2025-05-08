from odoo import models, fields
import base64

class Client(models.Model):
    _inherit = 'res.partner'

    equipement_ids = fields.One2many('gestion.equipement', 'client_id', string='Équipements')
    serial_number = fields.Char(string='Numéro de série')