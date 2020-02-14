from django.shortcuts import render
from charity.models import Modir , Charity , Project , ProjectType
from django.contrib.auth.models import User
from charity.models import Modir , Charity , Project , ProjectType , participateProject
# Create your views here.
# pylint: disable=E1101

def show_index(request):
    projectcount = Project.objects.count()
    usercount = User.objects.count()
    charitycount = Charity.objects.count()
    posts = Project.objects.filter(projectType=1)[0:5]
    posts3 = Project.objects.filter(projectType=1)[0:3]
    return render(request , 'index.html' , {'projectcount':projectcount , 'posts':posts , 'posts3':posts3 , 'charitycount':charitycount , 'usercount':usercount})

