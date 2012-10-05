# -*- coding: utf-8 -*-
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.core import signing
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings

from emails.models import Email


class Command(BaseCommand):
    help = u'Send email for voting on submissions'

    def get_email(self, email):
        subject = _(u'Votação das palestras submetidas para a PyconPE')
        from_email = settings.DEFAULT_FROM_EMAIL

        ctx = {
            'site': Site.objects.get_current().domain,
            'token': signing.dumps(email.pk),
        }

        text_content = render_to_string('submission/vote_email.txt', ctx)
        html_content = render_to_string('submission/vote_email.html', ctx)

        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [email.email],
        )
        msg.attach_alternative(html_content, "text/html")
        return msg

    def get_emails(self):
        emails = Email.active.all()
        return [self.get_email(email) for email in emails]

    def handle(self, *args, **options):
        connection = mail.get_connection()
        messages = self.get_emails()
        num_emails = connection.send_messages(messages)
        self.stdout.write(
            unicode(_(u'Foram enviados {0} emails\n'.format(num_emails))),
        )
