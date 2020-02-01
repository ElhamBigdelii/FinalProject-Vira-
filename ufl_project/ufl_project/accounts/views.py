from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from accounts.forms import RegistrationForm ,EditProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout
from django.contrib.auth.models import User
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


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        form2 = AuthenticationForm (data=request.POST)
        if form2.is_valid():
            user = form2.get_user()
            request.session['username'] = username
            login (request,user)
            if 'next' in request.POST:
                return redirect('accounts:login')
            return redirect('accounts:profil_accounts')
        else:
            form2 = AuthenticationForm()
    return render(request , 'accounts/signup.html' , {'form2':form2})



def view_profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts) 
        return render(request, 'accounts/Profile.html', {"query":query})
    else:
        return render(request, 'accounts/Profile.html', {})



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST , instance=request.user)

        if form.is_valid():
            form.save()
            return redirect ('accounts:profil_accounts')

    else:
        form = EditProfile(instance=request.user)
    return render(request , 'accounts/edit_profile.html' , {"form":form})
