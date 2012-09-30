# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel
from .managers import ActiveManager


class Event(TimeStampedModel):
    description = models.CharField(_(u'Descrição'), max_length=100)
    full_description = models.TextField(_(u'Descrição Completa'))
    date = models.DateTimeField(_(u'Data'))
    slug = models.SlugField()
    location = models.ForeignKey('geo.Location', verbose_name=_(u'Local'))

    class Meta:
        verbose_name = _(u'Evento')
        verbose_name_plural = _(u'Eventos')

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('event', kwargs={'slug': self.slug})


class EventTalk(TimeStampedModel):
    '''
    Meta dados de palestra no evento, afim de facilitar cadastro das palestras
    no evento
    '''
    status = models.BooleanField(_(u'Ativo'))

    event = models.ForeignKey('events.Event', verbose_name=_(u'Evento'))
    talk = models.ForeignKey('submission.Talk', verbose_name=_(u'Palestra'))

    start = models.TimeField(_(u'Início'))
    end = models.TimeField(_(u'Fim'))

    objects = models.Manager()
    active = ActiveManager()

    def __unicode__(self):
        return u'{0} - {1}'.format(self.event, self.talk)
