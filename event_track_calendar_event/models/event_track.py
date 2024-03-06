# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command
from datetime import timedelta
import logging

_logger = logging.getLogger(__name__)


class EventTrack(models.Model):
    _inherit = "event.track"

    calendar_event_ids = fields.One2many('calendar.event', 'event_track_id', 'Days')
    date = fields.Datetime(compute="_compute_date")

    def _compute_date(self):
        """Date become a field computed from first calendar event date
        """
        for event_track in self:
            if event_track.calendar_event_ids:
                event_track.date = event_track.calendar_event_ids.sorted(key=lambda r: r.start)[0].start
            else:
                event_track.date = None

    def get_calendar_event_values(self):
        """return default values of calendar events
        """
        return {
            'partner_ids':[Command.set(self.get_calendar_event_partner_value())], 
            'location':self.location_id.name if self.location_id else '',
            'user_id':self.user_id.id
        }

    def get_calendar_event_partner_value(self):
        """Compute list of partner ids for calendar event
        """
        # compute list of attendees
        partner_ids = []        

        # add event track contact
        if self.partner_id:
            partner_ids.append(self.partner_id.id)
                
        # add event registration attendees
        partner_ids.extend([registration.partner_id.id for registration in self.event_id.registration_ids if registration.partner_id])

        return partner_ids
    
    
    def sync_calendar_event(self):
        """synchronize calendar event values with event track data
        """
        _logger.warning("sync_calendar_event...")
        for track in self:
            track.calendar_event_ids.write(track.get_calendar_event_values())
        _logger.warning("sync_calendar_event done !")


    @api.model_create_multi
    def create(self, vals_list):
        """
            after creation of event track synchronise calendar event values
        """        
        res = super(EventTrack, self).create(vals_list)
        res.sync_calendar_event()
        return res
    
    def write(self, vals):
        """
            after modification of event track synchronise calendar event values
        """  
        res = super().write(vals)
        self.sync_calendar_event()
        return res
