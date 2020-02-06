
from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^charity/', include('charity.urls')),
    url(r'^index/', include('index.urls')),
]

urlpatterns +=staticfiles_urlpatterns()