from django.shortcuts import render , redirect
from users.models import Users
from . import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum , Min , Max
from django.db.models.aggregates import StdDev
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
# pylint: disable=E1101

def signeupusers(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        codemeli = request.POST['codemeli']
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']

        post = Users.objects.filter(Q(username=username) | Q(codemeli=codemeli) |  
            Q(phone=phone) | Q(email=email) )

        while post:
            #print ("این نام کاربری قبلا وجود دارد" )
            return render(request, 'signeup/signeup.html' )
        
        p = Users(firstname=firstname ,lastname=lastname , codemeli=codemeli
         , username=username , password=password ,phone=phone , email=email  )

        p.save()
        return redirect('users:test')

    return render(request, 'signeup/signeup.html' )
    