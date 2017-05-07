from django.conf.urls import url
from . import views

urlpatterns = [
    #/info/views.index looking for index function in views module
    url(r'^$', views.index, name='index'),

    # /info/<staff_id>/ ^ represent begining $ ends
    url(r'^(?P<staff_id>[0-9]+)/$', views.detail, name='detail'),
]
