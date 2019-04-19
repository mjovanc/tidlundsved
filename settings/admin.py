from django.contrib import admin
from .models import SitewideNotice
from django.utils.translation import gettext_lazy as _


@admin.register(SitewideNotice)
class AdminSitewideNotice(admin.ModelAdmin):
    class Meta:
        verbose_name = _('Sitewide Notice')
        verbose_name_plural = _('Sitewide Notices')
