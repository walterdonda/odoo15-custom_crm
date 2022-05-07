from odoo import fields, models, api
import datetime


class Visit(models.Model):

    _name = 'custom_crm.visit'
    _rec_name = 'name'
    _description = 'Comercial visit'

    name = fields.Char(string='Descripción')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha de visita', default=str(datetime.datetime.now()))
    type = fields.Selection(
        [('P', 'Presencial'), ('R', 'Remota')],
        string='Tipo de visita', required=True)
    state = fields.Selection(
        [('P', 'Pendiente'), ('C', 'En curso'), ('T', 'Terminada')],
        string='Estado de visita', required=True, default='P')
    code = fields.Char(string='Código de visita',
                       help='Código único de soporte o implementación',
                       index=True,
                       required=True)
    done = fields.Boolean(string='Realizada?')
    image = fields.Binary(string='Imagen')

    def toggle_state_visit(self):
        self.done = not self.done

class ReporteVisit(models.AbstractModel):
    _name = 'report.custom_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('custom_crm.report_visit_card')
        return {
            'docids': docids,
            'doc_model': self.env['custom_crm.visit'],
            'docs': self.env['custom_crm.visit'].browse(docids)
        }


