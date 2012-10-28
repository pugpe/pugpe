# -*- coding:utf-8 -*-
import string
import random
import boto

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from core.models import TimeStampedModel


class Signature(TimeStampedModel):
    '''
    Armazenar assinatura a ser usada em certificado
    Armazenar de forma segura, para não expor em repositório
    ou aberto via http
    '''
    name = models.CharField(_(u'Nome'), max_length=80)
    title = models.CharField(
        u'Título', max_length=80,
        help_text=_(u'Ex: Presidente da República'),
    )
    signature = models.ImageField(_(u'Assinatura'), upload_to='uploads/sign')

    class Meta:
        verbose_name = _(u'Assinatura')
        verbose_name_plural = _(u'Assinaturas')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # http://www.gyford.com/phil/writing/2012/09/26/django-s3-temporary.php
        super(Signature, self).save(*args, **kwargs)
        if self.signature and 'S3' in settings.DEFAULT_FILE_STORAGE:
            conn = boto.s3.connection.S3Connection(
                settings.AWS_ACCESS_KEY_ID,
                settings.AWS_SECRET_ACCESS_KEY,
            )

            # If the bucket already exists, this finds that, rather than
            # creating.
            bucket = conn.create_bucket(settings.AWS_STORAGE_BUCKET_NAME)
            k = bucket.get_key('media/' + self.signature.name)
            k.set_acl('private')


class Attendee(TimeStampedModel):
    event = models.ForeignKey('events.Event', verbose_name=_(u'Evento'))

    name = models.CharField(_(u'Nome'), max_length=80)
    email = models.EmailField(_(u'E-Mail'), max_length=254)

    # Campos referentes a certificado
    slug = models.SlugField(unique=True) # Usado para url de verificação
    sent_date = models.DateTimeField(null=True, blank=True)

    class  Meta:
        verbose_name = _(u'Participante')
        verbose_name = _(u'Participantes')
        unique_together = ('email', 'event')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(
                random.choice(string.ascii_uppercase + string.digits)
                for x in range(7),
            )
        super(Attendee, self).save(*args, **kwargs)
