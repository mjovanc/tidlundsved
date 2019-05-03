from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

