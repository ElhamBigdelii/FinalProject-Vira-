from django.shortcuts import render
from charity.models import Modir , Charity , Project , ProjectType
# Create your views here.
# pylint: disable=E1101

def show_index(request):
    posts = Project.objects.filter(projectType=1)[0:5]
    posts3 = Project.objects.filter(projectType=1)[0:3]
    return render(request , 'index/index.html' , {'posts':posts , 'posts3':posts3})