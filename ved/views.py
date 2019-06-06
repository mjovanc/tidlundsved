from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from ved.forms import *
from .functions import send_email, send_order_verification


class Contact(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('ovrigt')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class MixedHardWood(FormView):
    template_name = 'ved/mixed-hardwood.html'
    form_class = OrderFormMixedHardWood
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.product_type = _('Blandat lövträd')
        self.obj.save()
        return super().form_valid(self.obj)


class BirchWood(FormView):
    template_name = 'ved/birchwood.html'
    form_class = OrderFormBirchWood
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.product_type = _('Björkved')
        self.obj.save()
        return super().form_valid(self.obj)


class BeechWood(FormView):
    template_name = 'ved/beechwood.html'
    form_class = OrderFormBeechWood
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.product_type = _('Bokved')
        self.obj.save()
        return super().form_valid(self.obj)


class AshWood(FormView):
    template_name = 'ved/ashwood.html'
    form_class = OrderFormAshWood
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.product_type = _('Askved')
        self.obj.save()
        return super().form_valid(self.obj)


class Other(FormView):
    template_name = 'ved/other.html'
    form_class = OrderFormOther
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.product_type = _('Övrigt')
        self.obj.save()
        return super().form_valid(self.obj)


class Success(TemplateView):
    template_name = 'various/success.html'
