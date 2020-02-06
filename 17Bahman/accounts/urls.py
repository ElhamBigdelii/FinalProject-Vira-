from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns =[
    url(r'^signup_login/$' , views.signup_users , name="signup"),
    url(r'^login/$' , views.loginpage , name="loginpage"),
    url (r'profiles/$' , views.view_profile , name="profil_accounts"),
    url(r'^profiles/edit/$' , views.edit_profile , name="editprofile"),
    url(r'^logout/$' , views.logout_viwe , name="logout"),
    url(r'^test/$' , views.test , name="test"),
    url (r'^profile_charity$' , views.view_profile_charity , name="profile_charity"),
]