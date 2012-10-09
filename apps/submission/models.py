# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel


class Vote(TimeStampedModel):
    TYPES = (
        (u'like', _(u'Gostei')),
        (u'dislike', _(u'Não gostei')),
    )

    email = models.ForeignKey('emails.Email')
    talk = models.ForeignKey('submission.Talk')
    type = models.CharField(max_length=15, choices=TYPES)

    def __unicode__(self):
        return u'{0}; {1}; {2}'.format(self.email, self.talk.id, self.type)


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

    def _form(self, type):
        from .forms import VoteForm
        return VoteForm(initial={'talk': self.pk, 'type': type})

    def like_form(self):
        return self._form('like')

    def dislike_form(self):
        return self._form('dislike')
