from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Modir(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    codemeli = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)

    def __str__ (self):
        return self.firstname


class Charity(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=60)
    sabt_number = models.CharField(max_length=30)
    description = models.TextField()
    web = models.URLField()
    photo = models.ImageField(blank=True)
    photo_sanad = models.ImageField(default='default.png')
    modir = models.ForeignKey(User , on_delete=models.CASCADE )
    accept = models.BooleanField(default=False)

    def __str__(self):
        return self.name
   


class ProjectType(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField()
    #projectType = models.ForeignKey(ProjectType, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title



class Project(models.Model):
    title = models.TextField(max_length=50)
    cost = models.FloatField()
    endDate = models.DateField()
    startDate = models.DateField()
    publishDate = models.DateTimeField()
    rejistrationDate = models.DateTimeField(auto_now_add= True)
    description = models.TextField()
    modir= models.ForeignKey(Modir, on_delete=models.CASCADE)
    projectType = models.ForeignKey(ProjectType, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

