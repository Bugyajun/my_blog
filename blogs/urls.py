from django.conf.urls import url
from blogs import views

app_name = 'blogs'

urlpatterns = [

    url(r'^$', views.index,name = 'index'),
    #url(r'^/?P<pk>[0-9]+', views.detail,name = 'detail')
    url(r'^/(?P<pk>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name = 'archives'),
    url(r'^/details',views.detail)

]