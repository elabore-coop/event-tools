from odoo import _, api, Command, fields, models
from lxml import etree, html

class MailTemplate(models.Model):
    _inherit = "mail.template"

    event_attachment_name_prefix = fields.Char('Attachment name prefix', help="If there is an attachment in event registration, or in event, with a name that starts with this name, it will be attached to the mail.")
    

    def generate_email(self, res_ids, fields):
        res = super(MailTemplate, self).generate_email(res_ids, fields)
        
        self.ensure_one()
        multi_mode = True
        if isinstance(res_ids, int):
            res_ids = [res_ids]
            multi_mode = False
        
        for lang, (template, template_res_ids) in self._classify_per_lang(res_ids).items():
            #add reports attached to event.registration or event.event from attachment name
            if template.event_attachment_name_prefix:
                for res_id in template_res_ids:
                    event_registration = self.env['event.registration'].browse(res_id)    
                    attachments = self.env['ir.attachment']
                    for event_attachment_name_prefix in template.event_attachment_name_prefix.split(","):
                        attachments |= self.env['ir.attachment'].search([
                            ('res_model','=','event.registration'),
                            ('res_id','=',res_id), 
                            ('name','like',event_attachment_name_prefix)])
                        attachments |= self.env['ir.attachment'].search([
                            ('res_model','=','event.event'),
                            ('res_id','=',event_registration.event_id.id), 
                            ('name','like',event_attachment_name_prefix)])
                    
                    attachments_res = [(attachment.name, attachment.datas) for attachment in attachments]
                    
                    if multi_mode:
                        if res_id in res:
                            if not 'attachments' in res[res_id]:
                                res[res_id]['attachments'] = attachments_res
                            else:                            
                                res[res_id]['attachments'].extend(attachments_res)
                    else:
                        if not 'attachments' in res:
                            res['attachments'] = attachments_res
                        else:                            
                            res['attachments'].extend(attachments_res)

                        
        return res
