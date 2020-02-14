from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from accounts.forms import RegistrationForm ,EditProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout
from django.contrib.auth.models import User
from charity.models import Modir , Charity , Project , ProjectType , participateProject
from django.http import HttpResponseRedirect

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
    charit = Charity.objects.all()
    return render(request , 'accounts/test.html' , {'charit':charit})

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
                return redirect('show_indexx')
            superuser = User.objects.filter(username=username).get()
            superuser_result = superuser.is_superuser
            if superuser_result:
                return redirect('accounts:admin_panel')
            return redirect('show_indexx')
        else:
            form2 = AuthenticationForm()
    return render(request , 'accounts/signup.html' , {'form2':form2})


@login_required(login_url="/accounts/signup_login/")
def panel_admin(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts) 
        query2 = User.objects.filter(username=posts).get()
        modirId=query2.id
        charitymodir= Charity.objects.filter(modir=modirId)
    
        return render(request, 'accounts/panel_admin.html', {"query":query , "charitymodir":charitymodir} )
    else:
        return render(request, 'accounts/panel_admin.html', {})

@login_required(login_url="/accounts/signup_login/")
def view_profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts) 
        query2 = User.objects.filter(username=posts).get()
        modirId=query2.id
        charitymodir= Charity.objects.filter(modir=modirId)
        superuser = User.objects.filter(username=posts).get()
        superuser_result = superuser.is_superuser
        if superuser_result:
            return redirect('accounts:admin_panel')
        return render(request, 'accounts/profile_users.html', {"query":query , "charitymodir":charitymodir} )
    else:
        return render(request, 'accounts/profile_users.html', {})

@login_required(login_url="/accounts/signup_login/")
def view_profile_charity(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts) 
        query2 = User.objects.filter(username=posts).get()
        modirId=query2.id
        charitymodir= Charity.objects.filter(modir=modirId)
    
        return render(request, 'accounts/charity_profile.html', {"query":query , "charitymodir":charitymodir} )
    else:
        return render(request, 'accounts/charity_profile.html', {})



@login_required(login_url="/accounts/signup_login/")
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST , instance=request.user)

        if form.is_valid():
            form.save()
            return redirect ('accounts:profil_accounts')

    else:
        form = EditProfile(instance=request.user)
        
    return render(request , 'accounts/edit_Profile.html', {"form":form})

@login_required(login_url="/accounts/signup_login/")
def logout_viwe(request):
    if request.method=='POST':
        logout(request)
        return redirect('show_indexx')




