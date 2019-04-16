from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'product_type',
        'firewood_choice',
        'quantity',
        'delivery_option',
        'payment_method',
        'order_status'
    )
    list_filter = ('product_type', 'delivery_option', 'order_status', 'payment_method')
    list_per_page = 10


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'offer_date',
    )


admin.site.site_header = 'TIDLUNDS VED ADMIN'
admin.site.site_title = 'Tidlunds ved admin'
