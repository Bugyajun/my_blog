from django.conf.urls import include, url
from django.contrib import admin
import blogs.urls
import Users.urls
from Users import views
import comments.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blogs/', include('blogs.urls',namespace='blogs')),
    url(r'^comments',include('comments.urls',namespace='comments')),
    url(r'^users/',include('django.contrib.auth.urls')),
    url(r'^users/',include('Users.urls',namespace='Users')),
    url(r'',views.index,name = 'index'),
]
