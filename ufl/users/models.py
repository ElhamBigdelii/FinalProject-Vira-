from django.db import models

# Create your models here.

class Users(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=15)
    codemeli = models.CharField(max_length=11)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname
