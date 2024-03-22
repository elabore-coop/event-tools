# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api


class EventTrackLocation(models.Model):
    _inherit = 'event.track.location'

    partner_id = fields.Many2one('res.partner', 'Address', domain="[('is_company','=',True)]")
    
    def write(self, vals):
        """update calendar events related to event tracks if partner change
        """
        res = super(EventTrackLocation, self).write(vals)
        if 'partner_id' in vals:
            event_tracks = self.env['event.track'].search([('location_id','in',self.ids)])
            event_tracks.sync_calendar_event()
        return res