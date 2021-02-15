from django.db import models
from django.contrib .auth.models import User



def upload(instance,filename):
    return f"{instance.name}-{filename}"


class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    ddd = models.CharField(max_length=54) ####country code
    name = models.CharField(max_length=255)
    number_tel = models.CharField(max_length=54)
    photo = models.ImageField(upload_to=upload, blank=True, null=True)
    favorited = models.BooleanField(default=False)