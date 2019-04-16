from django.db import models
from .choices import *


class Order(models.Model):

    PAYMENT_METHODS = (
        ('Kontant', 'Kontant'),
        ('Swish', 'Swish'),
        ('Kort', 'Kort'),
        ('Faktura', 'Faktura'),
    )

    ORDER_STATUS = (
        ('Ej påbörjad', 'Ej påbörjad'),
        ('Påbörjad', 'Påbörjad'),
        ('Levererad', 'Levererad'),
    )

    name = models.CharField('Namn', max_length=50)
    email = models.EmailField('E-post', max_length=50)
    phone_number = models.CharField('Telefonnummer', max_length=20)
    product_type = models.CharField('Produkttyp', max_length=50, choices=PRODUCT_TYPE, default=1)
    firewood_choice = models.CharField('Val', max_length=50)
    quantity = models.PositiveIntegerField('Kvantitet (kubik/st)', default=1)
    delivery_option = models.CharField('Val av leverans', max_length=50, choices=DELIVERY_OPTIONS, default=1)
    delivery_address = models.CharField('Leveransadress (om valet är utkörning)', max_length=50, blank=True)
    description = models.TextField('Övrig info', max_length=1000, blank=True)
    payment_method = models.CharField('Betala med', max_length=50, choices=PAYMENT_METHODS, default='Kontant')
    order_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    order_status = models.CharField('Status på order', max_length=30, choices=ORDER_STATUS, default='Ej påbörjad')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Ordrar'


class Offer(models.Model):
    name = models.CharField('Namn på erbjudande', max_length=100)
    offer_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Erbjudande'
        verbose_name_plural = 'Erbjudanden'
