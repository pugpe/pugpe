from django.db import models
from django.utils.translation import ugettext_lazy as _


class ActiveManager(models.Manager):
    def get_query_set(self):
        qs = super(ActiveManager, self).get_query_set()
        return qs.filter(opt_in=True)


class Email(models.Model):
    email = models.EmailField(u'E-mail', max_length=254, unique=True)
    opt_in = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    active = ActiveManager()
    objects = models.Manager()

    def __unicode__(self):
        return self.email
