from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from accounts.forms import RegistrationForm
# Create your views here.
def signup_users(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('accounts:signup')
    else:
        form = RegistrationForm()
    return render(request , 'accounts/signup.html' , {'form':form}) 


def login(request):
    if request.method == 'POST':
        form2 = AuthenticationForm (data=request.POST)
        if form2.is_valid():

            return redirect('accounts:signup')
        else:
            form2 = AuthenticationForm()
    return render(request , 'accounts/signup.html' , {'form2':form2})