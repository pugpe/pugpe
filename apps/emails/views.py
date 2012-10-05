# -*- coding:utf-8 -*-
from django.shortcuts import render

from submission.utils import token_required


@token_required
def optout(request):
    email = request.session['email']
    email.opt_in = False
    email.save()
    return render(request, 'emails/optout.html', {})
