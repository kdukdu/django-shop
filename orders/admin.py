from django.contrib import admin
from django.utils.html import format_html

from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def order_payment(obj):
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}">{obj.stripe_id}</a>'
        return format_html(html)
    return ''


order_payment.short_description = 'Stripe payment'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    order_payment, 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = (OrderItemInline,)


admin.site.register(OrderItem)
