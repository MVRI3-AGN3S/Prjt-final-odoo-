from odoo import models, fields

class Facture(models.Model):
    _name = 'gestion.facture'
    _description = 'Facture générée automatiquement'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_facture desc'
    _rec_name = 'contrat_id'

    contrat_id = fields.Many2one('gestion.contrat', string="Contrat lié")
    client_id = fields.Many2one(related='contrat_id.client_id', string="Client", store=True)
    date_facture = fields.Date(string="Date de facturation", default=fields.Date.today)
    montant = fields.Float(string="Montant")
    statut = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('envoyee', 'Envoyée'),
        ('payee', 'Payée')
    ], default='brouillon')
