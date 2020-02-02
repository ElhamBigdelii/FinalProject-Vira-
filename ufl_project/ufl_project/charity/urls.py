from django.conf.urls import url
from .import views

app_name = 'charity'

urlpatterns =[
    url(r'^add_charity/$' , views.charityadd , name="addCharity"),
]