from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    delete_choices=((LIVE,'Live'),(DELETE,'Delete'))
    title=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    delete_status=models.IntegerField(choices=delete_choices,default=LIVE)

    def __str__(self) -> str:
        return self.title