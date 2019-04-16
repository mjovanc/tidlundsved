from django.conf import settings
from .models import Offer


def offerings(request):
    return {'offers': Offer.objects.all().order_by('-id')[0:1]}


def site_title(request):
    return {'SITE_TITLE': settings.SITE_TITLE}