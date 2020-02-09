from django.shortcuts import render , redirect
from .models import Modir , Charity , Project , ProjectType
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum , Min , Max
from django.db.models.aggregates import StdDev
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger , InvalidPage
from django.views.generic import ListView
from django.db.models import Prefetch
from django.http import HttpResponse , HttpResponseNotFound
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect



# pylint: disable=E1101

@login_required(login_url="/accounts/signup_login/")
def charity_profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts) 
        query2 = User.objects.filter(username=posts).get()
        modirId=query2.id
        charitymodir= Charity.objects.filter(modir=modirId)
        return render(request , 'charity/profile_charity.html' , {"charitymodir":charitymodir  ,"query":query })

@login_required(login_url="/accounts/signup_login/")
def charityadd(request):
    posts = request.session['username']
    query = User.objects.filter(username=posts) 
    query2 = User.objects.filter(username=posts).get()
    modirId=query2.id
    charitymodir= Charity.objects.filter(modir=modirId)
    if request.method=='POST':
       form= forms.Creatcharity(request.POST)
       if form.is_valid():
        instance=form.save(commit=False)
        instance.modir=request.user
        instance.save()
        return redirect('charity:addCharity')
    else:
        form = forms.Creatcharity()
    return render(request, 'charity/add_charity.html' , {'form':form , "query":query , "charitymodir":charitymodir})


@login_required(login_url="/accounts/loginpage/")
def addProject(request ):
    posts = request.session['username']
    query = User.objects.filter(username=posts) 
    query2 = User.objects.filter(username=posts).get()
    modirId=query2.id
    charitymodir= Charity.objects.filter(modir=modirId)
    if request.method=='POST':
       form= forms.addProject(request.POST)
       if form.is_valid():
        instance=form.save(commit=False)
        instance.modir=request.user
        modir=instance.modir
        modirId = modir.id
        charitymodir = Charity.objects.filter(modir=modirId).get()
        instance.charity=charitymodir
        instance.save()
        return redirect('charity:addProject')
    else:
        form = forms.addProject()
    return render(request, 'charity/addProject.html' , {'form':form , "query":query , "charitymodir":charitymodir})

def golrizoonshow(request):
    return render(request , 'charity/golrizzonha.html')

def golrizoon_list(request ):
    golrizoons_list = Project.objects.filter(projectType=1)
    paginator = Paginator(golrizoons_list , 4)

    try :
        page = int(request.GET.get('page' , '1'))
    except :
        page = 1
    try :
        posts = paginator.page(page)
    except (EmptyPage , InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render (request , 'charity/golrizzonha.html' ,{'posts':posts })


def datail_project(request , pk):
    posts = get_object_or_404(Project, pk=pk)
    return render(request, 'charity/detail.html', {'posts': posts})


def little_dream(request):
    golrizoons_list = Project.objects.filter(projectType=2)
    paginator = Paginator(golrizoons_list , 4)

    try :
        page = int(request.GET.get('page' , '1'))
    except :
        page = 1
    try :
        posts = paginator.page(page)
    except (EmptyPage , InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render (request , 'charity/little_dream.html' ,{'posts':posts} )


def accepted(request):
    return render(request , 'charity/profile_charity.html')

def show_5lastgolrizoon(request):
    posts = Project.objects.filter(projectType=1)[0:3]
    return render(request , 'index/index.html' , {'posts':posts})


def charityss(request):
    golrizoons_list = Charity.objects.all()
    paginator = Paginator(golrizoons_list , 4)

    try :
        page = int(request.GET.get('page' , '1'))
    except :
        page = 1
    try :
        posts = paginator.page(page)
    except (EmptyPage , InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render (request , 'charity/charitys.html' ,{'posts':posts} )



