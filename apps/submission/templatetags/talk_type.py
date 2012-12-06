from django import template

from submission.models import Talk

register = template.Library()


@register.filter
def verbose_talk_type(choice):
    return dict(Talk.TYPES)[choice]
