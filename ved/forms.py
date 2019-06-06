from django import forms
from django.forms import ModelForm
from django.core.mail import EmailMultiAlternatives
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

    def send_email(self):
        msg = EmailMultiAlternatives(
            subject="Please activate your account",
            body="Click to activate your account: http://example.com/activate",
            from_email="Tidlundsved.se <noreply@tidlundsved.se>",
            to=["New User <user1@example.com>", "account.manager@example.com"],
            reply_to=["Helpdesk <support@example.com>"])

        # Include an inline image in the html:
        html = """<p>Please <a href="http://example.com/activate">activate</a>
                  your account</p>"""
        msg.attach_alternative(html, "text/html")

        # Optional Anymail extensions:
        msg.metadata = {"user_id": "8675309", "experiment_variation": 1}
        msg.tags = ["activation", "onboarding"]
        msg.track_clicks = True

        # Send it:
        msg.send()
        return send_mail("Test Title", "Test message", "noreply@tidlundsved.se", ["mjovanc@protonmail.com"])

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['sender'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['rows'] = '4'
