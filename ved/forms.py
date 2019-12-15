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
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'firewood_choice': forms.Select( # does not work for some reason
                attrs={'class': 'custom-select'}
            ),
            'quantity': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'delivery_option': forms.Select(
                attrs={'class': 'custom-select'}
            ),
            'delivery_address': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3'
                }
            ),
            'payment_method': forms.Select(
                attrs={'class': 'custom-select'}
            ),
        }


class OrderFormMixedHardWood(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Choice'), choices=BLANDAT_LOVTRAD_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormBirchWood(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Choice'), choices=BJORKVED_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormBeechWood(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Choice'), choices=BOKVED_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormAshWood(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Choice'), choices=ASKVED_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormOther(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Choice'), choices=OTHER_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=50)
    email = forms.EmailField(label=_('E-Mail'))
    message = forms.CharField(label=_('Message'), widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['rows'] = '4'
