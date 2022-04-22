from odoo import fields, models


class Visit(models.Model):

    _name = 'custom_crm.visit'
    _rec_name = 'name'
    _description = 'Comercial visit'

    name = fields.Char(string='Descripción')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha de visita')
    type = fields.Selection(
        [('P', 'Presencial'), ('R', 'Remota')],
        string='Tipo de visita', required=True)
    state = fields.Selection(
        [('P', 'Pendiente'), ('C', 'En curso'), ('T', 'Terminada')],
        string='Tipo de visita', required=True)
    code = fields.Char(string='Código de visita',
                       help='Código único de soporte o implementación',
                       index=True,
                       required=True)
    done = fields.Boolean(string='Realizada?')
    image = fields.Binary(string='Imagen')

    def toggle_state_visit(self):
        self.done = not self.done
