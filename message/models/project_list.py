from django.db import models
import datetime
from store.models.customer import Customer


class Project_list(models.Model):
    title = models.CharField(max_length=1000)
    email = models.EmailField()
    description = models.CharField(max_length=10000)
    checkpoint = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,default=0)
    datetime = models.DateTimeField(default=datetime.datetime.now())
