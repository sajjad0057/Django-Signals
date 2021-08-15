from django.db import models
from buyers.models import Buyer
import uuid

# Create your models here.
class Car(models.Model):
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    code = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return f'{self.name} - {self.price} - {self.buyer}'

    def save(self,*args,**kwargs):
        if self.code =="":
            self.code = str(uuid.uuid4()).replace("-","").upper()[:10]

        return super().save(*args,**kwargs)