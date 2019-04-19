from .models import SitewideNotice


def settings(request):
    try:
        obj = SitewideNotice.objects.all().order_by('-id')[0]
    except IndexError:
        return {'SITEWIDE_NOTIC': None}
    return {'SITEWIDE_NOTICE': obj}
