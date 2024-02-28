# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command, _
from datetime import timedelta
from odoo.tools import format_date


class EventTrack(models.Model):
    _inherit = "event.track"
    

    location_already_in_use = fields.Boolean('Location already in use', compute='_compute_location_already_in_use')
    location_already_in_use_message = fields.Text(compute='_compute_location_already_in_use')

    @api.depends('date', 'duration', 'location_id')
    def _compute_location_already_in_use(self):
        for track in self:
            location_already_in_use = False
            location_already_in_use_message = ""

            for calendar_event in track.calendar_event_ids:
                if track.location_id and calendar_event.start:

                    #search if other calendar event exists for same day on same location
                    search_other_calendar_events = [('event_track_id.location_id','=',track.location_id.id),('start','>=',calendar_event.start.replace(hour=0,minute=0)),('start','<=',calendar_event.start.replace(hour=23,minute=59))]
                                        
                    if track.id or track.id.origin:
                        search_other_calendar_events.append(('event_track_id','!=',track.id or track.id.origin))
                    other_calendar_events = self.env["calendar.event"].search(search_other_calendar_events)

                    if other_calendar_events:
                        location_already_in_use = True                    
                        for other_calendar_event in other_calendar_events:
                            location_already_in_use_message += other_calendar_event.event_track_id.event_id.name+" - "+\
                                other_calendar_event.event_track_id.name+\
                                    " ("+format_date(self.env, other_calendar_event.start)+")"+"\n"

            track.location_already_in_use = location_already_in_use
            track.location_already_in_use_message = location_already_in_use_message
                        
                     

    def get_calendar_event_partner_value(self):
        """Add event track location partner to list of partner ids
        """

        res = super(EventTrack, self).get_calendar_event_partner_value()
        if self.location_id and self.location_id.partner_id:
            res.append(self.location_id.partner_id.id)
        return res

 