from django import template

register=template.Library()

@register.simple_tag(name='order_status')
def order_status(status):
    ord_status=['confirmed','processed','delivered','rejected']
    return ord_status[status-2]