from settings.models import Settings


def get_settings(request):
    try:
        obj = Settings.objects.all().order_by('-id')[0]
    except IndexError:
        return {'SETTING': None}
    return {'SETTING': obj}
