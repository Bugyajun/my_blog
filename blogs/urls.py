from django.conf.urls import url
from blogs import views
app_name = 'blogs'

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index,name = 'index'),
    url(r'^/?P<pk>[0-9]+', views.detail,name = 'detail')
]