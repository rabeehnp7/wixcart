from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    CART_STAGE=1
    ORDER_CONFIRMED=2
    ORDER_PROCESSED=3
    ORDER_DELIVERED=4
    ORDER_CANCELLED=5
    delete_choices=((LIVE,'Live'),(DELETE,'Delete'))
    STATUS_CHOICE=(
        (ORDER_PROCESSED,'ORDER PROCESSED'),
        (ORDER_DELIVERED,'ORDER DELIVERED'),
        (ORDER_CANCELLED,'ORDER CANCELLED')
    )
    total_price=models.FloatField(default=0.00)
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL,related_name='orders')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    delete_status=models.IntegerField(choices=delete_choices,default=LIVE)
    
    def __str__(self):
        return "order-{}-{}".format(self.id,self.customer.user.username)
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='added_carts',null=True)
    quantity=models.PositiveIntegerField(default=1)
    order=models.ForeignKey(Order,null=True,on_delete=models.CASCADE,related_name='cart_items')
