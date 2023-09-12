from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

'''
on_delete properties:
    # CASCADE -> if primary deleted, delete foreing too.
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value')
    # DO_NOTHING -> if primary deleted, do nothing.
    # PROTECT -> if foreign is exist, can not delete primary.
'''

class Address(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=120)
    user = models.ManyToManyField(User)