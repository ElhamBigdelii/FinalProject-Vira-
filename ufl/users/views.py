from django.shortcuts import render , redirect
from .models import Users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum , Min , Max
from django.db.models.aggregates import StdDev
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# pylint: disable=E1101
def test(request):
    return render(request , 'users/test.html')




