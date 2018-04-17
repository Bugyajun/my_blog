from django.conf.urls import include, url
from django.contrib import admin
import blogs.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blogs', include(blogs.urls,namespace='blogs')),
]
