# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command
from datetime import timedelta


class EventTrack(models.Model):
    _inherit = "event.track"

    calendar_event = fields.Many2one('calendar.event', 'Calendar event')


    def get_calendar_event_values(self):
        self.ensure_one()

        # compute list of attendees
        partner_ids = []        

        # add event track contact
        if self.partner_id:
            partner_ids.append(self.partner_id.id)
                
        # add event registration attendees
        partner_ids.extend([registration.partner_id.id for registration in self.event_id.registration_ids if registration.partner_id])
        

        return {
            'start':self.date, 
            'duration':self.duration,
            'stop':self.date + timedelta(minutes=round((self.duration or 1.0) * 60)),
            'user_id':self.user_id.id, 
            'partner_ids':[Command.set(partner_ids)], 
            'name':self.event_id.name+' - '+self.name,            
        }


    def sync_calendar_event(self):
        for track in self:
            if not track.calendar_event:
                track.calendar_event = self.env['calendar.event'].create(track.get_calendar_event_values())
            else:
                track.calendar_event.write(track.get_calendar_event_values())

    @api.model_create_multi
    def create(self, vals_list):
        res = super(EventTrack, self).create(vals_list)
        for track in res:
            track.sync_calendar_event()
        return res
    
    def write(self, vals):
        res = super().write(vals)
        self.sync_calendar_event()
        return res
