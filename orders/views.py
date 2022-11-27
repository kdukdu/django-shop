from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem, Order
from orders.tasks import order_created_task


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            order_created_task.delay(order.id)
            return HttpResponseRedirect(reverse('order_created', kwargs={'order_id': order.id}))
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


def order_created(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order/created.html', {'order': order})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', context={'order': order})
