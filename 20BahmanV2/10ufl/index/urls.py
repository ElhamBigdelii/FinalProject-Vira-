from django.conf.urls import url
from .import views

app_name = 'index'

urlpatterns =[
    url(r'^/$' , views.show_index , name="show_index"),
]