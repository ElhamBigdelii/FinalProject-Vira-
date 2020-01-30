from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'loginpage/' , views.login , name='loginpage'),
    url(r'^profile_user/' , views.profile_user , name="profile_users"),
    url(r'^profile_modir/' , views.profile_Modir , name="profile_modir")
]