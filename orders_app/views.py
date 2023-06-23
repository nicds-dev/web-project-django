from django.shortcuts import render, redirect
from orders_app.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from shopping_cart_app.cart import Cart

# Create your views here.

@login_required(login_url='/authentication_app/login')
def order_process(request):
    order = Order.objects.create(user=request.user)
    cart = Cart(request)
    products_list = list()
    for key, value in cart.cart.items():
        products_list.append(OrderItem(
            product_id = key,
            quantity = value['quantity'],
            user = request.user,
            order = order
        ))

    OrderItem.objects.bulk_create(products_list)

    send_on_mail(
        order = order,
        products_list = products_list,
        username = request.user.username,
        email_user = request.user.email
    )

    messages.success(request, 'Your order has been placed')

    return redirect('../shop')

def send_on_mail(**kwargs):
    subject = 'Thank you for your order'
    message = render_to_string('shop_app/templates/emails/order_mail.html', {
        'order': kwargs.get('order'),
        'products_list': kwargs.get('products_list'),
        'username': kwargs.get('username'),
    })
    message_text = strip_tags(message)
    from_email = 'cuentaparaadobe2001@gmail.com'
    to = kwargs.get('email_user')

    send_mail(subject, message_text, from_email, [to], html_message=message)