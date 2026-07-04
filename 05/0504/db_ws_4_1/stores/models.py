from django.db import models
from django.conf import settings

# Create your models here.
class Store(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="점장")
    address = models.CharField('주소', max_length=200)
    francise = models.BooleanField('체인점 여부', default=True)
    
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)