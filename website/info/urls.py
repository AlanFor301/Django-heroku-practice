from django.conf.urls import url
from . import views

urlpatterns = [
    #views.index looking for index function in views module 
    url(r'^$', views.index, name='index'),
]
