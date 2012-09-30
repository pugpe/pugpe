# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel


class Location(TimeStampedModel):
    description = models.CharField(_(u'Descrição'), max_length=100)

    street = models.CharField(_(u'Rua'), max_length=255)
    number = models.CharField(_(u'Número'), max_length='15')
    district = models.CharField(_(u'Bairro'), max_length='255')
    postal_code = models.CharField(_(u'CEP'), max_length='50')
    city = models.CharField(_(u'Cidade'), max_length=50)
    state = models.CharField(_(u'Estado'), max_length='50')
    country = models.CharField(_(u'País'), max_length='50')

    reference = models.CharField(_(u'Referência'), max_length=100)

    map = models.URLField(
        _(u'Mapa'), max_length=255, null=True, blank=True,
        help_text=u'Caso preenchido, sobrescreve o mapa gerado '
        u'automaticamente',
    )

    class Meta:
        verbose_name = _(u'Local')
        verbose_name_plural = _(u'Locais')

    def __unicode__(self):
        return self.description

    @property
    def address(self):
        address = (self.street, self.number, self.district)
        return u'{0} nº{1} {2}'.format(*address)

    def get_map(self):
        if self.map:
            return self.map

        base_url = 'http://maps.google.com.br/maps?q={0}'

        qs = u'{0},{1},{2},{3},{4}'
        qs = qs.format(
            self.street, self.number, self.district, self.city, self.state,
        )

        return base_url.format(qs)


