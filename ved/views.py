from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.conf import settings
from ved.forms import *
from .functions import send_email, send_order_verification
from .models import Product


# must change this later
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            if 'cc_myself' in request.POST:
                send_email('Tidlundsved.se - Kontaktformulär', message, settings.EMAIL_SEND_TO, sender)

            send_email('Tidlundsved.se - Kontaktformulär', message, sender, settings.EMAIL_SEND_TO)
            return TemplateResponse(request, 'various/mail.html')
    else:
        form = ContactForm()
    return TemplateResponse(request, 'contact.html', {'form': form})


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


def blandat_lovtrad(request):
    if request.method == 'POST':
        form = OrderFormMixedHardWood(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_type = 'Blandat lövträd'
            obj.save()

            send_order_verification(obj)

            return TemplateResponse(request, 'various/success.html', {'ORDER_ID': obj.pk})
    else:
        form = OrderFormMixedHardWood()
    return TemplateResponse(request, 'ved/mixed-hardwood.html',
        {
            'form': form,
            'wood': Product.objects.all().filter(ptype='Blandat lövträd')
        }
    )


def bjorkved(request):
    if request.method == 'POST':
        form = OrderFormBirchWood(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_type = 'Björkved'
            obj.save()

            send_order_verification(obj)

            return TemplateResponse(request, 'various/success.html',
                                    {'ORDER_ID': obj.pk})
    else:
        form = OrderFormBirchWood()
    return TemplateResponse(request, 'ved/birchwood.html',
        {
            'form': form,
            'wood': Product.objects.all().filter(ptype='Björkved')
        }
    )


def bokved(request):
    if request.method == 'POST':
        form = OrderFormBeechWood(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_type = 'Bokved'
            obj.save()

            send_order_verification(obj)

            return TemplateResponse(request, 'various/success.html',
                                    {'ORDER_ID': obj.pk})
    else:
        form = OrderFormBeechWood()
    return TemplateResponse(request, 'ved/beechwood.html',
        {
            'form': form,
            'wood': Product.objects.all().filter(ptype='Bokved')
        }
    )


def askved(request):
    if request.method == 'POST':
        form = OrderFormAshWood(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_type = 'Askved'
            obj.save()

            send_order_verification(obj)

            return TemplateResponse(request, 'various/success.html',
                                    {'ORDER_ID': obj.pk})
    else:
        form = OrderFormAshWood()
    return TemplateResponse(request, 'ved/ashwood.html',
        {
            'form': form,
            'wood': Product.objects.all().filter(ptype='Askved')
        }
    )


def ovrigt(request):
    if request.method == 'POST':
        form = OrderFormOther(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_type = 'Övrigt'
            obj.save()

            send_order_verification(obj)

            return TemplateResponse(request, 'various/success.html',
                                    {'ORDER_ID': obj.pk})
    else:
        form = OrderFormOther()
    return TemplateResponse(request, 'ved/other.html',
        {
            'form': form,
            'wood': Product.objects.all().filter(ptype='Övrigt')
        }
    )


def success(request):
    return TemplateResponse(request, 'various/success.html')
