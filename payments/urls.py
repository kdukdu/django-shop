from django.urls import re_path

from payments.views import payment_process, SuccessView, CancelView
from payments.webhooks import stripe_webhook

urlpatterns = [
    re_path(r'^cancel/$', CancelView.as_view(), name='payment_cancel'),
    re_path(r'^success/$', SuccessView.as_view(), name='payment_success'),
    re_path(r'^create-checkout-session/(?P<order_id>\d+)/$', payment_process, name='payment_process'),
    re_path(r'^webhooks/stripe/$', stripe_webhook, name='stripe-webhook'),
]
