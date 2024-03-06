from odoo import _, api, Command, fields, models
from lxml import etree, html
import logging
from odoo.exceptions import MissingError, ValidationError

_logger = logging.getLogger(__name__)

class EventMail(models.Model):
    _inherit = "event.mail"

    notification_type = fields.Selection(selection_add=[('mail_manual', 'Mail (manual)')], ondelete={'mail_manual': 'set default'})


    def _selection_template_model_get_mapping(self):
        return {**super(EventMail, self)._selection_template_model_get_mapping(), 'mail_manual': 'mail.template'}


    @api.depends('event_id.date_begin', 'event_id.date_end', 'interval_type', 'interval_unit', 'interval_nbr','notification_type')
    def _compute_scheduled_date(self):
        res = super(EventMail, self)._compute_scheduled_date()
        for scheduler in self:
            if scheduler.notification_type == 'mail_manual':
                scheduler.scheduled_date = '2148-12-31'
                scheduler.interval_type = 'after_sub'

        return res

    def send(self):        
        self.execute()
        return
    

class EventMailRegistration(models.Model):
    _inherit = 'event.mail.registration'
    

    def execute(self):
        """Inherit execute to send mail from schedulers "mail_manual"
        """
        res = super(EventMailRegistration, self).execute()
        
        todo_manual = self.filtered(lambda reg_mail:
            not reg_mail.mail_sent and 
            reg_mail.registration_id.state in ['open', 'done'] and        
            reg_mail.scheduler_id.notification_type == 'mail_manual'
        )
        done = self.browse()
        for reg_mail in todo_manual:
            organizer = reg_mail.scheduler_id.event_id.organizer_id
            company = self.env.company
            author = self.env.ref('base.user_root').partner_id
            if organizer.email:
                author = organizer
            elif company.email:
                author = company.partner_id
            elif self.env.user.email:
                author = self.env.user.partner_id

            email_values = {
                'author_id': author.id,
            }
            template = None
            try:
                template = reg_mail.scheduler_id.template_ref.exists()
            except MissingError:
                pass

            if not template:
                _logger.warning("Cannot process ticket %s, because Mail Scheduler %s has reference to non-existent template", reg_mail.registration_id, reg_mail.scheduler_id)
                continue

            if not template.email_from:
                email_values['email_from'] = author.email_formatted
            template.send_mail(reg_mail.registration_id.id, email_values=email_values)
            done |= reg_mail
        done.write({'mail_sent': True})

        return res


