from django.conf.urls import include, url
from django.contrib import admin
from Users import views

app_name = 'Users'

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', views.register,name = 'register'),
    url(r'^$', views.index,name = 'index'),
]
