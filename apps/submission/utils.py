# -*- coding:utf-8 -*-
from functools import wraps

from django.core import signing
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404

from emails.models import Email


def token_required(func):
    @wraps(func)
    def wrapped(request, *args, **kwargs):
        if request.session.get('email'):
            return func(request, *args, **kwargs)

        token = request.GET.get('token')
        if token is None:
            # Redirecionar, sem token
            return redirect(reverse('submission:error', kwargs=kwargs))

        try:
            pk = signing.loads(token)
            email = get_object_or_404(Email, pk=pk)
            request.session['email'] = email
        except signing.BadSignature:
            # Redirecionar, token inváldo
            return redirect(reverse('submission:error', kwargs=kwargs))

        return func(request, *args, **kwargs)
    return wrapped
