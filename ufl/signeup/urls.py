from django.conf.urls import url
from .import views

app_name = 'signeup'

urlpatterns = [
    url(r'^signeup/' , views.signeupusers , name="signeupuser")
]