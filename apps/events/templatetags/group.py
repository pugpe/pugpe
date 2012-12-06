# -*- coding:utf-8 -*-
from operator import attrgetter

from django import template
from django.utils.datastructures import SortedDict


register = template.Library()


@register.assignment_tag
def group(queryset, expression):
    '''
    Similar to regroup, but without restrict respect order


    Usage: {% group people 'gender' as grouped  %}

    '''
    key = attrgetter(expression)

    group = SortedDict()
    for item in queryset:
        try:
            k = key(item)
        except AttributeError:
            k = None
        group[k] = group.get(k, []) + [item]
    return group
