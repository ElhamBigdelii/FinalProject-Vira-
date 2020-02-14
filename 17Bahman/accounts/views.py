from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from accounts.forms import RegistrationForm ,EditProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout
from django.contrib.auth.models import User
from charity.models import Modir , Charity , Project , ProjectType
# pylint: disable=E1101
# Create your views here.
def signup_users(request):
    if request.method == 'POST':
        username = request.POST['username']
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['username'] = username
            return redirect('accounts:profil_accounts')
    else:
        form = RegistrationForm()
    return render(request , 'accounts/signup.html' , {'form':form}) 

def test(request):
    return render(request , 'accounts/test.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        form2 = AuthenticationForm (data=request.POST)
        if form2.is_valid():
            request.session['username'] = username
            user = form2.get_user()
            
            login (request,user)
            if 'next' in request.POST:
                request.session['username'] = username
            return redirect('accounts:profil_accounts')
        else:
            form2 = AuthenticationForm()
    return render(request , 'accounts/signup.html' , {'form2':form2})

@login_required(login_url="/accounts/signup_login/")
def view_profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts) 
        query2 = User.objects.filter(username=posts).get()
        modirId=query2.id
        charitymodir= Charity.objects.filter(modir=modirId)
    
        return render(request, 'accounts/Profile.html', {"query":query , "charitymodir":charitymodir} )
    else:
        return render(request, 'accounts/Profile.html', {})

@login_required(login_url="/accounts/signup_login/")
def view_profile_charity(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts) 
        query2 = User.objects.filter(username=posts).get()
        modirId=query2.id
        charitymodir= Charity.objects.filter(modir=modirId)
    
        return render(request, 'accounts/Profile_charity.html', {"query":query , "charitymodir":charitymodir} )
    else:
        return render(request, 'accounts/Profile_charity.html', {})



@login_required(login_url="/accounts/signup_login/")
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST , instance=request.user)

        if form.is_valid():
            form.save()
            return redirect ('accounts:profil_accounts')

    else:
        form = EditProfile(instance=request.user)
    return render(request , 'accounts/edit_profile.html' , {"form":form})

@login_required(login_url="/accounts/signup_login/")
def logout_viwe(request):
    if request.method=='POST':
        logout(request)
        return redirect('index:show_index')

    

