# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command, _
from datetime import timedelta


class EventTrack(models.Model):
    _inherit = "event.track"

    calendar_event = fields.Many2one('calendar.event', 'Calendar event')

    location_already_in_use = fields.Boolean('Location already in use', compute='_compute_location_already_in_use')
    location_already_in_use_message = fields.Text(compute='_compute_location_already_in_use')

    @api.depends('date', 'duration', 'location_id')
    def _compute_location_already_in_use(self):
        for track in self:
            location_already_in_use = False
            location_already_in_use_message = ""

            if track.location_id and track.date:

                #search if other track exists for same day on same location            
                search_other_tracks = [('location_id','=',track.location_id.id),('date','>',track.date.replace(hour=0,minute=0)),('date','<',track.date.replace(hour=23,minute=59))]
                if track.id or track.id.origin:
                    search_other_tracks.append(('id','!=',track.id or track.id.origin))
                other_tracks = self.search(search_other_tracks)

                if other_tracks:
                    location_already_in_use = True                    
                    for other_track in other_tracks:
                        location_already_in_use_message += other_track.event_id.name+" - "+other_track.name+"\n"

            track.location_already_in_use = location_already_in_use
            track.location_already_in_use_message = location_already_in_use_message
                        
                     

    def get_calendar_event_values(self):
        self.ensure_one()
        res = super(EventTrack, self).get_calendar_event_values()        
        res['location'] = self.location_id.name

        return res

    def get_calendar_event_partner_value(self):
        """Add event track location partner to list of partner ids
        """

        res = super(EventTrack, self).get_calendar_event_partner_value()
        if self.location_id and self.location_id.partner_id:
            res.append(self.location_id.partner_id.id)
        return res

 