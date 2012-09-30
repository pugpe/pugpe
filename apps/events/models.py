# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from core.models import TimeStampedModel


class Location(models.Model):
    class Meta:
        verbose_name = _(u'Local')
        verbose_name_plural = _(u'Locais')

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


class Event(models.Model):
    class Meta:
        verbose_name = _(u'Evento')
        verbose_name_plural = _(u'Eventos')

    description = models.CharField(_(u'Descrição'), max_length=100)
    full_description = models.TextField(_(u'Descrição Completa'))
    date = models.DateTimeField(_(u'Data'))
    slug = models.SlugField()
    location = models.ForeignKey(
        'Location', verbose_name=_(u'Local'),
    )

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('event', kwargs={'slug': self.slug})


class Talk(TimeStampedModel):
    TYPES = (
        ('talk', _(u'Palestra')),
        ('tutorial', _(u'Tutorial')),
        ('light', _(u'Palestra Relâmpago')),
    )

    LEVELS = (
        ('beginner', _(u'Iniciante')),
        ('intermediate', _(u'Intermediário')),
        ('advanced', _(u'Avançado')),
    )

    BOOL = (
        (False, _(u'Não')),
        (True, _(u'Sim')),
    )

    THEMES = (
        ('web', _(u'Desenvolvimento Web')),
        ('sci', _(u'Desenvolvimento Científico')),
        ('mobile', _(u'Mobile')),
        ('edu', _(u'Educação')),
        ('emp', _(u'Empreendedorismo')),
        ('adm', _(u'Administraçao de Sistemas')),
        ('hardware', _(u'Hardware, Robótica')),
        ('utils', _(u'Software Utilitários')),
        ('core', _(u'Core Python')),
        ('other', _(u'Outro')),
    )

    name = models.CharField(_(u'Nome'), max_length=150)
    email = models.EmailField(_(u'E-Mail'), max_length=254)
    phone = models.CharField(_(u'Telefone'), max_length=14)
    talk_once = models.BooleanField(_(u'Já palestrou'), choices=BOOL)
    macro_theme = models.CharField(
        _(u'MacroTema'), max_length=80, choices=THEMES,
    )
    title = models.CharField(_(u'Título'), max_length=80)
    type = models.CharField(_(u'Tipo'), max_length=20, choices=TYPES)
    level = models.CharField(_(u'Nível'), max_length=20, choices=LEVELS)
    summary = models.TextField(_(u'Resumo'))
    event = models.ForeignKey(
        'Event', verbose_name=_(u'Evento'),
    )

    class Meta:
        verbose_name = _(u'Palestra')
        verbose_name_plural = _(u'Palestras')

    def __unicode__(self):
        return u'{0} | {1}'.format(self.name, self.title)

    def get_type(self):
        return dict(self.TYPES)[self.type]

    def get_level(self):
        return dict(self.LEVELS)[self.level]

    def get_macro_theme(self):
        return dict(self.THEMES)[self.macro_theme]
