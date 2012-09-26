# -*- coding: utf-8 -*-
from django.db import models


class TimeStampedModel(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
