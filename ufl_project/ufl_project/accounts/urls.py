from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns =[
    url(r'^signup/$' , views.signup_users , name="signup"),
    url(r'^login/$' , views.loginpage , name="loginpage"),
    url (r'profiles/$' , views.view_profile , name="profil_accounts"),
    url(r'^profiles/edit/$' , views.edit_profile , name="editprofile"),
]