
from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('admin/', admin.site.urls),
    url (r'^users/',include('users.urls') , name='users'),
    url (r'^charityes/',include('charityes.urls')),
]

urlpatterns += staticfiles_urlpatterns()