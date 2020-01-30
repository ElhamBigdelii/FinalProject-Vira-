from django.shortcuts import render , redirect
from .models import Charityes2 , Modir
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum , Min , Max
from django.db.models.aggregates import StdDev
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# pylint: disable=E1101
# Create your views here.

def addcharityes(request):
    if request.method=='POST':
        name=request.POST['name']
        date_tasisi = request.POST['date_tasisi']
        web = request.POST['web']
        phone_markaz = request.POST['phone_markaz']
        address = request.POST['address']
        sabt_number = request.POST['sabt_number']
        image = request.POST['image']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        codemeli = request.POST['codemeli']
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']

        post = Charityes2.objects.filter(Q(sabt_number=sabt_number))
        post2 = Modir.objects.filter(Q(username=username) | Q(codemeli=codemeli) |  
            Q(phone=phone) | Q(email=email) )
        while (post):
            return render(request, 'charityes/addcharityes.html')
        while (post2):
            return render(request, 'charityes/addcharityes.html')

        p = Charityes2(name=name , date_tasisi=date_tasisi
        , web=web , phone_markaz=phone_markaz , address=address
        , sabt_number=sabt_number , image=image )

        p2 = Modir(firstname=firstname ,lastname=lastname , codemeli=codemeli
         , username=username , password=password ,phone=phone , email=email  )

        p.save()
        p2.save()
        return redirect('users:test')


    return render(request , 'charityes/addcharityes.html')


def profile_charity(request):
    return render(request , 'charityes/profile_charity.html')

