from django.conf.urls import url
from .import views

app_name = 'charityes'

urlpatterns = [
    url(r'^add_charityes/' , views.addcharityes , name='add_charitye'),
    url(r'^profile_charity/' , views.profile_charity , name='profile_charity'),
]