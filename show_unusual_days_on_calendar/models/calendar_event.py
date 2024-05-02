# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime, time

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    @api.model
    def get_unusual_days(self, date_from, date_to=None):
        return self.env['hr.leave'].get_unusual_days(date_from, date_to=date_to)