from django.db import models
#from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=100, unique=True, default="Unknown User")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name