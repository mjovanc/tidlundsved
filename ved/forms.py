from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from .models import Order
from .choices import *
from django.utils.translation import gettext_lazy as _


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['order_status']

    # def send_email(self):
    #     return send_mail(
    #         "Name",
    #         "Description",
    #         ["mjovanc@protonmail.com"],
    #         ['{0}'.format("mjovanc@protonmail.com")]
    #     )


class OrderFormMixedHardWood(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Val'), choices=BLANDAT_LOVTRAD_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormBirchWood(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Val'), choices=BJORKVED_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormBeechWood(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Val'), choices=BOKVED_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormAshWood(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Val'), choices=ASKVED_CHOICES, required=True)

    class Meta(OrderForm.Meta):
        exclude = ['product_type', 'order_status']


class OrderFormOther(OrderForm):
    firewood_choice = forms.ChoiceField(label=_('Val'), choices=OTHER_CHOICES, required=True)

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
