from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    

    LIVE=1
    DELETE=0
    delete_choices=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_details')
    delete_status=models.IntegerField(choices=delete_choices,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username

class Address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='addresses')
    address=models.TextField()

    def __str__(self) -> str:
        return self.address

