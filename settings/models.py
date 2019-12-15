from django.db import models
from django.utils.translation import gettext_lazy as _


class Settings(models.Model):
    sitewide_notice = models.CharField(verbose_name=_('Sitewide Notice'), max_length=150)

    def __str__(self):
        return "All Settings"

    class Meta:
        verbose_name = _('Setting')
        verbose_name_plural = _('Settings')