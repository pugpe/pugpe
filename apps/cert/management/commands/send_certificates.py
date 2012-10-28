# -*- coding: utf-8 -*-
import traceback
from datetime import timedelta

from django.core import mail
from django.core.mail import EmailMultiAlternatives, mail_admins
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils import translation
from django.utils import timezone

from cert.models import Attendee

class Command(BaseCommand):
    help = u'Send certificate e-mails'

    def get_email(self, attendee):
        translation.activate(settings.LANGUAGE_CODE)

        subject = _(u'Certificado de participação | PUG-PE')
        from_email = settings.DEFAULT_FROM_EMAIL

        ctx = {
            'site': Site.objects.get_current().domain,
            'event': attendee.event,
            'attendee': attendee,
        }

        text_content = render_to_string('cert/cert_email.txt', ctx)
        html_content = render_to_string('cert/cert_email.html', ctx)

        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [attendee.email],
        )
        msg.attach_alternative(html_content, "text/html")
        return msg

    def handle(self, *args, **options):
        connection = mail.get_connection()
        num_emails = 0

        attendees = Attendee.objects.filter(sent_date__isnull=True)

        # Evitar envio para eventos muito antigos
        attendees = attendees.filter(
            pub_date__gte=timezone.now() - timedelta(days=10),
        )

        for attendee in attendees:
            msg = self.get_email(attendee)
            try:
                num_emails += connection.send_messages([msg])
            except Exception as exc:
                subject = _(u'PUG-PE: Problema envio certificado')

                body = 'except: '.format(exc)
                body += traceback.format_exc()
                mail_admins(subject, body)
            else:
                attendee.sent_date = timezone.now()
                attendee.save()


        self.stdout.write(
            unicode(_(u'Foram enviados {0} emails\n'.format(num_emails))),
        )
