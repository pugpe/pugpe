# -*- coding: utf-8 -*-
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.core import signing
from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils import translation, timezone


from emails.models import Email
from events.models import Event


class Command(BaseCommand):
    args = u'event_slug'
    help = u'Send email for voting on submissions'

    def get_email(self, email, event):
        translation.activate(settings.LANGUAGE_CODE)


        subject = _(u'Votação das palestras submetidas para a PyconPE')
        from_email = settings.DEFAULT_FROM_EMAIL

        ctx = {
            'site': Site.objects.get_current().domain,
            'token': signing.dumps(email.pk),
            'event': event,
        }

        text_content = render_to_string('submission/vote_email.txt', ctx)
        html_content = render_to_string('submission/vote_email.html', ctx)

        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [email.email],
        )
        msg.attach_alternative(html_content, "text/html")
        return msg

    def get_emails(self, event):
        emails = Email.active.all()
        return [self.get_email(email, event) for email in emails]

    def handle(self, *args, **options):
        if not args:
            raise CommandError(unicode(_(u'event_slug required')))

        event = Event.objects.get(slug=args[0])
        if event.date <= timezone.now():
            raise CommandError(unicode(_(u'Evento ja realizado')))

        connection = mail.get_connection(fail_silently=True)
        messages = self.get_emails(event)
        num_emails = connection.send_messages(messages)
        self.stdout.write(
            unicode(_(u'Foram enviados {0}, de {1} emails\n'
                .format(num_emails, len(messages)))),
        )
