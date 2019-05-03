from django.template.response import TemplateResponse
from django.conf import settings
from .forms import *
from .functions import send_email, send_order_verification
from .models import Product


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


def blandat_lovtrad(request):
    if request.method == 'POST':
        form = OrderFormLovTrad(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_type = 'Blandat lövträd'
            obj.save()

            send_order_verification(obj)

            return TemplateResponse(request, 'various/success.html', {'ORDER_ID': obj.pk})
    else:
        form = OrderFormLovTrad()
    return TemplateResponse(request, 'ved/blandat_lovtrad.html',
        {
            'form': form,
            'wood': Product.objects.all().filter(ptype='Blandat lövträd')
        }
    )


def bjorkved(request):
    if request.method == 'POST':
        form = OrderFormBjorkved(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_type = 'Björkved'
            obj.save()

            send_order_verification(obj)

            return TemplateResponse(request, 'various/success.html',
                                    {'ORDER_ID': obj.pk})
    else:
        form = OrderFormBjorkved()
    return TemplateResponse(request, 'ved/bjorkved.html', 
        {
            'form': form,
            'wood': Product.objects.all().filter(ptype='Björkved')
        }
    )


def bokved(request):
    if request.method == 'POST':
        form = OrderFormBokved(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_type = 'Bokved'
            obj.save()

            send_order_verification(obj)

            return TemplateResponse(request, 'various/success.html',
                                    {'ORDER_ID': obj.pk})
    else:
        form = OrderFormBokved()
    return TemplateResponse(request, 'ved/bokved.html', 
        {
            'form': form,
            'wood': Product.objects.all().filter(ptype='Bokved')
        }
    )


def askved(request):
    if request.method == 'POST':
        form = OrderFormAskved(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_type = 'Askved'
            obj.save()

            send_order_verification(obj)

            return TemplateResponse(request, 'various/success.html',
                                    {'ORDER_ID': obj.pk})
    else:
        form = OrderFormAskved()
    return TemplateResponse(request, 'ved/askved.html', 
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
    return TemplateResponse(request, 'ved/ovrigt.html',  
        {
            'form': form,
            'wood': Product.objects.all().filter(ptype='Övrigt')
        }
    )


def success(request):
    return TemplateResponse(request, 'various/success.html')
