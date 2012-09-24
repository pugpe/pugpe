# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    class Meta:
        verbose_name = _(u'Evento')
        verbose_name_plural = _(u'Eventos')

    description = models.CharField(_(u'Descrição'), max_length=100)
    full_description = models.TextField(_(u'Descrição Completa'))
    date = models.DateTimeField(_(u'Data'))
    slug = models.SlugField()

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('event', kwargs={'slug': self.slug})
