from django.conf.urls import url
from .import views
from django.urls import include, path

app_name = 'charity'

urlpatterns =[
    url(r'^add_charity/$' , views.charityadd , name="addCharity"),
    url(r'^addProject/$',views.addProject,name="addProject"),
    url(r'^golrizoonha/$', views.golrizoon_list , name="golrizooon"),
    url(r'^little_dream/$' , views.little_dream , name="little_dream"),
    url (r'^charitys/$' , views.charityss , name="charitys"),
    url(r'^project/(?P<pk>\d+)/$' , views.datail_project , name="detail"),
    url(r'^thankyou/$' , views.show_thank_you , name="thank_you"),
    url(r'^charity/(?P<pk>\d+)/$' , views.datail_charity , name="detail_charity"),
]
