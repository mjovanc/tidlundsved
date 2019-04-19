from django import forms
from django.forms import ModelForm
from .models import Order
from .choices import *
from django.utils.translation import gettext_lazy as _


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['order_status']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = _('First name and last name')
        self.fields['name'].error_messages = {'required': _('This field is required')}
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'example@mail.se'
        self.fields['email'].error_messages = {'required': _('Enter a correct E-Mail address')}
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['placeholder'] = _('Phone Number')
        self.fields['firewood_choice'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_option'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_address'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_address'].widget.attrs['placeholder'] = _('Address')
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
    name = forms.CharField(label=_('Name'), max_length=50)
    sender = forms.EmailField(label=_('E-Mail'))
    message = forms.CharField(label=_('Message'), widget=forms.Textarea)
    cc_myself = forms.BooleanField(label=_('Copy to E-mail'), required=False)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = _('Name')
        self.fields['sender'].widget.attrs['class'] = 'form-control'
        self.fields['sender'].widget.attrs['placeholder'] = _('E-Mail')
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['rows'] = '4'
