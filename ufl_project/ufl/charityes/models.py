from django.db import models

# Create your models here.

class Charityes2(models.Model):
    name = models.CharField(max_length=20)
    date_tasisi = models.CharField(max_length=10)
    web = models.CharField(max_length=30)
    phone_markaz = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
    sabt_number = models.CharField(max_length=30)
    explain = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name

class Modir(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=15)
    codemeli = models.CharField(max_length=11)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname