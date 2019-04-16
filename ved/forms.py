from django import forms
from django.forms import ModelForm
from .models import Order
from .choices import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['order_status']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Förnamn och efternamn'
        self.fields['name'].error_messages = {'required': 'Detta fält är ett krav'}
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'exempel@mail.se'
        self.fields['email'].error_messages = {'required': 'Ange en korrekt emailaddress'}
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Telefonnummer'
        self.fields['firewood_choice'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_option'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_address'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_address'].widget.attrs['placeholder'] = 'Adress'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['rows'] = '4'
        self.fields['payment_method'].widget.attrs['class'] = 'form-control'


class OrderFormLovTrad(OrderForm):
    firewood_choice = forms.ChoiceField(label='Val', choices=BLANDAT_LOVTRAD_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormBjorkved(OrderForm):
    firewood_choice = forms.ChoiceField(label='Val', choices=BJORKVED_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormBokved(OrderForm):
    firewood_choice = forms.ChoiceField(label='Val', choices=BOKVED_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormAskved(OrderForm):
    firewood_choice = forms.ChoiceField(label='Val', choices=ASKVED_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormOther(OrderForm):
    firewood_choice = forms.ChoiceField(label='Val', choices=OTHER_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class ContactForm(forms.Form):
    name = forms.CharField(label='Namn', max_length=50)
    sender = forms.EmailField(label='E-post')
    message = forms.CharField(label='Meddelande', widget=forms.Textarea)
    cc_myself = forms.BooleanField(label='Kopia till mail', required=False)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Namn'
        self.fields['sender'].widget.attrs['class'] = 'form-control'
        self.fields['sender'].widget.attrs['placeholder'] = 'E-post'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['rows'] = '4'
