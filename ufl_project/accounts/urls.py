from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns =[
    url(r'^signup/$' , views.signup_users , name="signup"),
    url(r'^login/$' , views.login , name="loginpage"),
]