from django.shortcuts import render , redirect
from users.models import Users
from charityes.models import Modir
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum , Min , Max
from django.db.models.aggregates import StdDev
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# pylint: disable=E1101

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        post = Users.objects.filter(username=username , password=password)
        post2 = Modir.objects.filter(username=username , password=password)
       
        if post :
            username=request.POST['username']
            request.session['username'] = username
            return redirect('login:profile_users')
        if post2:
            username=request.POST['username']
            request.session['username'] = username
            return redirect('login:profile_modir')
        else :
            return render(request, 'login/loginpage.html', {})

    return render(request, 'login/loginpage.html', {})


def profile_user(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = Users.objects.filter(username=posts) 
        #query2 = Modir.objects.filter(username=posts)
        return render(request, 'login/profile_user.html', {"query":query })
    else:
        return render(request, 'login/loginpage.html', {})

def profile_Modir(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = Modir.objects.filter(username=posts) 
        #query2 = Modir.objects.filter(username=posts)
        return render(request, 'login/profile_modir.html', {"query":query })
    else:
        return render(request, 'login/loginpage.html', {})

def edit(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        codemeli = request.POST['codemeli']
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']

        post = Users.objects.get_or_create(codemeli=codemeli)[0]

            #print ("این نام کاربری قبلا وجود دارد" 
        p = post(firstname=firstname ,lastname=lastname , codemeli=codemeli
            , username=username , password=password ,phone=phone , email=email )
        p.save()
        return redirect('login:profile_users')
        
    return render(request, 'login/profile_user.html' )
    