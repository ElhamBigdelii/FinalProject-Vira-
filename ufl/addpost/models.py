from django.db import models

# Create your models here.
#class Golrizoon(models.Model):
class Posts(models.Model):
    titr = models.CharField(max_length=30)
    type_project = models.CharField(max_length=20)
    price = models.BigIntegerField()
    date_start = models.DateField()
    date_final = models.DateField()
    date_published = models.DateField()
    date_register = models.DateField()
    explian = models.TextField()