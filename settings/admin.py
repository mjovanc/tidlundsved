from django.contrib import admin
from .models import Settings
from django.utils.translation import gettext_lazy as _


@admin.register(Settings)
class AdminSettings(admin.ModelAdmin):
    class Meta:
        verbose_name = _('Setting')
        verbose_name_plural = _('Settings')
