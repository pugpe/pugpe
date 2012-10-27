# -*- coding:utf-8 -*-
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
            k = boto.s3.key.Key(bucket)
            k.key = settings.MEDIA_ROOT + self.signature
            k.set_acl('private')


class Attendee(TimeStampedModel):
    events = models.ManyToManyField('events.Event', verbose_name=_(u'Evento'))

    name = models.CharField(_(u'Nome'), max_length=80)
    email = models.EmailField(_(u'E-Mail'), max_length=254)

    class  Meta:
        verbose_name = _(u'Participante')
        verbose_name = _(u'Participantes')

    def __unicode__(self):
        return self.name
