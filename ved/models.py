from django.db import models
from .choices import *
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    PAYMENT_METHODS = (
        ('Cash', _('Cash')),
        ('Swish', _('Swish')),
        ('Card', _('Card')),
        ('Invoice', _('Invoice')),
    )

    ORDER_STATUS = (
        ('Not Started', _('Not Started')),
        ('Started', _('Started')),
        ('Delivered', _('Delivered')),
    )

    name = models.CharField(verbose_name=_('Name'), max_length=50)
    email = models.EmailField(verbose_name=_('E-Mail'), max_length=50)
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=20)
    product_type = models.CharField(verbose_name=_('Type'), max_length=50, choices=PRODUCT_TYPE, default=1)
    firewood_choice = models.CharField(verbose_name=_('Choice'), max_length=50)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity (cubic/piece)'), default=1)
    delivery_option = models.CharField(verbose_name=_('Delivery'), max_length=50, choices=DELIVERY_OPTIONS, default=1)
    delivery_address = models.CharField(verbose_name=_('Delivery Address (if choice is delivery)'), max_length=50, blank=True)
    description = models.TextField(verbose_name=_('Other Info'), max_length=1000, blank=True)
    payment_method = models.CharField(verbose_name=_('Pay With'), max_length=50, choices=PAYMENT_METHODS, default='Cash')
    order_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    order_status = models.CharField(verbose_name=_('Order Status'), max_length=30, choices=ORDER_STATUS, default='Not Started')

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class Offer(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    offer_date = models.DateTimeField(verbose_name=_('Date'), auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')


class Product(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    desc = models.TextField(verbose_name=_('Description'), max_length=1000, blank=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=7, decimal_places=2)
    ptype = models.CharField(verbose_name=_('Type'), max_length=50, choices=PRODUCT_TYPE, default=1)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
