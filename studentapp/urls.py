from django.conf.urls import url
from studentapp import views

urlpatterns = [
    url(r'^student$', views.studentApi),
    url(r'^student/([0-9]+)$', views.studentApi),
    url(r'^home$', views.home)
    
]
