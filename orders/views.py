from django.shortcuts import render,redirect
from . models import Order,OrderItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_orders(request):
    user=request.user
    customer=user.user_details
    all_orders=Order.objects.filter(customer=customer).exclude(order_status=Order.CART_STAGE)
    return render(request,'orders.html',{'orders':all_orders})

@login_required
def checkout(request):
    try:
        user=request.user
        customer=user.user_details
        total=request.POST.get('total')
        order_obj=Order.objects.get(
        customer=customer,
        order_status=Order.CART_STAGE
            )
        order_obj.order_status=Order.ORDER_CONFIRMED
        order_obj.total_price=total
        order_obj.save()
        status_message="Your order is Confirmed. Delivering soon !"
        messages.success(request,status_message)
    except Exception as e:
        status_message=" Your order could'nt processed"
        messages.error(request,status_message)
    return redirect('home')

@login_required
def show_cart(request):
    user=request.user
    customer=user.user_details
    cart_obj,created=Order.objects.get_or_create(
            customer=customer,
            order_status=Order.CART_STAGE,
        )
    return render(request,'cart.html',{'cart':cart_obj})

def remove_item_from_cart(request,pk):
    order_item_obj=OrderItem.objects.get(pk=pk)
    if order_item_obj:
        order_item_obj.delete()
    return redirect('cart')

def add_to_cart(request):
    if request.POST:
        user=request.user
        product_id=request.POST.get('product_id')
        quantity=int(request.POST.get('quantity'))
        customer=user.user_details
        product=Product.objects.get(pk=product_id)
        
        cart_obj,created=Order.objects.get_or_create(
            customer=customer,
            order_status=Order.CART_STAGE,
        )
        order_items,created=OrderItem.objects.get_or_create(
            product=product,
            order=cart_obj
        )
        if created:
            order_items.quantity=quantity
            order_items.save()
        else:
            order_items.quantity+=quantity
            order_items.save()
        return redirect('cart')