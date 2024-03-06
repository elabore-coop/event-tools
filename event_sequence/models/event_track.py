from odoo import _, api, Command, fields, models
from lxml import etree, html
from odoo.tools import format_time

class EventTrack(models.Model):
    _inherit = "event.track"

    sequence_id = fields.Many2one('event.sequence', 'Sequence', group_expand='_read_group_stage_ids')
    sequence = fields.Integer('Sequence') #for sorting

    @api.model_create_multi
    def create(self, vals_list):   
        if vals_list and 'sequence' not in vals_list[0]:
            vals_list[0]['sequence'] = 999
        tracks = super(EventTrack, self).create(vals_list)
        return tracks
    


    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        event_id = None
        for d in domain:
            if d[0] == "event_id" and d[1] == "=" and d[2]:
                event_id = d[2]

        if event_id:
            event = self.env['event.event'].browse(event_id)
            return stages.search([], order="sequence", limit=event.sequence_number)

        return stages.search([], order="sequence")
        