from odoo import models, fields, api

class Parc(models.Model):
    _name = 'gestion.parc'
    _description = 'Parc Informatique'

    name = fields.Char(string='Nom du parc', required=True)
    description = fields.Text(string='Description')
    client_id = fields.Many2one('res.partner', string='Client concerné')
    equipement_ids = fields.One2many('gestion.equipement', 'parc_id', string='Équipements')
    
    def action_ajouter_equipement(self):
        available_equipments = self.env['gestion.equipement'].search([
            ('parc_id', '=', False),
            ('client_id', '=', self.client_id.id)
        ])
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Nouvel Équipement',
            'view_mode': 'form',
            'res_model': 'gestion.equipement',
            'target': 'new',
            'context': {
                'default_parc_id': self.id,
                'default_client_id': self.client_id.id,
                'available_parc_ids': [self.id]
            },
            'domain': [('id', 'in', available_equipments.ids)] if available_equipments else []
        }