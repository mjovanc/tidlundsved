from .models import SitewideNotice


def settings(request):
    obj = SitewideNotice.objects.all().order_by('-id')[0]
    return {'SITEWIDE_NOTICE': obj }
