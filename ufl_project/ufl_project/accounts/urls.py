from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns =[
    url(r'^signup/$' , views.signup_users , name="signup"),
    url(r'^login/$' , views.loginpage , name="loginpage"),
    url (r'profile/$' , views.view_profile , name="profil_accounts"),
    url(r'^profile/edit/$' , views.edit_profile , name="editprofile"),
]