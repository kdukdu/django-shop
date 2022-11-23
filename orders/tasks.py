from time import sleep

from celery import shared_task
from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created_task(order_id):
    sleep(20)
    order = Order.objects.get(id=order_id)
    subject = f"Order #{order_id}"
    message = f"Dear {order.first_name},\n\nYou have successfully placed an order. Your order id is {order.id}."
    mail_send = send_mail(subject,
                          message,
                          'kocherizhkin@gmail.com',
                          [order.email])

    return mail_send
