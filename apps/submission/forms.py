# -*- coding:utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Talk, Vote
from events.models import EventTalk


class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')
        super(TalkForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'input-xxlarge'
            else:
                field.widget.attrs['class'] = 'input-xlarge'

    def save(self, *args, **kwargs):
        # Criar EventTalk, para já constar no admin e facilmente ser ativado
        # caso a palestra seja aprovada
        talk = super(TalkForm, self).save(*args, **kwargs)
        EventTalk.objects.create(talk=talk, event=self.event)

        return talk


class VoteForm(forms.Form):
    talk = forms.Field(widget=forms.HiddenInput)
    type = forms.Field(widget=forms.HiddenInput)

    def save(self, email):
        talk = self.cleaned_data['talk']
        talk = Talk.objects.get(pk=talk)
        type = self.cleaned_data['type']

        v = Vote.objects.get_or_create(email=email, talk=talk)[0]
        if v.type != type:
            v.type = type
            v.save()

        return v
