from django.db import models
from django.utils.translation import gettext_lazy as _


class SitewideNotice(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=150)
