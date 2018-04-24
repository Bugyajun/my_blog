from django.conf.urls import include, url
from comments import views

app_name = 'comments'

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^post/comments/(?P<airticle_pk>[0-9]+)/', views.post_comment,name='post_comment'),
]