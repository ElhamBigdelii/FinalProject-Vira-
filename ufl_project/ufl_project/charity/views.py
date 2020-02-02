from django.shortcuts import render , redirect
from .models import Modir , Charity
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum , Min , Max
from django.db.models.aggregates import StdDev
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/loginpage/")

def charityadd(request):
    if request.method=='POST':
       form= forms.Creatcharity(request.POST)
       if form.is_valid():
        instance=form.save(commit=False)
        instance.modir=request.user
        instance.save()
        return redirect('charity:addCharity')
    else:
        form = forms.Creatcharity()
    return render(request, 'charity/add_charity.html' , {'form':form})
