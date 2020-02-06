from django.conf.urls import url
from .import views

app_name = 'charity'

urlpatterns =[
    url(r'^add_charity/$' , views.charityadd , name="addCharity"),
    url(r'^addProject/$',views.addProject,name="addProject"),
    url(r'^golrizoonha/$', views.golrizoon_list , name="golrizooon"),
    url(r'^little_dream/$' , views.little_dream , name="little_dream"),
    url (r'^Profile_charity/$' , views.accepted , name="profile_charity"),
]