
from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('admin/', admin.site.urls),
    url (r'^users/',include('users.urls') , name='users'),
    url (r'^signeup/',include('signeup.urls') , name='signeup'),
    url (r'^login/',include('login.urls') , name='login'),
    url (r'^charityes/',include('charityes.urls')),
    url (r'^addpost/' , include('addpost.urls'))
]

urlpatterns += staticfiles_urlpatterns()