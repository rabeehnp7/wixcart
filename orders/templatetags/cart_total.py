from django import template

register=template.Library()

@register.simple_tag(name='cart_total')
def cart_total(cart):
    total=0
    for item in cart.cart_items.all():
        total+=item.product.price*item.quantity
    return total